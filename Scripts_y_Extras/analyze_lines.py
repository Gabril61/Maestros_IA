import xml.etree.ElementTree as ET

tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val')
root = tree.getroot()

print("Lines involving pinza bottom points:")
for line in root.findall('.//line'):
    p1 = line.get('firstPoint')
    p2 = line.get('secondPoint')
    if p1 in ['501', '502', '601', '602', '202', '213'] or p2 in ['501', '502', '601', '602', '202', '213']:
        print(f"Line ID: {line.get('id')}, {p1} -> {p2}")

print("Splines involving pinza bottom points:")
for spline in root.findall('.//spline'):
    p1 = spline.get('point1')
    p4 = spline.get('point4')
    if p1 in ['501', '502', '601', '602'] or p4 in ['501', '502', '601', '602']:
        print(f"Spline ID: {spline.get('id')}, {p1} -> {p4}")
