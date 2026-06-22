import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# 1. Update offset
pt_41000 = calculation.find(".//point[@id='41000']")
if pt_41000 is not None:
    pt_41000.set('length', '90')

# 2. Delete old splines and outlines
to_remove = []
for cid in ['44001', '44002', '44003', '44010', '44011', '44012', '44013', '44014', '44015', '44016', '44017', '44018', '44019', '44020', '44021']:
    el = calculation.find(f".//*[@id='{cid}']")
    if el is not None:
        to_remove.append(el)

for el in to_remove:
    calculation.remove(el)

new_elements = []

# Invisible reference lines for splines
new_elements.append(ET.Element('line', {'id': '44101', 'firstPoint': '42010', 'secondPoint': '42002', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44102', 'firstPoint': '42002', 'secondPoint': '42001', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44103', 'firstPoint': '43010', 'secondPoint': '43001', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35'}))

# Smooth Splines
new_elements.append(ET.Element('spline', {
    'id': '44002', 'type': 'simpleInteractive', 'point1': '42010', 'point4': '42002',
    'angle1': 'AngleLine_42010_42002 + 10', 'angle2': 'AngleLine_42010_42002 + 190',
    'length1': 'Line_42010_42002 * 0.4', 'length2': 'Line_42010_42002 * 0.4',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))
new_elements.append(ET.Element('spline', {
    'id': '44001', 'type': 'simpleInteractive', 'point1': '42002', 'point4': '42001',
    'angle1': 'AngleLine_42002_42001 + 10', 'angle2': 'AngleLine_42002_42001 + 190',
    'length1': 'Line_42002_42001 * 0.4', 'length2': 'Line_42002_42001 * 0.4',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))
new_elements.append(ET.Element('spline', {
    'id': '44003', 'type': 'simpleInteractive', 'point1': '43010', 'point4': '43001',
    'angle1': 'AngleLine_43010_43001 - 10', 'angle2': 'AngleLine_43010_43001 + 170',
    'length1': 'Line_43010_43001 * 0.4', 'length2': 'Line_43010_43001 * 0.4',
    'color': 'green', 'lineWeight': '0.35', 'penStyle': 'solidLine'
}))

# Center and Right Hem points
new_elements.append(ET.Element('point', {
    'id': '45005', 'type': 'endLine', 'basePoint': '42004',
    'angle': '180 - AngleLine_42003_42004', 'length': '@D_RUEDO_MANGA',
    'name': 'Bajera_Underarm_Hem', 'lineColor': 'green', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
new_elements.append(ET.Element('point', {
    'id': '45006', 'type': 'endLine', 'basePoint': '43008',
    'angle': '180 - AngleLine_43007_43008', 'length': '@D_RUEDO_MANGA',
    'name': 'Bajera_Corte_Espalda_Hem', 'lineColor': 'green', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))

# Aletillon Points
new_elements.append(ET.Element('point', {
    'id': '45001', 'type': 'alongLine', 'firstPoint': '43008', 'secondPoint': '43007',
    'length': '12', 'name': 'Bajera_Aletillon_Top',
    'lineColor': 'green', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
# Invisible line for angle
new_elements.append(ET.Element('line', {'id': '45100', 'firstPoint': '43008', 'secondPoint': '43007', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('point', {
    'id': '45002', 'type': 'endLine', 'basePoint': '45001',
    'angle': 'AngleLine_43008_43007 - 90', 'length': '3.5',
    'name': 'Bajera_Aletillon_Top_Ext', 'lineColor': 'green', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
new_elements.append(ET.Element('point', {
    'id': '45003', 'type': 'endLine', 'basePoint': '43008',
    'angle': 'AngleLine_43008_43007 - 90', 'length': '3.5',
    'name': 'Bajera_Aletillon_Bot_Ext', 'lineColor': 'green', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))
new_elements.append(ET.Element('point', {
    'id': '45004', 'type': 'endLine', 'basePoint': '45003',
    'angle': '180 - AngleLine_43007_43008', 'length': '@D_RUEDO_MANGA',
    'name': 'Bajera_Aletillon_Hem_Ext', 'lineColor': 'green', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
}))

# OUTLINES
# Left Edge
new_elements.append(ET.Element('line', {'id': '44010', 'firstPoint': '42010', 'secondPoint': '42006', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44011', 'firstPoint': '42006', 'secondPoint': '42007', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44012', 'firstPoint': '42007', 'secondPoint': '42008', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44013', 'firstPoint': '42008', 'secondPoint': '42009', 'lineColor': 'green', 'lineWeight': '0.35'}))

# Bottom Hem
new_elements.append(ET.Element('line', {'id': '44014', 'firstPoint': '42009', 'secondPoint': '45005', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44015', 'firstPoint': '45005', 'secondPoint': '45006', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44022', 'firstPoint': '45006', 'secondPoint': '45004', 'lineColor': 'green', 'lineWeight': '0.35'}))

# Right Edge (Placket)
new_elements.append(ET.Element('line', {'id': '44023', 'firstPoint': '45004', 'secondPoint': '45003', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44024', 'firstPoint': '45003', 'secondPoint': '45002', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44025', 'firstPoint': '45002', 'secondPoint': '45001', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44019', 'firstPoint': '45001', 'secondPoint': '43007', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44020', 'firstPoint': '43007', 'secondPoint': '43006', 'lineColor': 'green', 'lineWeight': '0.35'}))
new_elements.append(ET.Element('line', {'id': '44021', 'firstPoint': '43006', 'secondPoint': '43010', 'lineColor': 'green', 'lineWeight': '0.35'}))

# Underarm Seam (Center)
new_elements.append(ET.Element('line', {'id': '44016', 'firstPoint': '42001', 'secondPoint': '42003', 'lineColor': 'green', 'lineWeight': '0.35', 'lineType': 'dashLine'}))
new_elements.append(ET.Element('line', {'id': '44017', 'firstPoint': '42003', 'secondPoint': '42004', 'lineColor': 'green', 'lineWeight': '0.35', 'lineType': 'dashLine'}))
new_elements.append(ET.Element('line', {'id': '44026', 'firstPoint': '42004', 'secondPoint': '45005', 'lineColor': 'green', 'lineWeight': '0.35', 'lineType': 'dashLine'}))


for el in new_elements:
    calculation.append(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Bajera fixed.")
