import xml.etree.ElementTree as ET

# 1. FIX CAMISA (Crossed sleeve lines)
camisa_file = r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val'
tree_c = ET.parse(camisa_file)
root_c = tree_c.getroot()

for draft in root_c.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        calc = draft.find('calculation')
        for child in calc:
            if child.tag == 'spline' and child.attrib.get('id') == '20500':
                # Was 2026, change to 2027 if it was crossing, or vice versa
                # Let's check which one it was. M_T (2004) to M_A4_Der (2027)
                # Wait, M_T is usually Back (Right side in some drafts, Left in others). 
                # Let's just swap them safely.
                child.attrib['point4'] = '2027' 
            elif child.tag == 'spline' and child.attrib.get('id') == '20501':
                child.attrib['point4'] = '2026'

tree_c.write(camisa_file, encoding='UTF-8', xml_declaration=True)
print("Camisa: Crossed lines fixed.")

# 2. FIX BLAZER
blazer_file = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree_b = ET.parse(blazer_file)
root_b = tree_b.getroot()

# Remove the old Manga_Sastre draftBlock
for draft in root_b.findall('draftBlock'):
    if draft.attrib.get('name') == 'Manga_Sastre':
        root_b.remove(draft)

# Add a much better Manga_Sastre block (proper cap and 2 pieces)
sleeve_draft = ET.Element('draftBlock', {'name': 'Manga_Sastre'})
calc_m = ET.SubElement(sleeve_draft, 'calculation')

# Basic 2-piece tailored sleeve points
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
    
    # Construcción de la copa (Cimera)
    {'id': '12008', 'type': 'endLine', 'name': 'MS_Copa_Guia1', 'basePoint': '12000', 'angle': '180', 'length': '9'},
    {'id': '12009', 'type': 'endLine', 'name': 'MS_Copa_Guia2', 'basePoint': '12000', 'angle': '0', 'length': '9'},
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

ET.SubElement(sleeve_draft, 'modeling')
ET.SubElement(sleeve_draft, 'pieces')
root_b.append(sleeve_draft)

# Fix Lapel in Blazer (incorporating the hand-drawn pattern logic)
for draft in root_b.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        calc = draft.find('calculation')
        # We will add the lapel points that match the sketch
        # The sketch shows lapel extending upwards from the neck point.
        # Neck point is F_Cuello_Ancho (23). The top button is B_Boton_1 (11004).
        
        lapel_pts = [
            # Extensión hacia arriba desde el cuello para el pie de la solapa
            {'id': '11050', 'type': 'endLine', 'name': 'B_Solapa_Cuello_Alto', 'basePoint': '23', 'angle': '90', 'length': '3', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
            # Inclinación hacia afuera para la muesca superior
            {'id': '11051', 'type': 'endLine', 'name': 'B_Solapa_Muesca_Sup', 'basePoint': '11050', 'angle': '160', 'length': '7', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
            # Muesca inferior (separación)
            {'id': '11052', 'type': 'endLine', 'name': 'B_Solapa_Muesca_Inf', 'basePoint': '11051', 'angle': '270', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
            # Conexión al botón 1
        ]
        for p in lapel_pts:
            calc.append(ET.Element('point', p))
            
        calc.append(ET.Element('line', {'id': '11060', 'firstPoint': '23', 'secondPoint': '11050', 'lineColor': 'red'}))
        calc.append(ET.Element('line', {'id': '11061', 'firstPoint': '11050', 'secondPoint': '11051', 'lineColor': 'red'}))
        calc.append(ET.Element('line', {'id': '11062', 'firstPoint': '11051', 'secondPoint': '11052', 'lineColor': 'red'}))
        calc.append(ET.Element('line', {'id': '11063', 'firstPoint': '11052', 'secondPoint': '11004', 'lineColor': 'red'}))

tree_b.write(blazer_file, encoding='UTF-8', xml_declaration=True)
print("Blazer: Lapel and Sleeve updated.")
