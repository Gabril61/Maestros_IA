import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
for line in tree.getroot().findall('.//line'):
    print(f"id={line.get('id')} first={line.get('firstPoint')} second={line.get('secondPoint')}")
