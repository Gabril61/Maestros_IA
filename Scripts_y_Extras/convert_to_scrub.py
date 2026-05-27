import xml.etree.ElementTree as ET
import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Update metadata
desc = root.find('description')
if desc is not None:
    desc.text = "Patrón Maestro - Scrub Top Médico Dama"
notes = root.find('notes')
if notes is not None:
    notes.text = "Conjunto Médico: Scrub Top para dama. Cuello en V cruzado clásico, aberturas laterales y bolsillos inferiores."

# 2. Adjust Length
# Point F_Nivel_Largo is 118, T_Nivel_Largo is 126
for p in calc.findall('point'):
    if p.get('id') == '118' or p.get('name') == 'F_Nivel_Largo':
        p.set('length', '@S_TALLE_DELANTERO + 25')
    elif p.get('name') == 'T_Nivel_Largo':
        p.set('length', '@S_TALLE_TRASERO + 25')

# 3. Points to remove
# Anything starting with C_ (Collar), Solapa, Doblez, Aletilla, V_ (Vista)
pts_to_remove = []
for p in calc.findall('point'):
    name = p.get('name', '')
    if name.startswith('C_') or 'Solapa' in name or 'Doblez' in name or 'Aletilla' in name or 'V_' in name:
        pts_to_remove.append(p)
    elif name in ['T_Abertura_Top']: # Maybe remove T_Abertura_Top if it was a back vent for a gown? We want side slits for scrub.
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

# 4. Add V-Neck Geometry
# F_Escote_Alto is 102. F_Escote_Ancho is 101. F_Nivel_Largo is 118.
new_pts = []
line_id = 40000
pt_id = 40000

# F_Escote_V (Depth of V)
new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Escote_V', 'type': 'endLine', 'basePoint': '102', 'angle': '270', 'length': '@D_PROFUN_ESCOTE', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
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

# V-Neck Line (F_Escote_Ancho to F_Cruce_V)
calc.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '101', 'secondPoint': id_cruce_v, 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7'}))
line_id += 1

# Front Overlap Line (F_Cruce_V to F_Cruce_Ruedo)
calc.append(ET.Element('line', {'id': str(line_id), 'firstPoint': id_cruce_v, 'secondPoint': id_cruce_ruedo, 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7'}))
line_id += 1

# Bottom Hem Line (F_Nivel_Largo 118 to F_Cruce_Ruedo)
calc.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '118', 'secondPoint': id_cruce_ruedo, 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}))
line_id += 1

# 5. Vista del Cuello (Facing)
# Width of 4 cm
new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Vista_Hombro', 'type': 'alongLine', 'firstPoint': '101', 'secondPoint': '109', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})) # 109 is F_Caida_Hombro
id_vista_hombro = str(pt_id)
pt_id += 1

new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Vista_Abajo', 'type': 'alongLine', 'firstPoint': id_cruce_ruedo, 'secondPoint': '118', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
id_vista_abajo = str(pt_id)
pt_id += 1

new_pts.append(ET.Element('point', {'id': str(pt_id), 'name': 'F_Vista_Pico', 'type': 'endLine', 'basePoint': id_escote_v, 'angle': '0', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}))
id_vista_pico = str(pt_id)
pt_id += 1

calc.append(ET.Element('spline', {'id': str(line_id), 'point1': id_vista_hombro, 'point4': id_vista_pico, 'angle1': '270', 'angle2': '90', 'length1': '10', 'length2': '10', 'color': 'red'}))
line_id += 1
calc.append(ET.Element('line', {'id': str(line_id), 'firstPoint': id_vista_pico, 'secondPoint': id_vista_abajo, 'lineColor': 'red'}))
line_id += 1

for p in new_pts:
    calc.append(p)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Scrub Top converted from Gown! Points removed and V-neck added.")
