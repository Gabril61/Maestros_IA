import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val"
ET.register_namespace('', '')

try:
    tree = ET.parse(filepath)
    root = tree.getroot()
except Exception as e:
    print(f"Error parsing XML: {e}")
    exit(1)

calc = root.find('.//calculation')
modeling = root.find('.//modeling')

def insert_after(parent, target_id, new_elements):
    for i, child in enumerate(parent):
        if child.get('id') == target_id:
            for j, new_elem in enumerate(new_elements):
                parent.insert(i + 1 + j, new_elem)
            return True
    return False

# 1. Geometric Armhole fix
p_inter_pecho = ET.Element('point', {'angle': '180', 'basePoint': '209', 'curve': '247', 'id': '90005', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'T_Inter_Pecho', 'showPointName': 'false', 'type': 'curveIntersectAxis'})
p_inter_sisa = ET.Element('point', {'angle': '180', 'basePoint': '207', 'curve': '247', 'id': '90006', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'T_Inter_Sisa', 'showPointName': 'false', 'type': 'curveIntersectAxis'})

insert_after(calc, '209', [p_inter_pecho, p_inter_sisa])

for point in calc.findall('point'):
    if point.get('id') == '210':
        point.set('basePoint', '90005')
    elif point.get('id') == '211':
        point.set('basePoint', '90006')

