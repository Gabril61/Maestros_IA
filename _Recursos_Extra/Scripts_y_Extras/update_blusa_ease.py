import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Medica_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

variables = root.find('.//variables')

new_values = {
    '#holgura_busto': '6',
    '#holgura_cadera': '10',
    '#holgura_espalda': '1.5',
    '#holgura_pecho': '-1.5',
    '#holgura_bicep': '5'
}

for var in variables.findall('variable'):
    name = var.get('name')
    if name in new_values:
        var.set('formula', new_values[name])

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Ease values updated successfully!")
