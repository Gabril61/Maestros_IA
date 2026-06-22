import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Fix 701 length so it doesn't fly off
p701 = calc.find('point[@id="701"]')
if p701 is not None:
    p701.set('length', '4')

# 2. Add line from 250 to 218
l250_218 = ET.Element('line', {'firstPoint': '250', 'id': '9997', 'lineColor': 'black', 'lineType': 'solid', 'lineWeight': '0.35', 'secondPoint': '218'})

# Insert l250_218 at the end before splines
idx_target = 0
for i, el in enumerate(calc):
    if el.get('id') == '50207':
        idx_target = i
        break
if idx_target == 0: idx_target = len(calc)
calc.insert(idx_target, l250_218)

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Adjustments applied!")
