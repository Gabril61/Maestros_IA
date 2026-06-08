import xml.etree.ElementTree as ET
tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val')
calc = tree.getroot().find('.//calculation')
pts = ['701', '702', '710', '202', '203', '204', '213', '214', '215', '801', '802', '810', '601', '602', '610']
for pt_id in pts:
    pt = calc.find(f'point[@id="{pt_id}"]')
    if pt is not None:
        print(ET.tostring(pt, encoding='unicode').strip())
