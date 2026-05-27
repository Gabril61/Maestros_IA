import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Update hem drop to be shorter for a vest (e.g. 12 cm below waist)
# Currently it is '@G_ALTO_CADERA + 6'
pts_to_update = ['F_Ruedo', 'F_Ruedo_Pinza', 'T_Ruedo', 'T_Ruedo_Pinza']
for p in calc.findall('point'):
    if p.get('name') in pts_to_update:
        # Change the length to 12 cm (which represents the distance from the waistline down)
        p.set('length', '12')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Chaleco length shortened to 12 cm below waist.")
