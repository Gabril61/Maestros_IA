import xml.etree.ElementTree as ET

file_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

ids_to_remove = ['12041', '12042', '14005', '12045', '12044']
removed_count = 0

for parent in root.iter():
    to_remove = []
    for child in parent:
        if child.get('id') in ids_to_remove:
            to_remove.append(child)
    for child in to_remove:
        parent.remove(child)
        removed_count += 1
        print(f"Removed element with ID: {child.get('id')}")

if removed_count > 0:
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Archivo Blazer_Dama_Maestro.val guardado con éxito.")
else:
    print("No se encontraron elementos para eliminar.")
