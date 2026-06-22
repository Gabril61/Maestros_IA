import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('draw/calculation')

points = [
    # PRETINA
    {'id': '301', 'name': 'C', 'type': 'single', 'x': '120', 'y': '10', 'mx': '0.1', 'my': '0.1'},
    {'id': '302', 'name': 'P_Largo_Mitad', 'type': 'endLine', 'basePoint': '301', 'angle': '0', 'length': '((@I_CONTCINBA + @M_HOLGURA_PANTALON) / 2)'},
    {'id': '303', 'name': 'P_Ancho_Doble', 'type': 'endLine', 'basePoint': '301', 'angle': '270', 'length': '(@D_ANCHO_PRETINA * 2)'},
    {'id': '304', 'name': 'P_Esquina', 'type': 'pointOfIntersection', 'firstPoint': '302', 'angle1': '270', 'secondPoint': '303', 'angle2': '0'},
    # Linea de doblez pretina (mitad)
    {'id': '305', 'name': 'P_Linea_Doblez_Izq', 'type': 'endLine', 'basePoint': '301', 'angle': '270', 'length': '@D_ANCHO_PRETINA'},
    {'id': '306', 'name': 'P_Linea_Doblez_Der', 'type': 'endLine', 'basePoint': '302', 'angle': '270', 'length': '@D_ANCHO_PRETINA'},
    
    # PUÑOS (RIB) PARA 1 PIERNA (Se cortan 2)
    # Largo = Ancho del tobillo de la pierna completa.
    # El delantero tiene (@I_CONT_TOBILLO / 4) - 1 por lado = (@I_CONT_TOBILLO / 2) - 2.
    # El trasero tiene (@I_CONT_TOBILLO / 4) + 1 por lado = (@I_CONT_TOBILLO / 2) + 2.
    # Total de 1 pierna = @I_CONT_TOBILLO.
    {'id': '401', 'name': 'D', 'type': 'single', 'x': '120', 'y': '40', 'mx': '0.1', 'my': '0.1'},
    # Hacemos el puño 2 cm mas ajustado que la bota para que recoja la tela.
    {'id': '402', 'name': 'Rib_Largo', 'type': 'endLine', 'basePoint': '401', 'angle': '0', 'length': '@I_CONT_TOBILLO - 2'},
    # Ancho del rib (5 cm visible, 10 cm total)
    {'id': '403', 'name': 'Rib_Ancho', 'type': 'endLine', 'basePoint': '401', 'angle': '270', 'length': '10'},
    {'id': '404', 'name': 'Rib_Esquina', 'type': 'pointOfIntersection', 'firstPoint': '402', 'angle1': '270', 'secondPoint': '403', 'angle2': '0'},
    # Linea de doblez rib (mitad)
    {'id': '405', 'name': 'Rib_Linea_Doblez_Izq', 'type': 'endLine', 'basePoint': '401', 'angle': '270', 'length': '5'},
    {'id': '406', 'name': 'Rib_Linea_Doblez_Der', 'type': 'endLine', 'basePoint': '402', 'angle': '270', 'length': '5'},
]

for p in points:
    attrs = {k: v for k, v in p.items() if k not in ['id', 'type', 'name']}
    attrs['id'] = p['id']
    attrs['name'] = p['name']
    attrs['type'] = p['type']
    el = ET.Element('point', attrs)
    calc.append(el)

lines = [
    # Pretina
    {'id': '310', 'first': '301', 'second': '302'},
    {'id': '311', 'first': '302', 'second': '304'},
    {'id': '312', 'first': '304', 'second': '303'},
    {'id': '313', 'first': '303', 'second': '301'},
    {'id': '314', 'first': '305', 'second': '306', 'color': 'green', 'type': 'dotLine'},
    
    # Rib
    {'id': '410', 'first': '401', 'second': '402'},
    {'id': '411', 'first': '402', 'second': '404'},
    {'id': '412', 'first': '404', 'second': '403'},
    {'id': '413', 'first': '403', 'second': '401'},
    {'id': '414', 'first': '405', 'second': '406', 'color': 'green', 'type': 'dotLine'}
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
print("Pretina and Rib geometries added!")
