import xml.etree.ElementTree as ET

val_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(val_path)
root = tree.getroot()

changed = False
for p in root.findall('.//point'):
    name = p.attrib.get('name', '')
    if name == 'B_Sup_Der':
        # Use the valid line direction and reverse it mathematically
        p.attrib['angle'] = 'AngleLine_F_Costado_Cintura_F_Costado_Ruedo + 180'
        changed = True

if changed:
    tree.write(val_path, encoding='UTF-8', xml_declaration=True)
    print("Angulo reparado exitosamente.")
else:
    print("No se encontro B_Sup_Der")
