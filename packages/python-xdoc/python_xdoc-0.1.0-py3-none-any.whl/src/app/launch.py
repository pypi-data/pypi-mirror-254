import gradio as gr
from PyPDF2 import PdfMerger
from io import BytesIO
import tempfile
import os
import pypandoc
import markdown_it
from weasyprint import HTML

def md2html(markdown_text):
    md = markdown_it.MarkdownIt()
    html_content = md.render(markdown_text)
    return html_content

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


class PDFProcessor:
    @staticmethod
    def gen(html_content, style, template, output_file):
        css_content = read_file(style)
        template_content = read_file(template)

        html_with_style = f"<style>{css_content}</style>{html_content}"

        # Insert HTML content into the template TODO
        # full_html = template_content.replace('$content$', html_with_style)
        full_html = html_with_style

        # Create a temporary HTML file with a shorter name
        with tempfile.NamedTemporaryFile(mode='w', delete=False, prefix='temp_html_', suffix='.html') as temp_html:
            temp_html.write(full_html)
            temp_html_path = temp_html.name

        try:
            HTML(string=full_html).write_pdf(output_file)
            # Convert HTML to PDF using pyPandoc TODO
            # pypandoc.convert_text(full_html, 'pdf', format='html', outputfile=output_file,
            # extra_args=['--pdf-engine=lualatex',
            # '--template=' + template,
            # '--css=' + style]
            # )
            # # Convert MD to HTML using pyPandoc
            # # Convert HTML to DOCX using pyPandoc
            # pypandoc.convert_file(md_file,
            #     'docx',
            #     outputfile=docx_file,
            #     extra_args=['-s',
            #     '-f',
            #     'markdown+east_asian_line_breaks',
            #     '--reference-doc=' + docx_template]
            #     )

            return output_file
        finally:
            # Clean up the temporary HTML file
            os.remove(temp_html_path)

    @staticmethod
    def merge(input_files, output_file):
        try:
            merger = PdfMerger()
            for file in input_files:
                merger.append(file)
            with open(output_file, 'wb') as merged:
                merger.write(merged)
            print('[*] Merge operation completed.')
        except Exception as e:
            print(f'[!] {e}')

    @staticmethod
    def write(input_file, output_file, start_page, end_page):
        try:
            reader = PdfReader([input_file])
            writer = PdfWriter()

            for page_num in range(start_page - 1, end_page):
                writer.add_page(reader.pages[page_num])

            with open(output_file, 'wb') as extracted:
                writer.write(extracted)
            print('[*] Extract operation completed.')

        except Exception as e:
            print(f'[!] {e}')

def process_files(markdown_files, css_file, html_template_file):
    pdf_buffers = []

    final_pdf_path = "output.pdf"
    for markdown_file in markdown_files:
        tmp_pdf = tempfile.NamedTemporaryFile(mode='w+b', delete=False, prefix='temp_pdf_', suffix='.pdf')
        markdown_content = read_file(markdown_file.name)
        html_content = md2html(markdown_content)

        pdf_buffers.append(PDFProcessor.gen(html_content, css_file.name, html_template_file.name, tmp_pdf.name))

    # Merge PDFs
    PDFProcessor.merge([pdf_buffer for pdf_buffer in pdf_buffers], final_pdf_path)

    return gr.File(final_pdf_path)

# webui

inputs = [
    gr.Files(label="Markdown"),
    gr.File(label="CSS"),
    gr.File(label="HTML Template"),
]

outputs = gr.File(label="PDF")

examples = [
    [["src/md/demo/demo_1.md", "src/md/demo/demo_2.md"], "src/css/style_01.css", "src/html/template_01.html"]
]

iface = gr.Interface(
    title="Markdown to PDF",
    fn=process_files,
    inputs=inputs,
    outputs=outputs,
    live=False,
    examples=examples
)

# Launch the Gradio interface
iface.launch()


# https://www.gradio.app/guides/pdf-component-example