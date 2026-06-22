import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

# 1. HOLGURAS
variables = root.find('.//variables')
for var in variables.findall('variable'):
    if var.get('name') == '#holgura_bata':
        variables.remove(var)

new_vars = [
    ET.Element('variable', {'description': 'Holgura de busto', 'formula': '6', 'name': '#holgura_busto'}),
    ET.Element('variable', {'description': 'Holgura de cadera', 'formula': '10', 'name': '#holgura_cadera'}),
    ET.Element('variable', {'description': 'Holgura de espalda', 'formula': '1.5', 'name': '#holgura_espalda'}),
    ET.Element('variable', {'description': 'Holgura de pecho', 'formula': '-1.5', 'name': '#holgura_pecho'}),
    ET.Element('variable', {'description': 'Holgura bicep', 'formula': '5', 'name': '#holgura_bicep'})
]
variables.extend(new_vars)

calc = root.find('.//calculation')

formulas = {
    '111': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '119': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '121': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)'},
    '211': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '219': {'length': '((@S_CONT_BUSTO + #holgura_busto)/4)'},
    '221': {'length': '((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)'},
    '261': {'length': '(@S_SEP_BUSTO / 2)'}  # Back dart axis aligned to scapula
}

for pt in calc.findall('point'):
    pid = pt.get('id')
    if pid in formulas:
        for k, v in formulas[pid].items():
            pt.set(k, v)
    if pt.get('length') == '(@S_ANCHO_ESPALDA/2)':
        pt.set('length', '((@S_ANCHO_ESPALDA + #holgura_espalda)/2)')
    if pt.get('length') == '(@S_ANCHO_PECHO/2)':
        pt.set('length', '((@S_ANCHO_PECHO + #holgura_pecho)/2)')

# 2. INJECT NEW POINTS
pt_701 = ET.Element('point', {'angle': 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa', 'basePoint': '110', 'id': '701', 'length': 'Line_F_Ancho_Pecho_F_Costado_Sisa * 0.3', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'name': 'F_Sisa_Pinza_Sup', 'type': 'endLine'})
pt_702 = ET.Element('point', {'angle': 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa', 'basePoint': '701', 'id': '702', 'length': '2', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'name': 'F_Sisa_Pinza_Inf', 'type': 'endLine'})
pt_800 = ET.Element('point', {'angle': 'AngleLine_T_Escote_Ancho_T_Caida_Hombro', 'basePoint': '201', 'id': '800', 'length': 'Line_T_Escote_Ancho_T_Caida_Hombro / 2', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'name': 'T_Hombro_Medio', 'type': 'endLine'})

# Insert points before lines
line_start_idx = 0
for i, el in enumerate(calc):
    if el.tag == 'line':
        line_start_idx = i
        break
if line_start_idx == 0: line_start_idx = len(calc)

calc.insert(line_start_idx, pt_701)
calc.insert(line_start_idx+1, pt_702)
calc.insert(line_start_idx+2, pt_800)

# 3. INJECT LINES
lines_to_add = [
    {'id': '9990', 'firstPoint': '110', 'secondPoint': '111', 'name': 'Line_F_Ancho_Pecho_F_Costado_Sisa'},
    {'id': '9989', 'firstPoint': '201', 'secondPoint': '205', 'name': 'Line_T_Escote_Ancho_T_Caida_Hombro'},
    {'id': '9991', 'firstPoint': '160', 'secondPoint': '701', 'name': 'Line_F_Centro_Busto_F_Sisa_Pinza_Sup'},
    {'id': '9992', 'firstPoint': '160', 'secondPoint': '702', 'name': 'Line_F_Centro_Busto_F_Sisa_Pinza_Inf'},
    {'id': '9993', 'firstPoint': '160', 'secondPoint': '162', 'name': 'Line_F_Centro_Busto_F_Pinza_Izq'},
    {'id': '9994', 'firstPoint': '160', 'secondPoint': '163', 'name': 'Line_F_Centro_Busto_F_Pinza_Der'},
    {'id': '9995', 'firstPoint': '800', 'secondPoint': '263', 'name': 'Line_T_Hombro_Medio_T_Pinza_Izq'},
    {'id': '9996', 'firstPoint': '800', 'secondPoint': '262', 'name': 'Line_T_Hombro_Medio_T_Pinza_Der'}
]

spline_start_idx = len(calc)
for i, el in enumerate(calc):
    if el.tag == 'spline':
        spline_start_idx = i
        break

for l in lines_to_add:
    el = ET.Element('line', {'firstPoint': l['firstPoint'], 'id': l['id'], 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'secondPoint': l['secondPoint']})
    calc.insert(spline_start_idx, el)
    spline_start_idx += 1

# 4. INJECT SPLINES
splines_to_add = [
    # Front Princess
    ET.Element('spline', {'id': '207', 'point1': '701', 'point4': '160', 'angle1': 'AngleLine_F_Centro_Busto_F_Sisa_Pinza_Sup + 165', 'angle2': 'AngleLine_F_Centro_Busto_F_Pinza_Izq - 180', 'length1': 'Line_F_Centro_Busto_F_Sisa_Pinza_Sup * 0.25', 'length2': 'Line_F_Centro_Busto_F_Sisa_Pinza_Sup * 0.25', 'color': 'black', 'type': 'simpleInteractive', 'lineWeight': '0.7'}),
    ET.Element('spline', {'id': '209', 'point1': '702', 'point4': '160', 'angle1': 'AngleLine_F_Centro_Busto_F_Sisa_Pinza_Inf + 165', 'angle2': 'AngleLine_F_Centro_Busto_F_Pinza_Der - 180', 'length1': 'Line_F_Centro_Busto_F_Sisa_Pinza_Inf * 0.25', 'length2': 'Line_F_Centro_Busto_F_Sisa_Pinza_Inf * 0.25', 'color': 'black', 'type': 'simpleInteractive', 'lineWeight': '0.7'}),
    # Back Princess (Bypass Apex)
    ET.Element('spline', {'id': '612', 'point1': '800', 'point4': '263', 'angle1': '270', 'angle2': '90', 'length1': 'Line_T_Hombro_Medio_T_Pinza_Izq * 0.4', 'length2': 'Line_T_Hombro_Medio_T_Pinza_Izq * 0.4', 'color': 'black', 'type': 'simpleInteractive', 'lineWeight': '0.7'}),
    ET.Element('spline', {'id': '613', 'point1': '800', 'point4': '262', 'angle1': '270', 'angle2': '90', 'length1': 'Line_T_Hombro_Medio_T_Pinza_Der * 0.4', 'length2': 'Line_T_Hombro_Medio_T_Pinza_Der * 0.4', 'color': 'black', 'type': 'simpleInteractive', 'lineWeight': '0.7'}),
]

for s in splines_to_add:
    calc.append(s)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Princess seams mathematical injection complete!")
