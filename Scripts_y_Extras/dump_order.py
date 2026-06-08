import xml.etree.ElementTree as ET
tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val')
calc = tree.getroot().find('.//calculation')
for i, el in enumerate(calc):
    if 'id' in el.attrib:
        print(i, el.tag, el.get('id'))
