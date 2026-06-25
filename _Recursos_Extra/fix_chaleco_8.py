import xml.etree.ElementTree as ET

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

# 1. Update points (Subtract to carve INWARD more aggressively)
for p in root.findall('.//point'):
    p_id = p.attrib.get('id')
    
    if p_id == '701': # F_Sisa_Pinza_Sup
        # Increase subtraction from -12 to -18 for a deeper armhole "cave"
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 18' 
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.45'
        
    elif p_id == '31': # F_Ancho_Pecho (Bypassed but kept valid for XML sequence)
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 18'
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.45'
        
    elif p_id == '702': # F_Sisa_Pinza_Inf
        p.attrib['basePoint'] = '701'
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 18' # point slightly inward
        p.attrib['length'] = '1.5'

# 2. Update splines for a true French Curve (Sisa)
for s in root.findall('.//spline'):
    s_id = s.attrib.get('id')
    
    if s_id == '32':
        # Leaves shoulder pointing down/inward (-25)
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 25'
        # Arrives at the midpoint slightly more vertical than the chord
        s.attrib['angle2'] = 'AngleLine_F_Hombro_F_Costado_Sisa + 180 - 15'
        # Increase tension to push the curve deeper
        s.attrib['length1'] = 'Line_F_Hombro_F_Costado_Sisa * 0.35'
        s.attrib['length2'] = 'Line_F_Hombro_F_Costado_Sisa * 0.30'
        
    elif s_id == '34': # Invisible spline
        pass
        
    elif s_id == '33':
        # Leaves midpoint pointing down/inward steeper than the chord
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 15'
        # Arrives at armpit horizontally
        s.attrib['angle2'] = '180'
        s.attrib['length1'] = 'Line_F_Hombro_F_Costado_Sisa * 0.30'
        s.attrib['length2'] = 'Line_F_Hombro_F_Costado_Sisa * 0.25'

tree.write(val_path, encoding="UTF-8", xml_declaration=True)
print("Fix aplicado: Curvatura de sisa profundizada (Efecto French Curve).")
