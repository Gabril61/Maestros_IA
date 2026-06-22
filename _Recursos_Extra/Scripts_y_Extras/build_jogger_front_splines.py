import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('draw/calculation')

points = [
    # Intersección Cadera
    {'id': '126', 'name': 'F_Cadera_Centro', 'type': 'pointOfIntersection', 'firstPoint': '103', 'angle1': '0', 'secondPoint': '106', 'angle2': '90'},
    
    # Costado Cadera
    {'id': '127', 'name': 'F_Cadera_Costado', 'type': 'endLine', 'basePoint': '126', 'angle': '180', 'length': '((@I_CONTCADBA + @M_HOLGURA_PANTALON) / 4)'},
    
    # Costado Tiro
    {'id': '128', 'name': 'F_Tiro_Costado', 'type': 'pointOfIntersection', 'firstPoint': '102', 'angle1': '180', 'secondPoint': '127', 'angle2': '270'},
    
    # Punto guía para la curva de tiro delantero (bisectriz)
    {'id': '129', 'name': 'F_Tiro_Guia', 'type': 'pointOfIntersection', 'firstPoint': '106', 'angle1': '45', 'secondPoint': '107', 'angle2': '135'},
]

for p in points:
    attrs = {k: v for k, v in p.items() if k not in ['id', 'type', 'name']}
    attrs['id'] = p['id']
    attrs['name'] = p['name']
    attrs['type'] = p['type']
    el = ET.Element('point', attrs)
    calc.append(el)

# Splines
splines = [
    # Curva Centro Frente (Cintura a Cadera)
    {'id': '130', 'name': 'Curve_F_Centro', 'type': 'simpleInteractive', 'firstPoint': '117', 'secondPoint': '126', 'angle1': '270', 'length1': '3', 'angle2': '90', 'length2': '3'},
    # Curva de Tiro Frente
    {'id': '131', 'name': 'Curve_F_Tiro', 'type': 'simpleInteractive', 'firstPoint': '126', 'secondPoint': '107', 'angle1': '270', 'length1': '3', 'angle2': '180', 'length2': '2'},
    # Curva Entrepierna
    {'id': '132', 'name': 'Curve_F_Entre', 'type': 'simpleInteractive', 'firstPoint': '107', 'secondPoint': '112', 'angle1': '270', 'length1': '4', 'angle2': '90', 'length2': '4'},
    # Curva Costado (Cintura a Cadera)
    {'id': '133', 'name': 'Curve_F_Cost_Sup', 'type': 'simpleInteractive', 'firstPoint': '118', 'secondPoint': '127', 'angle1': '270', 'length1': '2', 'angle2': '90', 'length2': '2'},
    # Curva Costado (Cadera a Rodilla)
    {'id': '134', 'name': 'Curve_F_Cost_Inf', 'type': 'simpleInteractive', 'firstPoint': '127', 'secondPoint': '113', 'angle1': '270', 'length1': '8', 'angle2': '90', 'length2': '4'},
]

for sp in splines:
    el = ET.Element('spline', {
        'id': sp['id'],
        'point1': sp['firstPoint'],
        'point4': sp['secondPoint'],
        'angle1': sp['angle1'],
        'length1': sp['length1'],
        'angle2': sp['angle2'],
        'length2': sp['length2'],
        'type': sp['type'],
        'color': 'black'
    })
    calc.append(el)

# Straight lines for bota (Rodilla a Bota)
lines = [
    {'id': '135', 'first': '112', 'second': '114'},
    {'id': '136', 'first': '113', 'second': '115'},
    {'id': '137', 'first': '114', 'second': '115'}, # Bota bottom
    {'id': '138', 'first': '118', 'second': '117'}, # Cintura top
]
for ln in lines:
    el = ET.Element('line', {
        'id': ln['id'],
        'firstPoint': ln['first'],
        'secondPoint': ln['second'],
        'lineColor': 'black',
        'lineType': 'solidLine'
    })
    calc.append(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Front block splines and lines added!")
