import xml.etree.ElementTree as ET
tree = ET.parse('c:/Users/Ricx18/Desktop/Maestros_IA/Chaleco_Femenino_Maestro.val')
root = tree.getroot()

id_to_name = {}
for p in root.findall('.//point'):
    id_to_name[p.get('id')] = p.get('name')

print('Splines touching F_APEX:')
for s in root.findall('.//spline'):
    p1_name = id_to_name.get(s.get('point1', ''))
    p4_name = id_to_name.get(s.get('point4', ''))
    if p1_name == 'F_APEX' or p4_name == 'F_APEX':
        print('Spline ID:', s.get('id'), p1_name, '->', p4_name)
        print('  angle1:', s.get('angle1'), 'length1:', s.get('length1'))
        print('  angle2:', s.get('angle2'), 'length2:', s.get('length2'))

print('\nLooking for lapel points...')
for p in root.findall('.//point'):
    name = p.get('name', '')
    if name in ['A1', 'A2', 'A7_Piquete', 'B_Boton_1', 'B_Cruce_Sup']:
        print(name, '-> type:', p.get('type'), 'length:', p.get('length'), 'angle:', p.get('angle'))
