import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('draw/calculation')

# Clean up existing points just in case
for child in list(calc):
    calc.remove(child)

points = [
    # Base A
    {'id': '101', 'name': 'A', 'type': 'single', 'x': '10', 'y': '10', 'mx': '0.1', 'my': '0.1'},
    
    # Niveles de Altura (Y axis)
    {'id': '102', 'name': 'F_Nivel_Tiro', 'type': 'endLine', 'basePoint': '101', 'angle': '270', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)'},
    {'id': '103', 'name': 'F_Nivel_Cadera', 'type': 'endLine', 'basePoint': '102', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)/3'},
    {'id': '104', 'name': 'F_Nivel_Bota', 'type': 'endLine', 'basePoint': '102', 'angle': '270', 'length': '@I_ENTREPIERNA'},
    {'id': '105', 'name': 'F_Nivel_Rodilla', 'type': 'endLine', 'basePoint': '104', 'angle': '90', 'length': '@I_ALTO_RODILLA'},
    
    # Anchos (X axis) en Nivel Tiro
    # Contorno cadera / 4 + holgura
    {'id': '106', 'name': 'F_Tiro_Centro', 'type': 'endLine', 'basePoint': '102', 'angle': '0', 'length': '((@I_CONTCADBA + @M_HOLGURA_PANTALON) / 4)'},
    # Avance de tiro delantero: Contorno Cadera / 20 (fórmula estándar o contorno muslo)
    {'id': '107', 'name': 'F_Tiro_Avance', 'type': 'endLine', 'basePoint': '106', 'angle': '0', 'length': '(@I_CONTCADBA / 20)'},
    
    # Linea de plomo (Centro de la pierna)
    # Se calcula como la mitad desde A (101) proyectado hasta el Avance de Tiro
    {'id': '108', 'name': 'F_Plomo_Tiro', 'type': 'alongLine', 'firstPoint': '102', 'secondPoint': '107', 'length': 'CurrentLength/2'},
    
    # Proyectar Linea de Plomo arriba y abajo
    {'id': '109', 'name': 'F_Plomo_Cintura', 'type': 'pointOfIntersection', 'firstPoint': '108', 'angle1': '90', 'secondPoint': '101', 'angle2': '0'},
    {'id': '110', 'name': 'F_Plomo_Rodilla', 'type': 'pointOfIntersection', 'firstPoint': '108', 'angle1': '270', 'secondPoint': '105', 'angle2': '0'},
    {'id': '111', 'name': 'F_Plomo_Bota', 'type': 'pointOfIntersection', 'firstPoint': '108', 'angle1': '270', 'secondPoint': '104', 'angle2': '0'},
    
    # Anchos Rodilla
    # Jogger: Rodilla ajustada. (Contorno / 4) - 1cm para el delantero
    {'id': '112', 'name': 'F_Rodilla_Int', 'type': 'endLine', 'basePoint': '110', 'angle': '0', 'length': '(@I_CONT_RODILLA / 4) - 1'},
    {'id': '113', 'name': 'F_Rodilla_Ext', 'type': 'endLine', 'basePoint': '110', 'angle': '180', 'length': '(@I_CONT_RODILLA / 4) - 1'},
    
    # Anchos Bota (Tobillo)
    # Jogger: Bota muy ajustada. (Contorno / 4) - 1cm para el delantero
    {'id': '114', 'name': 'F_Bota_Int', 'type': 'endLine', 'basePoint': '111', 'angle': '0', 'length': '(@I_CONT_TOBILLO / 4) - 1'},
    {'id': '115', 'name': 'F_Bota_Ext', 'type': 'endLine', 'basePoint': '111', 'angle': '180', 'length': '(@I_CONT_TOBILLO / 4) - 1'},
    
    # Cintura Superior
    {'id': '116', 'name': 'F_Cintura_Centro', 'type': 'pointOfIntersection', 'firstPoint': '106', 'angle1': '90', 'secondPoint': '101', 'angle2': '0'},
    # Caída del centro delantero por anatomía (1.5 cm)
    {'id': '117', 'name': 'F_Cintura_Centro_Bajo', 'type': 'endLine', 'basePoint': '116', 'angle': '270', 'length': '1.5'},
    
    # Ancho de cintura: (Contorno / 4) + holgura cintura (o pinza si la hubiera)
    # En joggers médicos usualmente se hace elástico, así que la cintura llega casi a la medida de la cadera para poder subirlo.
    # Pero para no hacer mucho bulto, lo haremos intermedio: Cadera/4
    {'id': '118', 'name': 'F_Cintura_Costado', 'type': 'endLine', 'basePoint': '117', 'angle': '180', 'length': '((@I_CONTCADBA + @M_HOLGURA_PANTALON) / 4)'}
]

for p in points:
    attrs = {k: v for k, v in p.items() if k not in ['id', 'type', 'name']}
    attrs['id'] = p['id']
    attrs['name'] = p['name']
    attrs['type'] = p['type']
    el = ET.Element('point', attrs)
    calc.append(el)

# Lines
lines = [
    {'id': '120', 'first': '101', 'second': '102'},
    {'id': '121', 'first': '102', 'second': '107'},
    {'id': '122', 'first': '109', 'second': '111'}, # Plomo
    {'id': '123', 'first': '113', 'second': '112'}, # Rodilla
    {'id': '124', 'first': '115', 'second': '114'}, # Bota
    {'id': '125', 'first': '106', 'second': '116'}  # Centro Frente
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
print("Front block base geometry added!")
