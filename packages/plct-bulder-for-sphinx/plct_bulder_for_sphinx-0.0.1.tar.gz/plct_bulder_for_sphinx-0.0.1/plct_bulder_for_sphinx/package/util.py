import os
import re
import shutil
import tempfile
import jinja2
import time
import hashlib
import cyrtranslit
import xml.etree.cElementTree as ET
from pkg_resources import resource_filename

_TEMPLATE_PATTERN = re.compile(r"^.*(\.t)\.[^\.]+$")

def apply_template_dir(src_dir, dest_dir, template_params, filter_name=None):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for item in os.listdir(src_dir):
        if filter_name and not filter_name(src_dir, item):
            continue
        src_item_path = os.path.join(src_dir, item)
        if os.path.isdir(src_item_path):
            dest_item_path = os.path.join(dest_dir, item)
            apply_template_dir(src_item_path, dest_item_path, template_params, filter_name)
        else:
            match = _TEMPLATE_PATTERN.match(item)
            if match:
                i, j = match.span(1)
                d = os.path.join(dest_dir, item[:i] + item[j:])
                with open(src_item_path, "r", encoding='utf8') as sf:
                    template = jinja2.Template(sf.read())
                filled_template = template.render(template_params)
                with open(d, "w", encoding='utf8') as df:
                    df.write(filled_template)
            else:
                dest_item_path = os.path.join(dest_dir, item)
                shutil.copyfile(src_item_path, dest_item_path)

def make_zip_delete_src(file_path):
    shutil.make_archive(file_path, "zip", file_path)
    shutil.rmtree(file_path)


class IdGenerator:
    _instance = None
    id = 200

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = IdGenerator()
        return cls._instance

    def get_unused_id(self):
        # Increment the id
        self.id += 1
        # Return the unused id
        return str(self.id)


def get_unused_id():
    return IdGenerator.get_instance().get_unused_id()


def get_time_stamp():
    return str(round(time.time()))


def Sha1Hasher(file_path):

    buf_size = 65536
    sha1 = hashlib.sha1()

    with open(file_path, 'rb') as f:
        while True:
            data = f.read(buf_size)
            if not data:
                break
            sha1.update(data)

    return sha1.hexdigest()

def getNormalizedLatinEntry(yaml_block, yaml_key):
    return cyrtranslit.to_latin(yaml_block[yaml_key])


def copy_xml_file(xml_template_file_path, data, zip_ref, zip_file_path):
    tree = ET.parse(xml_template_file_path)
    root = tree.getroot()
    if data.get(root.tag):
        if data[root.tag].get("attributes"):
            attribute_dict = data[root.tag].pop("attributes")
            for attribute_key, attribute_value in attribute_dict.items():
                root.set(attribute_key, attribute_value)
        if data[root.tag].get("root_elements"):
            et_element = data[root.tag].pop("root_elements")
            if isinstance(et_element, list):
                for el in et_element:
                    root.append(el)
        for key, value in data[root.tag].items():
            element = root.find(key)
            if element is not None:
                if isinstance(value, list):
                    for el in value:
                        element.append(el)
                elif isinstance(value, dict):
                    for k, v in value.items():
                        element.set(k, v)
                else:
                    element.text = value

    temp_file = tempfile.NamedTemporaryFile(mode='w+b', delete=False)
    temp_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n".encode())
    ET.ElementTree(root).write(temp_file)
    temp_file.flush()
    zip_ref.write(temp_file.name, zip_file_path)
    temp_file.close()
    os.unlink(temp_file.name)


def apply_moodle_template_dir(src_dir, zip_ref, filter_name=None, root_copy_path='', xml_data={}):
    for item in os.listdir(src_dir):
        if filter_name and item in filter_name:
            continue
        s = os.path.join(src_dir, item)
        if os.path.isdir(s):
            apply_moodle_template_dir(
                s, zip_ref,  filter_name, root_copy_path, xml_data)
        else:
            d = os.path.relpath(s, resource_filename(
                'plct_bulder_for_sphinx', 'moodle-templates'))
            if root_copy_path:
                d = os.path.join(root_copy_path, os.path.basename(d))
            if d.endswith('.xml'):
                copy_xml_file(s, xml_data, zip_ref, d)
            else:
                zip_ref.write(s, d)

ensure_dir = lambda file_path: os.makedirs(file_path, exist_ok=True)