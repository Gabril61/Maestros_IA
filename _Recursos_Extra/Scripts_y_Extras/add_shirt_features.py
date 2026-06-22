import xml.etree.ElementTree as ET
import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val'

# Parse the XML
tree = ET.parse(file_path)
root = tree.getroot()

# Update description and notes
desc = root.find('description')
if desc is not None:
    desc.text = "Matriz Maestra TextilFit - CAMISA EJECUTIVA DAMA (Corte Princesa)"

notes = root.find('notes')
if notes is not None:
    notes.text = "Fase 1: Camisa Ejecutiva. Basada en el corte princesa definitivo. Se añade aletilla de abotonadura y bloque de cuello camisero clásico."

# Find the calculation block in Corpino_y_Manga to add the placket (Aletilla)
corp_calc = None
for draft in root.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        corp_calc = draft.find('calculation')
        break

if corp_calc is not None:
    # Placket points (Aletilla) - assuming Center Front is at X=0 and extends left (angle 180)
    placket_points = [
        # Cruce de botones (1.5 cm)
        ET.Element('point', {'id': '10001', 'name': 'F_Aletilla_Sup', 'type': 'endLine', 'basePoint': '24', 'angle': '180', 'length': '1.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('point', {'id': '10002', 'name': 'F_Aletilla_Inf', 'type': 'endLine', 'basePoint': '301', 'angle': '180', 'length': '1.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        # Vista de la aletilla (3 cm total desde el centro)
        ET.Element('point', {'id': '10003', 'name': 'F_Vista_Sup', 'type': 'endLine', 'basePoint': '24', 'angle': '180', 'length': '4.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('point', {'id': '10004', 'name': 'F_Vista_Inf', 'type': 'endLine', 'basePoint': '301', 'angle': '180', 'length': '4.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        # Lines for the placket
        ET.Element('line', {'id': '10005', 'firstPoint': '10001', 'secondPoint': '10002', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
        ET.Element('line', {'id': '10006', 'firstPoint': '10003', 'secondPoint': '10004', 'lineColor': 'black', 'lineType': 'dotLine', 'lineWeight': '0.35'})
    ]
    
    for pt in placket_points:
        corp_calc.append(pt)

# Add a new draft block for the Collar (Cuello_y_Tirilla)
collar_draft = ET.Element('draftBlock', {'name': 'Cuello_y_Tirilla'})
calc = ET.SubElement(collar_draft, 'calculation')

# Base points for the Collar Stand (Tirilla)
points = [
    # Origin
    {'id': '10100', 'type': 'single', 'name': 'C_Origen', 'x': '150', 'y': '0', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    # Centro Espalda Tirilla
    {'id': '10101', 'type': 'endLine', 'name': 'C_Tirilla_Alto', 'basePoint': '10100', 'angle': '90', 'length': '3', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    # Largo Tirilla (Mitad del contorno + cruce de 1.5)
    {'id': '10102', 'type': 'endLine', 'name': 'C_Tirilla_Largo', 'basePoint': '10100', 'angle': '0', 'length': '(@S_CONT_CUELLO / 2) + 1.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    # Rectángulo Tirilla
    {'id': '10103', 'type': 'endLine', 'name': 'C_Tirilla_Largo_Alto', 'basePoint': '10102', 'angle': '90', 'length': '3', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    # Puntos de forma (Elevación en el frente)
    {'id': '10104', 'type': 'endLine', 'name': 'C_Tirilla_Elevacion', 'basePoint': '10102', 'angle': '90', 'length': '1', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '10105', 'type': 'endLine', 'name': 'C_Tirilla_Curva_Sup', 'basePoint': '10103', 'angle': '90', 'length': '1', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    # Punta redonda de la tirilla (Botón)
    {'id': '10106', 'type': 'endLine', 'name': 'C_Tirilla_Boton', 'basePoint': '10104', 'angle': '180', 'length': '1.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    
    # Base points for the Collar Fall (Cuello)
    {'id': '10200', 'type': 'endLine', 'name': 'C_Cuello_Base', 'basePoint': '10101', 'angle': '90', 'length': '0.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '10201', 'type': 'endLine', 'name': 'C_Cuello_Alto', 'basePoint': '10200', 'angle': '90', 'length': '4.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '10202', 'type': 'endLine', 'name': 'C_Cuello_Largo', 'basePoint': '10200', 'angle': '0', 'length': '(@S_CONT_CUELLO / 2)', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '10203', 'type': 'endLine', 'name': 'C_Cuello_Punta', 'basePoint': '10202', 'angle': '0', 'length': '1.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '10204', 'type': 'endLine', 'name': 'C_Cuello_Punta_Alto', 'basePoint': '10203', 'angle': '90', 'length': '5.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
]

for p in points:
    ET.SubElement(calc, 'point', p)

# Splines for the collar
splines = [
    {'id': '10150', 'type': 'simpleInteractive', 'point1': '10100', 'point4': '10104', 'angle1': '0', 'angle2': '180', 'length1': '3', 'length2': '3', 'color': 'black'},
    {'id': '10151', 'type': 'simpleInteractive', 'point1': '10101', 'point4': '10105', 'angle1': '0', 'angle2': '180', 'length1': '3', 'length2': '3', 'color': 'black'},
    {'id': '10250', 'type': 'simpleInteractive', 'point1': '10200', 'point4': '10202', 'angle1': '0', 'angle2': '180', 'length1': '3', 'length2': '3', 'color': 'black'},
]
for s in splines:
    ET.SubElement(calc, 'spline', s)

# Lines
lines = [
    {'id': '10160', 'firstPoint': '10100', 'secondPoint': '10101', 'lineColor': 'black'},
    {'id': '10161', 'firstPoint': '10200', 'secondPoint': '10201', 'lineColor': 'black'},
    {'id': '10162', 'firstPoint': '10201', 'secondPoint': '10204', 'lineColor': 'black'},
    {'id': '10163', 'firstPoint': '10204', 'secondPoint': '10202', 'lineColor': 'black'},
    {'id': '10164', 'firstPoint': '10104', 'secondPoint': '10105', 'lineColor': 'black'},
]
for l in lines:
    ET.SubElement(calc, 'line', l)

ET.SubElement(collar_draft, 'modeling')
ET.SubElement(collar_draft, 'pieces')

root.append(collar_draft)

# Write output
tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Shirt features added successfully!")
