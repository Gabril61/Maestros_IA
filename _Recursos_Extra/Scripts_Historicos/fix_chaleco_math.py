import xml.etree.ElementTree as ET

def fix_math():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    count = 0
    for pt in root.findall('.//point'):
        name = pt.get('name')
        
        # 1. Back Bust & Waist widths
        if name in ['T_Costado_Sisa', 'T_Costado_Cintura']:
            old = pt.get('length')
            if old == '((@S_CONT_BUSTO / 4) + #holgura_superior) + 1.5':
                pt.set('length', '((@S_CONT_BUSTO / 4) + #holgura_superior) - 1.5')
                count += 1
                
        # 2. Back Hip width
        elif name == 'T_Costado_Cadera':
            old = pt.get('length')
            if old == '((@G_CONT_CADERA_BAJA / 4) + #holgura_inferior) + 1.5':
                pt.set('length', '((@G_CONT_CADERA_BAJA / 4) + #holgura_inferior) - 1.5')
                count += 1
                
        # 3. Front Hip width (add +1.5)
        elif name in ['F_Costado_Cadera_Temp', 'F_Costado_Ruedo_Temp']:
            old = pt.get('length')
            if old == '(@G_CONT_CADERA_BAJA / 4) + #holgura_inferior':
                pt.set('length', '((@G_CONT_CADERA_BAJA / 4) + #holgura_inferior) + 1.5')
                count += 1
                
        # 4. Waist Entalle (Take-in) for Front and Back
        elif name in ['F_Costado_Temp', 'T_Costado_Real']:
            old = pt.get('length')
            if old == '(@S_CONT_BUSTO - @G_CONT_CINTURA) / 8':
                pt.set('length', '((@S_CONT_BUSTO - @G_CONT_CINTURA) / 4) - #pinza_cint_sup')
                count += 1

    tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)
    print(f"Fixed {count} parametric formulas.")

if __name__ == '__main__':
    fix_math()
