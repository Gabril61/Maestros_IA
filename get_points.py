import xml.etree.ElementTree as ET

tree = ET.parse('c:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val')
root = tree.getroot()

points = ['12000', '12006', '12004', '12007', '12005']
for p in root.iter('point'):
    if p.get('id') in points:
        print(f"ID: {p.get('id')}, Name: {p.get('name')}")
