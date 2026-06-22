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

# 1. Update Upper Pocket Coordinates
# Chest pocket center at same X as lower pocket (which is at length Busto/8 = 11.5)
# Width = 11cm. Center = 11.5. So it goes from 6 to 17.
# 890010 = Ref point at X=11.5 on Nivel Pecho (109)
for pt in calc.findall('point'):
    if pt.get('id') == '890010':
        pt.set('length', '(@S_CONT_BUSTO/8)') # Center X
    elif pt.get('id') == '890011': # Center dropped by 2cm -> TopCenter
        pt.set('length', '2')
        pt.set('name', 'F_BP_TopCenter')
    elif pt.get('id') == '890012': # TL
        pt.set('angle', '180')
        pt.set('length', '5.5')
        pt.set('name', 'F_BP_TL')
    elif pt.get('id') == '890013': # TR
        # The script originally had BR here. Let's fix the logic.
        pass

# Let's just remove and recreate the points for the upper pocket to be safe.
# We will identify them by ID and overwrite their attributes.
updates = {
    '890010': {'angle': '0', 'basePoint': '109', 'length': '(@S_CONT_BUSTO/8)', 'name': 'F_BP_Center', 'type': 'endLine'},
    '890011': {'angle': '270', 'basePoint': '890010', 'length': '2', 'name': 'F_BP_TopCenter', 'type': 'endLine'},
    '890012': {'angle': '180', 'basePoint': '890011', 'length': '5.5', 'name': 'F_BP_TL', 'type': 'endLine'},
    '890013': {'angle': '0', 'basePoint': '890011', 'length': '5.5', 'name': 'F_BP_TR', 'type': 'endLine'},
    '890014': {'angle': '270', 'basePoint': '890012', 'length': '13', 'name': 'F_BP_BL', 'type': 'endLine'},
    '890025': {'angle': '270', 'basePoint': '890013', 'length': '13', 'name': 'F_BP_BR', 'type': 'endLine'}, # New point
}

for pt in calc.findall('point'):
    if pt.get('id') in updates:
        for k, v in updates[pt.get('id')].items():
            pt.set(k, v)

# Add the new point 890025 if it doesn't exist
if not calc.find('.//point[@id="890025"]'):
    new_pt = ET.Element('point', {'angle': '270', 'basePoint': '890013', 'id': '890025', 'length': '13', 'name': 'F_BP_BR', 'type': 'endLine', 'mx':'0.1', 'my':'0.1', 'showPointName': 'false'})
    # Insert it near 890014
    for i, child in enumerate(calc):
        if child.get('id') == '890014':
            calc.insert(i + 1, new_pt)
            break

# Update lines
lines_updates = {
    '890015': {'firstPoint': '890012', 'secondPoint': '890013'}, # Top
    '890016': {'firstPoint': '890013', 'secondPoint': '890025'}, # Right
    '890017': {'firstPoint': '890025', 'secondPoint': '890014'}, # Bottom
    '890018': {'firstPoint': '890014', 'secondPoint': '890012'}, # Left
}
for ln in calc.findall('line'):
    if ln.get('id') in lines_updates:
        for k, v in lines_updates[ln.get('id')].items():
            ln.set(k, v)

# Update Pen Slot (3.5 cm from the right side)
for pt in calc.findall('point'):
    if pt.get('id') == '890019':
        pt.set('firstPoint', '890013')
        pt.set('secondPoint', '890012')
        pt.set('length', '3.5')
        pt.set('name', 'F_BP_PenTop')
    elif pt.get('id') == '890020':
        pt.set('firstPoint', '890025')
        pt.set('secondPoint', '890014')
        pt.set('length', '3.5')
        pt.set('name', 'F_BP_PenBot')

# Update modeling nodes for Chest Pocket
# The path nodes were m890012, m890011, m890013, m890014, m890012. We need to update them.
# The path id is 890022.
path_bp = modeling.find('.//path[@id="890022"]')
if path_bp is not None:
    nodes = path_bp.find('nodes')
    if nodes is not None:
        nodes.clear()
        nodes.extend([
            ET.Element('node', {'idObject': '890012', 'type': 'NodePoint'}),
            ET.Element('node', {'idObject': '890013', 'type': 'NodePoint'}),
            ET.Element('node', {'idObject': '890025', 'type': 'NodePoint'}),
            ET.Element('node', {'idObject': '890014', 'type': 'NodePoint'}),
            ET.Element('node', {'idObject': '890012', 'type': 'NodePoint'}),
        ])

# 2. Add Lower Pocket Detail
# We need to add modeling points for 142, 143, 145, 146, 144
# And a path for the lower pocket.
mod_nodes = []
for pid in ['142', '143', '145', '146', '144']:
    if not modeling.find(f'.//point[@idObject="{pid}"]'):
        mod_nodes.append(ET.Element('point', {'id': f'891{pid}', 'idObject': pid, 'inUse': 'true', 'type': 'modeling'}))

if not modeling.find('.//path[@id="890100"]'):
    p_lower = ET.Element('path', {'cut': 'false', 'id': '890100', 'inUse': 'true', 'lineColor': 'darkBlue', 'lineType': 'dashLine', 'lineWeight': '0.35', 'name': 'Bolsillo_Inferior', 'type': '2'})
    nodes_lower = ET.SubElement(p_lower, 'nodes')
    nodes_lower.extend([
        ET.Element('node', {'idObject': '142', 'type': 'NodePoint'}),
        ET.Element('node', {'idObject': '143', 'type': 'NodePoint'}),
        ET.Element('node', {'idObject': '145', 'type': 'NodePoint'}),
        ET.Element('node', {'idObject': '146', 'type': 'NodePoint'}),
        ET.Element('node', {'idObject': '144', 'type': 'NodePoint'}),
        ET.Element('node', {'idObject': '142', 'type': 'NodePoint'}),
    ])
    mod_nodes.append(p_lower)

modeling.extend(mod_nodes)

# Insert into Delantero iPaths
delantero = root.find('.//piece[@name="Delantero"]')
ip_del = delantero.find('iPaths')
if ip_del is None:
    ip_del = ET.SubElement(delantero, 'iPaths')

if not ip_del.find('.//record[@path="890100"]'):
    ip_del.append(ET.Element('record', {'path': '890100'}))

# Ensure modeling points exist for the upper pocket
for pid in ['890012', '890013', '890025', '890014', '890019', '890020']:
    if not modeling.find(f'.//point[@idObject="{pid}"]'):
        modeling.append(ET.Element('point', {'id': f'892{pid}', 'idObject': pid, 'inUse': 'true', 'type': 'modeling'}))

# Remove newlines to avoid massive file bloat
xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
# Clean up duplicate whitespace from previous ET bugs
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Pocket fixes applied successfully!")
