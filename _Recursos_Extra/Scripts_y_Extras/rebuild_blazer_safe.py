import xml.etree.ElementTree as ET

source_file = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Dama_CortePrincesa_Maestro.val'
blazer_file = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'

tree = ET.parse(source_file)
root = tree.getroot()

# Update description
desc = root.find('description')
if desc is not None:
    desc.text = "Matriz Maestra TextilFit - BLAZER EJECUTIVO DAMA (3 Botones)"

notes = root.find('notes')
if notes is not None:
    notes.text = "Fase 2: Blazer Ejecutivo. Entalle sastre anatómico basado en corte princesa con holgura de +6cm. Solapa de muesca y manga sastre de dos piezas."

for draft in root.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        calc = draft.find('calculation')
        if calc is not None:
            # 1. Inject Ease (Holgura)
            for pt in calc.findall('point'):
                name = pt.attrib.get('name', '')
                if name in ('F_Costado_Sisa', 'F_Costado_Cintura', 'F_Costado_Cadera', 'F_Costado_Ruedo',
                            'T_Costado_Sisa', 'T_Costado_Cintura', 'T_Costado_Cadera', 'T_Costado_Ruedo'):
                    pt.attrib['length'] = f"({pt.attrib.get('length', '0')}) + 1.5"

            # 2. Add 3-Button Closure and Notch Lapel Points
            # B_Boton_1 is 11004. Neck is 23 (F_Cuello_Ancho).
            blazer_front_points = [
                # Centro delantero extendido (Cruce de 2.5 cm)
                {'id': '11000', 'type': 'endLine', 'name': 'B_Cruce_Cuello', 'basePoint': '24', 'angle': '180', 'length': '2.5'},
                {'id': '11001', 'type': 'endLine', 'name': 'B_Cruce_Cintura', 'basePoint': '2', 'angle': '180', 'length': '2.5'},
                {'id': '11002', 'type': 'endLine', 'name': 'B_Cruce_Ruedo', 'basePoint': '301', 'angle': '180', 'length': '2.5'},
                
                # Botones
                {'id': '11003', 'type': 'endLine', 'name': 'B_Boton_2', 'basePoint': '11001', 'angle': '90', 'length': '0'},
                {'id': '11004', 'type': 'endLine', 'name': 'B_Boton_1', 'basePoint': '11003', 'angle': '90', 'length': '8'},
                {'id': '11005', 'type': 'endLine', 'name': 'B_Boton_3', 'basePoint': '11003', 'angle': '270', 'length': '8'},
                
                # Solapa de Muesca Expandida (Hacia la izquierda)
                # Base del pie de cuello (extensión hacia arriba)
                {'id': '11100', 'type': 'endLine', 'name': 'B_Solapa_Cuello_Base', 'basePoint': '23', 'angle': '100', 'length': '3'},
                # Punta de la solapa (hacia la izquierda, fuera del patrón)
                {'id': '11101', 'type': 'endLine', 'name': 'B_Solapa_Punta', 'basePoint': '11100', 'angle': '170', 'length': '9'},
                # Muesca interna
                {'id': '11102', 'type': 'endLine', 'name': 'B_Solapa_Muesca', 'basePoint': '11101', 'angle': '290', 'length': '4'},
                # Punta baja de la solapa (Peak)
                {'id': '11103', 'type': 'endLine', 'name': 'B_Solapa_Peak', 'basePoint': '11102', 'angle': '150', 'length': '4'},
            ]
            
            for p in blazer_front_points:
                p['mx'] = '0.1'
                p['my'] = '0.1'
                p['showPointName'] = 'true'
                calc.append(ET.Element('point', p))
                
            calc.append(ET.Element('line', {'id': '11110', 'firstPoint': '23', 'secondPoint': '11100', 'lineColor': 'black'}))
            calc.append(ET.Element('line', {'id': '11111', 'firstPoint': '11100', 'secondPoint': '11101', 'lineColor': 'black'}))
            calc.append(ET.Element('line', {'id': '11112', 'firstPoint': '11101', 'secondPoint': '11102', 'lineColor': 'black'}))
            calc.append(ET.Element('line', {'id': '11113', 'firstPoint': '11102', 'secondPoint': '11103', 'lineColor': 'black'}))
            # Curved breakline to the first button
            calc.append(ET.Element('spline', {'id': '11114', 'type': 'simpleInteractive', 'point1': '11103', 'point4': '11004', 'angle1': '270', 'angle2': '135', 'length1': '10', 'length2': '10', 'color': 'black'}))

        # Hide old sleeve visually if possible by changing lineType, but let's just leave it alone to be safe.
        # However, we CAN delete the 'Manga' piece from details so it doesn't show up.
        pieces = draft.find('pieces')
        if pieces is not None:
            to_remove = []
            for piece in pieces:
                if piece.attrib.get('name', '') == 'Manga':
                    to_remove.append(piece)
            for el in to_remove:
                pieces.remove(el)

# 3. Add Manga Sastre (2-piece sleeve) draftBlock
sleeve_draft = ET.Element('draftBlock', {'name': 'Manga_Sastre'})
calc_m = ET.SubElement(sleeve_draft, 'calculation')

