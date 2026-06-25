import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/Ricx18/Desktop/Maestros_IA/Chaleco_Femenino_Maestro.val')
spline_ids = {}
for p in tree.findall('.//point'):
    spline_ids[p.attrib.get('id')] = p.attrib.get('name')
for spline in tree.findall('.//spline'):
    p1 = spline.attrib.get('point1')
    p4 = spline.attrib.get('point4')
    if p1 in spline_ids and p4 in spline_ids:
        print(f"{spline.attrib.get('id')}: Spl_{spline_ids[p1]}_{spline_ids[p4]}")
        print(f"  angle1: {spline.attrib.get('angle1')}")
        print(f"  length1: {spline.attrib.get('length1')}")
        print(f"  angle2: {spline.attrib.get('angle2')}")
        print(f"  length2: {spline.attrib.get('length2')}")
