import xml.etree.ElementTree as ET
import re

filepath = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
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

    print('POINTS TO CHECK:')
    calc = tree.getroot().find('.//calculation')
    for pt in ['14', '701', '702', '710', '213', '800', '801', '802', '610']:
        p = calc.find('point[@id="' + pt + '"]')
        if p is not None:
            print(p.get('id'), p.get('name'), p.get('basePoint'))
except FileNotFoundError:
    print('File not found:', filepath)
