import os
import sys
import time
import uuid
import argparse
import gradio as gr
import pypandoc
import pandas as pd
from pyppeteer import launch

from modules.common import Interface, Logger

def add_common_props(state, input_file, doc_choices=None, additional_keys=None):
    data = Interface.read_file(input_file)
    data = recursive_filter(data, doc_choices, additional_keys)
    print(data)

    return data

def filter_entries(entries, doc_choices):
    filtered_entries = []
    for entry in entries:
        if isinstance(entry, dict) and entry.get('title') in doc_choices:
            filtered_entries.append(entry)
    return filtered_entries

def recursive_filter(data, doc_choices, additional_keys=None):
    for key, value in data.items():
        if isinstance(value, list):
            data[key] = filter_entries(value, doc_choices)
        elif isinstance(value, dict):
            data[key] = recursive_filter(value, doc_choices, additional_keys)

            # ネストされた辞書に追加のキーを更新
            if additional_keys is not None and key in additional_keys:
                if isinstance(additional_keys[key], pd.DataFrame):
                    # DataFrameを辞書に変換して追加
                    data[key].update(additional_keys[key].to_dict(orient='records'))
                else:
                    data[key].update(additional_keys[key])

    return data

def update_params(input):
    data = Interface.read_file(input.name)
    props = []
    for key, val in data['docs'].items():
        if isinstance(val, list):
            for p in val:
                if 'title' in p and 'document_id' in p:
                    prop = {
                        'title': p['title'],
                        'document_id': p['document_id']
                    }
                    props.append(prop)
    titles = [prop['title'] for prop in props]
    print(titles)

    return gr.Dropdown(choices=titles)

def add_common_props(state):
    data = Interface.read_file(input_file)
    data = recursive_filter(data, doc_choices, additional_keys)
    print(data)

    return data

def create_docs(state):
    if clear_cache:
        clear_cache()
    ts, tmp_dir = Interface.get_tempdir()
    tmp_file = f'{tmp_dir}/{ts}'
    data = add_common_props(state)

    struct_docs(data, input_style.name, input_template_html.name, tmp_file)
    gr.Info(f"Conversion completed. Output written to {result_file}")

    return result_file, tmp_dir

def struct_docs(*params):
    input_data, input_style, input_template_html, tmp_file = params
    keys, dep_name, doc_type, templates = params # TODO

    dep_name = Interface.read_file(params['dep_name'])
    doc_type = Interface.read_file(params['doc_type'])

    tmp_dir = os.path.dirname(tmp_file)
    create_directory(tmp_dir)

    result = process_docs(input_data, tmp_dir, templates, keys)

    md_file = os.path.join(tmp_dir, 'readme.md')
    with open(md_file, 'w') as file:
        file.write(''.join(result))

    extensions = ['csv', 'json', 'yaml', 'toml', 'html', 'docx']
    for ext in extensions:
        output = f'{tmp_dir}/index.{ext}'
        Interface.write_file(data, output)

    zip_file = tmp_file + '.zip'

    convert_docs(md_file, html_file, docx_file, templates['css'], templates['html'], templates['docx'])

    files_dir = os.path.join(tmp_dir, 'docs')  # TODO
    file_list = [files_dir, md_file, html_file]
    Interface.create_zip(file_list, zip_file)

    return zip_file

def make_copy(origin_file, out_file):
    with open(origin_file, 'r') as file:
        content = file.read()
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        with open(out_file, 'w') as f:
            f.write(content)

def make_copy_binary(origin_file, out_file):
    with open(origin_file, 'rb') as file:
        content = file.read()
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        with open(out_file, 'wb') as f:
            f.write(content)

def duplicate_contents(tmp_dir, path, templates):
    folder_path = os.path.join(tmp_dir, os.path.dirname(path))
    file_path = os.path.join(tmp_dir, path)

    os.makedirs(folder_path, exist_ok=True)

    for template_key, template_path in templates.items():
        copy_path = os.path.join(folder_path, template_path)
        if template_key == 'docx':
            make_copy_binary(template_path, copy_path)
        else:
            make_copy(template_path, copy_path)

    return file_path

def process_docs(*params):
    input_data, tmp_dir, templates, keys = params

    for key, obj in input_data['docs'].items():
        for item in obj:
            if isinstance(obj, list):
                path = item.get("path", "")
                docs_dir = os.path.join(tmp_dir, 'docs')
                file_path = duplicate_contents(docs_dir, path, templates)
                print(file_path)

                tmp_name = os.path.basename(file_path)
                md_file_ = file_path

                exts = ['html', 'docx', 'pdf']
                file_paths = [f"{file_path}.{ext}" for ext in exts]
                html_file_, docx_file_, pdf_file_ = file_paths

                with open(md_file_, 'w') as file:
                    file.write(content)

                convert_docs(md_file_, html_file_, docx_file_, templates['css'], templates['html'], templates['docx'])

    extensions = ['md', 'csv', 'json', 'toml', 'yaml', 'html', 'docx']
    file_paths = {}
    for ext in extensions:
        file_paths[ext] = os.path.join(tmp_dir, f'index.{ext}')

    zip_file = tmp_file + '.zip'

    files_dir = os.path.join(tmp_dir, 'docs') # TODO
    Interface.create_zip(files_dir, zip_file)

    return zip_file, result


