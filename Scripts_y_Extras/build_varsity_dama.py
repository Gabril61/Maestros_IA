import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Update metadata
desc = root.find('description')
if desc is not None:
    desc.text = "Patrón Maestro - Chaqueta Universitaria (Varsity) Dama"

# 2. Clean old collar points
pts_to_delete = []
pt_ids_to_delete = []
for p in calc.findall('point'):
    name = p.get('name', '')
    if name.startswith('C_'):
        pts_to_delete.append(p)
        pt_ids_to_delete.append(p.get('id'))

for p in pts_to_delete:
    calc.remove(p)

# Remove lines/splines dependent on old collar
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

# 3. Increase ease, drop shoulders, drop armholes, and shorten hem
for p in calc.findall('point'):
    name = p.get('name', '')
    # Drop armholes by 2 cm
    if name in ['F_Linea_Sisa', 'T_Linea_Sisa']:
        p.set('length', '(@S_ANCHO_ESPALDA / 2) + 8')
    # Extend shoulders by 2 cm
    elif name == 'F_Hombro':
        p.set('length', '@S_ANCHO_HOMBRO + 2')
    elif name == 'T_Hombro':
        p.set('length', '(@S_ANCHO_HOMBRO + 0.5) + 2')
    # Increase side ease by 2 cm
    elif name in ['F_Costado_Sisa', 'T_Costado_Sisa']:
        p.set('length', '(@S_CONT_BUSTO / 4) + @D_HOLGURA_SUPERIOR + 2')
    elif name in ['F_Costado_Cintura', 'T_Costado_Cintura']:
        p.set('length', '(@S_CONT_BUSTO / 4) + @D_HOLGURA_SUPERIOR + 2')
    elif name in ['F_Costado_Ruedo_Temp', 'F_Costado_Cadera_Temp', 'T_Costado_Ruedo', 'T_Costado_Cadera']:
        p.set('length', '(@G_CONT_CADERA_BAJA / 4) + @D_HOLGURA_INFERIOR + 2')
    # Raise hem by 6 cm (subtract 6 from drop)
    elif name in ['F_Ruedo', 'F_Ruedo_Pinza', 'T_Ruedo', 'T_Ruedo_Pinza', 'F_Cadera', 'T_Cadera']:
        if p.get('length') == '@G_ALTO_CADERA + 6':
            p.set('length', '@G_ALTO_CADERA')

# 4. Add Rib (Pretina, Puño, Cuello) base geometries
# These will be standalone rectangular drafts to serve as the Rib pieces.
# Base point for Ribs
rib_origin = ET.Element('point', {'id': '30000', 'mx': '1', 'my': '1', 'name': 'Rib_Origen', 'type': 'single', 'x': '150', 'y': '0'})
calc.append(rib_origin)

# Pretina (Hem Band): height 6, width (Hip/2 + Ease)
calc.append(ET.Element('point', {'angle': '0', 'basePoint': '30000', 'id': '30001', 'length': '(@G_CONT_CADERA_BAJA / 2) + (@D_HOLGURA_INFERIOR * 2)', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'Pretina_Ancho', 'showPointName': 'true', 'type': 'endLine'}))
calc.append(ET.Element('point', {'angle': '270', 'basePoint': '30000', 'id': '30002', 'length': '6', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'Pretina_Alto', 'showPointName': 'true', 'type': 'endLine'}))
calc.append(ET.Element('point', {'firstPoint': '30001', 'id': '30003', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'Pretina_Esquina', 'secondPoint': '30002', 'showPointName': 'true', 'type': 'pointOfIntersection'}))

# Cuello Bomber (Rib): height 4, width (Neck/2)
calc.append(ET.Element('point', {'id': '30004', 'mx': '1', 'my': '1', 'name': 'CuelloRib_Origen', 'type': 'single', 'x': '150', 'y': '20'}))
calc.append(ET.Element('point', {'angle': '0', 'basePoint': '30004', 'id': '30005', 'length': '(@S_CONT_CUELLO / 2) + 2', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'CuelloRib_Ancho', 'showPointName': 'true', 'type': 'endLine'}))
calc.append(ET.Element('point', {'angle': '270', 'basePoint': '30004', 'id': '30006', 'length': '4', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'CuelloRib_Alto', 'showPointName': 'true', 'type': 'endLine'}))
calc.append(ET.Element('point', {'firstPoint': '30005', 'id': '30007', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'CuelloRib_Esquina', 'secondPoint': '30006', 'showPointName': 'true', 'type': 'pointOfIntersection'}))

# 5. Clear Pieces to prevent crash
details = root.find('.//detail')
if details is not None:
    for piece in details.findall('.//piece'):
        try:
            # find parent of piece
            parent = {c: p for p in tree.iter() for c in p}[piece]
            parent.remove(piece)
        except:
            pass

# Also try pieces tag
for pieces in root.findall('.//pieces'):
    for piece in pieces.findall('.//piece'):
        try:
            pieces.remove(piece)
        except:
            pass

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Varsity Dama build completed successfully.")
