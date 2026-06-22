import xml.etree.ElementTree as ET

def fix_formulas():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    fixed_count = 0
    # Fix point F_Mitad_Hombro_Vista length
    for pt in root.findall('.//point'):
        name = pt.get('name')
        if name == 'F_Mitad_Hombro_Vista':
            old = pt.get('length')
            if 'Line_23_28' in old:
                pt.set('length', old.replace('Line_23_28', 'Line_F_Cuello_Ancho_F_Hombro'))
                fixed_count += 1
                print("Fixed F_Mitad_Hombro_Vista formula.")
                
    # Fix splines
    for spl in root.findall('.//spline'):
        if spl.get('id') == '30104': # spline_vista_1
            l1 = spl.get('length1')
            if l1 and 'Line_30100_30102' in l1:
                spl.set('length1', l1.replace('Line_30100_30102', 'Line_F_Mitad_Hombro_Vista_F_Vista_Busto'))
                spl.set('length2', spl.get('length2').replace('Line_30100_30102', 'Line_F_Mitad_Hombro_Vista_F_Vista_Busto'))
                fixed_count += 1
                print("Fixed spline_vista_1 formulas.")
        elif spl.get('id') == '30105': # spline_vista_2
            l1 = spl.get('length1')
            if l1 and 'Line_30102_30103' in l1:
                spl.set('length1', l1.replace('Line_30102_30103', 'Line_F_Vista_Busto_F_Vista_Ruedo'))
                spl.set('length2', spl.get('length2').replace('Line_30102_30103', 'Line_F_Vista_Busto_F_Vista_Ruedo'))
                fixed_count += 1
                print("Fixed spline_vista_2 formulas.")
                
    tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)
    print(f"Fixed {fixed_count} items.")

if __name__ == '__main__':
    fix_formulas()
