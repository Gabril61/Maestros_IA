import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

# Find the splines we injected and rename their IDs
for spline in calc.findall('spline'):
    if spline.get('id') == '207' and spline.get('point1') == '701':
        spline.set('id', '50207')
    elif spline.get('id') == '209' and spline.get('point1') == '702':
        spline.set('id', '50209')
    elif spline.get('id') == '612' and spline.get('point1') == '800':
        spline.set('id', '50612')
    elif spline.get('id') == '613' and spline.get('point1') == '800':
        spline.set('id', '50613')

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Spline IDs fixed!")
