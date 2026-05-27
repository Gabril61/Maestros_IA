import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'

tree = ET.parse(file_path)
root = tree.getroot()

# 1. Remove the bad points and lines from <calculation>
calc = root.find('.//calculation')

# Find points with name Ext_...
bad_pts = [p for p in calc.findall('point') if p.get('name') and p.get('name').startswith('Ext_')]
bad_pt_ids = [p.get('id') for p in bad_pts]

for p in bad_pts:
    calc.remove(p)

# Find lines connected to bad points
bad_lines = []
for l in calc.findall('line'):
    if l.get('firstPoint') in bad_pt_ids or l.get('secondPoint') in bad_pt_ids:
        bad_lines.append(l)

for l in bad_lines:
    calc.remove(l)

# 2. Add them back with IDs 15000+
hem_points = [
    {'base': '11002', 'name': 'B_Cruce_Ruedo'},
    {'base': '301', 'name': 'F_Ruedo'},
    {'base': '502', 'name': 'F_Ruedo_Pinza'},
    {'base': '303', 'name': 'F_Costado_Ruedo'},
    {'base': '403', 'name': 'T_Costado_Ruedo'},
    {'base': '602', 'name': 'T_Ruedo_Pinza'},
    {'base': '401', 'name': 'T_Ruedo'},
]

existing_points = {p.get('id'): p for p in calc.findall('point')}
valid_hem_points = [hp for hp in hem_points if hp['base'] in existing_points]

new_points = []
base_id = 15000

for i, hp in enumerate(valid_hem_points):
    pt_id = str(base_id + i)
    hp['ext_id'] = pt_id
    new_pt = ET.Element('point', {
        'id': pt_id,
        'name': f"Ext_{hp['name']}",
        'type': 'endLine',
        'basePoint': hp['base'],
        'angle': '270',
        'length': '@D_RUEDO_PRENDA',
        'mx': '0.1',
        'my': '0.1',
        'showPointName': 'true'
    })
    new_points.append(new_pt)

for pt in new_points:
    calc.append(pt)

# Lines
new_lines = []
line_id = 15100

delantero_bases = ['11002', '301', '502', '303']
del_exts = [hp['ext_id'] for hp in valid_hem_points if hp['base'] in delantero_bases]
for i in range(len(del_exts) - 1):
    new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': del_exts[i], 'secondPoint': del_exts[i+1], 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}))
    line_id += 1
    
trasero_bases = ['403', '602', '401']
tras_exts = [hp['ext_id'] for hp in valid_hem_points if hp['base'] in trasero_bases]
for i in range(len(tras_exts) - 1):
    new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': tras_exts[i], 'secondPoint': tras_exts[i+1], 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'}))
    line_id += 1

# Verticals
for hp in valid_hem_points:
    if hp['base'] in ['11002', '303', '403', '401']:
        new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': hp['base'], 'secondPoint': hp['ext_id'], 'lineColor': 'black'}))
        line_id += 1

for l in new_lines:
    calc.append(l)

# 3. Fix the modeling points
mapping = {}
for i, hp in enumerate(valid_hem_points):
    mapping[hp['base']] = hp['ext_id']
    # And map the erroneous 1200X back to 1500X
    mapping[str(12000 + i)] = hp['ext_id']

for pt in root.findall('.//modeling//point'):
    old_id = pt.get('idObject')
    if old_id in mapping:
        pt.set('idObject', mapping[old_id])

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Fixed ID collision in Blazer_Dama_Maestro.val successfully!")
