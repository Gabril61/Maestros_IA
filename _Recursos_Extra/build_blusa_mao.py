import xml.etree.ElementTree as ET

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

# 1. Variables
variables_node = root.find('.//variables')
if variables_node is not None:
    vars_to_add = {
        '#largo_manga_corta': '20',
        '#altura_cuello_mao': '3.5',
        '#ancho_bolsillo': '16',
        '#alto_bolsillo': '18',
        '#holgura_manga_corta': '3'
    }
    existing_vars = [v.attrib.get('name') for v in variables_node.findall('variable')]
    for k, v in vars_to_add.items():
        if k not in existing_vars:
            ET.SubElement(variables_node, 'variable', {'name': k, 'value': v, 'description': ''})

# 2. Modify Sleeve
for p in root.findall('.//point'):
    name = p.attrib.get('name', '')
    if name == 'M_Largo':
        # min(#largo_manga_corta, 28) logic
        p.attrib['length'] = 'min(#largo_manga_corta, 28)'
    elif name == 'M_Puno_Izq':
        p.attrib['length'] = 'Line_M_Origen_M_Ancho_Izq * 0.9'
    elif name == 'M_Puno_Der':
        p.attrib['length'] = 'Line_M_Origen_M_Ancho_Der * 0.9'

# Get the DraftBlock
draft_block = root.find('.//draftBlock')
if draft_block is None:
    draft_block = root.findall('.//draftBlock')[0]

# Helper to find max ID
max_id = max([int(e.attrib.get('id', 0)) for e in root.iter() if 'id' in e.attrib])

def next_id():
    global max_id
    max_id += 1
    return str(max_id)

# 3. Add Cuello Mao Points
cm_origen_id = next_id()
ET.SubElement(draft_block, 'point', {'id': cm_origen_id, 'name': 'CM_Origen', 'type': 'single', 'x': '150', 'y': '0', 'mx': '0', 'my': '0'})

cm_alto_id = next_id()
ET.SubElement(draft_block, 'point', {'id': cm_alto_id, 'name': 'CM_Alto', 'type': 'endLine', 'basePoint': cm_origen_id, 'angle': '90', 'length': '#altura_cuello_mao', 'mx': '0', 'my': '0'})

cm_largo_id = next_id()
ET.SubElement(draft_block, 'point', {'id': cm_largo_id, 'name': 'CM_Largo_Temp', 'type': 'endLine', 'basePoint': cm_origen_id, 'angle': '0', 'length': 'Spl_F_Escote_Ancho_F_Escote_Alto + Spl_T_Escote_Profundidad_T_Escote_Ancho', 'mx': '0', 'my': '0'})

# Curve up at the front for Mao
cm_frente_base_id = next_id()
ET.SubElement(draft_block, 'point', {'id': cm_frente_base_id, 'name': 'CM_Centro_Frente_Base', 'type': 'endLine', 'basePoint': cm_largo_id, 'angle': '90', 'length': '1.5', 'mx': '0', 'my': '0'})

cm_frente_alto_id = next_id()
ET.SubElement(draft_block, 'point', {'id': cm_frente_alto_id, 'name': 'CM_Centro_Frente_Alto', 'type': 'endLine', 'basePoint': cm_frente_base_id, 'angle': '90', 'length': '#altura_cuello_mao', 'mx': '0', 'my': '0'})

# Guide points for spline tangents
cm_guia_inf_id = next_id()
ET.SubElement(draft_block, 'point', {'id': cm_guia_inf_id, 'name': 'CM_Guia_Inf', 'type': 'alongLine', 'firstPoint': cm_origen_id, 'secondPoint': cm_largo_id, 'length': 'Line_CM_Origen_CM_Largo_Temp * 0.6', 'mx': '0', 'my': '0'})

cm_guia_sup_id = next_id()
ET.SubElement(draft_block, 'point', {'id': cm_guia_sup_id, 'name': 'CM_Guia_Sup', 'type': 'alongLine', 'firstPoint': cm_alto_id, 'secondPoint': cm_frente_alto_id, 'length': 'Line_CM_Origen_CM_Largo_Temp * 0.6', 'mx': '0', 'my': '0'})

