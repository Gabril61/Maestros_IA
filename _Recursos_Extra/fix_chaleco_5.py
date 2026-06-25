import xml.etree.ElementTree as ET

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

# 1. Update points
for p in root.findall('.//point'):
    p_id = p.attrib.get('id')
    
    if p_id == '701': # F_Sisa_Pinza_Sup
        p.attrib['basePoint'] = '28'
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa + 15' # INWARD
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.45'
        
    elif p_id == '31': # F_Ancho_Pecho (Bypassed)
        p.attrib['basePoint'] = '701'
        p.attrib['angle'] = '0'
        p.attrib['length'] = '0.01' # Effectively invisible
        
    elif p_id == '702': # F_Sisa_Pinza_Inf
        p.attrib['basePoint'] = '701'
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa'
        p.attrib['length'] = '1.5'

# 2. Update splines
for s in root.findall('.//spline'):
    s_id = s.attrib.get('id')
    
    if s_id == '32':
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Sisa_Pinza_Sup + 15'
        s.attrib['angle2'] = 'AngleLine_F_Hombro_F_Sisa_Pinza_Sup + 180 - 15'
        s.attrib['length1'] = 'Line_F_Hombro_F_Sisa_Pinza_Sup * 0.4'
        s.attrib['length2'] = 'Line_F_Hombro_F_Sisa_Pinza_Sup * 0.4'
        
    elif s_id == '34': # Invisible spline
        s.attrib['angle1'] = '0'
        s.attrib['angle2'] = '180'
        s.attrib['length1'] = '0'
        s.attrib['length2'] = '0'
        
    elif s_id == '33':
        s.attrib['angle1'] = 'AngleLine_F_Sisa_Pinza_Inf_F_Costado_Sisa + 20'
        s.attrib['angle2'] = '180'
        s.attrib['length1'] = 'Line_F_Sisa_Pinza_Inf_F_Costado_Sisa * 0.4'
        s.attrib['length2'] = 'Line_F_Sisa_Pinza_Inf_F_Costado_Sisa * 0.4'
        
    elif s_id == '207': # Princess seam (no S curve)
        s.attrib['angle1'] = 'AngleLine_F_Sisa_Pinza_Sup_F_APEX + 10'
        s.attrib['angle2'] = 'AngleLine_F_Sisa_Pinza_Sup_F_APEX + 180 - 10'
        s.attrib['length1'] = 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.35'
        s.attrib['length2'] = 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.35'
        
    elif s_id == '209':
        s.attrib['angle1'] = 'AngleLine_F_Sisa_Pinza_Inf_F_APEX + 10'
        s.attrib['angle2'] = 'AngleLine_F_Sisa_Pinza_Inf_F_APEX + 180 - 10'
        s.attrib['length1'] = 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.35'
        s.attrib['length2'] = 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.35'

tree.write(val_path, encoding="UTF-8", xml_declaration=True)
print("Fix aplicado: F_Ancho_Pecho bypassado y sumas vectoriales corregidas.")
