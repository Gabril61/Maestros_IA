import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Caballero_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Update metadata
desc = root.find('description')
if desc is not None:
    desc.text = "Patrón Maestro - Scrub Top Médico Caballero"
notes = root.find('notes')
if notes is not None:
    notes.text = "Conjunto Médico: Scrub Top para caballero. Cuello en V cruzado clásico, aberturas laterales y bolsillos inferiores."

# 2. Adjust Length
for p in calc.findall('point'):
    if p.get('id') == '118' or p.get('name') == 'F_Nivel_Largo':
        p.set('length', '@S_TALLEDEL + 25')
    elif p.get('id') == '218' or p.get('name') == 'T_Nivel_Largo':
        p.set('length', '@S_TALLETRA + 25')

# 3. Points to remove
pts_to_remove = []
for p in calc.findall('point'):
    name = p.get('name', '')
    if name.startswith('C_') or 'Solapa' in name or 'Doblez' in name or 'Aletilla' in name or 'V_' in name:
        pts_to_remove.append(p)
    elif name in ['T_Abertura_Top']:
        pts_to_remove.append(p)

pt_ids_to_remove = [p.get('id') for p in pts_to_remove]

for p in pts_to_remove:
    calc.remove(p)

# Also remove lines and splines connected to these points
lines_to_remove = []
for l in calc.findall('line'):
    if l.get('firstPoint') in pt_ids_to_remove or l.get('secondPoint') in pt_ids_to_remove:
        lines_to_remove.append(l)
for s in calc.findall('spline'):
    if s.get('point1') in pt_ids_to_remove or s.get('point4') in pt_ids_to_remove:
        lines_to_remove.append(s)

for l in lines_to_remove:
    calc.remove(l)

# 4. Add V-Neck and Hem Geometry
new_pts = []
new_lines = []
pt_id = 40000
line_id = 40100

# F_Escote_V (Depth of V - 18 cm)
new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Escote_V', 'type': 'endLine', 'basePoint': '102', 'angle': '270', 'length': '18', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
id_escote_v = str(pt_id)
pt_id += 1

# F_Cruce_V (Overlap of V)
new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Cruce_V', 'type': 'endLine', 'basePoint': id_escote_v, 'angle': '180', 'length': '1.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
id_cruce_v = str(pt_id)
pt_id += 1

# F_Cruce_Ruedo (Overlap at Hem)
new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Cruce_Ruedo', 'type': 'endLine', 'basePoint': '118', 'angle': '180', 'length': '1.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
id_cruce_ruedo = str(pt_id)
pt_id += 1

# V-Neck Line (F_Escote_Ancho 101 to F_Cruce_V)
new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '101', 'secondPoint': id_cruce_v, 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7'}))
line_id += 1

# Front Overlap Line (F_Cruce_V to F_Cruce_Ruedo)
new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': id_cruce_v, 'secondPoint': id_cruce_ruedo, 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7'}))
line_id += 1

# Bottom Hem Line (F_Nivel_Largo 118 to F_Cruce_Ruedo)
new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '118', 'secondPoint': id_cruce_ruedo, 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}))
line_id += 1

# Vista del Cuello (Facing)
new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Vista_Hombro', 'type': 'alongLine', 'firstPoint': '101', 'secondPoint': '109', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
id_vista_hombro = str(pt_id)
pt_id += 1

new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Vista_Abajo', 'type': 'alongLine', 'firstPoint': id_cruce_ruedo, 'secondPoint': '118', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
id_vista_abajo = str(pt_id)
pt_id += 1

new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Vista_Pico', 'type': 'endLine', 'basePoint': id_escote_v, 'angle': '0', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
id_vista_pico = str(pt_id)
pt_id += 1

new_lines.append(ET.Element('spline', {'id': str(line_id), 'point1': id_vista_hombro, 'point4': id_vista_pico, 'angle1': '270', 'angle2': '90', 'length1': '10', 'length2': '10', 'color': 'black', 'type': 'simpleInteractive'}))
line_id += 1
new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': id_vista_pico, 'secondPoint': id_vista_abajo, 'lineColor': 'black'}))
line_id += 1

# 5. Hem extensions (4 cm static to avoid D_RUEDO_PRENDA error)
pt_id = 40200
line_id = 40300

points_to_extend = [
    (id_cruce_ruedo, 'Ext_F_Cruce_Ruedo'),
    ('118', 'Ext_F_Nivel_Largo'),
    ('121', 'Ext_F_Costado_Ruedo'), # verify F_Costado_Ruedo is 121
    ('221', 'Ext_T_Costado_Ruedo'), # verify T_Costado_Ruedo is 221
    ('218', 'Ext_T_Nivel_Largo')    # verify T_Nivel_Largo is 218
]

ext_ids = {}

for base_id, name in points_to_extend:
    new_pts.append(ET.Element('point', {
        'id': str(pt_id),
        'name': name,
        'type': 'endLine',
        'basePoint': base_id,
        'angle': '270',
        'length': '4',
        'mx': '0.1',
        'my': '0.1',
        'showPointName': 'true'
    }))
    ext_ids[name] = str(pt_id)
    pt_id += 1

for base_id, name in points_to_extend:
    new_lines.append(ET.Element('line', {
        'id': str(line_id),
        'firstPoint': base_id,
        'secondPoint': ext_ids[name],
        'lineColor': 'black',
        'lineType': 'solidLine',
        'lineWeight': '0.35'
    }))
    line_id += 1

hem_lines = [
    ('Ext_F_Cruce_Ruedo', 'Ext_F_Nivel_Largo'),
    ('Ext_F_Nivel_Largo', 'Ext_F_Costado_Ruedo'),
    ('Ext_T_Costado_Ruedo', 'Ext_T_Nivel_Largo')
]

for p1_name, p2_name in hem_lines:
    new_lines.append(ET.Element('line', {
        'id': str(line_id),
        'firstPoint': ext_ids[p1_name],
        'secondPoint': ext_ids[p2_name],
        'lineColor': 'black',
        'lineType': 'solidLine',
        'lineWeight': '0.7'
    }))
    line_id += 1

# APPEND POINTS FIRST, THEN LINES!
for p in new_pts:
    calc.append(p)
for l in new_lines:
    calc.append(l)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Scrub Top Caballero generated perfectly!")
