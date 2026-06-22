import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Points to restore
pt_400 = ET.Element('point', {
    'angle': '270', 'basePoint': '101', 'id': '400', 'length': '@G_ALTO_CADERA',
    'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1',
    'name': 'T_Cadera', 'showPointName': 'true', 'type': 'endLine'
})

pt_401 = ET.Element('point', {
    'angle': '270', 'basePoint': '101', 'id': '401', 'length': '@G_ALTO_CADERA + 6',
    'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1',
    'name': 'T_Ruedo', 'showPointName': 'true', 'type': 'endLine'
})

# Find 101 and insert after
idx = -1
for i, child in enumerate(list(calculation)):
    if child.get('id') == '101':
        idx = i
        break

if idx != -1:
    calculation.insert(idx + 1, pt_400)
    calculation.insert(idx + 2, pt_401)
    
tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Points 400 and 401 restored successfully.")
