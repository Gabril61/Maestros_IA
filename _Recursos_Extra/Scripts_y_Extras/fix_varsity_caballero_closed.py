import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Fix angle formulas for closed side seams by removing the dart angle difference
for p in calc.findall('point'):
    if p.get('id') == '9001':
        p.set('angle', 'AngleLine_F_APEX_F_Costado_Sisa')
    elif p.get('id') == '9002':
        p.set('angle', 'AngleLine_T_Apex_Espalda_T_Costado_Sisa')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Closed side seam points fixed.")
