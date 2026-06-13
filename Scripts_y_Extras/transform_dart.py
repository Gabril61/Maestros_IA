import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calc = root.find('.//calculation')

# 1. Remove old nodes
to_remove = ['141', '144', '145']
for el in list(calc):
    if el.get('id') in to_remove:
        calc.remove(el)

# 2. Add new nodes for the open dart
# We drop points from 138 (Der) and 139 (Izq) straight down (angle 270)
# We use intersectLineLine or just endLine with length = Line_101_111 (waist to hem) and Line_101_116 (waist to dobladillo)
new_points = [
    # Right Side (Der)
    ET.Element('point', {'id': '150', 'name': 'E_Pinza_Ruedo_Der', 'type': 'endLine', 'basePoint': '138', 'angle': '270', 'length': 'Line_E_Nivel_Cintura_E_Centro_Ruedo'}),
    ET.Element('point', {'id': '151', 'name': 'E_Pinza_Dobladillo_Der', 'type': 'endLine', 'basePoint': '138', 'angle': '270', 'length': 'Line_E_Nivel_Cintura_E_Dobladillo_Centro'}),
    # Left Side (Izq)
    ET.Element('point', {'id': '152', 'name': 'E_Pinza_Ruedo_Izq', 'type': 'endLine', 'basePoint': '139', 'angle': '270', 'length': 'Line_E_Nivel_Cintura_E_Centro_Ruedo'}),
    ET.Element('point', {'id': '153', 'name': 'E_Pinza_Dobladillo_Izq', 'type': 'endLine', 'basePoint': '139', 'angle': '270', 'length': 'Line_E_Nivel_Cintura_E_Dobladillo_Centro'}),
]

new_lines = [
    # Right vertical lines
    ET.Element('line', {'id': '154', 'firstPoint': '138', 'secondPoint': '150', 'lineColor': 'black', 'lineWeight': '0.35', 'type': 'none'}),
    ET.Element('line', {'id': '155', 'firstPoint': '150', 'secondPoint': '151', 'lineColor': 'black', 'lineWeight': '0.35', 'type': 'none'}),
    # Left vertical lines
    ET.Element('line', {'id': '156', 'firstPoint': '139', 'secondPoint': '152', 'lineColor': 'black', 'lineWeight': '0.35', 'type': 'none'}),
    ET.Element('line', {'id': '157', 'firstPoint': '152', 'secondPoint': '153', 'lineColor': 'black', 'lineWeight': '0.35', 'type': 'none'}),
    # Horizontal connectors (Hem and Dobladillo inner gap)
    ET.Element('line', {'id': '158', 'firstPoint': '150', 'secondPoint': '152', 'lineColor': 'black', 'lineWeight': '0.35', 'type': 'none'}),
    ET.Element('line', {'id': '159', 'firstPoint': '151', 'secondPoint': '153', 'lineColor': 'black', 'lineWeight': '0.35', 'type': 'none'}),
]

for el in new_points + new_lines:
    calc.append(el)

# 3. Remove modeling node 436 (which referenced 141)
modeling = root.find('.//modeling')
if modeling is not None:
    for el in list(modeling):
        if el.get('idObject') == '141' or el.get('id') == '436':
            modeling.remove(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Dart transformed successfully!")
