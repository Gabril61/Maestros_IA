import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('draw/calculation')

points = [
    # BOLSILLO CARGO (Pieza separada)
    {'id': '501', 'name': 'E', 'type': 'single', 'x': '140', 'y': '10', 'mx': '0.1', 'my': '0.1'},
    {'id': '502', 'name': 'Cargo_Ancho', 'type': 'endLine', 'basePoint': '501', 'angle': '0', 'length': '18'},
    {'id': '503', 'name': 'Cargo_Largo', 'type': 'endLine', 'basePoint': '501', 'angle': '270', 'length': '20'},
    {'id': '504', 'name': 'Cargo_Esquina', 'type': 'pointOfIntersection', 'firstPoint': '502', 'angle1': '270', 'secondPoint': '503', 'angle2': '0'},
    
    # Marca de doblez superior para el dobladillo del bolsillo (3cm)
    {'id': '505', 'name': 'Cargo_Doblez_Izq', 'type': 'endLine', 'basePoint': '501', 'angle': '270', 'length': '3'},
    {'id': '506', 'name': 'Cargo_Doblez_Der', 'type': 'endLine', 'basePoint': '502', 'angle': '270', 'length': '3'},
    
    # BOLSILLO DIAGONAL FRONTAL (Marcas en Delantero)
    # Entrada de bolsillo: 4cm desde el costado hacia el centro
    {'id': '507', 'name': 'F_Bols_Boca_Sup', 'type': 'alongLine', 'firstPoint': '118', 'secondPoint': '117', 'length': '4'},
    # Entrada inferior: 15cm desde el costado hacia abajo por la curva
    # Nota: para simplificar en el borrador base usaremos linea recta desde la cadera
    {'id': '508', 'name': 'F_Bols_Boca_Inf', 'type': 'alongLine', 'firstPoint': '118', 'secondPoint': '127', 'length': '15'},
    
    # Fondo de bolsillo
    {'id': '509', 'name': 'F_Bols_Fondo_Centro', 'type': 'alongLine', 'firstPoint': '118', 'secondPoint': '117', 'length': '12'},
    {'id': '510', 'name': 'F_Bols_Fondo_Inf', 'type': 'alongLine', 'firstPoint': '118', 'secondPoint': '127', 'length': '28'},
    # Esquina interior del fondo de bolsillo
    {'id': '511', 'name': 'F_Bols_Fondo_Esq', 'type': 'pointOfIntersection', 'firstPoint': '509', 'angle1': '270', 'secondPoint': '510', 'angle2': '0'},
]

for p in points:
    attrs = {k: v for k, v in p.items() if k not in ['id', 'type', 'name']}
    attrs['id'] = p['id']
    attrs['name'] = p['name']
    attrs['type'] = p['type']
    el = ET.Element('point', attrs)
    calc.append(el)

lines = [
    # Cargo
    {'id': '520', 'first': '501', 'second': '502'},
    {'id': '521', 'first': '502', 'second': '504'},
    {'id': '522', 'first': '504', 'second': '503'},
    {'id': '523', 'first': '503', 'second': '501'},
    {'id': '524', 'first': '505', 'second': '506', 'color': 'green', 'type': 'dotLine'},
    
    # Marcas Bolsillo Frontal
    {'id': '525', 'first': '507', 'second': '508', 'color': 'blue', 'type': 'dashDotLine'}, # Boca
    {'id': '526', 'first': '509', 'second': '511', 'color': 'red', 'type': 'dashDotLine'}, # Fondo interior
    {'id': '527', 'first': '511', 'second': '510', 'color': 'red', 'type': 'dashDotLine'}, # Fondo inferior
]
for ln in lines:
    el = ET.Element('line', {
        'id': ln['id'],
        'firstPoint': ln['first'],
        'secondPoint': ln['second'],
        'lineColor': ln.get('color', 'black'),
        'lineType': ln.get('type', 'solidLine')
    })
    calc.append(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Pockets added!")
