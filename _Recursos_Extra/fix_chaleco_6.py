import xml.etree.ElementTree as ET

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

# Fix the sequence error for F_Ancho_Pecho (ID 31)
for p in root.findall('.//point'):
    p_id = p.attrib.get('id')
    if p_id == '31': # F_Ancho_Pecho
        p.attrib['basePoint'] = '28' # F_Hombro instead of 701
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa + 15'
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.45'

tree.write(val_path, encoding="UTF-8", xml_declaration=True)
print("Fix aplicado: F_Ancho_Pecho independizado para respetar el orden XML.")
