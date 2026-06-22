import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
for spline in tree.getroot().findall('.//spline'):
    for k, v in spline.attrib.items():
        if v in ['221', '232', '31002', '31003', '218']:
            print(f"spline id={spline.get('id')} uses {v} as {k}")
