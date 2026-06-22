import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('.//calculation')

# Task 1 & 2: Front edge and hem lines
lines_to_remove = []
for l in calc.findall('line'):
    # line 304 is usually 301 to 303
    if l.get('id') == '304' or (l.get('firstPoint') in ['301', '303'] and l.get('secondPoint') in ['301', '303']):
        lines_to_remove.append(l)

for l in lines_to_remove:
    calc.remove(l)

new_lines = []
line_id = 16000

# 301 to 502
new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '301', 'secondPoint': '502', 'lineColor': 'black'}))
line_id += 1

# 502 to 303
new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '502', 'secondPoint': '303', 'lineColor': 'black'}))
line_id += 1

# Front edge line B_Boton_1 (11004) to Ext_B_Cruce_Ruedo (15000)
new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '11004', 'secondPoint': '15000', 'lineColor': 'black', 'lineWeight': '0.35'}))
line_id += 1

# Task 3: Sleeve lines
sleeve_lines = [
    # Cimera Left
    ('12004', '12010'), ('12010', '12014'),
    # Cimera Right
    ('12005', '12011'), ('12011', '12015'),
    # Cimera Hem
    ('12014', '12015'),
    
    # Bajera Left
    ('12006', '12012'), ('12012', '12016'),
    # Bajera Right
    ('12007', '12013'), ('12013', '12017'),
    # Bajera Hem
    ('12016', '12017')
]

for p1, p2 in sleeve_lines:
    new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': p1, 'secondPoint': p2, 'lineColor': 'blue' if '12006' in [p1,p2] or '12007' in [p1,p2] or '12016' in [p1,p2] or '12017' in [p1,p2] else 'black'}))
    line_id += 1

for l in new_lines:
    calc.append(l)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Finished applying all 3 requested fixes to Blazer_Dama_Maestro.val!")
