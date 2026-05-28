import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('draw/calculation')

# Trasero Points
points = [
    # Base B
    {'id': '201', 'name': 'B', 'type': 'single', 'x': '70', 'y': '10', 'mx': '0.1', 'my': '0.1'},
    
    # Niveles de Altura (Y axis)
    {'id': '202', 'name': 'T_Nivel_Tiro', 'type': 'endLine', 'basePoint': '201', 'angle': '270', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)'},
    {'id': '203', 'name': 'T_Nivel_Cadera', 'type': 'endLine', 'basePoint': '202', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)/3'},
    {'id': '204', 'name': 'T_Nivel_Bota', 'type': 'endLine', 'basePoint': '202', 'angle': '270', 'length': '@I_ENTREPIERNA'},
    {'id': '205', 'name': 'T_Nivel_Rodilla', 'type': 'endLine', 'basePoint': '204', 'angle': '90', 'length': '@I_ALTO_RODILLA'},
    
    # Anchos (X axis) en Nivel Tiro
    # El trasero se construye hacia la izquierda
    {'id': '206', 'name': 'T_Tiro_Centro', 'type': 'endLine', 'basePoint': '202', 'angle': '180', 'length': '((@I_CONTCADBA + @M_HOLGURA_PANTALON) / 4) + 1'},
    # Avance de tiro trasero: Contorno Cadera / 10
    {'id': '207', 'name': 'T_Tiro_Avance', 'type': 'endLine', 'basePoint': '206', 'angle': '180', 'length': '(@I_CONTCADBA / 10)'},
    
    # Linea de plomo (Centro de la pierna)
    {'id': '208', 'name': 'T_Plomo_Tiro', 'type': 'alongLine', 'firstPoint': '202', 'secondPoint': '207', 'length': 'CurrentLength/2'},
    
    # Proyectar Linea de Plomo arriba y abajo
    {'id': '209', 'name': 'T_Plomo_Cintura', 'type': 'pointOfIntersection', 'firstPoint': '208', 'angle1': '90', 'secondPoint': '201', 'angle2': '180'},
    {'id': '210', 'name': 'T_Plomo_Rodilla', 'type': 'pointOfIntersection', 'firstPoint': '208', 'angle1': '270', 'secondPoint': '205', 'angle2': '180'},
    {'id': '211', 'name': 'T_Plomo_Bota', 'type': 'pointOfIntersection', 'firstPoint': '208', 'angle1': '270', 'secondPoint': '204', 'angle2': '180'},
    
    # Anchos Rodilla (Trasero es 2cm mas ancho que delantero en total, 1cm por lado)
    # Delantero era /4 - 1. Trasero será /4 + 1.
    {'id': '212', 'name': 'T_Rodilla_Ext', 'type': 'endLine', 'basePoint': '210', 'angle': '0', 'length': '(@I_CONT_RODILLA / 4) + 1'},
    {'id': '213', 'name': 'T_Rodilla_Int', 'type': 'endLine', 'basePoint': '210', 'angle': '180', 'length': '(@I_CONT_RODILLA / 4) + 1'},
    
    # Anchos Bota
    {'id': '214', 'name': 'T_Bota_Ext', 'type': 'endLine', 'basePoint': '211', 'angle': '0', 'length': '(@I_CONT_TOBILLO / 4) + 1'},
    {'id': '215', 'name': 'T_Bota_Int', 'type': 'endLine', 'basePoint': '211', 'angle': '180', 'length': '(@I_CONT_TOBILLO / 4) + 1'},
    
    # Cintura y Cadera Trasera
    # Interseccion de linea centro con cintura y cadera
    {'id': '216', 'name': 'T_Cintura_Centro', 'type': 'pointOfIntersection', 'firstPoint': '206', 'angle1': '90', 'secondPoint': '201', 'angle2': '180'},
    {'id': '217', 'name': 'T_Cadera_Centro', 'type': 'pointOfIntersection', 'firstPoint': '206', 'angle1': '90', 'secondPoint': '203', 'angle2': '180'},
    
    # Elevacion y entrada de tiro trasero (para acomodar el gluteo)
    {'id': '218', 'name': 'T_Cintura_Centro_Elevado', 'type': 'endLine', 'basePoint': '216', 'angle': '30', 'length': '3'},
    
    # Costado Cintura y Cadera
    {'id': '219', 'name': 'T_Cadera_Costado', 'type': 'endLine', 'basePoint': '217', 'angle': '0', 'length': '((@I_CONTCADBA + @M_HOLGURA_PANTALON) / 4) + 1'},
    {'id': '220', 'name': 'T_Tiro_Costado', 'type': 'pointOfIntersection', 'firstPoint': '202', 'angle1': '0', 'secondPoint': '219', 'angle2': '270'},
    {'id': '221', 'name': 'T_Cintura_Costado', 'type': 'pointOfIntersection', 'firstPoint': '201', 'angle1': '0', 'secondPoint': '219', 'angle2': '90'},
    
    # Ajuste de la cintura desde T_Cintura_Centro_Elevado hacia Costado
    {'id': '222', 'name': 'T_Cintura_Extremo', 'type': 'pointOfIntersection', 'firstPoint': '218', 'angle1': '345', 'secondPoint': '221', 'angle2': '270'},
    
    # Punto guía para la curva de tiro trasero (bisectriz)
    {'id': '223', 'name': 'T_Tiro_Guia', 'type': 'pointOfIntersection', 'firstPoint': '206', 'angle1': '135', 'secondPoint': '207', 'angle2': '45'},
]

