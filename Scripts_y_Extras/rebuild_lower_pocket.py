import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

calc = root.find('.//calculation')
modeling = root.find('.//modeling')

# 1. Nuke invalid lower pocket elements
def delete_by_id(parent, tag, id_list):
    to_remove = []
    for elem in parent.findall(tag):
        if elem.get('id') in id_list:
            to_remove.append(elem)
    for elem in to_remove:
        parent.remove(elem)

# Remove invalid lines 73001-73005
delete_by_id(calc, 'line', ['73001', '73002', '73003', '73004', '73005'])

# Remove invalid modeling points 891142-891146
delete_by_id(modeling, 'point', ['891142', '891143', '891144', '891145', '891146'])

# Remove invalid path 890100
delete_by_id(modeling, 'path', ['890100'])

# 2. Rebuild cleanly
new_pts = [
    ET.Element('point', {'angle': '0', 'basePoint': '116', 'id': '74000', 'length': '(@S_CONT_BUSTO/8)', 'name': 'F_Bolsillo_Inf_Ref', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '74000', 'id': '74001', 'length': '5', 'name': 'F_Bolsillo_Inf_TopCenter', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '180', 'basePoint': '74001', 'id': '74002', 'length': '8', 'name': 'F_Bolsillo_Inf_TL', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '0', 'basePoint': '74001', 'id': '74003', 'length': '8', 'name': 'F_Bolsillo_Inf_TR', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '74002', 'id': '74004', 'length': '16', 'name': 'F_Bolsillo_Inf_BL', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '74003', 'id': '74005', 'length': '16', 'name': 'F_Bolsillo_Inf_BR', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
    ET.Element('point', {'angle': '270', 'basePoint': '74001', 'id': '74006', 'length': '18', 'name': 'F_Bolsillo_Inf_BotCenter', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'}),
]
calc.extend(new_pts)

new_lines = [
    ET.Element('line', {'firstPoint': '74002', 'id': '74010', 'secondPoint': '74003', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '74003', 'id': '74011', 'secondPoint': '74005', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '74005', 'id': '74012', 'secondPoint': '74006', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '74006', 'id': '74013', 'secondPoint': '74004', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
    ET.Element('line', {'firstPoint': '74004', 'id': '74014', 'secondPoint': '74002', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}),
]
calc.extend(new_lines)

mod_pts = [
    ET.Element('point', {'id': '75002', 'idObject': '74002', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '75003', 'idObject': '74003', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '75005', 'idObject': '74005', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '75006', 'idObject': '74006', 'inUse': 'true', 'type': 'modeling'}),
    ET.Element('point', {'id': '75004', 'idObject': '74004', 'inUse': 'true', 'type': 'modeling'}),
]
modeling.extend(mod_pts)

p_lower = ET.Element('path', {'cut': 'false', 'id': '76000', 'inUse': 'true', 'lineColor': 'darkBlue', 'lineType': 'dashLine', 'lineWeight': '0.35', 'name': 'Bolsillo_Inferior', 'type': '2'})
n_lower = ET.SubElement(p_lower, 'nodes')
n_lower.extend([
    ET.Element('node', {'idObject': '75002', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '75003', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '75005', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '75006', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '75004', 'type': 'NodePoint'}),
    ET.Element('node', {'idObject': '75002', 'type': 'NodePoint'}),
])
modeling.append(p_lower)

delantero = root.find('.//piece[@name="Delantero"]')
ip_del = delantero.find('iPaths')
if ip_del is not None:
    # remove old broken path 890100
    to_remove = []
    for r in ip_del.findall('record'):
        if r.get('path') == '890100':
            to_remove.append(r)
    for r in to_remove:
        ip_del.remove(r)
    
    # add new
    ip_del.append(ET.Element('record', {'path': '76000'}))

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Nuke and pave of lower pocket successful.")
