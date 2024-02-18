import xml.etree.ElementTree as ET
import xml.dom.minidom

def insert_target_comment(input_ptr_path,
                          output_ptr_path=False,
                          target='JUPITER',
                          verbose=True):

    if not output_ptr_path:
        output_ptr_path = input_ptr_path + '.output'

    # Read the XML content from the file
    with open(input_ptr_path, 'r') as file:
        xml_input = file.read()

    root = ET.fromstring(xml_input)

    # Iterate through all 'block' elements and check for the target
    for block in root.iter('block'):
        attitude = block.find('attitude')
        if attitude is not None:
            metadata = block.find('metadata')
            if metadata is not None:
                comment_element = ET.Element('comment')
                comment_element.text = f'TARGET={target}'
                metadata.append(comment_element)

    # Convert the modified XML back to string
    modified_xml = ET.tostring(root, encoding='unicode')
    # Write the modified XML to a new file
    with open(output_ptr_path, 'w') as file:
        file.write(modified_xml)

    if verbose:
        print(modified_xml)

    return modified_xml






