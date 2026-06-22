import xml.etree.ElementTree as ET
tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Caballero_Maestro.val')
calc = tree.getroot().find('.//calculation')
p = calc.find('point[@id="250"]')
if p is not None:
    print(ET.tostring(p, encoding='unicode').strip())
