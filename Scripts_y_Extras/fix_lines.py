import xml.etree.ElementTree as ET

file_path = "Blazer_Dama_Maestro.val"
tree = ET.parse(file_path)
root = tree.getroot()

calculation_node = None
for draft in root.findall('.//draftBlock'):
    if draft.get('name') == 'Corpino_y_Manga':
        calculation_node = draft.find('calculation')
        break

# Find the lines 30061 and 30062
line1 = None
line2 = None
for node in list(calculation_node):
    if node.get('id') == '30061':
        line1 = node
    elif node.get('id') == '30062':
        line2 = node

if line1 is not None and line2 is not None:
    calculation_node.remove(line1)
    calculation_node.remove(line2)
    
    # Find the index of 12005 to insert lines right after it
    insert_idx = -1
    for i, node in enumerate(list(calculation_node)):
        if node.get('id') == '12005':
            insert_idx = i
            break
            
    if insert_idx != -1:
        calculation_node.insert(insert_idx + 1, line1)
        calculation_node.insert(insert_idx + 2, line2)

tree.write(file_path, encoding="utf-8", xml_declaration=True)
print("Lines moved before they are used.")
