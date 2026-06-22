import xml.etree.ElementTree as ET
import re

filepath = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Caballero_Maestro.val'
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'\n\s*\n', '\n', text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

    tree = ET.parse(filepath)
    root = tree.getroot()

    print('VARIABLES:')
    for var in root.findall('.//variable'):
        print(var.get('name'), var.get('formula'))

    print('COSTADOS Y SISA:')
    calc = root.find('.//calculation')
    for pt in ['4', '5', '6', '1302', '1303', '103', '104', '105', '402', '403', '3', '102']:
        p = calc.find('point[@id="' + pt + '"]')
        if p is not None:
            print(p.get('id'), p.get('name'), p.get('length'))
except FileNotFoundError:
    print("File not found:", filepath)
