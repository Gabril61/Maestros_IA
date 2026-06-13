import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# 1. Clean up intermediate points (make them invisible)
for pt_id in ['40001', '40002', '40003', '40004', '40005', '40011', '40012', '40013', '40014']:
    pt = calculation.find(f".//point[@id='{pt_id}']")
    if pt is not None:
        pt.set('lineType', 'none')
        pt.set('lineColor', 'none')
        pt.set('showPointName', 'false')

# 2. Remove old splines and lines
to_remove = []
for cid in ['40006', '40007', '40015', '40020', '40021', '40022', '40023', '40024']:
    el = calculation.find(f".//*[@id='{cid}']")
    if el is not None:
        to_remove.append(el)

for el in to_remove:
    calculation.remove(el)

new_elements = []

# 3. Create Bajera_Ancho (Target location for the Underarm Seam)
# Using 12000 (MS_Origen) as base, move 45 cm to the right.
new_elements.append(ET.Element('point', {
    'id': '41000', 'type': 'endLine', 'basePoint': '12000',
    'angle': '0', 'length': '45', 'name': 'Bajera_Ancho',
    'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))

# 4. Invisible translation vectors
new_elements.append(ET.Element('line', {
    'id': '41001', 'firstPoint': '40001', 'secondPoint': '41000', 'lineColor': 'none', 'lineType': 'none'
}))
new_elements.append(ET.Element('line', {
    'id': '41002', 'firstPoint': '40011', 'secondPoint': '41000', 'lineColor': 'none', 'lineType': 'none'
}))

# 5. Translated Points - FRONT
front_pts = {
    '40001': '42001', '40002': '42002', '40003': '42003', '40004': '42004', '40005': '42005',
    '30011': '42006', '30012': '42007', '30013': '42008', '89502': '42009', '30031': '42010'
}
for old_id, new_id in front_pts.items():
    new_elements.append(ET.Element('point', {
        'id': new_id, 'type': 'endLine', 'basePoint': old_id,
        'angle': 'AngleLine_F_Ancho_Izq_Flip_Bajera_Ancho', 'length': 'Line_F_Ancho_Izq_Flip_Bajera_Ancho',
        'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'false'
    }))

# 6. Translated Points - BACK
back_pts = {
    '40011': '43001', '40012': '43002', '40013': '43003', '40014': '43004',
    '30014': '43006', '30015': '43007', '30016': '43008', '30032': '43010'
}
for old_id, new_id in back_pts.items():
    new_elements.append(ET.Element('point', {
        'id': new_id, 'type': 'endLine', 'basePoint': old_id,
        'angle': 'AngleLine_T_Ancho_Der_Flip_Bajera_Ancho', 'length': 'Line_T_Ancho_Der_Flip_Bajera_Ancho',
        'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'false'
    }))

# To ensure formulas evaluate, add invisible lines for handles
new_elements.append(ET.Element('line', {'id': '43999', 'firstPoint': '42010', 'secondPoint': '42002', 'lineColor': 'none', 'lineType': 'none'}))
new_elements.append(ET.Element('line', {'id': '43998', 'firstPoint': '42006', 'secondPoint': '42002', 'lineColor': 'none', 'lineType': 'none'}))


# 7. Translated Splines
new_elements.append(ET.Element('spline', {
    'id': '44001', 'type': 'simpleInteractive', 'point1': '42002', 'point4': '42001',
    'angle1': '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - (AngleLine_MS_Origen_MS_Ancho_Izq + 20)',
    'angle2': '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - 0',
    'length1': '(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.4',
    'length2': '(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.2',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))
new_elements.append(ET.Element('spline', {
    'id': '44002', 'type': 'simpleInteractive', 'point1': '42010', 'point4': '42002',
    'angle1': 'AngleLine_Corte_Frente_Bicep_F_Guia_Izq_Flip + 90',
    'angle2': '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - (AngleLine_MS_Origen_MS_Ancho_Izq - 180)',
    'length1': 'Line_Copa_Frente_Pico_F_Guia_Izq_Flip * 0.4',
    'length2': '(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.05',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))
new_elements.append(ET.Element('spline', {
    'id': '44003', 'type': 'simpleInteractive', 'point1': '43010', 'point4': '43001',
    'angle1': '(AngleLine_Fold_Espalda_Bicep_Fold_Espalda_Codo * 2) - (AngleLine_MS_Origen_MS_Ancho_Der - 20)',
    'angle2': '(AngleLine_Fold_Espalda_Bicep_Fold_Espalda_Codo * 2) - 180',
    'length1': '(Line_MS_Origen_MS_Ancho_Der / 2) * 0.3',
    'length2': '(Line_MS_Origen_MS_Ancho_Der / 2) * 0.2',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))

# 8. Translated Outlines
# Front Edge
new_elements.append(ET.Element('line', {'id': '44010', 'firstPoint': '42010', 'secondPoint': '42006', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44011', 'firstPoint': '42006', 'secondPoint': '42007', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44012', 'firstPoint': '42007', 'secondPoint': '42008', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44013', 'firstPoint': '42008', 'secondPoint': '42009', 'lineColor': 'green', 'lineWeight': '0.35'}))

# Bottom Edge Front
new_elements.append(ET.Element('line', {'id': '44014', 'firstPoint': '42009', 'secondPoint': '42005', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44015', 'firstPoint': '42005', 'secondPoint': '42004', 'lineColor': 'green', 'lineWeight': '0.35'}))

# Underarm Seam (Center)
new_elements.append(ET.Element('line', {'id': '44016', 'firstPoint': '42001', 'secondPoint': '42003', 'lineColor': 'green', 'lineWeight': '0.35', 'lineType': 'dashLine'}))
new_elements.append(ET.Element('line', {'id': '44017', 'firstPoint': '42003', 'secondPoint': '42004', 'lineColor': 'green', 'lineWeight': '0.35', 'lineType': 'dashLine'}))

# Bottom Edge Back
new_elements.append(ET.Element('line', {'id': '44018', 'firstPoint': '43004', 'secondPoint': '43008', 'lineColor': 'green', 'lineWeight': '0.35'}))

# Right Edge Back
new_elements.append(ET.Element('line', {'id': '44019', 'firstPoint': '43008', 'secondPoint': '43007', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44020', 'firstPoint': '43007', 'secondPoint': '43006', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44021', 'firstPoint': '43006', 'secondPoint': '43010', 'lineColor': 'green', 'lineWeight': '0.35'}))

def insert_after(calc, after_id, new_els):
    idx = 0
    for i, child in enumerate(list(calc)):
        if child.get('id') == after_id:
            idx = i
            break
    for el in reversed(new_els):
        calc.insert(idx + 1, el)

insert_after(calculation, '30055', new_elements)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Translated Bajera injected successfully.")
