import xml.etree.ElementTree as ET
tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Caballero_Maestro.val')
calc = tree.getroot().find('.//calculation')
for pt in ['211', '219', '221']:
    p = calc.find('point[@id="' + pt + '"]')
    if p is not None:
        print(p.get('id'), p.get('name'), p.get('basePoint'), p.get('angle'))
for spline in calc.findall('spline'):
    if spline.get('id') == '247':
        print('SPLINE 247:', spline.get('point1'), spline.get('point4'))
