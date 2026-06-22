import xml.etree.ElementTree as ET
tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val')
calc = tree.getroot().find('.//calculation')
for pt in ['701', '702', '14', '710', '214', '215']:
    p = calc.find('point[@id="' + pt + '"]')
    if p is not None:
        print(ET.tostring(p, encoding='unicode').strip())
for spline in calc.findall('spline'):
    if spline.get('id') in ['207', '209', '611', '614', '612', '613']:
        print(ET.tostring(spline, encoding='unicode').strip())
