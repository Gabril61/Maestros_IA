import xml.etree.ElementTree as ET

blazer_file = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(blazer_file)
root = tree.getroot()

for draft in root.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        calc = draft.find('calculation')
        if calc is not None:
            # 1. Ocultar la manga vieja (hacer invisibles las líneas 2000+)
            for child in calc:
                if child.tag in ('line', 'spline'):
                    child_id = child.attrib.get('id', '')
                    if child_id.startswith('20') and len(child_id) == 4:
                        # IDs como 2006, 2018, 2040, etc.
                        child.attrib['lineType'] = 'none'
                        if 'penStyle' in child.attrib:
                            child.attrib['penStyle'] = 'none'

# 2. Crear bloque Cuello_Sastre
collar_draft = ET.Element('draftBlock', {'name': 'Cuello_Sastre'})
calc_c = ET.SubElement(collar_draft, 'calculation')

# Puntos del cuello
collar_pts = [
    {'id': '13000', 'type': 'single', 'name': 'C_Origen', 'x': '400', 'y': '0'},
    # Centro atrás
    {'id': '13001', 'type': 'endLine', 'name': 'C_Medio_Atras_Tirilla', 'basePoint': '13000', 'angle': '270', 'length': '3'},
    {'id': '13002', 'type': 'endLine', 'name': 'C_Medio_Atras_Caida', 'basePoint': '13001', 'angle': '270', 'length': '4'},
    # Largo escote trasero
    {'id': '13003', 'type': 'endLine', 'name': 'C_Hombro', 'basePoint': '13000', 'angle': '0', 'length': 'Spl_T_Cuello_Ancho_T_Cuello_Prof'},
    # Largo escote delantero (solapa) - la longitud de F_Cuello_Ancho a A1 es 10
    {'id': '13004', 'type': 'endLine', 'name': 'C_Frente_Punto', 'basePoint': '13003', 'angle': '0', 'length': '10'},
    # Inclinación del frente para darle curva al cuello
    {'id': '13005', 'type': 'endLine', 'name': 'C_Frente_Elevado', 'basePoint': '13004', 'angle': '90', 'length': '1.5'},
    # Extremo de la tirilla y caída en el frente
    {'id': '13006', 'type': 'normal', 'name': 'C_Frente_Tirilla', 'firstPoint': '13005', 'secondPoint': '13003', 'angle': '0', 'length': '3'},
    {'id': '13007', 'type': 'normal', 'name': 'C_Frente_Punta', 'firstPoint': '13006', 'secondPoint': '13005', 'angle': '0', 'length': '5'},
    
    # Proyección de las líneas de atrás para cerrar el rectángulo base
    {'id': '13008', 'type': 'endLine', 'name': 'C_Hombro_Tirilla', 'basePoint': '13003', 'angle': '270', 'length': '3'},
    {'id': '13009', 'type': 'endLine', 'name': 'C_Hombro_Caida', 'basePoint': '13008', 'angle': '270', 'length': '4'},
]

for p in collar_pts:
    p['mx'] = '0.1'
    p['my'] = '0.1'
    p['showPointName'] = 'true'
    ET.SubElement(calc_c, 'point', p)

# Líneas y curvas del cuello
collar_lines = [
    {'id': '13010', 'firstPoint': '13000', 'secondPoint': '13002', 'lineColor': 'black'},
    {'id': '13011', 'firstPoint': '13002', 'secondPoint': '13009', 'lineColor': 'black'},
    {'id': '13012', 'firstPoint': '13000', 'secondPoint': '13003', 'lineColor': 'black'},
    {'id': '13013', 'firstPoint': '13001', 'secondPoint': '13008', 'lineColor': 'black'},
]

for l in collar_lines:
    ET.SubElement(calc_c, 'line', l)

# Splines para las curvas del cuello sastre
ET.SubElement(calc_c, 'spline', {'id': '13020', 'type': 'simpleInteractive', 'point1': '13003', 'point4': '13005', 'angle1': '0', 'angle2': '180', 'length1': '3', 'length2': '3', 'color': 'black'})
ET.SubElement(calc_c, 'spline', {'id': '13021', 'type': 'simpleInteractive', 'point1': '13008', 'point4': '13006', 'angle1': '0', 'angle2': '180', 'length1': '3', 'length2': '3', 'color': 'black'})
ET.SubElement(calc_c, 'spline', {'id': '13022', 'type': 'simpleInteractive', 'point1': '13009', 'point4': '13007', 'angle1': '0', 'angle2': '220', 'length1': '3', 'length2': '3', 'color': 'black'})
ET.SubElement(calc_c, 'line', {'id': '13023', 'firstPoint': '13005', 'secondPoint': '13006', 'lineColor': 'black'})
ET.SubElement(calc_c, 'line', {'id': '13024', 'firstPoint': '13006', 'secondPoint': '13007', 'lineColor': 'black'})

ET.SubElement(collar_draft, 'modeling')
ET.SubElement(collar_draft, 'pieces')

# Append collar block
# remove old one if exists
for d in root.findall('draftBlock'):
    if d.attrib.get('name') == 'Cuello_Sastre':
        root.remove(d)

root.append(collar_draft)

tree.write(blazer_file, encoding='UTF-8', xml_declaration=True)
print("Sleeve hidden and Collar added.")
