import xml.etree.ElementTree as ET

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

# 1. Update points to be carved inward
for p in root.findall('.//point'):
    p_id = p.attrib.get('id')
    
    if p_id == '31': # F_Ancho_Pecho
        p.attrib['basePoint'] = '28'
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 12'
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.25'
        
    elif p_id == '701': # F_Sisa_Pinza_Sup
        p.attrib['basePoint'] = '28'
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 18'
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.5'
        
    elif p_id == '702': # F_Sisa_Pinza_Inf
        p.attrib['basePoint'] = '28'
        p.attrib['angle'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 15'
        p.attrib['length'] = 'Line_F_Hombro_F_Costado_Sisa * 0.55'

# 2. Update splines
for s in root.findall('.//spline'):
    s_id = s.attrib.get('id')
    
    # Armhole curves
    if s_id == '32':
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 20'
        s.attrib['angle2'] = 'AngleLine_F_Hombro_F_Costado_Sisa + 160'
        
    elif s_id == '34':
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 20'
        s.attrib['angle2'] = 'AngleLine_F_Hombro_F_Costado_Sisa + 160'
        
    elif s_id == '33':
        s.attrib['angle1'] = 'AngleLine_F_Hombro_F_Costado_Sisa - 20'
        s.attrib['angle2'] = '180'
        
    # Princess Seam curves
    elif s_id == '207':
        s.attrib['angle1'] = 'AngleLine_F_Sisa_Pinza_Sup_F_APEX'
        s.attrib['angle2'] = 'AngleLine_F_APEX_F_Pinza_P1 - 180'
        
    elif s_id == '209':
        s.attrib['angle1'] = 'AngleLine_F_Sisa_Pinza_Inf_F_APEX'
        s.attrib['angle2'] = 'AngleLine_F_APEX_F_Pinza_P2 - 180'

# 3. Inject lines safely if missing
calculation = root.find('.//calculation')
def add_line(first_point, second_point, id_str, insert_after_id):
    for el in calculation:
        if el.tag == 'line' and el.attrib.get('firstPoint') == first_point and el.attrib.get('secondPoint') == second_point:
            return False
    index = -1
    for i, el in enumerate(calculation):
        if el.attrib.get('id') == insert_after_id:
            index = i + 1
            break
    if index != -1:
        line_el = ET.Element('line', {
            'firstPoint': first_point,
            'id': id_str,
            'lineColor': 'black',
            'lineType': 'none',
            'lineWeight': '0.35',
            'secondPoint': second_point
        })
        calculation.insert(index, line_el)
        return True
    return False

add_line('701', '14', '19998', '701')
add_line('702', '14', '19997', '702')

tree.write(val_path, encoding="UTF-8", xml_declaration=True)
print("Fix aplicado: Puntos cavados y Curvas 'S' erradicadas.")
