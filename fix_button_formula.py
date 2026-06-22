import xml.etree.ElementTree as ET

def fix_formula():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    calc = root.find('.//calculation')
    
    # Check if line already exists
    line_exists = False
    for line in calc.findall('.//line'):
        if (line.get('firstPoint') == '11004' and line.get('secondPoint') == '11006') or \
           (line.get('firstPoint') == '11006' and line.get('secondPoint') == '11004'):
            line_exists = True
            break
            
    if not line_exists:
        # Find index of B_Boton_4
        b4_idx = -1
        children = list(calc)
        for i, child in enumerate(children):
            if child.get('name') == 'B_Boton_4':
                b4_idx = i
                break
                
        if b4_idx != -1:
            # Create the line between B_Boton_1 (11004) and B_Boton_4 (11006)
            new_line = ET.Element('line', {
                'firstPoint': '11004',
                'id': '11008',
                'lineColor': 'black',
                'lineType': 'dotLine', # or none
                'secondPoint': '11006'
            })
            calc.insert(b4_idx + 1, new_line)
            print("Inserted line 11008 between Boton 1 and 4.")
            
    # Also check if the formula in Boton 2 and 3 has a comma instead of dot
    for pt in calc.findall('.//point'):
        name = pt.get('name')
        if name in ('B_Boton_2', 'B_Boton_3'):
            l = pt.get('length')
            if l and ',' in l:
                pt.set('length', l.replace(',', '.'))
                print(f"Fixed comma to dot in {name}")
                
    tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)

if __name__ == '__main__':
    fix_formula()
