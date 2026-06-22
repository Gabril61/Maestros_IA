import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Caballero_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

variables = root.find('.//variables')

# Remove #holgura_bata
for var in variables.findall('variable'):
    if var.get('name') == '#holgura_bata':
        variables.remove(var)

new_vars = [
    ET.Element('variable', {'description': 'Holgura de busto/pecho', 'formula': '12', 'name': '#holgura_busto'}),
    ET.Element('variable', {'description': 'Holgura de cadera/ruedo', 'formula': '12', 'name': '#holgura_cadera'}),
    ET.Element('variable', {'description': 'Holgura de ancho de espalda', 'formula': '2', 'name': '#holgura_espalda'}),
    ET.Element('variable', {'description': 'Holgura de ancho de pecho', 'formula': '2', 'name': '#holgura_pecho'}),
    ET.Element('variable', {'description': 'Holgura de manga bicep', 'formula': '8', 'name': '#holgura_bicep'}),
]
variables.extend(new_vars)

calc = root.find('.//calculation')

formulas = {
    '111': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '119': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '121': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)'},
    '140': {'length': '((@S_CONT_BUSTO + #holgura_busto)/8)'},
    '211': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '219': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '221': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)'},
}

for pt in calc:
    pid = pt.get('id')
    if pid in formulas:
        for k, v in formulas[pid].items():
            pt.set(k, v)

# Also check points that might use @S_ANCHO_ESPALDA and add #holgura_espalda
# Wait, let's look at 104 and 103 from query_scrub_caballero.py
# 104 F_Guia_Espalda (@S_ANCHO_ESPALDA/2)
for pt in calc.findall('point'):
    if pt.get('length') == '(@S_ANCHO_ESPALDA/2)':
        pt.set('length', '((@S_ANCHO_ESPALDA + #holgura_espalda)/2)')

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Scrub Top Caballero refactored!")
