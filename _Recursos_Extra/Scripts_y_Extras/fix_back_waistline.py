import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Pantalon_Medico_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Find line 226 and change its lineType to solidLine
for line in calc.findall('line'):
    if line.get('id') == '226':
        line.set('lineType', 'solidLine')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Back waistline made visible.")
