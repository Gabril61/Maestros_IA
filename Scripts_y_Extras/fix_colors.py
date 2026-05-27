import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

changed = False
for tag in ['line', 'spline']:
    for el in root.findall(f'.//{tag}'):
        if el.get('color') == 'red':
            el.set('color', 'black')
            changed = True
        if el.get('lineColor') == 'red':
            el.set('lineColor', 'black')
            changed = True

if changed:
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Fixed colors successfully.")
else:
    print("No red colors found.")
