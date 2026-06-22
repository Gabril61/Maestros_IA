import xml.etree.ElementTree as ET

def fix_pockets(file_path):
    tree = ET.parse(file_path)
    calc = tree.getroot().find('.//calculation')

    # Fix pocket angles
    # We want: 
    # Ref from F_Cintura (2) inwards to the right
    # F_Bolsillo_Sup from Ref up
    # F_Bolsillo_Inf from Sup down and right (towards side seam)
    for p in calc.findall('point'):
        if p.get('id') == '90050':
            p.set('basePoint', '2')  # F_Cintura (Center front)
            p.set('angle', '0')      # Right (towards side seam)
            p.set('length', '8')
        elif p.get('id') == '90051':
            p.set('angle', '90')     # Up
            p.set('length', '10')
        elif p.get('id') == '90052':
            p.set('angle', '300')    # Down and Right (towards side seam)
            p.set('length', '15')

    tree.write(file_path, encoding='UTF-8', xml_declaration=True)

fix_pockets(r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val')
fix_pockets(r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val')
print("Pockets inverted correctly.")
