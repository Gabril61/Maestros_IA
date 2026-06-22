import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
calc = tree.getroot().find('draftBlock/calculation')
for child in calc:
    if child.tag == 'line':
        fp = child.get('firstPoint')
        sp = child.get('secondPoint')
        if '802' in [fp, sp] or '232' in [fp, sp]:
            print(f"id={child.get('id')} first={fp} second={sp}")
