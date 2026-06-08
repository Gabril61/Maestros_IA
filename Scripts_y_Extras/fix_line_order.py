import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

lines_to_move = ['9991', '9992', '9993', '9994', '9995', '9996']
elements_to_move = []

for lid in lines_to_move:
    line_el = calc.find('line[@id="' + lid + '"]')
    if line_el is not None:
        elements_to_move.append(line_el)
        calc.remove(line_el)

idx_target = 0
for i, el in enumerate(calc):
    if el.get('id') == '50207':
        idx_target = i
        break

if idx_target == 0: idx_target = len(calc)

for line_el in elements_to_move:
    calc.insert(idx_target, line_el)
    idx_target += 1

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Line order for 160 fixed!")
