import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Medica_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

calc = root.find('.//calculation')

# Find and extract 90005 and 90006
p90005 = None
p90006 = None

to_remove = []
for elem in calc:
    if elem.get('id') == '90005':
        p90005 = elem
        to_remove.append(elem)
    elif elem.get('id') == '90006':
        p90006 = elem
        to_remove.append(elem)

for elem in to_remove:
    calc.remove(elem)

# Find 210 and insert before it
anchor_idx = 0
for i, elem in enumerate(calc):
    if elem.get('id') == '210':
        anchor_idx = i
        break

if p90005 is not None and p90006 is not None:
    calc.insert(anchor_idx, p90005)
    calc.insert(anchor_idx + 1, p90006)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("XML order fixed!")
