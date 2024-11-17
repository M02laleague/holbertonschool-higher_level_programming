#!/usr/bin/python3
import xml.etree.ElementTree as ET
import xml.dom.minidom

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    
    # Convert the ElementTree to a string
    xml_str = ET.tostring(root, encoding='unicode')
    
    # Parse the string using minidom for pretty printing
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml_str = dom.toprettyxml(indent="  ")
    
    # Write the pretty-printed XML to the file
    with open(filename, 'w') as f:
        f.write(pretty_xml_str)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary

if __name__ == "__main__":
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)