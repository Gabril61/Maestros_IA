import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val')
for p in tree.getroot().findall('.//piece'):
    if p.get('name') in ['Manga', 'Cuello', 'Centro_Espalda']:
        nodes = p.findall('.//node')
        ids = [n.get('idObject') for n in nodes]
        print(f"{p.get('name')}: {ids}")
