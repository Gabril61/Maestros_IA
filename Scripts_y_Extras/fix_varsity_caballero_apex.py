import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Replace invalid Line reference with a constant equivalent (7 cm)
for p in calc.findall('point'):
    if p.get('id') == '610':
        p.set('length', '7')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("T_Apex_Espalda formula fixed.")
