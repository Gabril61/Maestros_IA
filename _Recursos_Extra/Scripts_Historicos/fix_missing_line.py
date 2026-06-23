import xml.etree.ElementTree as ET

paths = [
    r"C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Patrones_Generados\Roxana_Acosta_2026-06-22T213406\Chaleco_Femenino_Maestro.val",
    r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
]

for path in paths:
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        
        # Check if the line already exists
        line_exists = False
        for line in root.iter('line'):
            p1 = line.get('firstPoint')
            p2 = line.get('secondPoint')
            if (p1 == '28' and p2 == '701') or (p1 == '701' and p2 == '28'):
                line_exists = True
                break
                
        if not line_exists:
            calc_block = root.find('.//calculation')
            if calc_block is not None:
                spline_32_idx = -1
                for idx, child in enumerate(calc_block):
                    if child.tag == 'spline' and child.get('id') == '32':
                        spline_32_idx = idx
                        break
                
                if spline_32_idx != -1:
                    new_line = ET.Element('line', {
                        'firstPoint': '28', 
                        'secondPoint': '701', 
                        'id': '9999',
                        'lineColor': 'black',
                        'lineType': 'none',
                        'lineWeight': '0.35'
                    })
                    calc_block.insert(spline_32_idx, new_line)
                    tree.write(path, encoding='UTF-8', xml_declaration=True)
                    print(f"Línea 9999 inyectada en {path}")
    except Exception as e:
        print(f"Error procesando {path}: {e}")
