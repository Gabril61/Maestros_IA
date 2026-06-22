import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

# Find all <draw> blocks and empty them of <piece> and <path>
for draw in root.findall('.//draw'):
    elements_to_remove = []
    for child in draw:
        if child.tag in ['piece', 'path']:
            elements_to_remove.append(child)
    for el in elements_to_remove:
        draw.remove(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("All pieces and paths removed from draw.")
