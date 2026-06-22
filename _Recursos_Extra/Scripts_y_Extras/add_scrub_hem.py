import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

pt_id = 40200
line_id = 40300

points_to_extend = [
    ('40002', 'Ext_F_Cruce_Ruedo'),
    ('118', 'Ext_F_Nivel_Largo'),
    ('121', 'Ext_F_Costado_Ruedo'),
    ('221', 'Ext_T_Costado_Ruedo'),
    ('218', 'Ext_T_Nivel_Largo')
]

ext_ids = {}

# 1. Add Extension Points
for base_id, name in points_to_extend:
    calc.append(ET.Element('point', {
        'id': str(pt_id),
        'name': name,
        'type': 'endLine',
        'basePoint': base_id,
        'angle': '270',
        'length': '@D_RUEDO_PRENDA',
        'mx': '0.1',
        'my': '0.1',
        'showPointName': 'true'
    }))
    ext_ids[name] = str(pt_id)
    pt_id += 1

# 2. Add Vertical connecting lines
for base_id, name in points_to_extend:
    calc.append(ET.Element('line', {
        'id': str(line_id),
        'firstPoint': base_id,
        'secondPoint': ext_ids[name],
        'lineColor': 'black',
        'lineType': 'solidLine',
        'lineWeight': '0.35'
    }))
    line_id += 1

# 3. Add Horizontal connecting lines (The Hem edges)
hem_lines = [
    ('Ext_F_Cruce_Ruedo', 'Ext_F_Nivel_Largo'),
    ('Ext_F_Nivel_Largo', 'Ext_F_Costado_Ruedo'),
    ('Ext_T_Costado_Ruedo', 'Ext_T_Nivel_Largo')
]

for p1_name, p2_name in hem_lines:
    calc.append(ET.Element('line', {
        'id': str(line_id),
        'firstPoint': ext_ids[p1_name],
        'secondPoint': ext_ids[p2_name],
        'lineColor': 'black',
        'lineType': 'solidLine',
        'lineWeight': '0.7'
    }))
    line_id += 1

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Hem extensions added to Scrub Top Dama.")
