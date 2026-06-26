import xml.etree.ElementTree as ET
filepath = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(filepath)
calc = tree.getroot().find('.//calculation')

p701 = calc.find('.//point[@name="F_Sisa_Pinza_Sup"]')
p702 = calc.find('.//point[@name="F_Sisa_Pinza_Inf"]')
if p701 is not None and p702 is not None:
    print('Sisa Pinza found. IDs:', p701.get('id'), p702.get('id'))
    print(ET.tostring(p702).decode('utf-8').strip())
else:
    print('Sisa Pinza points not found.')

print('\n--- Cuello Mao Splines ---')
for s in calc.findall('.//spline'):
    p1 = s.get('point1')
    p4 = s.get('point4')
    p1_name = next((p.get('name') for p in calc.findall('.//point') if p.get('id') == p1), str(p1))
    p4_name = next((p.get('name') for p in calc.findall('.//point') if p.get('id') == p4), str(p4))
    if 'CM_' in p1_name or 'CM_' in p4_name:
        print(f'Spline {s.get("id")}: {p1_name} -> {p4_name}')
        print(f'  a1={s.get("angle1")} L1={s.get("length1")}')
        print(f'  a2={s.get("angle2")} L2={s.get("length2")}')
