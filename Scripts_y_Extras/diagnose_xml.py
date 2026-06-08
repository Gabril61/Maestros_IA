import xml.etree.ElementTree as ET

tree = ET.parse('Bata_Medica_Caballero_Maestro.val')
root = tree.getroot()

modeling = root.find('.//modeling')
paths = modeling.findall('.//path')
print('Paths in modeling:')
for p in paths:
    print(p.attrib.get('id'), p.attrib.get('name'))

delantero = root.find('.//piece[@name="Delantero"]')
print('\nRecords in Delantero:')
if delantero is not None:
    for r in delantero.findall('.//record'):
        print(r.attrib.get('path'))
else:
    print('Delantero not found')
