import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

variables = root.find('.//variables')
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

# 1. Update lengths
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
    '701': {'length': 'Line_F_Ancho_Pecho_F_Costado_Sisa * 0.15'},
    '702': {'length': '3'},
    '213': {'length': '(@S_SEP_BUSTO / 2)'},
}

for pt in calc:
    pid = pt.get('id')
    if pid in formulas:
        for k, v in formulas[pid].items():
            pt.set(k, v)

# 2. Add 710 for Front Dart
p710 = ET.Element('point', {'angle': '(AngleLine_F_APEX_F_Sisa_Pinza_Sup + AngleLine_F_APEX_F_Sisa_Pinza_Inf) / 2', 'basePoint': '14', 'id': '710', 'length': '2.5', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Punta_Pinza_Sisa', 'showPointName': 'true', 'type': 'endLine'})
# Insert 710 after 702
for i, elem in enumerate(calc):
    if elem.get('id') == '702':
        calc.insert(i + 1, p710)
        break

# Update lines and splines connected to 701/702 and 14
for elem in calc:
    if elem.tag in ['line', 'spline']:
        p1 = elem.get('point1') or elem.get('firstPoint')
        p2 = elem.get('point4') or elem.get('secondPoint')
        if (p1 in ['701', '702'] and p2 == '14') or (p1 == '14' and p2 in ['701', '702']):
            if elem.get('point4') == '14': elem.set('point4', '710')
            if elem.get('point1') == '14': elem.set('point1', '710')
            if elem.get('secondPoint') == '14': elem.set('secondPoint', '710')
            if elem.get('firstPoint') == '14': elem.set('firstPoint', '710')

# 3. Back Princess Seam (Shoulder)
p800 = ET.Element('point', {'angle': 'AngleLine_T_Cuello_Ancho_T_Hombro', 'basePoint': '112', 'id': '800', 'length': 'Line_T_Cuello_Ancho_T_Hombro / 2', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'T_Hombro_Medio', 'showPointName': 'true', 'type': 'endLine'})
# Insert 800 before 801
for i, elem in enumerate(calc):
    if elem.get('id') == '801':
        calc.insert(i, p800)
        elem.set('basePoint', '800')
        elem.set('length', '0')
        elem.set('angle', '270')
        break
for elem in calc:
    if elem.get('id') == '802':
        elem.set('basePoint', '801')
        elem.set('length', '0')
        elem.set('angle', '0')
        break

# 4. Fix Back Armhole Splines
to_remove = []
for elem in calc:
    if elem.tag == 'spline':
        if elem.get('id') == '124':
            elem.set('point4', '104')
            elem.set('angle2', '0')
        elif elem.get('id') == '122':
            to_remove.append(elem)
    elif elem.tag == 'point':
        if elem.get('id') in ['2003', '2004', '2005', '999']:
            old_len = elem.get('length', '')
            new_len = old_len.replace('Spl_T_Ancho_Espalda_T_Sisa_Pinza_Sup + Spl_T_Sisa_Pinza_Inf_T_Costado_Sisa', 'Spl_T_Ancho_Espalda_T_Costado_Sisa')
            elem.set('length', new_len)

for elem in to_remove:
    calc.remove(elem)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Chaqueta Dama refactored successfully!")
