import xml.etree.ElementTree as ET
try:
    tree = ET.parse('c:/Users/Ricx18/Desktop/Maestros_IA/Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    for spline in root.iter('spline'):
        id_val = spline.get('id')
        if id_val in ['207', '209']:
            print(f"Spline {id_val}:")
            for attr, val in spline.attrib.items():
                print(f"  {attr}: {val}")
except Exception as e:
    print(e)
