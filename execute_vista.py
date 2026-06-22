import xml.etree.ElementTree as ET

def execute():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    # 1. Adjust ease variables to 1
    vars_node = root.find('.//variables')
    for v in vars_node.findall('.//variable'):
        if v.get('name') in ('#holgura_superior', '#holgura_inferior'):
            v.set('formula', '1')
            print(f"Set {v.get('name')} to 1")

    calc = root.find('.//calculation')
    
    # Check if F_Cuello_Ancho and F_Hombro exist
    p_cuello = None
    p_hombro = None
    p_apex = None
    p_ruedo = None
    for pt in calc.findall('.//point'):
        if pt.get('name') == 'F_Cuello_Ancho':
            p_cuello = pt.get('id')
        elif pt.get('name') == 'F_Hombro':
            p_hombro = pt.get('id')
        elif pt.get('name') == 'F_APEX':
            p_apex = pt.get('id')
        elif pt.get('name') == 'F_Ruedo': # the center front hem
            p_ruedo = pt.get('id')
            
    if p_cuello and p_hombro and p_apex and p_ruedo:
        # Create F_Mitad_Hombro_Vista
        # ID 30100 for Vista nodes
        pt_mitad_hombro = ET.Element('point', {
            'id': '30100', 'name': 'F_Mitad_Hombro_Vista',
            'type': 'alongLine',
            'firstPoint': p_cuello, 'secondPoint': p_hombro,
            'length': f'Line_{p_cuello}_{p_hombro} * 0.5' if f'Line_{p_cuello}_{p_hombro}' else '5',
            'lineColor': 'black', 'lineType': 'none', 'showPointName': 'true'
        })
        
        # To avoid formula error if the line doesn't exist, we use pointFromLineAndAxis or simply alongLine
        # Wait, if F_Cuello_Ancho and F_Hombro are not connected by a line, Line_... will fail.
        # Let's ensure the line exists
        line_hombro = ET.Element('line', {
            'firstPoint': p_cuello, 'secondPoint': p_hombro,
            'id': '30101', 'lineColor': 'black', 'lineType': 'dotLine'
        })
        
        # We need the length of the line, so we create the line.
        pt_mitad_hombro.set('length', f'Line_{p_cuello}_{p_hombro} * 0.5')
        
        # F_Vista_Busto: user said "alinearla con el punto del busto" for the ruedo, so we can use F_APEX directly,
        # but to "esquivar" the dart, maybe shift F_Vista_Busto slightly towards the center.
        pt_vista_busto = ET.Element('point', {
            'id': '30102', 'name': 'F_Vista_Busto',
            'type': 'endLine',
            'basePoint': p_apex, 'angle': '180', 'length': '1.5', # Shift 1.5cm left (center)
            'lineColor': 'black', 'lineType': 'none', 'showPointName': 'true'
        })
        
        # F_Vista_Ruedo: vertically aligned with F_APEX (so same X).
        # We can use pointIntersectAxis with basePoint F_APEX going down (angle 270)
        # intersecting the hem line (which is B_Cruce_Ruedo to F_Ruedo... wait, F_Costado_Ruedo to F_Ruedo).
        # Let's check hem line. F_Pinza_Centro is at waist. 
        # A simple way to get the Y of the hem is to use pointIntersectAxis with hem line.
        # Let's find F_Ruedo (center front hem) and F_Costado_Ruedo.
        p_cost_ruedo = None
        for pt in calc.findall('.//point'):
            if pt.get('name') == 'F_Costado_Ruedo':
                p_cost_ruedo = pt.get('id')
                break
                
        if p_cost_ruedo:
            pt_vista_ruedo = ET.Element('point', {
                'id': '30103', 'name': 'F_Vista_Ruedo',
                'type': 'lineIntersectAxis',
                'basePoint': p_apex, 'angle': '270', # vertical line from APEX down
                'p1Line': p_ruedo, 'p2Line': p_cost_ruedo,
                'lineColor': 'black', 'lineType': 'none', 'showPointName': 'true'
            })
            
            # Spline for the Vista
            spline_vista = ET.Element('spline', {
                'id': '30104',
                'type': 'simpleInteractive',
                'point1': '30100', 'point4': '30103',
                'length1': '10', 'length2': '15',
                'angle1': '270', 'angle2': '90',
                'color': 'black', 'lineWeight': '1.5'
            })
            # To make it curve through F_Vista_Busto, we could use a path (splinePath) or just a curve passing near it.
            # Actually, a 3-point spline doesn't exist in Seamly2D, we must use splinePath or two simple splines.
            # Spline 1: Mitad_Hombro to Vista_Busto
            spline_vista_1 = ET.Element('spline', {
                'id': '30104', 'type': 'simpleInteractive',
                'point1': '30100', 'point4': '30102',
                'length1': 'Line_30100_30102 * 0.5', 'length2': 'Line_30100_30102 * 0.5',
                'angle1': '270', 'angle2': '90',
                'color': 'black', 'lineWeight': '1.5'
            })
            # Spline 2: Vista_Busto to Vista_Ruedo
            spline_vista_2 = ET.Element('spline', {
                'id': '30105', 'type': 'simpleInteractive',
                'point1': '30102', 'point4': '30103',
                'length1': 'Line_30102_30103 * 0.3', 'length2': 'Line_30102_30103 * 0.3',
                'angle1': '270', 'angle2': '90',
                'color': 'black', 'lineWeight': '1.5'
            })
            
            # Create lines so Line_... formulas work
            line_1 = ET.Element('line', {'id': '30106', 'firstPoint': '30100', 'secondPoint': '30102', 'lineColor': 'black', 'lineType': 'dotLine'})
            line_2 = ET.Element('line', {'id': '30107', 'firstPoint': '30102', 'secondPoint': '30103', 'lineColor': 'black', 'lineType': 'dotLine'})

            # Append everything
            calc.append(line_hombro)
            calc.append(pt_mitad_hombro)
            calc.append(pt_vista_busto)
            calc.append(pt_vista_ruedo)
            calc.append(line_1)
            calc.append(line_2)
            calc.append(spline_vista_1)
            calc.append(spline_vista_2)
            
            print("Successfully added Vista nodes.")

    tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)

if __name__ == '__main__':
    execute()
