import xml.etree.ElementTree as ET
import shutil

FILES = [
    'c:\\Users\\Ricx18\\Desktop\\Maestros_IA\\Bata_Medica_Dama_Maestro.val',
    'c:\\Users\\Ricx18\\Desktop\\Maestros_IA\\Bata_Medica_Estandar_Maestro.val'
]

HEM_AMOUNT = "3"
NEW_ID_START = 30000

for filepath in FILES:
    shutil.copy(filepath, filepath + '.bak2')
    tree = ET.parse(filepath)
    root = tree.getroot()
    calc = root.find('.//calculation')
    
    # Existing points mapping by name
    points_by_name = {}
    for child in calc:
        if child.tag == 'point':
            points_by_name[child.get('name')] = child.get('id')
            
    # Define which points need extending
    # Name -> (AngleFormula, LengthFormula)
    extensions = {}
    
    # Frente Rectos
    for p in ['F_Nivel_Largo', 'F_Pinza_Ruedo_Centro', 'F_Pinza_Ruedo_Der', 'F_Pinza_Ruedo_Izq', 'F_Solapa_Bot', 'V_Bot_Extremo', 'F_Cruce_Ruedo']:
        if p in points_by_name:
            extensions[p] = ("270", HEM_AMOUNT)
            
    # Frente Espejo (Costado)
    if 'F_Costado_Ruedo' in points_by_name and 'F_Costado_Cintura' in points_by_name:
        angle_f = "360 - AngleLine_F_Costado_Ruedo_F_Costado_Cintura"
        extensions['F_Costado_Ruedo'] = (angle_f, HEM_AMOUNT)
        
    # Espalda Rectos
    for p in ['T_Nivel_Largo', 'T_Pinza_Ruedo_Centro', 'T_Pinza_Ruedo_Der', 'T_Pinza_Ruedo_Izq']:
        if p in points_by_name:
            extensions[p] = ("270", HEM_AMOUNT)
            
    # Espalda Espejo (Costado)
    if 'T_Costado_Ruedo' in points_by_name and 'T_Costado_Cintura' in points_by_name:
        angle_t = "360 - AngleLine_T_Costado_Ruedo_T_Costado_Cintura"
        extensions['T_Costado_Ruedo'] = (angle_t, HEM_AMOUNT)
        
    # Create the points
    new_points = {}
    for base_name, (angle, length) in extensions.items():
        base_id = points_by_name[base_name]
        ext_name = base_name.replace('_Ruedo', '_Doblez').replace('_Largo', '_Doblez_Largo').replace('_Bot', '_Doblez_Bot').replace('_Extremo', '_Doblez_Extremo')
        if base_name == 'F_Nivel_Largo': ext_name = 'F_Nivel_Doblez'
        if base_name == 'T_Nivel_Largo': ext_name = 'T_Nivel_Doblez'
        if base_name == 'F_Cruce_Ruedo': ext_name = 'F_Cruce_Doblez'
        
        # Check if already exists
        if ext_name in points_by_name:
            continue
            
        p = ET.Element('point', {
            'id': str(NEW_ID_START),
            'name': ext_name,
            'type': 'endLine',
            'basePoint': base_id,
            'angle': angle,
            'length': length,
            'lineType': 'none',
            'lineColor': 'black'
        })
        calc.append(p)
        new_points[base_name] = str(NEW_ID_START)
        NEW_ID_START += 1
        
    # Create lines connecting the new hem points
    # We need to mirror the existing horizontal connections.
    # Dama front connections (roughly left to right or right to left)
    # T_Nivel_Largo -> T_Pinza_Ruedo_Izq -> T_Pinza_Ruedo_Centro -> T_Pinza_Ruedo_Der -> T_Costado_Ruedo
    # Actually, Seamly2D doesn't strict require lines to trace, but it's good for visualization.
    # I'll just add vertical lines connecting base to extension to see them.
    for base_name, new_id in new_points.items():
        base_id = points_by_name[base_name]
        l = ET.Element('line', {
            'id': str(NEW_ID_START),
            'firstPoint': base_id,
            'secondPoint': new_id,
            'lineType': 'solidLine',
            'lineColor': 'blue'
        })
        calc.append(l)
        NEW_ID_START += 1
        
    # And horizontal lines connecting the extensions
    # Let's dynamically find lines that connected the base points, and duplicate them for the extension points.
    lines_to_add = []
    for child in calc:
        if child.tag == 'line':
            fp = child.get('firstPoint')
            sp = child.get('secondPoint')
            # If BOTH points of the line have an extension, connect the extensions!
            fp_base = [k for k, v in points_by_name.items() if v == fp]
            sp_base = [k for k, v in points_by_name.items() if v == sp]
            if fp_base and sp_base:
                fp_name = fp_base[0]
                sp_name = sp_base[0]
                if fp_name in new_points and sp_name in new_points:
                    l = ET.Element('line', {
                        'id': str(NEW_ID_START),
                        'firstPoint': new_points[fp_name],
                        'secondPoint': new_points[sp_name],
                        'lineType': 'solidLine',
                        'lineColor': 'blue'
                    })
                    lines_to_add.append(l)
                    NEW_ID_START += 1
                    
    for l in lines_to_add:
        calc.append(l)

    tree.write(filepath, encoding='UTF-8', xml_declaration=True)
    print(f"Modificado {filepath}: Añadidos {len(new_points)} puntos de extensión de ruedo.")

