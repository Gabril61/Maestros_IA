import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

line9993 = calc.find('line[@id="9993"]')
line9994 = calc.find('line[@id="9994"]')

if line9993 is not None: calc.remove(line9993)
if line9994 is not None: calc.remove(line9994)

idx = 0
for i, elem in enumerate(calc):
    if elem.get('id') == '612':
        idx = i
        break

if line9993 is not None: calc.insert(idx, line9993)
if line9994 is not None: calc.insert(idx + 1, line9994)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Reordered lines for Back Princess Seam!")
