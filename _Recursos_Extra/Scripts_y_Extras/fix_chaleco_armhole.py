import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Fix armhole depth formula
for p in calc.findall('point'):
    name = p.get('name', '')
    if name in ['F_Linea_Sisa', 'T_Linea_Sisa']:
        p.set('length', '(@S_ANCHO_ESPALDA / 2) + 7.5')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Chaleco armhole depth fixed.")
