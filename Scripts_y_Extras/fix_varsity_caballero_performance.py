import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

for s in calc.findall('spline'):
    if s.get('id') == '80001':
        s.set('length1', '6')
        s.set('length2', '7')
    elif s.get('id') == '80002':
        s.set('length1', '6')
        s.set('length2', '7')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Spline handles simplified to constant lengths.")
