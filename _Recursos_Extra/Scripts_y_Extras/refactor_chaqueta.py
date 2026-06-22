import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

variables = root.find('.//variables')

# Create variables block if it doesn't exist
if variables is None:
    variables = ET.SubElement(root, 'variables')

new_vars = [
    ET.Element('variable', {'description': 'Holgura de busto', 'formula': '16', 'name': '#holgura_busto'}),
    ET.Element('variable', {'description': 'Holgura de cadera', 'formula': '16', 'name': '#holgura_cadera'}),
    ET.Element('variable', {'description': 'Holgura de espalda/hombro', 'formula': '4', 'name': '#holgura_espalda'}),
    ET.Element('variable', {'description': 'Holgura profundidad sisa', 'formula': '8', 'name': '#holgura_prof_sisa'}),
]
variables.extend(new_vars)

calc = root.find('.//calculation')

formulas = {
    '4': {'length': '((@S_CONT_BUSTO + #holgura_busto) / 4)'},
    '5': {'length': '((@S_CONT_BUSTO + #holgura_busto) / 4)'},
    '6': {'length': '((@S_CONT_BUSTO + #holgura_busto) / 4)'},
    '1302': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera) / 4)'},
    '1303': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera) / 4)'},
    '103': {'length': '((@S_CONT_BUSTO + #holgura_busto) / 4)'},
    '104': {'length': '((@S_CONT_BUSTO + #holgura_busto) / 4)'},
    '105': {'length': '((@S_CONT_BUSTO + #holgura_busto) / 4)'},
    '402': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera) / 4)'},
    '403': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera) / 4)'},
    '3': {'length': '(@S_ANCHO_ESPALDA / 2) + #holgura_prof_sisa'},
    '102': {'length': '(@S_ANCHO_ESPALDA / 2) + #holgura_prof_sisa'},
    '26': {'length': '(@S_ANCHO_ESPALDA + #holgura_espalda) / 2'},
    '115': {'length': '(@S_ANCHO_ESPALDA + #holgura_espalda) / 2'},
}

for pt in calc:
    pid = pt.get('id')
    if pid in formulas:
        for k, v in formulas[pid].items():
            pt.set(k, v)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Chaqueta refactoring applied successfully!")
