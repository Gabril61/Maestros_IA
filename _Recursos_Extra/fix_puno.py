import xml.etree.ElementTree as ET

val_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(val_path)
root = tree.getroot()

changed = False
for p in root.findall('.//point'):
    name = p.attrib.get('name', '')
    if name == 'M_Puno_Izq':
        p.attrib['length'] = '(@S_CONT_SISA / 2) * 0.85 + (#holgura_manga_corta / 2)'
        changed = True
    elif name == 'M_Puno_Der':
        p.attrib['length'] = '(@S_CONT_SISA / 2) * 0.85 + (#holgura_manga_corta / 2)'
        changed = True

if changed:
    tree.write(val_path, encoding='UTF-8', xml_declaration=True)
    print("Formula reparada exitosamente.")
else:
    print("No se encontro M_Puno_Izq")
