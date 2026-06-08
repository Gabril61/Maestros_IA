import xml.etree.ElementTree as ET
tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val')
calc = tree.getroot().find('.//calculation')
for pt_id in ['14', '701', '702']:
    pt = calc.find(f'point[@id="{pt_id}"]')
    if pt is not None:
        print(pt.get('id'), pt.get('name'))
