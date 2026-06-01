import xml.etree.ElementTree as ET

tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val')
root = tree.getroot()

print("Splines involving APEX (14) and Sisa Pinza (701, 702):")
for spline in root.findall('.//spline'):
    p1 = spline.get('point1')
    p4 = spline.get('point4')
    if p1 in ['14', '701', '702'] or p4 in ['14', '701', '702']:
        print(f"Spline ID: {spline.get('id')}, P1: {p1}, P4: {p4}, Angle1: {spline.get('angle1')}, Length1: {spline.get('length1')}, Angle2: {spline.get('angle2')}, Length2: {spline.get('length2')}")

print("\nLines involving APEX (14) and Sisa Pinza (701, 702):")
for line in root.findall('.//line'):
    p1 = line.get('firstPoint')
    p2 = line.get('secondPoint')
    if p1 in ['14', '701', '702'] or p2 in ['14', '701', '702']:
        print(f"Line ID: {line.get('id')}, {p1} -> {p2}")
