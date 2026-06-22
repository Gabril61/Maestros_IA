import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val')
for line in tree.getroot().findall('.//line'):
    if line.get('firstPoint') in ['30035', '30036'] or line.get('secondPoint') in ['30035', '30036']:
        print(f"Estandar: id={line.get('id')} first={line.get('firstPoint')} second={line.get('secondPoint')}")

tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
for line in tree.getroot().findall('.//line'):
    if line.get('firstPoint') in ['31002', '31003'] or line.get('secondPoint') in ['31002', '31003']:
        print(f"Unisex: id={line.get('id')} first={line.get('firstPoint')} second={line.get('secondPoint')}")
