import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

changed = False
for p in root.findall('.//point'):
    if '@D_PROFUN_ESCOTE' in p.get('length', ''):
        p.set('length', '18')
        changed = True

if changed:
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Fixed @D_PROFUN_ESCOTE variable successfully.")
else:
    print("Variable @D_PROFUN_ESCOTE not found.")
