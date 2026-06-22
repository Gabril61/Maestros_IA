import xml.etree.ElementTree as ET
tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val')
calc = tree.getroot().find('.//calculation')
for line in calc.findall('line'):
    p1 = calc.find('point[@id="' + str(line.get('firstPoint')) + '"]')
    p2 = calc.find('point[@id="' + str(line.get('secondPoint')) + '"]')
    n1 = p1.get('name') if p1 is not None else str(line.get('firstPoint'))
    n2 = p2.get('name') if p2 is not None else str(line.get('secondPoint'))
    print(line.get('id'), n1, n2)
