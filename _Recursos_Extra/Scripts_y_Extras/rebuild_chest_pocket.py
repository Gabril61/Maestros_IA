import xml.etree.ElementTree as ET

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

calc = root.find('.//calculation')
modeling = root.find('.//modeling')

# 1. Delete old stuff
def delete_by_id_prefix(parent, tag, prefixes):
    to_remove = []
    for elem in parent.findall(tag):
        eid = elem.get('id')
        if eid:
            for p in prefixes:
                if eid.startswith(p):
                    to_remove.append(elem)
                    break
    for elem in to_remove:
        parent.remove(elem)

# Calculation points and lines for pocket had IDs 90010-90025, 890010-890025
delete_by_id_prefix(calc, 'point', ['9001', '90020', '90025', '89001', '890020', '890025'])
delete_by_id_prefix(calc, 'line', ['9001', '90021', '89001', '890021'])

# Modeling points had IDs m9001x, 89001x, 89289001x
delete_by_id_prefix(modeling, 'point', ['m9001', '89001', '89289001', '89289002'])

# Paths had IDs 90022, 90023, 890022, 890023
delete_by_id_prefix(modeling, 'path', ['90022', '90023', '890022', '890023'])

# 2. Recreate cleanly
# Base point 109 (Nivel Pecho)
new_pts = [
    ET.Element('point', {'angle': '0', 'basePoint': '109', 'id': '70010', 'length': '(@S_CONT_BUSTO/8)', 'name': 'F_BP_Center', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '70010', 'id': '70011', 'length': '2', 'name': 'F_BP_TopCenter', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '180', 'basePoint': '70011', 'id': '70012', 'length': '5.5', 'name': 'F_BP_TL', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '0', 'basePoint': '70011', 'id': '70013', 'length': '5.5', 'name': 'F_BP_TR', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '70012', 'id': '70014', 'length': '13', 'name': 'F_BP_BL', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '70013', 'id': '70015', 'length': '13', 'name': 'F_BP_BR', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'firstPoint': '70013', 'id': '70016', 'length': '3.5', 'name': 'F_BP_PenTop', 'secondPoint': '70012', 'type': 'alongLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'firstPoint': '70015', 'id': '70017', 'length': '3.5', 'name': 'F_BP_PenBot', 'secondPoint': '70014', 'type': 'alongLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
]
calc.extend(new_pts)

new_lines = [
    ET.Element('line', {'firstPoint': '70012', 'id': '70030', 'secondPoint': '70013', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '70013', 'id': '70031', 'secondPoint': '70015', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '70015', 'id': '70032', 'secondPoint': '70014', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '70014', 'id': '70033', 'secondPoint': '70012', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '70016', 'id': '70034', 'secondPoint': '70017', 'lineColor': 'black', 'lineType': 'dashLine', 'lineWeight': '0.35'}),
]
calc.extend(new_lines)

# Modeling points
mod_pts = [
    ET.Element('point', {'id': '71012', 'idObject': '70012', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '71013', 'idObject': '70013', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '71015', 'idObject': '70015', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '71014', 'idObject': '70014', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '71016', 'idObject': '70016', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '71017', 'idObject': '70017', 'inUse': 'true', 'type': 'modeling'}),
]
modeling.extend(mod_pts)

# Paths
p_pocket = ET.Element('path', {'cut': 'false', 'id': '72000', 'inUse': 'true', 'lineColor': 'darkBlue', 'lineType': 'dashLine', 'lineWeight': '0.35', 'name': 'Bolsillo_Pecho', 'type': '2'})
n_pocket = ET.SubElement(p_pocket, 'nodes')
n_pocket.extend([
    ET.Element('node', {'idObject': '71012', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '71013', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '71015', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '71014', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '71012', 'type': 'NodePoint'}),
])

p_pen = ET.Element('path', {'cut': 'false', 'id': '72001', 'inUse': 'true', 'lineColor': 'darkBlue', 'lineType': 'dashLine', 'lineWeight': '0.35', 'name': 'Division_Lapiz', 'type': '2'})
n_pen = ET.SubElement(p_pen, 'nodes')
n_pen.extend([
    ET.Element('node', {'idObject': '71016', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '71017', 'type': 'NodePoint'}),
])

modeling.extend([p_pocket, p_pen])

# Update Piece
delantero = root.find('.//piece[@name="Delantero"]')
ip_del = delantero.find('iPaths')
if ip_del is not None:
    # remove old
    to_remove = []
    for r in ip_del.findall('record'):
        p = r.get('path')
        if p in ['90022', '90023', '890022', '890023']:
            to_remove.append(r)
    for r in to_remove:
        ip_del.remove(r)
    # add new
    ip_del.append(ET.Element('record', {'path': '72000'}))
    ip_del.append(ET.Element('record', {'path': '72001'}))

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
import re
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Nuke and pave of chest pocket successful.")
