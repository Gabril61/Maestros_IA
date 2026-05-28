import xml.etree.ElementTree as ET
import os
files = [
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val'
]
for f in files:
    tree = ET.parse(f)
    for line in tree.getroot().findall('.//line'):
        if line.get('firstPoint') == '232' or line.get('secondPoint') == '232' or line.get('id') == '249':
            fname = os.path.basename(f)
            print(f"{fname}: id={line.get('id')} first={line.get('firstPoint')} second={line.get('secondPoint')}")
