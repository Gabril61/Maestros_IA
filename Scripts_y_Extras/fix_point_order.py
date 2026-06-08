import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

p701 = calc.find('point[@id="701"]')
p702 = calc.find('point[@id="702"]')
p800 = calc.find('point[@id="800"]')

if p701 is not None: calc.remove(p701)
if p702 is not None: calc.remove(p702)
if p800 is not None: calc.remove(p800)

idx_111 = 0
idx_205 = 0
for i, el in enumerate(calc):
    if el.get('id') == '111': idx_111 = i
    if el.get('id') == '205': idx_205 = i

if p701 is not None: calc.insert(idx_111 + 1, p701)
if p702 is not None: calc.insert(idx_111 + 2, p702)
if p800 is not None: calc.insert(idx_205 + 3, p800) # +3 to be safe

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Points reordered successfully!")
