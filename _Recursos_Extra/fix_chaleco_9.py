import xml.etree.ElementTree as ET

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

# Update splines for a more stable and anatomic French Curve
for s in root.findall('.//spline'):
    s_id = s.attrib.get('id')
    
    if s_id == '32':
        # Apply the user's validated calibration for lengths
        s.attrib['length1'] = 'Line_F_Hombro_F_Costado_Sisa * 0.25'
        s.attrib['length2'] = 'Line_F_Hombro_F_Costado_Sisa * 0.1'
        
        # Keep the angles that cave the armhole inward
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 25'
        s.attrib['angle2'] = 'AngleLine_F_Hombro_F_Costado_Sisa + 180 - 15'
        
    elif s_id == '33':
        # Harmonize the bottom curve so it doesn't bulge out
        # Keeping angle1 leaving the dart point down-left
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 15'
        s.attrib['angle2'] = '180'
        # Reduce tension here too for stability
        s.attrib['length1'] = 'Line_F_Hombro_F_Costado_Sisa * 0.15'
        s.attrib['length2'] = 'Line_F_Hombro_F_Costado_Sisa * 0.25'

tree.write(val_path, encoding="UTF-8", xml_declaration=True)
print("Fix aplicado: Tensión de Bezier calibrada para evitar bucles (0.25 y 0.1).")
