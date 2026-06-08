import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Medica_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

# 1. Update variables
variables = root.find('.//variables')
for var in variables.findall('variable'):
    if var.get('name') == '#holgura_bata':
        variables.remove(var)

new_vars = [
    ET.Element('variable', {'description': 'Holgura de busto', 'formula': '8', 'name': '#holgura_busto'}),
    ET.Element('variable', {'description': 'Holgura de cadera', 'formula': '24', 'name': '#holgura_cadera'}),
    ET.Element('variable', {'description': 'Holgura de espalda', 'formula': '-1', 'name': '#holgura_espalda'}),
    ET.Element('variable', {'description': 'Holgura de pecho', 'formula': '-3', 'name': '#holgura_pecho'}),
    ET.Element('variable', {'description': 'Holgura de bicep', 'formula': '4', 'name': '#holgura_bicep'}),
]
variables.extend(new_vars)

# 2. Update Calculations
calc = root.find('.//calculation')

formulas = {
    '111': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '119': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4) - 2'},
    '121': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)'},
    '211': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '219': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4) - 2'},
    '221': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)'},
    '110': {'length': '(@S_ANCHO_ESPALDA + #holgura_pecho)/2'},
    '210': {'length': '(@S_ANCHO_ESPALDA + #holgura_espalda)/2'},
    '1003': {'length': '(@S_CONT_BICEP + #holgura_bicep)/2'},
    '1004': {'length': '(@S_CONT_BICEP + #holgura_bicep)/2'},
}

for pt in calc:
    pid = pt.get('id')
    if pid in formulas:
        for k, v in formulas[pid].items():
            pt.set(k, v)
    if pt.get('length') and '#holgura_bata' in pt.get('length'):
        pt.set('length', pt.get('length').replace('#holgura_bata', '#holgura_busto'))

# 3. XML Reordering
# We must move 202, 20000, 20001, 20002 BEFORE 210, 211, etc.
# Actually, moving them to the top of the T_ variables is safer.
# Find T_Nivel_Sisa (207), which is a good anchor. We'll insert BEFORE 207.

ids_to_move = ['202', '20000', '20001', '20002']
nodes_to_move = []

for elem in list(calc):
    if elem.get('id') in ids_to_move:
        nodes_to_move.append(elem)
        calc.remove(elem)

# Find index of 207
anchor_idx = 0
for i, elem in enumerate(calc):
    if elem.get('id') == '207':
        anchor_idx = i
        break

# Insert nodes
for i, node in enumerate(nodes_to_move):
    calc.insert(anchor_idx + i, node)

# Now they are safely before 210 and 211.

# 4. Geometric Fix
p_inter_pecho = ET.Element('point', {'angle': '180', 'basePoint': '209', 'curve': '20002', 'id': '90005', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'T_Inter_Pecho', 'showPointName': 'false', 'type': 'curveIntersectAxis'})
p_inter_sisa = ET.Element('point', {'angle': '180', 'basePoint': '207', 'curve': '20002', 'id': '90006', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'T_Inter_Sisa', 'showPointName': 'false', 'type': 'curveIntersectAxis'})

# Insert after 20002
for i, elem in enumerate(calc):
    if elem.get('id') == '20002':
        calc.insert(i + 1, p_inter_pecho)
        calc.insert(i + 2, p_inter_sisa)
        break

# Re-base 210 and 211
for pt in calc.findall('point'):
    if pt.get('id') == '210':
        pt.set('basePoint', '90005')
    elif pt.get('id') == '211':
        pt.set('basePoint', '90006')


xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Blusa Dama refactoring applied successfully!")