sleeve_pts = [
    {'id': '12000', 'type': 'single', 'name': 'MS_Origen', 'x': '200', 'y': '0'},
    {'id': '12001', 'type': 'endLine', 'name': 'MS_Largo', 'basePoint': '12000', 'angle': '270', 'length': '@S_LARGO_MANGA'},
    {'id': '12002', 'type': 'endLine', 'name': 'MS_Codo', 'basePoint': '12000', 'angle': '270', 'length': '(@S_LARGO_MANGA/2)+2'},
    
    # Copa
    {'id': '12003', 'type': 'endLine', 'name': 'MS_Copa_Alto', 'basePoint': '12000', 'angle': '270', 'length': '15'},
    {'id': '12004', 'type': 'endLine', 'name': 'MS_Ancho_Cimera_Izq', 'basePoint': '12003', 'angle': '180', 'length': '18'},
    {'id': '12005', 'type': 'endLine', 'name': 'MS_Ancho_Cimera_Der', 'basePoint': '12003', 'angle': '0', 'length': '18'},
    {'id': '12006', 'type': 'endLine', 'name': 'MS_Ancho_Bajera_Izq', 'basePoint': '12003', 'angle': '180', 'length': '14'},
    {'id': '12007', 'type': 'endLine', 'name': 'MS_Ancho_Bajera_Der', 'basePoint': '12003', 'angle': '0', 'length': '14'},
    
    # Codo
    {'id': '12010', 'type': 'endLine', 'name': 'MS_Codo_Cimera_Izq', 'basePoint': '12002', 'angle': '180', 'length': '15'},
    {'id': '12011', 'type': 'endLine', 'name': 'MS_Codo_Cimera_Der', 'basePoint': '12002', 'angle': '0', 'length': '15'},
    {'id': '12012', 'type': 'endLine', 'name': 'MS_Codo_Bajera_Izq', 'basePoint': '12002', 'angle': '180', 'length': '12'},
    {'id': '12013', 'type': 'endLine', 'name': 'MS_Codo_Bajera_Der', 'basePoint': '12002', 'angle': '0', 'length': '12'},
    
    # Puño
    {'id': '12014', 'type': 'endLine', 'name': 'MS_Puno_Cimera_Izq', 'basePoint': '12001', 'angle': '180', 'length': '13'},
    {'id': '12015', 'type': 'endLine', 'name': 'MS_Puno_Cimera_Der', 'basePoint': '12001', 'angle': '0', 'length': '13'},
    {'id': '12016', 'type': 'endLine', 'name': 'MS_Puno_Bajera_Izq', 'basePoint': '12001', 'angle': '180', 'length': '10'},
    {'id': '12017', 'type': 'endLine', 'name': 'MS_Puno_Bajera_Der', 'basePoint': '12001', 'angle': '0', 'length': '10'},
]

for p in sleeve_pts:
    p['mx'] = '0.1'
    p['my'] = '0.1'
    p['showPointName'] = 'true'
    ET.SubElement(calc_m, 'point', p)

# Splines para la copa (Cimera y Bajera)
ET.SubElement(calc_m, 'spline', {'id': '12020', 'type': 'simpleInteractive', 'point1': '12004', 'point4': '12000', 'angle1': '90', 'angle2': '180', 'length1': '8', 'length2': '8', 'color': 'black'})
ET.SubElement(calc_m, 'spline', {'id': '12021', 'type': 'simpleInteractive', 'point1': '12000', 'point4': '12005', 'angle1': '0', 'angle2': '90', 'length1': '8', 'length2': '8', 'color': 'black'})
ET.SubElement(calc_m, 'spline', {'id': '12022', 'type': 'simpleInteractive', 'point1': '12006', 'point4': '12007', 'angle1': '270', 'angle2': '270', 'length1': '10', 'length2': '10', 'color': 'blue'})

# Lines to connect the sleeve
lower_lines = [
    # Cimera (Top sleeve)
    {'id': '12030', 'firstPoint': '12004', 'secondPoint': '12010', 'lineColor': 'black'},
    {'id': '12031', 'firstPoint': '12010', 'secondPoint': '12014', 'lineColor': 'black'},
    {'id': '12032', 'firstPoint': '12005', 'secondPoint': '12011', 'lineColor': 'black'},
    {'id': '12033', 'firstPoint': '12011', 'secondPoint': '12015', 'lineColor': 'black'},
    {'id': '12034', 'firstPoint': '12014', 'secondPoint': '12015', 'lineColor': 'black'}, # Hem
    
    # Bajera (Under sleeve) - in blue
    {'id': '12035', 'firstPoint': '12006', 'secondPoint': '12012', 'lineColor': 'blue'},
    {'id': '12036', 'firstPoint': '12012', 'secondPoint': '12016', 'lineColor': 'blue'},
    {'id': '12037', 'firstPoint': '12007', 'secondPoint': '12013', 'lineColor': 'blue'},
    {'id': '12038', 'firstPoint': '12013', 'secondPoint': '12017', 'lineColor': 'blue'},
    {'id': '12039', 'firstPoint': '12016', 'secondPoint': '12017', 'lineColor': 'blue'}, # Hem
]
for l in lower_lines:
    ET.SubElement(calc_m, 'line', l)

ET.SubElement(sleeve_draft, 'modeling')
ET.SubElement(sleeve_draft, 'pieces')
root.append(sleeve_draft)

tree.write(blazer_file, encoding='UTF-8', xml_declaration=True)
print("Blazer safely rebuilt.")
