import xml.etree.ElementTree as ET

tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val')
root = tree.getroot()

for point in root.findall('.//point'):
    name = point.get('name')
    if name:
        print(f"ID: {point.get('id')}, Name: {name}, Formula: {point.get('length', '')} {point.get('basePoint', '')} {point.get('x', '')} {point.get('y', '')}")
