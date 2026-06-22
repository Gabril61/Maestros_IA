import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

line208 = calc.find('line[@id="208"]')
line210 = calc.find('line[@id="210"]')

if line208 is not None: calc.remove(line208)
if line210 is not None: calc.remove(line210)

# find index of spline 207
idx = 0
for i, elem in enumerate(calc):
    if elem.get('id') == '207':
        idx = i
        break

if line208 is not None: calc.insert(idx, line208)
if line210 is not None: calc.insert(idx + 1, line210)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Reordered lines to fix parsing error!")
