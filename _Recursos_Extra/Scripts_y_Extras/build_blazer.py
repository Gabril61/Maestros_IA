import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'

tree = ET.parse(file_path)
root = tree.getroot()

# Update description
desc = root.find('description')
if desc is not None:
    desc.text = "Matriz Maestra TextilFit - BLAZER EJECUTIVO DAMA (3 Botones)"

notes = root.find('notes')
if notes is not None:
    notes.text = "Fase 2: Blazer Ejecutivo. Entalle sastre anatómico basado en corte princesa con holgura de +6cm. Solapa de muesca y manga sastre de dos piezas."

corp_calc = None
for draft in root.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        corp_calc = draft.find('calculation')
        break

if corp_calc is not None:
    # 1. Inject Ease (Holgura)
    # The bust points are typically F_Costado_Sisa and T_Costado_Sisa. We'll search for them.
    for pt in corp_calc.findall('point'):
        name = pt.attrib.get('name', '')
        if name in ('F_Costado_Sisa', 'F_Costado_Cintura', 'F_Costado_Cadera', 'F_Costado_Ruedo'):
            # Add + 1.5 cm to the length formula for front ease
            pt.attrib['length'] = f"({pt.attrib['length']}) + 1.5"
        if name in ('T_Costado_Sisa', 'T_Costado_Cintura', 'T_Costado_Cadera', 'T_Costado_Ruedo'):
            # Add + 1.5 cm to the length formula for back ease
            pt.attrib['length'] = f"({pt.attrib['length']}) + 1.5"

    # 2. Add 3-Button Closure and Notch Lapel Points
    # Assuming F_Cintura (2) is waist, F_Cuello_Ancho (23) is neck.
    blazer_front_points = [
        # Centro delantero extendido (Cruce de 2.5 cm)
        ET.Element('point', {'id': '11000', 'name': 'B_Cruce_Cuello', 'type': 'endLine', 'basePoint': '24', 'angle': '180', 'length': '2.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('point', {'id': '11001', 'name': 'B_Cruce_Cintura', 'type': 'endLine', 'basePoint': '2', 'angle': '180', 'length': '2.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('point', {'id': '11002', 'name': 'B_Cruce_Ruedo', 'type': 'endLine', 'basePoint': '301', 'angle': '180', 'length': '2.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        
        # Botones (Boton 1: superior, Boton 2: cintura, Boton 3: inferior)
        ET.Element('point', {'id': '11003', 'name': 'B_Boton_2', 'type': 'endLine', 'basePoint': '11001', 'angle': '90', 'length': '0', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('point', {'id': '11004', 'name': 'B_Boton_1', 'type': 'endLine', 'basePoint': '11003', 'angle': '90', 'length': '8', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('point', {'id': '11005', 'name': 'B_Boton_3', 'type': 'endLine', 'basePoint': '11003', 'angle': '270', 'length': '8', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        
        # Solapa de Muesca (Notch Lapel)
        # Quiebre de solapa empieza en Boton 1 (11004) y va hasta el cuello (23) desplazado 2 cm.
        ET.Element('point', {'id': '11006', 'name': 'B_Quiebre_Cuello', 'type': 'endLine', 'basePoint': '23', 'angle': '180', 'length': '2', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('line', {'id': '11007', 'firstPoint': '11004', 'secondPoint': '11006', 'lineColor': 'black', 'lineType': 'dotLine'}),
        
        # Dibujo de la muesca
        ET.Element('point', {'id': '11008', 'name': 'B_Muesca_Punta', 'type': 'endLine', 'basePoint': '11006', 'angle': '240', 'length': '9', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('point', {'id': '11009', 'name': 'B_Muesca_Entrada', 'type': 'endLine', 'basePoint': '11008', 'angle': '60', 'length': '3.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        ET.Element('point', {'id': '11010', 'name': 'B_Solapa_Cuello', 'type': 'endLine', 'basePoint': '11009', 'angle': '150', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}),
        
        # Lineas frontales
        ET.Element('line', {'id': '11011', 'firstPoint': '11004', 'secondPoint': '11008', 'lineColor': 'black'}),
        ET.Element('line', {'id': '11012', 'firstPoint': '11008', 'secondPoint': '11009', 'lineColor': 'black'}),
        ET.Element('line', {'id': '11013', 'firstPoint': '11009', 'secondPoint': '11010', 'lineColor': 'black'})
    ]
    for element in blazer_front_points:
        corp_calc.append(element)

# 3. Add Manga Sastre (2-piece sleeve) draftBlock
sleeve_draft = ET.Element('draftBlock', {'name': 'Manga_Sastre'})
calc = ET.SubElement(sleeve_draft, 'calculation')

sleeve_points = [
    # Eje central de la manga
    {'id': '12000', 'type': 'single', 'name': 'MS_Origen', 'x': '200', 'y': '0', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '12001', 'type': 'endLine', 'name': 'MS_Largo', 'basePoint': '12000', 'angle': '270', 'length': '@S_LARGO_MANGA', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '12002', 'type': 'endLine', 'name': 'MS_Codo', 'basePoint': '12000', 'angle': '270', 'length': '(@S_LARGO_MANGA / 2) + 2', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    
    # Ancho de copa
    {'id': '12003', 'type': 'endLine', 'name': 'MS_Copa_Alto', 'basePoint': '12000', 'angle': '270', 'length': '15', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '12004', 'type': 'endLine', 'name': 'MS_Ancho_Izq', 'basePoint': '12003', 'angle': '180', 'length': '18', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '12005', 'type': 'endLine', 'name': 'MS_Ancho_Der', 'basePoint': '12003', 'angle': '0', 'length': '18', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    
    # Bajera (Under-sleeve)
    {'id': '12006', 'type': 'endLine', 'name': 'MS_Bajera_Izq', 'basePoint': '12003', 'angle': '180', 'length': '14', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '12007', 'type': 'endLine', 'name': 'MS_Bajera_Der', 'basePoint': '12003', 'angle': '0', 'length': '14', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    
    # Curvatura del codo (Sartorial curve)
    {'id': '12008', 'type': 'endLine', 'name': 'MS_Codo_Izq', 'basePoint': '12002', 'angle': '180', 'length': '16', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '12009', 'type': 'endLine', 'name': 'MS_Codo_Der', 'basePoint': '12002', 'angle': '0', 'length': '16', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '12010', 'type': 'endLine', 'name': 'MS_Codo_Curva', 'basePoint': '12008', 'angle': '0', 'length': '2', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    
    # Puño
    {'id': '12011', 'type': 'endLine', 'name': 'MS_Puno_Izq', 'basePoint': '12001', 'angle': '180', 'length': '13', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    {'id': '12012', 'type': 'endLine', 'name': 'MS_Puno_Der', 'basePoint': '12001', 'angle': '0', 'length': '13', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    
    # Inclinación del puño
    {'id': '12013', 'type': 'endLine', 'name': 'MS_Puno_Curva', 'basePoint': '12011', 'angle': '90', 'length': '1.5', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'}
]
for p in sleeve_points:
    ET.SubElement(calc, 'point', p)

sleeve_lines = [
    {'id': '12020', 'firstPoint': '12000', 'secondPoint': '12004', 'lineColor': 'black'},
    {'id': '12021', 'firstPoint': '12000', 'secondPoint': '12005', 'lineColor': 'black'},
    {'id': '12022', 'firstPoint': '12004', 'secondPoint': '12008', 'lineColor': 'black'},
    {'id': '12023', 'firstPoint': '12005', 'secondPoint': '12009', 'lineColor': 'black'},
    {'id': '12024', 'firstPoint': '12008', 'secondPoint': '12013', 'lineColor': 'black'},
    {'id': '12025', 'firstPoint': '12009', 'secondPoint': '12012', 'lineColor': 'black'},
    {'id': '12026', 'firstPoint': '12012', 'secondPoint': '12013', 'lineColor': 'black'},
]
for l in sleeve_lines:
    ET.SubElement(calc, 'line', l)

ET.SubElement(sleeve_draft, 'modeling')
ET.SubElement(sleeve_draft, 'pieces')
root.append(sleeve_draft)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Blazer build script executed successfully!")
