import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Find all nodes with IDs starting with 41, 42, 43, 44
nodes_to_move = []
for child in calculation:
    cid = child.get('id')
    if cid and cid.startswith(('41', '42', '43', '44')):
        nodes_to_move.append(child)

# Remove them from their current position
for node in nodes_to_move:
    calculation.remove(node)

# Append them at the end of calculation
for node in nodes_to_move:
    calculation.append(node)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Node ordering fixed.")
