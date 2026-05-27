import xml.etree.ElementTree as ET
import os
import shutil

DAMA_PATH = 'c:\\Users\\Ricx18\\Desktop\\Maestros_IA\\Bata_Medica_Dama_Maestro.val'
ESTANDAR_PATH = 'c:\\Users\\Ricx18\\Desktop\\Maestros_IA\\Bata_Medica_Estandar_Maestro.val'

# Backup Estandar
shutil.copy(ESTANDAR_PATH, ESTANDAR_PATH + '.bak')

tree_d = ET.parse(DAMA_PATH)
calc_d = tree_d.getroot().find('.//calculation')

tree_e = ET.parse(ESTANDAR_PATH)
calc_e = tree_e.getroot().find('.//calculation')

# 1. Update cruce length in Estandar
for child in calc_e:
    if child.get('id') in ['152', '150', '151']:
        child.set('length', '1')

# 2. Delete spline 240 in Estandar
to_remove = []
for child in calc_e:
    if child.get('id') == '240':
        to_remove.append(child)
for child in to_remove:
    calc_e.remove(child)

# 3. Extract points from Dama
points_to_import = []
point_ids_imported = set()

for child in calc_d:
    if child.tag == 'point':
        name = child.get('name', '')
        id_ = child.get('id')
        if (name.startswith('M_') or 
            name.startswith('C_') or 
            name.startswith('F_Solapa') or 
            name == 'V_Cuello_Espejo' or 
            id_ == '202'):
            points_to_import.append(child)
            point_ids_imported.add(id_)

# We also care about Escote nodes that are already in Estandar (101, 102, 201, 202)
escote_point_ids = {'101', '102', '201', '202'}
all_relevant_point_ids = point_ids_imported.union(escote_point_ids)

# Extract lines and splines from Dama that connect these points
lines_splines_to_import = []
for child in calc_d:
    if child.tag in ['line', 'spline']:
        points_used = []
        for k, v in child.attrib.items():
            if k.startswith('point') or k in ['firstPoint', 'secondPoint']:
                points_used.append(v)
        
        # If it uses AT LEAST ONE of the imported points (or Escote points)
        # Wait, if it connects an imported point to an existing point (e.g. C_Origen to 100), we import it.
        # But for Escote points, we ONLY import if it's the specific Escote curve
        # Let's check if all points_used are in Estandar's ID space + imported IDs
        # Actually, let's explicitly include it if ANY point used is in point_ids_imported
        # OR if it's the spline between 101 and 102, or 201 and 202.
        
        is_relevant = False
        if any(p in point_ids_imported for p in points_used):
            is_relevant = True
        elif set(points_used).issubset(escote_point_ids) and len(points_used) > 0:
            is_relevant = True
            
        # Exception: Dama might have lines connecting 101 to 105 which we might not want to overwrite if Estandar has it.
        # But let's just grab the curves: spline between 101, 102 and spline between 201, 202.
        if child.tag == 'spline' and set(points_used).issubset({'101', '102'}):
            is_relevant = True
        elif child.tag == 'spline' and set(points_used).issubset({'201', '202'}):
            is_relevant = True
            
        if is_relevant:
            lines_splines_to_import.append(child)

# 4. Inject into Estandar
# First, points
existing_e_ids = {c.get('id') for c in calc_e}

for p in points_to_import:
    if p.get('id') not in existing_e_ids:
        calc_e.append(p)
        existing_e_ids.add(p.get('id'))

# Then lines and splines. Give them new IDs to avoid any clash
new_id_counter = 20000
for el in lines_splines_to_import:
    el_copy = ET.Element(el.tag, el.attrib)
    el_copy.set('id', str(new_id_counter))
    new_id_counter += 1
    calc_e.append(el_copy)

# Save
tree_e.write(ESTANDAR_PATH, encoding='UTF-8', xml_declaration=True)
print(f"Sincronizado exitosamente. Puntos importados: {len(points_to_import)}, Lineas/Splines importados: {len(lines_splines_to_import)}")
