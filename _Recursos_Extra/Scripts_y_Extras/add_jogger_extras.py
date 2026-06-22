import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('draftBlock/calculation')

# Base ID offset for new points
current_id = 5000

def add_point(calc_node, attrib):
    global current_id
    attrib['id'] = str(current_id)
    current_id += 1
    ET.SubElement(calc_node, 'point', attrib)

def add_line(calc_node, attrib):
    global current_id
    attrib['id'] = str(current_id)
    current_id += 1
    ET.SubElement(calc_node, 'line', attrib)

# 1. Cargo Pocket at X=200, Y=0
add_point(calc, {'name': 'C_Origen', 'x': '200', 'y': '0', 'type': 'single', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'C_Ancho', 'basePoint': str(current_id-1), 'angle': '0', 'length': '18', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'C_Largo', 'basePoint': str(current_id-2), 'angle': '270', 'length': '20', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'C_Esquina', 'basePoint': str(current_id-1), 'angle': '0', 'length': '18', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})

add_line(calc, {'firstPoint': str(current_id-4), 'secondPoint': str(current_id-3), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(current_id-4), 'secondPoint': str(current_id-2), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(current_id-3), 'secondPoint': str(current_id-2), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(current_id-4), 'secondPoint': str(current_id-2), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})


# 2. Pretina at X=300, Y=0
p_orig = current_id
add_point(calc, {'name': 'P_Origen', 'x': '300', 'y': '0', 'type': 'single', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'P_Mitad', 'basePoint': str(p_orig), 'angle': '0', 'length': '(@G_CONT_CINTURA + @M_HOLGURA_PANTALON)/2', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'P_Alto', 'basePoint': str(p_orig), 'angle': '270', 'length': '@D_ANCHO_PRETINA*2', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'P_Esquina', 'basePoint': str(p_orig+2), 'angle': '0', 'length': '(@G_CONT_CINTURA + @M_HOLGURA_PANTALON)/2', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'P_Centro', 'basePoint': str(p_orig), 'angle': '270', 'length': '@D_ANCHO_PRETINA', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'P_Centro_Fin', 'basePoint': str(p_orig+1), 'angle': '270', 'length': '@D_ANCHO_PRETINA', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})

add_line(calc, {'firstPoint': str(p_orig), 'secondPoint': str(p_orig+1), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(p_orig), 'secondPoint': str(p_orig+2), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(p_orig+1), 'secondPoint': str(p_orig+3), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(p_orig+2), 'secondPoint': str(p_orig+3), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(p_orig+4), 'secondPoint': str(p_orig+5), 'lineColor': 'black', 'lineType': 'dashLine', 'lineWeight': '0.35'})


# 3. Ribs (Puños) at X=300, Y=50
r_orig = current_id
add_point(calc, {'name': 'R_Origen', 'x': '300', 'y': '50', 'type': 'single', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'R_Mitad', 'basePoint': str(r_orig), 'angle': '0', 'length': '@I_CONT_TOBILLO - 2', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'R_Alto', 'basePoint': str(r_orig), 'angle': '270', 'length': '10', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'R_Esquina', 'basePoint': str(r_orig+2), 'angle': '0', 'length': '@I_CONT_TOBILLO - 2', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'R_Centro', 'basePoint': str(r_orig), 'angle': '270', 'length': '5', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})
add_point(calc, {'name': 'R_Centro_Fin', 'basePoint': str(r_orig+1), 'angle': '270', 'length': '5', 'type': 'endLine', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'})

add_line(calc, {'firstPoint': str(r_orig), 'secondPoint': str(r_orig+1), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(r_orig), 'secondPoint': str(r_orig+2), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(r_orig+1), 'secondPoint': str(r_orig+3), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(r_orig+2), 'secondPoint': str(r_orig+3), 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35'})
add_line(calc, {'firstPoint': str(r_orig+4), 'secondPoint': str(r_orig+5), 'lineColor': 'black', 'lineType': 'dashLine', 'lineWeight': '0.35'})

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print('Extra geometric blocks appended!')
