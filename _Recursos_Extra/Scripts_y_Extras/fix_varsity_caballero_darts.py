import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# 1. Identify Pinza points to delete
pts_to_delete = []
pt_ids_to_delete = []
for p in calc.findall('point'):
    name = p.get('name', '')
    if 'Pinza' in name:
        pts_to_delete.append(p)
        pt_ids_to_delete.append(p.get('id'))

for p in pts_to_delete:
    calc.remove(p)

# 2. Delete lines and splines touching Pinza points
elements_to_remove = []
for l in calc.findall('line'):
    if l.get('firstPoint') in pt_ids_to_delete or l.get('secondPoint') in pt_ids_to_delete:
        elements_to_remove.append(l)
for s in calc.findall('spline'):
    if s.get('point1') in pt_ids_to_delete or s.get('point4') in pt_ids_to_delete:
        elements_to_remove.append(s)

for el in elements_to_remove:
    try:
        calc.remove(el)
    except:
        pass

# 3. Add continuous lines and splines to close the block
# Front Armhole Spline (31 to 5)
calc.append(ET.Element('spline', {'angle1': '270', 'angle2': '130', 'color': 'black', 'id': '80001', 'length1': '3', 'length2': '4', 'point1': '31', 'point4': '5', 'type': 'simpleInteractive'}))

# Back Armhole Spline (120 to 104)
calc.append(ET.Element('spline', {'angle1': '270', 'angle2': '50', 'color': 'black', 'id': '80002', 'length1': '3', 'length2': '4', 'point1': '120', 'point4': '104', 'type': 'simpleInteractive'}))

# Front Waist Line (2 to 6)
calc.append(ET.Element('line', {'firstPoint': '2', 'id': '80003', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '6'}))

# Back Waist Line (101 to 105)
calc.append(ET.Element('line', {'firstPoint': '101', 'id': '80004', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '105'}))

# Front Hem Line (301 to 303)
calc.append(ET.Element('line', {'firstPoint': '301', 'id': '80005', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '303'}))

# Back Hem Line (401 to 403)
calc.append(ET.Element('line', {'firstPoint': '401', 'id': '80006', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '403'}))

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Varsity Caballero darts removed and draft closed.")
