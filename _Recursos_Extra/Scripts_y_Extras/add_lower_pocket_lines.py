import xml.etree.ElementTree as ET

tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val')
calc = tree.getroot().find('.//calculation')

# Add missing lines for lower pocket
lines = [
    ET.Element('line', {'firstPoint': '142', 'id': '73001', 'secondPoint': '143', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '143', 'id': '73002', 'secondPoint': '145', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '145', 'id': '73003', 'secondPoint': '146', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '146', 'id': '73004', 'secondPoint': '144', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '144', 'id': '73005', 'secondPoint': '142', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
]
calc.extend(lines)

xmlstr = ET.tostring(tree.getroot(), encoding='utf-8', method='xml').decode('utf-8')
import re
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(r'c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val', 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Lower pocket lines added.")
