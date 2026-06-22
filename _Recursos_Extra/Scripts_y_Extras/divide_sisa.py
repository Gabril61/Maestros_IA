import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

s115 = calc.find('spline[@id="115"]')
if s115 is not None:
    calc.remove(s115)

s115A = ET.Element('spline', {
    'id': '50115', 
    'point1': '110', 
    'point4': '701', 
    'angle1': '270', 
    'angle2': '180', 
    'length1': '2', 
    'length2': '2', 
    'color': 'black', 
    'type': 'simpleInteractive', 
    'lineWeight': '0.35'
})

s115B = ET.Element('spline', {
    'id': '50116', 
    'point1': '702', 
    'point4': '111', 
    'angle1': '270', 
    'angle2': '180', 
    'length1': '3', 
    'length2': '3', 
    'color': 'black', 
    'type': 'simpleInteractive', 
    'lineWeight': '0.35'
})

idx_target = 0
for i, el in enumerate(calc):
    if el.get('id') == '50207':
        idx_target = i
        break
if idx_target == 0: idx_target = len(calc)

calc.insert(idx_target, s115A)
calc.insert(idx_target, s115B)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Sisa dividida!")
