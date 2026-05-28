import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
calc = tree.getroot().find('draftBlock/calculation')
for child in calc:
    if child.tag == 'point' and child.get('name') == 'T_Pasamanos_Bot':
        print(f"T_Pasamanos_Bot is {child.get('id')}")
