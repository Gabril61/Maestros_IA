import xml.etree.ElementTree as ET

blazer_file = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(blazer_file)
root = tree.getroot()

for draft in root.findall('draftBlock'):
    # 1. Clean up old sleeve and old lapel from Corpino_y_Manga
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        calc = draft.find('calculation')
        if calc is not None:
            elements_to_remove = []
            for child in calc:
                # Remove old sleeve drawing (lines and splines starting from M_)
                if child.tag in ('line', 'spline'):
                    first = child.attrib.get('firstPoint', '')
                    second = child.attrib.get('secondPoint', '')
                    pt1 = child.attrib.get('point1', '')
                    pt4 = child.attrib.get('point4', '')
                    if any(x.startswith('M_') or x.startswith('20') for x in [first, second, pt1, pt4]):
                        # If it has M_ or ID is in the 2000s (sleeve points)
                        elements_to_remove.append(child)
                
                # Remove the bad lapel points and lines from apply_fixes.py
                if child.attrib.get('id') in ('11050', '11051', '11052', '11060', '11061', '11062', '11063'):
                    elements_to_remove.append(child)

            for el in elements_to_remove:
                if el in calc:
                    calc.remove(el)

            # 2. Add correct Lapel expanded OUT to the left
            # B_Boton_1 is 11004. Neck is 23 (F_Cuello_Ancho).
            # B_Quiebre_Cuello is 11006.
            lapel_pts = [
                # Base del pie de cuello (extensión hacia arriba)
                {'id': '11100', 'type': 'endLine', 'name': 'B_Solapa_Cuello_Base', 'basePoint': '23', 'angle': '100', 'length': '3', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                # Punta de la solapa (hacia la izquierda, fuera del patrón)
                {'id': '11101', 'type': 'endLine', 'name': 'B_Solapa_Punta', 'basePoint': '11100', 'angle': '170', 'length': '9', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                # Muesca interna
                {'id': '11102', 'type': 'endLine', 'name': 'B_Solapa_Muesca', 'basePoint': '11101', 'angle': '290', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                # Punta baja de la solapa (Peak)
                {'id': '11103', 'type': 'endLine', 'name': 'B_Solapa_Peak', 'basePoint': '11102', 'angle': '150', 'length': '4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
            ]
            for p in lapel_pts:
                calc.append(ET.Element('point', p))
            
            calc.append(ET.Element('line', {'id': '11110', 'firstPoint': '23', 'secondPoint': '11100', 'lineColor': 'black'}))
            calc.append(ET.Element('line', {'id': '11111', 'firstPoint': '11100', 'secondPoint': '11101', 'lineColor': 'black'}))
            calc.append(ET.Element('line', {'id': '11112', 'firstPoint': '11101', 'secondPoint': '11102', 'lineColor': 'black'}))
            calc.append(ET.Element('line', {'id': '11113', 'firstPoint': '11102', 'secondPoint': '11103', 'lineColor': 'black'}))
            calc.append(ET.Element('spline', {'id': '11114', 'type': 'simpleInteractive', 'point1': '11103', 'point4': '11004', 'angle1': '270', 'angle2': '135', 'length1': '10', 'length2': '10', 'color': 'black'}))


    # 3. Complete Manga_Sastre
    if draft.attrib.get('name') == 'Manga_Sastre':
        calc = draft.find('calculation')
        if calc is not None:
            # We already have points 12000 to 12009. We need to add the lower sleeve points and lines
            lower_pts = [
                # Codo
                {'id': '12010', 'type': 'endLine', 'name': 'MS_Codo_Cimera_Izq', 'basePoint': '12002', 'angle': '180', 'length': '15', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                {'id': '12011', 'type': 'endLine', 'name': 'MS_Codo_Cimera_Der', 'basePoint': '12002', 'angle': '0', 'length': '15', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                {'id': '12012', 'type': 'endLine', 'name': 'MS_Codo_Bajera_Izq', 'basePoint': '12002', 'angle': '180', 'length': '12', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                {'id': '12013', 'type': 'endLine', 'name': 'MS_Codo_Bajera_Der', 'basePoint': '12002', 'angle': '0', 'length': '12', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                
                # Puño
                {'id': '12014', 'type': 'endLine', 'name': 'MS_Puno_Cimera_Izq', 'basePoint': '12001', 'angle': '180', 'length': '13', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                {'id': '12015', 'type': 'endLine', 'name': 'MS_Puno_Cimera_Der', 'basePoint': '12001', 'angle': '0', 'length': '13', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                {'id': '12016', 'type': 'endLine', 'name': 'MS_Puno_Bajera_Izq', 'basePoint': '12001', 'angle': '180', 'length': '10', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
                {'id': '12017', 'type': 'endLine', 'name': 'MS_Puno_Bajera_Der', 'basePoint': '12001', 'angle': '0', 'length': '10', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
            ]
            for p in lower_pts:
                calc.append(ET.Element('point', p))
            
            # Lines to connect the sleeve
            lower_lines = [
                # Cimera (Top sleeve)
                {'id': '12030', 'firstPoint': '12004', 'secondPoint': '12010', 'lineColor': 'black'},
                {'id': '12031', 'firstPoint': '12010', 'secondPoint': '12014', 'lineColor': 'black'},
                {'id': '12032', 'firstPoint': '12005', 'secondPoint': '12011', 'lineColor': 'black'},
                {'id': '12033', 'firstPoint': '12011', 'secondPoint': '12015', 'lineColor': 'black'},
                {'id': '12034', 'firstPoint': '12014', 'secondPoint': '12015', 'lineColor': 'black'}, # Hem
                
                # Bajera (Under sleeve) - in blue to differentiate visually
                {'id': '12035', 'firstPoint': '12006', 'secondPoint': '12012', 'lineColor': 'blue'},
                {'id': '12036', 'firstPoint': '12012', 'secondPoint': '12016', 'lineColor': 'blue'},
                {'id': '12037', 'firstPoint': '12007', 'secondPoint': '12013', 'lineColor': 'blue'},
                {'id': '12038', 'firstPoint': '12013', 'secondPoint': '12017', 'lineColor': 'blue'},
                {'id': '12039', 'firstPoint': '12016', 'secondPoint': '12017', 'lineColor': 'blue'}, # Hem
            ]
            for l in lower_lines:
                calc.append(ET.Element('line', l))


tree.write(blazer_file, encoding='UTF-8', xml_declaration=True)
print("Blazer fixes applied successfully!")
