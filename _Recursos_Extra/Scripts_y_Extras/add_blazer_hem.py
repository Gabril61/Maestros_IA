import xml.etree.ElementTree as ET
import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'

tree = ET.parse(file_path)
root = tree.getroot()

# Find the calculation block inside the main draft block (Corpino)
calc = None
for draft in root.findall('draftBlock'):
    # Let's see if we can find the one with the hem points
    pts = draft.findall('.//point')
    pt_ids = [p.get('id') for p in pts]
    if '301' in pt_ids:  # F_Ruedo is usually 301
        calc = draft.find('calculation')
        break

if calc is not None:
    # Points to extend
    hem_points = [
        {'base': '11002', 'name': 'B_Cruce_Ruedo'},
        {'base': '301', 'name': 'F_Ruedo'},
        {'base': '502', 'name': 'F_Ruedo_Pinza'},
        {'base': '303', 'name': 'F_Costado_Ruedo'},
        {'base': '403', 'name': 'T_Costado_Ruedo'},
        {'base': '602', 'name': 'T_Ruedo_Pinza'},
        {'base': '401', 'name': 'T_Ruedo'},
    ]
    
    # Check which points actually exist in the file to avoid errors
    existing_points = {p.get('id'): p for p in calc.findall('point')}
    
    valid_hem_points = [hp for hp in hem_points if hp['base'] in existing_points]
    
    new_points = []
    base_id = 12000
    
    for i, hp in enumerate(valid_hem_points):
        pt_id = str(base_id + i)
        hp['ext_id'] = pt_id
        new_pt = ET.Element('point', {
            'id': pt_id,
            'name': f"Ext_{hp['name']}",
            'type': 'endLine',
            'basePoint': hp['base'],
            'angle': '270',
            'length': '@D_RUEDO_PRENDA',
            'mx': '0.1',
            'my': '0.1',
            'showPointName': 'true'
        })
        new_points.append(new_pt)
    
    # Append new points
    for pt in new_points:
        calc.append(pt)
        
    # Create lines between the new extension points (horizontal hem line)
    new_lines = []
    line_id = 12100
    
    # Connect Delantero (Left to Right): B_Cruce_Ruedo -> F_Ruedo -> F_Ruedo_Pinza -> F_Costado_Ruedo
    delantero_bases = ['11002', '301', '502', '303']
    del_exts = [hp['ext_id'] for hp in valid_hem_points if hp['base'] in delantero_bases]
    for i in range(len(del_exts) - 1):
        line = ET.Element('line', {
            'id': str(line_id),
            'firstPoint': del_exts[i],
            'secondPoint': del_exts[i+1],
            'lineColor': 'black',
            'lineType': 'solidLine',
            'lineWeight': '0.35'
        })
        new_lines.append(line)
        line_id += 1
        
    # Connect Trasero (Left to Right): T_Costado_Ruedo -> T_Ruedo_Pinza -> T_Ruedo
    trasero_bases = ['403', '602', '401']
    tras_exts = [hp['ext_id'] for hp in valid_hem_points if hp['base'] in trasero_bases]
    for i in range(len(tras_exts) - 1):
        line = ET.Element('line', {
            'id': str(line_id),
            'firstPoint': tras_exts[i],
            'secondPoint': tras_exts[i+1],
            'lineColor': 'black',
            'lineType': 'solidLine',
            'lineWeight': '0.35'
        })
        new_lines.append(line)
        line_id += 1
        
    # Vertical lines for visual closure
    # Cruce Ruedo
    ext_b_cruce = [hp['ext_id'] for hp in valid_hem_points if hp['base'] == '11002']
    if ext_b_cruce:
        new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '11002', 'secondPoint': ext_b_cruce[0], 'lineColor': 'black'}))
        line_id += 1
    
    # F_Costado_Ruedo
    ext_f_costado = [hp['ext_id'] for hp in valid_hem_points if hp['base'] == '303']
    if ext_f_costado:
        new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '303', 'secondPoint': ext_f_costado[0], 'lineColor': 'black'}))
        line_id += 1
        
    # T_Costado_Ruedo
    ext_t_costado = [hp['ext_id'] for hp in valid_hem_points if hp['base'] == '403']
    if ext_t_costado:
        new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '403', 'secondPoint': ext_t_costado[0], 'lineColor': 'black'}))
        line_id += 1
        
    # T_Ruedo
    ext_t_ruedo = [hp['ext_id'] for hp in valid_hem_points if hp['base'] == '401']
    if ext_t_ruedo:
        new_lines.append(ET.Element('line', {'id': str(line_id), 'firstPoint': '401', 'secondPoint': ext_t_ruedo[0], 'lineColor': 'black'}))
        line_id += 1
        
    for l in new_lines:
        calc.append(l)

    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Hem extensions added successfully to Blazer_Dama_Maestro.val!")
else:
    print("Could not find the calculation block for the front/back bodices.")
