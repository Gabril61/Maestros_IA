import xml.etree.ElementTree as ET

val_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(val_path)
calc = tree.find('.//calculation')

point_names = {}
for p in calc.findall('.//point'):
    point_names[p.attrib.get('id')] = p.attrib.get('name')

print("Todas las lineas en la manga:")
for l in calc.findall('.//line'):
    p1 = l.attrib.get('firstPoint')
    p2 = l.attrib.get('secondPoint')
    n1 = point_names.get(p1, '')
    n2 = point_names.get(p2, '')
    if n1.startswith('M_') or n2.startswith('M_'):
        print(f"Line_{n1}_{n2}")
