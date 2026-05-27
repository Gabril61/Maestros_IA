import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

changed = False
for p in root.findall('.//point'):
    length = p.get('length', '')
    if '@S_TALLE_DELANTERO' in length:
        p.set('length', length.replace('@S_TALLE_DELANTERO', '@S_TALLEDEL'))
        changed = True
    if '@S_TALLE_TRASERO' in length:
        p.set('length', length.replace('@S_TALLE_TRASERO', '@S_TALLETRA'))
        changed = True

if changed:
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Fixed formula variables successfully.")
else:
    print("No variables found to replace.")
