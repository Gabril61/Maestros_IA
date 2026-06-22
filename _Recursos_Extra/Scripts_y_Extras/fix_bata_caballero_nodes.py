import xml.etree.ElementTree as ET

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

modeling = root.find('.//modeling')

# Create a mapping of calculation idObject -> modeling point id
# e.g., mapping['142'] = '891142'
# If multiple exist, take the first one.
calc_to_mod = {}
for pt in modeling.findall('point'):
    mod_id = pt.get('id')
    calc_id = pt.get('idObject')
    if mod_id and calc_id:
        calc_to_mod[calc_id] = mod_id

# Update all path nodes
for path in modeling.findall('path'):
    nodes = path.find('nodes')
    if nodes is not None:
        for node in nodes.findall('node'):
            calc_id = node.get('idObject')
            # If the node's idObject is a calculation ID (which is an error in Seamly2D),
            # replace it with the corresponding modeling point ID.
            if calc_id in calc_to_mod:
                # Check if calc_id is already a modeling ID?
                # If calc_id is in calc_to_mod as a value, it's already a mod_id.
                # But here we assume if it's a key in calc_to_mod, it's a calc_id.
                # Wait! What if mod_id == calc_id? (Sometimes people do that, but Seamly2D generates unique ids).
                if calc_id != calc_to_mod[calc_id]:
                    node.set('idObject', calc_to_mod[calc_id])

# Save it back
xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Nodes inside paths successfully remapped to modeling IDs.")
