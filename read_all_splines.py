import xml.etree.ElementTree as ET

tree = ET.parse('c:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val')
root = tree.getroot()

for spline in root.iter('spline'):
    id_val = spline.get('id')
    print(f"Spline {id_val}: length1={spline.get('length1')}, length2={spline.get('length2')}")
