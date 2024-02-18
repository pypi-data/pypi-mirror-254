import xml.etree.ElementTree as ET
from yasik.yasik_interpreter import yasik_compiler


def get_xml_param_list(path):
    tree = ET.parse(path)
    root = tree.getroot()
    param_list = []
    for each in root.findall('*'):
        for subeach in each.findall('*'):
            param_list.append(subeach.tag)
    return param_list


def compiler(input_string: str, xml_path: str):
    list_param = get_xml_param_list(xml_path)
    result = yasik_compiler(input_string, list_param)
    return result
