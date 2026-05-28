import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
for line in tree.getroot().findall('.//line'):
    fp = line.get('firstPoint')
    sp = line.get('secondPoint')
    if fp == '232' and sp not in ['231', '31002']:
        print(f"id={line.get('id')} first={fp} second={sp}")
    if sp == '232' and fp not in ['231', '31002']:
        print(f"id={line.get('id')} first={fp} second={sp}")
