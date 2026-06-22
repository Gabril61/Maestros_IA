import xml.etree.ElementTree as ET
tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val')
calc = tree.getroot().find('.//calculation')
for pt in ['110', '111', '701', '702']:
    p = calc.find('point[@id="' + pt + '"]')
    if p is not None:
        print(ET.tostring(p, encoding='unicode').strip())
