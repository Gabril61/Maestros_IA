import xml.etree.ElementTree as ET
import os

def redefine_pockets(calc):
    # Remove existing pocket points/lines if they exist
    to_remove = []
    for el in calc:
        if el.get('id') in ['90050', '90051', '90052', '90053']:
            to_remove.append(el)
    for el in to_remove:
        calc.remove(el)

    # Re-insert pocket
    # F_Bolsillo_Ref: 11cm from F_Cintura (2) towards the right
    calc.append(ET.Element('point', {'angle': '0', 'basePoint': '2', 'id': '90050', 'length': '11', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Ref', 'showPointName': 'false', 'type': 'endLine'}))
    
    # F_Bolsillo_Sup: 6cm up
    calc.append(ET.Element('point', {'angle': '90', 'basePoint': '90050', 'id': '90051', 'length': '6', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Sup', 'showPointName': 'true', 'type': 'endLine'}))
    
    # F_Bolsillo_Inf: 15cm down and right (angle 300)
    calc.append(ET.Element('point', {'angle': '300', 'basePoint': '90051', 'id': '90052', 'length': '15', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Inf', 'showPointName': 'true', 'type': 'endLine'}))
    
    # Line
    calc.append(ET.Element('line', {'firstPoint': '90051', 'id': '90053', 'lineColor': 'blue', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '90052'}))

def fix_dama():
    file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val'
    tree = ET.parse(file_path)
    calc = tree.getroot().find('.//calculation')
    redefine_pockets(calc)
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)

def rebuild_caballero():
    dama_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val'
    caballero_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
    
    tree = ET.parse(dama_path)
    root = tree.getroot()
    calc = root.find('.//calculation')
    
    # 1. Metadata & Hem Length
    desc = root.find('description')
    if desc is not None:
        desc.text = "Patrón Maestro - Chaqueta Universitaria (Varsity) Caballero"
    
    for p in calc.findall('point'):
        name = p.get('name', '')
        if name in ['F_Ruedo', 'F_Ruedo_Pinza', 'T_Ruedo', 'T_Ruedo_Pinza']:
            p.set('length', '@G_ALTO_CADERA')
            
    # 2. Remove Darts
    pt_ids_to_delete = []
    for p in calc.findall('point'):
        if 'Pinza' in p.get('name', ''):
            pt_ids_to_delete.append(p.get('id'))
            calc.remove(p)
            
    elements_to_remove = []
    for l in calc.findall('line'):
        if l.get('firstPoint') in pt_ids_to_delete or l.get('secondPoint') in pt_ids_to_delete:
            elements_to_remove.append(l)
        if l.get('firstPoint') in ['200', '211'] or l.get('secondPoint') in ['200', '211']:
            elements_to_remove.append(l)
    for s in calc.findall('spline'):
        if s.get('point1') in pt_ids_to_delete or s.get('point4') in pt_ids_to_delete:
            elements_to_remove.append(s)
        if s.get('id') in ['307', '407']:
            elements_to_remove.append(s)
    for el in elements_to_remove:
        try:
            calc.remove(el)
        except: pass

    # 3. Boxy Side Seams
    f_sisa_formula = "(@S_CONT_BUSTO / 4) + @D_HOLGURA_SUPERIOR + 2"
    pts_to_straighten = ['F_Costado_Cintura', 'F_Costado_Cadera_Temp', 'F_Costado_Ruedo_Temp', 'T_Costado_Cintura', 'T_Costado_Cadera', 'T_Costado_Ruedo']
    for p in calc.findall('point'):
        if p.get('name') in pts_to_straighten:
            p.set('length', f_sisa_formula)
        elif p.get('name') in ['F_Costado_Real', 'T_Costado_Real']:
            p.set('length', '0')
        elif p.get('id') == '610':
            p.set('length', '7')
        elif p.get('id') == '9001':
            p.set('angle', 'AngleLine_F_APEX_F_Costado_Sisa')
        elif p.get('id') == '9002':
            p.set('angle', 'AngleLine_T_Apex_Espalda_T_Costado_Sisa')

    # 4. Fix formulas
    old_f_full = "Spl_F_Hombro_F_Ancho_Pecho + Spl_F_Ancho_Pecho_F_Sisa_Pinza_Sup + Spl_F_Sisa_Pinza_Inf_F_Costado_Sisa"
    new_f_full = "Spl_F_Hombro_F_Ancho_Pecho + Spl_F_Ancho_Pecho_F_Costado_Sisa"
    old_t_full = "Spl_T_Hombro_T_Ancho_Espalda + Spl_T_Ancho_Espalda_T_Sisa_Pinza_Sup + Spl_T_Sisa_Pinza_Inf_T_Costado_Sisa"
    new_t_full = "Spl_T_Hombro_T_Ancho_Espalda + Spl_T_Ancho_Espalda_T_Costado_Sisa"
    
    for p in calc.findall('point'):
        length = p.get('length', '')
        if old_f_full in length:
            p.set('length', length.replace(old_f_full, new_f_full))
        if old_t_full in length:
            p.set('length', length.replace(old_t_full, new_t_full))

    # 5. Insert new elements sequentially
    new_elements = [
        ET.Element('spline', {'angle1': '270', 'angle2': '180', 'color': 'black', 'id': '80001', 'length1': '6', 'length2': '7', 'point1': '31', 'point4': '5', 'type': 'simpleInteractive'}),
        ET.Element('spline', {'angle1': '270', 'angle2': '0', 'color': 'black', 'id': '80002', 'length1': '6', 'length2': '7', 'point1': '120', 'point4': '104', 'type': 'simpleInteractive'}),
        ET.Element('line', {'firstPoint': '5', 'id': '90021', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '6'}),
        ET.Element('line', {'firstPoint': '6', 'id': '90022', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '303'}),
        ET.Element('line', {'firstPoint': '104', 'id': '90023', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '105'}),
        ET.Element('line', {'firstPoint': '105', 'id': '90024', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '403'})
    ]
    
    insert_idx = 0
    for i, el in enumerate(list(calc)):
        if el.get('id') == '120':
            insert_idx = i + 1
            break
            
    for el in reversed(new_elements):
        calc.insert(insert_idx, el)
        
    tree.write(caballero_path, encoding='UTF-8', xml_declaration=True)

fix_dama()
rebuild_caballero()
print("Dama updated and Caballero completely rebuilt.")
