import xml.etree.ElementTree as ET

tree = ET.parse('c:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val')
root = tree.getroot()

for p in root.iter('point'):
    name = p.get('name', '')
    if 'MS_' in name:
        print("Point:", name)

for p in root.iter('line'):
    print("Line ID:", p.get('id'))
