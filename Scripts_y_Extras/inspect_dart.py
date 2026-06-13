import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val')
calc = tree.find('.//calculation')

p101 = calc.find(".//*[@id='101']")
if p101 is not None:
    print("Point 101:", p101.attrib)

print("\nAll points containing 'E_' (Espalda):")
for p in calc.findall('point'):
    name = p.get('name', '')
    if name.startswith('E_') or 'E_Centro' in name:
        print(f"ID: {p.get('id')}, Name: {name}, Attr: {p.attrib}")
