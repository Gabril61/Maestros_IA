import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

changed = False
for s in calc.findall('spline'):
    if not s.get('type'):
        s.set('type', 'simpleInteractive')
        changed = True

if changed:
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Fixed missing spline types.")
else:
    print("No missing spline types found.")