for p in points:
    attrs = {k: v for k, v in p.items() if k not in ['id', 'type', 'name']}
    attrs['id'] = p['id']
    attrs['name'] = p['name']
    attrs['type'] = p['type']
    el = ET.Element('point', attrs)
    calc.append(el)

# Splines Trasero
splines = [
    # Curva Centro Trasero (Cintura Elevada a Cadera)
    {'id': '230', 'name': 'Curve_T_Centro', 'type': 'simpleInteractive', 'firstPoint': '218', 'secondPoint': '217', 'angle1': '250', 'length1': '3', 'angle2': '90', 'length2': '3'},
    # Curva de Tiro Trasero
    {'id': '231', 'name': 'Curve_T_Tiro', 'type': 'simpleInteractive', 'firstPoint': '217', 'secondPoint': '207', 'angle1': '270', 'length1': '4', 'angle2': '0', 'length2': '3'},
    # Curva Entrepierna Trasera
    {'id': '232', 'name': 'Curve_T_Entre', 'type': 'simpleInteractive', 'firstPoint': '207', 'secondPoint': '213', 'angle1': '270', 'length1': '5', 'angle2': '90', 'length2': '5'},
    # Curva Costado (Cintura a Cadera)
    {'id': '233', 'name': 'Curve_T_Cost_Sup', 'type': 'simpleInteractive', 'firstPoint': '222', 'secondPoint': '219', 'angle1': '270', 'length1': '2', 'angle2': '90', 'length2': '2'},
    # Curva Costado (Cadera a Rodilla)
    {'id': '234', 'name': 'Curve_T_Cost_Inf', 'type': 'simpleInteractive', 'firstPoint': '219', 'secondPoint': '212', 'angle1': '270', 'length1': '8', 'angle2': '90', 'length2': '4'},
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

# Straight lines Trasero
lines = [
    {'id': '235', 'first': '213', 'second': '215'},
    {'id': '236', 'first': '212', 'second': '214'},
    {'id': '237', 'first': '214', 'second': '215'}, # Bota bottom
    {'id': '238', 'first': '218', 'second': '222'}, # Cintura top
    {'id': '239', 'first': '201', 'second': '202'},
    {'id': '240', 'first': '202', 'second': '206'}
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
print("Back block geometry added!")
