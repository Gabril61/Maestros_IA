import xml.etree.ElementTree as ET
import os

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

modified = False

# 1. Update points
for p in root.findall('.//point'):
    p_id = p.attrib.get('id')
    
    if p_id == '31': # F_Ancho_Pecho
        p.attrib['basePoint'] = '28' # F_Hombro
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa'
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.25'
        modified = True
        
    elif p_id == '701': # F_Sisa_Pinza_Sup
        p.attrib['basePoint'] = '31' # F_Ancho_Pecho
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa'
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.20'
        modified = True
        
    elif p_id == '702': # F_Sisa_Pinza_Inf
        p.attrib['basePoint'] = '701' # F_Sisa_Pinza_Sup
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa'
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.05'
        modified = True

# 2. Update splines
for s in root.findall('.//spline'):
    s_id = s.attrib.get('id')
    
    if s_id == '32':
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 25'
        s.attrib['angle2'] = 'AngleLine_F_Hombro_F_Costado_Sisa + 155'
        modified = True
        
    elif s_id == '34':
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 25'
        s.attrib['angle2'] = 'AngleLine_F_Hombro_F_Costado_Sisa + 155'
        modified = True
        
    elif s_id == '33':
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 25'
        s.attrib['angle2'] = '180'
        modified = True
        
    elif s_id == '207':
        s.attrib['angle1'] = 'AngleLine_F_Sisa_Pinza_Sup_F_APEX - 15'
        s.attrib['angle2'] = 'AngleLine_F_APEX_F_Pinza_P1 - 180'
        modified = True
        
    elif s_id == '209':
        s.attrib['angle1'] = 'AngleLine_F_Sisa_Pinza_Inf_F_APEX + 15'
        s.attrib['angle2'] = 'AngleLine_F_APEX_F_Pinza_P2 - 180'
        modified = True

if modified:
    tree.write(val_path, encoding="UTF-8", xml_declaration=True)
    print("El archivo Chaleco_Femenino_Maestro.val fue modificado exitosamente.")
else:
    print("No se encontraron los nodos a modificar.")
