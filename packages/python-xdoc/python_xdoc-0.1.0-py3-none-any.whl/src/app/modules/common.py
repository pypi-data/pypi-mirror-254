import time
import datetime
import tempfile
import zipfile
import csv
import json
import yaml
import toml

class Interface:

    def get_tempdir():
        timestamp = int(time.time())
        temp_dir = tempfile.mkdtemp()
        return timestamp, temp_dir

    def create_zip(file_list, zip_path, password=None):
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
            if password:
                zipf.setpassword(bytes(password, 'utf-8'))
            for item in file_list:
                if os.path.isdir(item):
                    for root, _, files in os.walk(item):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, item)
                            zipf.write(file_path, arcname)
                else:
                    arcname = os.path.basename(item)
                    zipf.write(item, arcname)

    def read_csv(csv_file):
        feeds = []
        with open(csv_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                feeds.append(row)
        data = {"items": feeds}
        return data

    def read_json(json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
        return data

    def read_yaml(yaml_file):
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
        return data

    def read_toml(toml_file):
        with open(toml_file, 'r') as f:
            data = toml.load(f)
        return data

    def read_raw(raw_file):
        with open(raw_file, 'r') as f:
            data = f.read()
        return {"items": [{'data': data}]}

    def read_file(fpath):
        if fpath.endswith('.csv'):
            data = Interface.read_csv(fpath)
        elif fpath.endswith('.json'):
            data = Interface.read_json(fpath)
        elif fpath.endswith('.toml'):
            data = Interface.read_toml(fpath)
        elif fpath.endswith('.yaml') or fpath.endswith('.yml'):
            data = Interface.read_yaml(fpath)
        elif fpath.endswith(''):
            data = Interface.read_raw(fpath)
        else:
            raise ValueError(f"Invalid file format: {fpath}")
        return data


    def write_csv(data, path):
        with open(path, 'w', encoding='utf-8-sig', newline='') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for feed_obj in data:
                writer.writerow(feed_obj)

    def write_json(data, path):
        data = {"items": data}
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def write_yaml(data, path):
        with open(path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, default_flow_style=False, allow_unicode=True)

    def write_toml(data, path):
        with open(path, 'w', encoding='utf-8') as f:
            toml.dump(data, f)

    def write_xml(data, path, root_element="root"):
        def to_xml(data):
            xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n'
            xml_string += f'<{root_element}>\n'
            for key, value in data.items():
                xml_string += f'  <{key}>{value}</{key}>\n'
            xml_string += f'</{root_element}>'
            return xml_string
        try:
            xml_data = to_xml(data)
            with open(path, 'w') as f:
                f.write(xml_data)
        except Exception as e:
            print("Error while writing to file:", str(e))

    def write_raw(data, path):
        with open(path, 'w') as f:
            f.write(data, f)

    def write_file(fpath, result):
        if fpath.endswith('.csv'):
            Interface.write_csv(result, fpath)
        elif fpath.endswith('.json'):
            Interface.write_json(result, fpath)
        elif fpath.endswith('.toml'):
            Interface.write_toml(result, fpath)
        elif fpath.endswith('.yaml') or fpath.endswith('.yml'):
            Interface.write_yaml(result, fpath)
        elif fpath.endswith(''):
            Interface.write_raw(result, fpath)
        else:
            raise ValueError(f"Invalid file format: {fpath}")