# Add Cuello Mao splines
spline_inf_id = next_id()
ET.SubElement(draft_block, 'spline', {'id': spline_inf_id, 'point1': cm_guia_inf_id, 'point4': cm_frente_base_id, 'angle1': '0', 'length1': 'Line_CM_Guia_Inf_CM_Largo_Temp * 0.5', 'angle2': '180', 'length2': 'Line_CM_Guia_Inf_CM_Largo_Temp * 0.5', 'type': 'simple'})

spline_sup_id = next_id()
ET.SubElement(draft_block, 'spline', {'id': spline_sup_id, 'point1': cm_guia_sup_id, 'point4': cm_frente_alto_id, 'angle1': '0', 'length1': 'Line_CM_Guia_Sup_CM_Centro_Frente_Alto * 0.5', 'angle2': '180', 'length2': 'Line_CM_Guia_Sup_CM_Centro_Frente_Alto * 0.5', 'type': 'simple'})

# Add Cuello Mao Lines
ET.SubElement(draft_block, 'line', {'id': next_id(), 'firstPoint': cm_origen_id, 'secondPoint': cm_guia_inf_id})
ET.SubElement(draft_block, 'line', {'id': next_id(), 'firstPoint': cm_alto_id, 'secondPoint': cm_guia_sup_id})
ET.SubElement(draft_block, 'line', {'id': next_id(), 'firstPoint': cm_origen_id, 'secondPoint': cm_alto_id})
ET.SubElement(draft_block, 'line', {'id': next_id(), 'firstPoint': cm_frente_base_id, 'secondPoint': cm_frente_alto_id})


# 4. Add Bolsillos Bajos Points
# We need the IDs for F_Costado_Ruedo and F_Costado_Cintura.
# F_Costado_Cintura = 119
# F_Costado_Ruedo = 121
b_sup_der_id = next_id()
ET.SubElement(draft_block, 'point', {'id': b_sup_der_id, 'name': 'B_Sup_Der', 'type': 'endLine', 'basePoint': '121', 'angle': 'AngleLine_F_Costado_Ruedo_F_Costado_Cintura', 'length': '#alto_bolsillo', 'mx': '0', 'my': '0'})

b_inf_der_id = next_id()
# Same as 121, but a separate point for clarity of the pocket
ET.SubElement(draft_block, 'point', {'id': b_inf_der_id, 'name': 'B_Inf_Der', 'type': 'endLine', 'basePoint': '121', 'angle': '0', 'length': '0', 'mx': '0', 'my': '0'})

b_sup_izq_id = next_id()
ET.SubElement(draft_block, 'point', {'id': b_sup_izq_id, 'name': 'B_Sup_Izq', 'type': 'endLine', 'basePoint': b_sup_der_id, 'angle': '180', 'length': '#ancho_bolsillo', 'mx': '0', 'my': '0'})

b_inf_izq_id = next_id()
ET.SubElement(draft_block, 'point', {'id': b_inf_izq_id, 'name': 'B_Inf_Izq', 'type': 'endLine', 'basePoint': b_inf_der_id, 'angle': '180', 'length': '#ancho_bolsillo', 'mx': '0', 'my': '0'})

# Bolsillo lines
ET.SubElement(draft_block, 'line', {'id': next_id(), 'firstPoint': b_sup_der_id, 'secondPoint': b_sup_izq_id})
ET.SubElement(draft_block, 'line', {'id': next_id(), 'firstPoint': b_sup_izq_id, 'secondPoint': b_inf_izq_id})
ET.SubElement(draft_block, 'line', {'id': next_id(), 'firstPoint': b_inf_izq_id, 'secondPoint': b_inf_der_id})
# The right side is already part of the side seam, but let's draw it for the pocket
ET.SubElement(draft_block, 'line', {'id': next_id(), 'firstPoint': b_inf_der_id, 'secondPoint': b_sup_der_id})

# Clean up empty lines to avoid the bloat issue again!
xml_str = ET.tostring(root, encoding='utf-8', xml_declaration=True).decode('utf-8')
clean_lines = [line for line in xml_str.split('\n') if line.strip()]
with open(val_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(clean_lines))

print("Inyeccion exitosa: Cuello Mao, Bolsillo Acoplado y Manga Corta M.A.S.")
