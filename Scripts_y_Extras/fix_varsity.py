import xml.etree.ElementTree as ET

def fix_varsity(file_path, is_dama):
    tree = ET.parse(file_path)
    calc = tree.getroot().find('.//calculation')

    # Fix the pointOfIntersection error by replacing it with a simple endLine
    pts_to_remove = []
    for p in calc.findall('point'):
        if p.get('type') == 'pointOfIntersection':
            pts_to_remove.append(p)
    
    for p in pts_to_remove:
        calc.remove(p)

    # Re-create the corners using endLine
    # Pretina_Esquina (30003)
    calc.append(ET.Element('point', {
        'angle': '270', 'basePoint': '30001', 'id': '30003', 'length': '6', 
        'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 
        'mx': '0.1', 'my': '0.1', 'name': 'Pretina_Esquina', 'showPointName': 'true', 'type': 'endLine'
    }))
    
    # CuelloRib_Esquina (30007)
    calc.append(ET.Element('point', {
        'angle': '270', 'basePoint': '30005', 'id': '30007', 'length': '4', 
        'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 
        'mx': '0.1', 'my': '0.1', 'name': 'CuelloRib_Esquina', 'showPointName': 'true', 'type': 'endLine'
    }))

    # Adjust Lengths
    # Dama is shorter, Caballero is standard
    hem_formula = '(@G_ALTO_CADERA) - 4' if is_dama else '@G_ALTO_CADERA'
    
    for p in calc.findall('point'):
        name = p.get('name', '')
        if name in ['F_Ruedo', 'F_Ruedo_Pinza', 'T_Ruedo', 'T_Ruedo_Pinza']:
            p.set('length', hem_formula)

    tree.write(file_path, encoding='UTF-8', xml_declaration=True)

fix_varsity(r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val', True)
fix_varsity(r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val', False)
print("Varsity files fixed: point type corrected and lengths adjusted.")
