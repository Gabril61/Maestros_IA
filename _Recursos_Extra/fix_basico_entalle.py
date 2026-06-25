import xml.etree.ElementTree as ET
import os

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

modified = False
for p in root.findall('.//point'):
    name = p.attrib.get('name', '')
    if name in ['F_Costado_Cintura', 'T_Costado_Cintura']:
        old_formula = p.attrib.get('length', '')
        new_formula = "((@S_CONT_BUSTO + #holgura_busto)/4) - ((@S_CONT_BUSTO - @S_CONT_CINTURA)/10)"
        if old_formula != new_formula:
            p.attrib['length'] = new_formula
            print(f"Modificado {name}: {old_formula} -> {new_formula}")
            modified = True

if modified:
    tree.write(val_path, encoding="UTF-8", xml_declaration=True)
    print(f"Archivo guardado exitosamente: {val_path}")
else:
    print("No se requirieron modificaciones.")
