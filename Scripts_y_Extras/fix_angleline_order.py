import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

line9990 = calc.find('line[@id="9990"]')
line9989 = calc.find('line[@id="9989"]')

if line9990 is not None: calc.remove(line9990)
if line9989 is not None: calc.remove(line9989)

idx_701 = 0
idx_800 = 0
for i, el in enumerate(calc):
    if el.get('id') == '701': idx_701 = i
    if el.get('id') == '800': idx_800 = i

# Insert line 9990 BEFORE 701
if line9990 is not None: calc.insert(idx_701, line9990)
# Note: idx_800 might have shifted by 1 because we inserted 9990
# But let's recalculate to be safe
idx_800 = 0
for i, el in enumerate(calc):
    if el.get('id') == '800': idx_800 = i
if line9989 is not None: calc.insert(idx_800, line9989)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Line order for points fixed!")
