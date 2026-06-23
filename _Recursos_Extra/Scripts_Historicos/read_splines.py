import xml.etree.ElementTree as ET

tree = ET.parse('c:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val')
root = tree.getroot()

for spline in root.iter('spline'):
    id_val = spline.get('id')
    if id_val and id_val.startswith('120') and len(id_val) == 5:
        print(f"Spline {id_val}:")
        print(f"  length1: {spline.get('length1')}")
        print(f"  length2: {spline.get('length2')}")