# 2. Chest Pocket
bp_points = [
    ET.Element('point', {'angle': '0', 'basePoint': '109', 'id': '90010', 'length': '(@S_CONT_BUSTO/10)+1', 'name': 'F_BP_Ref_1', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '90010', 'id': '90011', 'length': '2', 'name': 'F_BP_TopRight', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '180', 'basePoint': '90011', 'id': '90012', 'length': '11', 'name': 'F_BP_TopLeft', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '90011', 'id': '90013', 'length': '13', 'name': 'F_BP_BotRight', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '90012', 'id': '90014', 'length': '13', 'name': 'F_BP_BotLeft', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('line', {'firstPoint': '90012', 'id': '90015', 'secondPoint': '90011', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '90011', 'id': '90016', 'secondPoint': '90013', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '90013', 'id': '90017', 'secondPoint': '90014', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '90014', 'id': '90018', 'secondPoint': '90012', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('point', {'firstPoint': '90012', 'id': '90019', 'length': '3.5', 'name': 'F_BP_PenTop', 'secondPoint': '90011', 'type': 'alongLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'firstPoint': '90014', 'id': '90020', 'length': '3.5', 'name': 'F_BP_PenBot', 'secondPoint': '90013', 'type': 'alongLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('line', {'firstPoint': '90019', 'id': '90021', 'secondPoint': '90020', 'lineColor': 'black', 'lineType': 'dashLine', 'lineWeight': '0.35'}),
]
calc.extend(bp_points)

# 3. Yoke
yoke_points = [
    ET.Element('point', {'firstPoint': '200', 'id': '90030', 'length': '12', 'name': 'T_Canesu_Ref', 'secondPoint': '216', 'type': 'alongLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '180', 'basePoint': '90030', 'curve': '247', 'id': '90031', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'T_Canesu_Centro', 'showPointName': 'false', 'type': 'curveIntersectAxis'}),
    ET.Element('point', {'angle': '180', 'basePoint': '90031', 'curve': '214', 'id': '90032', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'T_Canesu_Sisa', 'showPointName': 'false', 'type': 'curveIntersectAxis'}),
    ET.Element('line', {'firstPoint': '90031', 'id': '90033', 'secondPoint': '90032', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
]
calc.extend(yoke_points)

# 4. Martingala
mart_points = [
    ET.Element('point', {'angle': '180', 'basePoint': '216', 'id': '90040', 'p1Line': '211', 'p2Line': '221', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'T_Costado_Cintura_Real', 'showPointName': 'false', 'type': 'lineIntersectAxis'}),
    ET.Element('point', {'angle': '90', 'basePoint': '250', 'id': '90041', 'length': '2.5', 'name': 'T_Mart_Centro_Top', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '250', 'id': '90042', 'length': '2.5', 'name': 'T_Mart_Centro_Bot', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '90', 'basePoint': '90040', 'id': '90043', 'length': '2.5', 'name': 'T_Mart_Costado_Top', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '90040', 'id': '90044', 'length': '2.5', 'name': 'T_Mart_Costado_Bot', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('line', {'firstPoint': '90041', 'id': '90045', 'secondPoint': '90043', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '90042', 'id': '90046', 'secondPoint': '90044', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
]
calc.extend(mart_points)

# Add Nodes to modeling
mod_nodes = [
    ET.Element('point', {'id': 'm90012', 'idObject': '90012', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90011', 'idObject': '90011', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90013', 'idObject': '90013', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90014', 'idObject': '90014', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90019', 'idObject': '90019', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90020', 'idObject': '90020', 'inUse': 'true', 'type': 'modeling'}),
    
    ET.Element('path', {'cut': 'false', 'id': '90022', 'inUse': 'true', 'lineColor': 'darkBlue', 'lineType': 'dashLine', 'lineWeight': '0.35', 'name': 'Bolsillo_Pecho', 'type': '2'}),
    ET.Element('path', {'cut': 'false', 'id': '90023', 'inUse': 'true', 'lineColor': 'darkBlue', 'lineType': 'dashLine', 'lineWeight': '0.35', 'name': 'Division_Lapiz', 'type': '2'}),
    
    ET.Element('point', {'id': 'm90031', 'idObject': '90031', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90032', 'idObject': '90032', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('path', {'cut': 'false', 'id': '90034', 'inUse': 'true', 'lineColor': 'darkBlue', 'lineType': 'dashLine', 'lineWeight': '0.35', 'name': 'Canesu', 'type': '2'}),
    
    ET.Element('point', {'id': 'm90043', 'idObject': '90043', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90041', 'idObject': '90041', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90042', 'idObject': '90042', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': 'm90044', 'idObject': '90044', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('path', {'cut': 'false', 'id': '90047', 'inUse': 'true', 'lineColor': 'darkBlue', 'lineType': 'dashLine', 'lineWeight': '0.35', 'name': 'Martingala', 'type': '2'})
]

# Configure path nodes
def create_node_point(id_str):
    return ET.Element('node', {'idObject': id_str, 'type': 'NodePoint'})

path_bp = mod_nodes[6]
nodes_bp = ET.SubElement(path_bp, 'nodes')
nodes_bp.extend([create_node_point(id) for id in ['m90012', 'm90011', 'm90013', 'm90014', 'm90012']])

path_pen = mod_nodes[7]
nodes_pen = ET.SubElement(path_pen, 'nodes')
nodes_pen.extend([create_node_point(id) for id in ['m90019', 'm90020']])

path_yoke = mod_nodes[10]
nodes_yoke = ET.SubElement(path_yoke, 'nodes')
nodes_yoke.extend([create_node_point(id) for id in ['m90031', 'm90032']])

path_mart = mod_nodes[15]
nodes_mart = ET.SubElement(path_mart, 'nodes')
nodes_mart.extend([create_node_point(id) for id in ['m90043', 'm90041', 'm90042', 'm90044', 'm90043']])

modeling.extend(mod_nodes)

# Insert into pieces
delantero = root.find('.//piece[@name="Delantero"]')
ip_del = delantero.find('iPaths')
if ip_del is None:
    ip_del = ET.SubElement(delantero, 'iPaths')
ip_del.append(ET.Element('record', {'path': '90022'}))
ip_del.append(ET.Element('record', {'path': '90023'}))

posterior = root.find('.//piece[@name="Posterior"]')
ip_post = posterior.find('iPaths')
if ip_post is None:
    ip_post = ET.SubElement(posterior, 'iPaths')
ip_post.append(ET.Element('record', {'path': '90034'}))
ip_post.append(ET.Element('record', {'path': '90047'}))

# Fix the typo "Padamano"
for path in root.findall('.//path'):
    if path.get('name') == 'Padamano':
        path.set('name', 'Pasamanos')

# Formatting back to string to save
xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = xmlstr.replace(' />', '/>')

# Quick hack to make sure it declares XML correctly
with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Caballero fixes applied successfully!")
