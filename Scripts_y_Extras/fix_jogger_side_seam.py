import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Dama_Jogger_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

changed = False
for p in root.findall('.//point'):
    if p.get('name') == 'T_Guia_Cintura_Cost':
        current_len = p.get('length')
        if current_len == '@I_ALTO_TIRO - 1':
            p.set('length', '@I_ALTO_TIRO')
            changed = True
            print("Fixed T_Guia_Cintura_Cost length (-1 removed).")
        else:
            print(f"Current length is {current_len}, doing nothing.")

if changed:
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("File saved successfully.")
