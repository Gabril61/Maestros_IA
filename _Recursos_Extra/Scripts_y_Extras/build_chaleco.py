import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Update metadata
desc = root.find('description')
if desc is not None:
    desc.text = "Patrón Maestro - Chaleco Femenino Sastre"

# Find IDs of points to delete (Sleeves and Collars)
prefixes_to_delete = ['MS_', 'MI_', 'Manga_', 'C_', 'Cuello_', 'Solapa_']
pts_to_delete = []
pt_ids_to_delete = []

for p in calc.findall('point'):
    name = p.get('name', '')
    if any(name.startswith(pre) for pre in prefixes_to_delete) or 'Quiebre' in name:
        pts_to_delete.append(p)
        pt_ids_to_delete.append(p.get('id'))

for p in pts_to_delete:
    calc.remove(p)

# Remove lines and splines that depend on deleted points
elements_to_remove = []
for l in calc.findall('line'):
    if l.get('firstPoint') in pt_ids_to_delete or l.get('secondPoint') in pt_ids_to_delete:
        elements_to_remove.append(l)
for s in calc.findall('spline'):
    if s.get('point1') in pt_ids_to_delete or s.get('point4') in pt_ids_to_delete:
        elements_to_remove.append(s)

for el in elements_to_remove:
    try:
        calc.remove(el)
    except:
        pass

# 2. Modify Armholes and Shoulders
for p in calc.findall('point'):
    name = p.get('name', '')
    if name in ['F_Linea_Sisa', 'T_Linea_Sisa']:
        p.set('length', '(@S_SISA_PROF + 3.5)')  # Dropped 1.5cm from blazer (+2)
    elif name in ['F_Hombro', 'T_Hombro']:
        p.set('length', '(@S_ANCHO_HOMBRO - 0.5)')  # Reduced 1.5cm from blazer (+1)

# 3. V-Neckline to Buttons
# We need to find F_Cuello_Ancho and B_Boton_1
id_hombro_cuello = None
id_boton_1 = None
for p in calc.findall('point'):
    if p.get('name') == 'F_Cuello_Ancho':
        id_hombro_cuello = p.get('id')
    elif p.get('name') == 'B_Boton_1':
        id_boton_1 = p.get('id')

if id_hombro_cuello and id_boton_1:
    # Remove existing neck splines
    for s in calc.findall('spline'):
        if s.get('point1') == id_hombro_cuello or s.get('point4') == id_hombro_cuello:
            try:
                calc.remove(s)
            except:
                pass
    
    # Add straight V-neck line
    new_neck = ET.Element('line', {
        'id': '90001',
        'firstPoint': id_hombro_cuello,
        'secondPoint': id_boton_1,
        'lineColor': 'black',
        'lineType': 'solidLine',
        'lineWeight': '0.7'
    })
    calc.append(new_neck)

# 4. Clear Pieces to prevent crash
details = root.find('.//detail')
if details is not None:
    for piece in details.findall('piece'):
        details.remove(piece)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Chaleco build completed successfully.")
