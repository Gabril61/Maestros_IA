import xml.etree.ElementTree as ET

def add_pocket(calc, is_dama):
    # F_Costado_Cintura is '6' in both files
    # 90050: Ref point (inwards from side seam by 8cm)
    calc.append(ET.Element('point', {'angle': '180', 'basePoint': '6', 'id': '90050', 'length': '8', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Ref', 'showPointName': 'false', 'type': 'endLine'}))
    
    # 90051: Pocket Top (up by 10cm from ref)
    calc.append(ET.Element('point', {'angle': '90', 'basePoint': '90050', 'id': '90051', 'length': '10', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Sup', 'showPointName': 'true', 'type': 'endLine'}))
    
    # 90052: Pocket Bottom (down and left, angle 245, length 15cm)
    calc.append(ET.Element('point', {'angle': '245', 'basePoint': '90051', 'id': '90052', 'length': '15', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Inf', 'showPointName': 'true', 'type': 'endLine'}))
    
    # 90053: Pocket Line
    calc.append(ET.Element('line', {'firstPoint': '90051', 'id': '90053', 'lineColor': 'blue', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '90052'}))

def fix_caballero():
    file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
    tree = ET.parse(file_path)
    calc = tree.getroot().find('.//calculation')

    # 1. Revert spline angle1 to 270 for straight down drop
    for s in calc.findall('spline'):
        if s.get('id') in ['80001', '80002']:
            s.set('angle1', '270')
            
    # 2. Delete lines connecting to 200 or 211
    lines_to_remove = []
    for l in calc.findall('line'):
        if l.get('firstPoint') in ['200', '211'] or l.get('secondPoint') in ['200', '211']:
            lines_to_remove.append(l)
    for l in lines_to_remove:
        calc.remove(l)

    # 3. Add pocket
    add_pocket(calc, False)
    
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)

def fix_dama():
    file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val'
    tree = ET.parse(file_path)
    calc = tree.getroot().find('.//calculation')
    
    # Add pocket
    add_pocket(calc, True)
    
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)

fix_caballero()
fix_dama()
print("Final fixes applied: armholes corrected, extra lines deleted, pockets added.")
