import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calc = root.find('.//calculation')

# 1. Remove 141 and lines 144, 145
for el in calc.findall('*'):
    if el.get('id') in ['141', '144', '145']:
        calc.remove(el)

# 2. Add new dart points
# IDs: Let's use 150, 151, 152, 153
# 101 to 111 is waist to hem
# 101 to 116 is waist to dobladillo

new_points = [
    # Right side
    ET.Element('point', {'id': '150', 'name': 'E_Pinza_Ruedo_Der', 'type': 'endLine', 'basePoint': '138', 'angle': '270', 'length': 'Line_E_Nivel_Cintura_E_Centro_Ruedo'}),
    ET.Element('point', {'id': '151', 'name': 'E_Pinza_Dobladillo_Der', 'type': 'endLine', 'basePoint': '138', 'angle': '270', 'length': 'Line_E_Nivel_Cintura_E_Dobladillo_Centro'}),
    # Left side
    ET.Element('point', {'id': '152', 'name': 'E_Pinza_Ruedo_Izq', 'type': 'endLine', 'basePoint': '139', 'angle': '270', 'length': 'Line_E_Nivel_Cintura_E_Centro_Ruedo'}),
    ET.Element('point', {'id': '153', 'name': 'E_Pinza_Dobladillo_Izq', 'type': 'endLine', 'basePoint': '139', 'angle': '270', 'length': 'Line_E_Nivel_Cintura_E_Dobladillo_Centro'}),
]

new_lines = [
    ET.Element('line', {'id': '154', 'firstPoint': '138', 'secondPoint': '150', 'lineColor': 'black', 'lineWeight': '0.35'}),
    ET.Element('line', {'id': '155', 'firstPoint': '150', 'secondPoint': '151', 'lineColor': 'black', 'lineWeight': '0.35'}),
    ET.Element('line', {'id': '156', 'firstPoint': '139', 'secondPoint': '152', 'lineColor': 'black', 'lineWeight': '0.35'}),
    ET.Element('line', {'id': '157', 'firstPoint': '152', 'secondPoint': '153', 'lineColor': 'black', 'lineWeight': '0.35'}),
    ET.Element('line', {'id': '158', 'firstPoint': '150', 'secondPoint': '152', 'lineColor': 'black', 'lineWeight': '0.35'}), # Connecting Ruedo inner
    ET.Element('line', {'id': '159', 'firstPoint': '151', 'secondPoint': '153', 'lineColor': 'black', 'lineWeight': '0.35'}), # Connecting Dobladillo inner
]

for el in new_points + new_lines:
    calc.append(el)

# 3. Fix modeling
modeling = root.find('.//modeling')
# Need to replace point 436 (which referenced 141) with the new path
# Wait, let's see how the detail piece was constructed.
# The user probably clicked: E_Costado_Cintura, E_Costado_Ruedo, E_Centro_Ruedo, E_Pinza_Bot, E_Centro_Ruedo?
# Let's check modeling points for 141.
for mp in modeling.findall('point'):
    if mp.get('idObject') == '141':
        # Instead of 141, the path depends on how the user traversed the back.
        # Let's inspect the piece that uses 436.
        pass

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Points added. Need to inspect detail piece.")
