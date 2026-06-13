import xml.etree.ElementTree as ET
import os

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# 1. Update MS_Copa_Alto formula
for pt in calculation.findall('.//point'):
    if pt.get('name') == 'MS_Copa_Alto':
        pt.set('length', '(@S_CONT_SISA / 3) + 1')

# Helper function to append elements safely
def insert_after(calc, after_id, new_elements):
    idx = 0
    for i, child in enumerate(list(calc)):
        if child.get('id') == after_id:
            idx = i
            break
    for el in reversed(new_elements):
        calc.insert(idx + 1, el)

new_elements = []

# --- FRONT FLIPPED POINTS ---
# 40001: F_Ancho_Izq_Flip
new_elements.append(ET.Element('point', {
    'id': '40001', 'type': 'endLine', 'basePoint': '30011',
    'angle': '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - AngleLine_Corte_Frente_Bicep_MS_Ancho_Izq',
    'length': 'Line_Corte_Frente_Bicep_MS_Ancho_Izq',
    'name': 'F_Ancho_Izq_Flip', 'lineColor': 'green', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
# 40002: F_Guia_Izq_Flip
new_elements.append(ET.Element('point', {
    'id': '40002', 'type': 'endLine', 'basePoint': '30011',
    'angle': '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - AngleLine_Corte_Frente_Bicep_MS_Guia_Izq',
    'length': 'Line_Corte_Frente_Bicep_MS_Guia_Izq',
    'name': 'F_Guia_Izq_Flip', 'lineColor': 'green', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
# 40003: F_Codo_Izq_Flip
new_elements.append(ET.Element('point', {
    'id': '40003', 'type': 'endLine', 'basePoint': '30012',
    'angle': '(AngleLine_Corte_Frente_Codo_Corte_Frente_Bicep * 2) - AngleLine_Corte_Frente_Codo_MS_Codo_Izq',
    'length': 'Line_Corte_Frente_Codo_MS_Codo_Izq',
    'name': 'F_Codo_Izq_Flip', 'lineColor': 'green', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
# 40004: F_Puno_Izq_Flip
new_elements.append(ET.Element('point', {
    'id': '40004', 'type': 'endLine', 'basePoint': '30013',
    'angle': '(AngleLine_Corte_Frente_Puno_Corte_Frente_Codo * 2) - AngleLine_Corte_Frente_Puno_MS_Puno_Izq',
    'length': 'Line_Corte_Frente_Puno_MS_Puno_Izq',
    'name': 'F_Puno_Izq_Flip', 'lineColor': 'green', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
# 40005: F_Ext_Puno_Izq_Flip
new_elements.append(ET.Element('point', {
    'id': '40005', 'type': 'endLine', 'basePoint': '30013',
    'angle': '(AngleLine_Corte_Frente_Puno_Corte_Frente_Codo * 2) - AngleLine_Corte_Frente_Puno_Ext_MS_Puno_Izq',
    'length': 'Line_Corte_Frente_Puno_Ext_MS_Puno_Izq',
    'name': 'F_Ext_Puno_Izq_Flip', 'lineColor': 'green', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))

# Front splines
# 40006: Mirrored 12021
new_elements.append(ET.Element('spline', {
    'id': '40006', 'type': 'simpleInteractive', 'point1': '40002', 'point4': '40001',
    'angle1': '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - (AngleLine_MS_Origen_MS_Ancho_Izq + 20)',
    'angle2': '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - 0',
    'length1': '(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.4',
    'length2': '(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.2',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))
# 40007: Mirrored chunk from 30031 to F_Guia_Izq_Flip
new_elements.append(ET.Element('spline', {
    'id': '40007', 'type': 'simpleInteractive', 'point1': '30031', 'point4': '40002',
    'angle1': 'AngleLine_Corte_Frente_Bicep_F_Guia_Izq_Flip + 90',
    'angle2': '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - (AngleLine_MS_Origen_MS_Ancho_Izq - 180)',
    'length1': 'Line_Copa_Frente_Pico_F_Guia_Izq_Flip * 0.4',
    'length2': '(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.05',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))

# --- BACK FLIPPED POINTS ---
# 40011: T_Ancho_Der_Flip
new_elements.append(ET.Element('point', {
    'id': '40011', 'type': 'endLine', 'basePoint': '30014',
    'angle': '(AngleLine_Corte_Espalda_Bicep_Corte_Espalda_Codo * 2) - AngleLine_Corte_Espalda_Bicep_MS_Ancho_Der',
    'length': 'Line_Corte_Espalda_Bicep_MS_Ancho_Der',
    'name': 'T_Ancho_Der_Flip', 'lineColor': 'green', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
# 40013: T_Codo_Der_Flip
new_elements.append(ET.Element('point', {
    'id': '40013', 'type': 'endLine', 'basePoint': '30015',
    'angle': '(AngleLine_Corte_Espalda_Codo_Corte_Espalda_Bicep * 2) - AngleLine_Corte_Espalda_Codo_MS_Codo_Der',
    'length': 'Line_Corte_Espalda_Codo_MS_Codo_Der',
    'name': 'T_Codo_Der_Flip', 'lineColor': 'green', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
# 40014: T_Puno_Der_Flip
new_elements.append(ET.Element('point', {
    'id': '40014', 'type': 'endLine', 'basePoint': '30016',
    'angle': '(AngleLine_Corte_Espalda_Puno_Corte_Espalda_Codo * 2) - AngleLine_Corte_Espalda_Puno_MS_Puno_Der',
    'length': 'Line_Corte_Espalda_Puno_MS_Puno_Der',
    'name': 'T_Puno_Der_Flip', 'lineColor': 'green', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))

# Back Spline
# 40015: Mirrored 12023
new_elements.append(ET.Element('spline', {
    'id': '40015', 'type': 'simpleInteractive', 'point1': '30032', 'point4': '40011',
    'angle1': '(AngleLine_Corte_Espalda_Bicep_Corte_Espalda_Codo * 2) - (AngleLine_MS_Origen_MS_Ancho_Der - 20)',
    'angle2': '(AngleLine_Corte_Espalda_Bicep_Corte_Espalda_Codo * 2) - 180',
    'length1': '(Line_MS_Origen_MS_Ancho_Der / 2) * 0.3',
    'length2': '(Line_MS_Origen_MS_Ancho_Der / 2) * 0.2',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))

# Outline lines
new_elements.append(ET.Element('line', {'id': '40020', 'firstPoint': '40001', 'secondPoint': '40003', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '40021', 'firstPoint': '40003', 'secondPoint': '40004', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '40022', 'firstPoint': '40004', 'secondPoint': '40005', 'lineColor': 'green', 'lineWeight': '0.35'}))

new_elements.append(ET.Element('line', {'id': '40023', 'firstPoint': '40011', 'secondPoint': '40013', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '40024', 'firstPoint': '40013', 'secondPoint': '40014', 'lineColor': 'green', 'lineWeight': '0.35'}))

# Insert after 30055 (which is near the end of the calculation block, before detail specific points)
insert_after(calculation, '30055', new_elements)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Sleeve parametric flipping injected successfully.")
