import xml.etree.ElementTree as ET
import os
files = [
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val'
]
for f in files:
    tree = ET.parse(f)
    print(f"--- {os.path.basename(f)} ---")
    for line in tree.getroot().findall('.//line'):
        fp = line.get('firstPoint')
        sp = line.get('secondPoint')
        if fp in ['221', '218', '232', '31002', '31003', '30035', '30036', '231'] or sp in ['221', '218', '232', '31002', '31003', '30035', '30036', '231']:
            print(f"id={line.get('id')} first={fp} second={sp}")