def convert_docs(*params):
    md_file, html_file, docx_file, css_template, html_template, docx_template = params
    pypandoc.convert_file(md_file,
        'html',
        outputfile=html_file,
        extra_args=['--template=' + html_template,
        '--css=' + css_template]
        )
    pypandoc.convert_file(md_file,
        'docx',
        outputfile=docx_file,
        extra_args=['-s',
        '-f',
        'markdown+east_asian_line_breaks',
        '--reference-doc=' + docx_template]
        )

def clear_cache():
    try:
        dir = "/tmp/"
        for root, dirs, files in os.walk(dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
        gr.Info(f'Clear cache done.')
    except Exception as e:
        gr.Error(f'Failed to delete files in {dir}. Reason: {e}')

def webui(params):

    df = pd.DataFrame(list(additional_keys.items()), columns=['key', 'value'])

    with gr.Blocks(css=params['css'], title=params['title']) as app:
        title = gr.HTML(params['html_title'])
        state = gr.State({'items':[]})

        with gr.Row(variant='panel'):
            input_clr_cache = gr.ClearButton(value='C')
            input_run = gr.Button(value='▶', variant="primary")

        with gr.Tab('Processor') as tab1:
            with gr.Row():
                with gr.Column(variant='panel') as col1:
                    input_file = gr.File(elem_id=f'{uuid.uuid4()}')
                    with gr.Accordion("Templates", open=False):
                        input_style = gr.File(elem_id=f'{uuid.uuid4()}')
                        input_template_html = gr.File(elem_id=f'{uuid.uuid4()}')
                    input_doc = gr.Dropdown(choices=[], value=[], multiselect=True, label='Select')
                    input_code =gr.Code(tmp_file, elem_id=f'{uuid.uuid4()}', visible=False)
                    input_table = gr.Dataframe(df, interactive=True, headers=['key', 'value'],  elem_id=f'{uuid.uuid4()}')

                with gr.Column(variant='panel'):
                    output_file = gr.File(elem_id=f'{uuid.uuid4()}')
                    output_explorer = gr.FileExplorer("", elem_id=f'{uuid.uuid4()}')

        inputs = [
            state,
            input_file,
            input_style,
            input_template_html,
            input_doc,
            input_code,
            input_table,
            input_clr_cache
        ]

        outputs = [
            output_file,
            output_explorer,
        ]

        with tab1:
            examples = gr.Examples(params['examples'], [input_file, input_style, input_template_html], [input_file, input_style, input_template_html])

        input_file.change(update_params, input_file, input_doc)
        input_run.click(create_docs, inputs, outputs)
        input_clr_cache.click(clear_cache, None, None)


    app.queue().launch(
        )

if __name__ == "__main__":

    with open('config.json') as f:
        config = json.load(f)

    keys = ["title", "description", "own", "auth", "type", "author", "path", "locale", "document_id", "related_id", "priority", "version", "last_updated", "expiration", "category", "tag", "status", "approval", "subtitle", "target_group", "target_name", "timestamp", "from_group", "from_name", "from_mark", "pre_text", "main_text", "mid_text",  "end_text", "closing_text", "memo_mark", "ol1", "ol2", "ol3", "ol4", "ol5", "closing", "signature_name", "signature", "contact_name", "contact_email", "comments"]

    dep_name = Interface.read_file('data/yaml/dep_name.yaml')
    doc_type = Interface.read_file('data/yaml/doc_type.yaml')

    templates = {
        'css': os.path.join('static/style', os.path.basename(input_style)),
        'html': os.path.join('static/templates', os.path.basename(input_template_html)),
        'docx': 'static/references/reference_01.docx'
    }

    params = {
        'version': 'v0.1.0',
        'title': 'Company Template Generator',
        'css': 'footer {visibility: hidden}',
        'html_title': f"<div style='max-width:100%; max-height:360px; text-align: center; overflow:auto'><h1>Company Template Generator {version}</h1></div>",
        'examples': [
                ['data/toml/company_documents.toml', 'src/css/style_01.css', 'src/css/template_01.html'],
                ['data/yaml/store_documents.yaml', 'src/css/style_02.css', 'src/css/template_02.html']
            ]
    }

    webui(params)