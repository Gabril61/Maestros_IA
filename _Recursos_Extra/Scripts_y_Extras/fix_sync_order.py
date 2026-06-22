import xml.etree.ElementTree as ET
import os
import shutil

DAMA_PATH = 'c:\\Users\\Ricx18\\Desktop\\Maestros_IA\\Bata_Medica_Dama_Maestro.val'
ESTANDAR_PATH = 'c:\\Users\\Ricx18\\Desktop\\Maestros_IA\\Bata_Medica_Estandar_Maestro.val'
BAK_PATH = ESTANDAR_PATH + '.bak'

# Restore from backup first to start clean
if os.path.exists(BAK_PATH):
    shutil.copy(BAK_PATH, ESTANDAR_PATH)

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

# Find which IDs from Dama we need to import
point_ids_imported = set()
escote_point_ids = {'101', '102', '201', '202'}

existing_e_ids = {c.get('id') for c in calc_e}

# Iteratively find all points that need importing based on references
# First pass: explicitly targeted points
for child in calc_d:
    if child.tag == 'point':
        name = child.get('name', '')
        id_ = child.get('id')
        if (name.startswith('M_') or 
            name.startswith('C_') or 
            name.startswith('F_Solapa') or 
            name.startswith('V_') or 
            id_ == '202'):
            point_ids_imported.add(id_)

# Second pass: ensure any line/spline that we intend to import has ALL its points resolved
lines_to_import = []
for child in calc_d:
    if child.tag in ['line', 'spline']:
        points_used = []
        for k, v in child.attrib.items():
            if k.startswith('point') or k in ['firstPoint', 'secondPoint']:
                points_used.append(v)
        
        is_relevant = False
        if any(p in point_ids_imported for p in points_used):
            is_relevant = True
        elif set(points_used).issubset(escote_point_ids) and len(points_used) > 0:
            is_relevant = True
            
        if child.tag == 'spline' and set(points_used).issubset({'101', '102'}):
            is_relevant = True
        elif child.tag == 'spline' and set(points_used).issubset({'201', '202'}):
            is_relevant = True
            
        if is_relevant:
            lines_to_import.append(child)
            # Add all missing points to point_ids_imported!
            for p in points_used:
                if p not in existing_e_ids:
                    point_ids_imported.add(p)

new_id_counter = 20000

# Third pass: Extract elements IN ORDER
for child in calc_d:
    if child.tag == 'point':
        if child.get('id') in point_ids_imported:
            if child.get('id') not in existing_e_ids:
                calc_e.append(child)
                existing_e_ids.add(child.get('id'))
    elif child.tag in ['line', 'spline']:
        if child in lines_to_import:
            el_copy = ET.Element(child.tag, child.attrib)
            el_copy.set('id', str(new_id_counter))
            new_id_counter += 1
            calc_e.append(el_copy)

# Save
tree_e.write(ESTANDAR_PATH, encoding='UTF-8', xml_declaration=True)
print("Corregido: Nodos transferidos en orden exacto y con resolución recursiva de dependencias V_.")
