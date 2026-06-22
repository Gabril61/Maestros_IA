import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Restore 701 length to Blazer standard
p701 = calc.find('point[@id="701"]')
if p701 is not None:
    p701.set('length', 'Line_F_Ancho_Pecho_F_Costado_Sisa * 0.3')

# 2. Remove my bad splines
s50115 = calc.find('spline[@id="50115"]')
s50116 = calc.find('spline[@id="50116"]')
if s50115 is not None: calc.remove(s50115)
if s50116 is not None: calc.remove(s50116)

# 3. Add necessary lines for the lengths
lines_to_add = [
    {'id': '9980', 'firstPoint': '110', 'secondPoint': '701', 'name': 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup'},
    {'id': '9981', 'firstPoint': '702', 'secondPoint': '111', 'name': 'Line_F_Sisa_Pinza_Inf_F_Costado_Sisa'},
    {'id': '9982', 'firstPoint': '105', 'secondPoint': '110', 'name': 'Line_F_Caida_Hombro_F_Ancho_Pecho'}
]

idx_target = 0
for i, el in enumerate(calc):
    if el.get('id') == '50207':
        idx_target = i
        break
if idx_target == 0: idx_target = len(calc)

for l in lines_to_add:
    el = ET.Element('line', {'firstPoint': l['firstPoint'], 'id': l['id'], 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'secondPoint': l['secondPoint']})
    calc.insert(idx_target, el)
    idx_target += 1

# 4. Add perfect Blazer splines
s1 = ET.Element('spline', {
    'id': '50115', 
    'point1': '110', 
    'point4': '701', 
    'angle1': 'AngleLine_F_Caida_Hombro_F_Ancho_Pecho + 20', 
    'angle2': 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa + 180', 
    'length1': 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup * 0.35', 
    'length2': 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup * 0.35', 
    'color': 'black', 
    'type': 'simpleInteractive', 
    'lineWeight': '0.7'
})

s2 = ET.Element('spline', {
    'id': '50116', 
    'point1': '702', 
    'point4': '111', 
    'angle1': 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa', 
    'angle2': '180', 
    'length1': 'Line_F_Sisa_Pinza_Inf_F_Costado_Sisa * 0.4', 
    'length2': 'Line_F_Sisa_Pinza_Inf_F_Costado_Sisa * 0.3', 
    'color': 'black', 
    'type': 'simpleInteractive', 
    'lineWeight': '0.7'
})

calc.insert(idx_target, s1)
calc.insert(idx_target+1, s2)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Perfect Blazer Armhole calibration applied!")
