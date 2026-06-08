import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

# Insert invisible lines 14 to 701 and 14 to 702
line_sup = ET.Element('line', {'firstPoint': '14', 'id': '9991', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'secondPoint': '701'})
line_inf = ET.Element('line', {'firstPoint': '14', 'id': '9992', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'secondPoint': '702'})

# Ensure they are inserted BEFORE point 710 is defined, or just at the beginning of the lines block
# Actually, lines can be defined anywhere as long as the points exist. 14, 701, 702 are already defined.
# I will just insert them right after point 702.

for i, elem in enumerate(calc):
    if elem.get('id') == '702':
        calc.insert(i + 1, line_sup)
        calc.insert(i + 2, line_inf)
        break

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Fixed AngleLine bug!")
