import xml.etree.ElementTree as ET
import os

file_path = "Chaleco_Femenino_Maestro.val"
tree = ET.parse(file_path)
root = tree.getroot()

def find_by_id(tag, element_id):
    for elem in root.iter(tag):
        if elem.get('id') == element_id:
            return elem
    return None

# 1. F_Ancho_Pecho (31): Anclar al centro frontal con medida proporcional
pt_31 = find_by_id('point', '31')
if pt_31 is not None:
    pt_31.set('basePoint', '30')
    pt_31.set('angle', '0')
    pt_31.set('length', '(@S_ANCHO_ESPALDA / 2) - 1.5')
    print("-> F_Ancho_Pecho (31) reconfigurado a basePoint 30 con longitud paramétrica.")

# 2. Spline superior (32)
sp_32 = find_by_id('spline', '32')
if sp_32 is not None:
    sp_32.set('angle2', 'AngleLine_F_Ancho_Pecho_F_Hombro + 20')
    print("-> Spline 32 tangencia ajustada.")

# 3. Spline medio (34)
sp_34 = find_by_id('spline', '34')
if sp_34 is not None:
    sp_34.set('angle1', 'AngleLine_F_Hombro_F_Ancho_Pecho + 20')
    sp_34.set('angle2', 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa + 180')
    sp_34.set('length1', 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup * 0.35')
    sp_34.set('length2', 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup * 0.35')
    print("-> Spline 34 liberada de ángulos fijos (130 -> tangencia dinámica).")

# 4. Spline inferior (33)
sp_33 = find_by_id('spline', '33')
if sp_33 is not None:
    sp_33.set('angle1', 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa')
    sp_33.set('angle2', '180')
    sp_33.set('length1', 'Line_F_Sisa_Pinza_Inf_F_Costado_Sisa * 0.35')
    sp_33.set('length2', 'Line_F_Sisa_Pinza_Inf_F_Costado_Sisa * 0.35')
    print("-> Spline 33 conectada geométricamente a Spline 34 (270 -> tangencia dinámica).")

# 5. Profundidad Pinza Sisa (702)
pt_702 = find_by_id('point', '702')
if pt_702 is not None:
    pt_702.set('length', 'Line_F_Ancho_Pecho_F_Costado_Sisa * 0.15')
    print("-> F_Sisa_Pinza_Inf (702) convertida de absoluta (2cm) a paramétrica.")

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Archivos actualizados correctamente.")
