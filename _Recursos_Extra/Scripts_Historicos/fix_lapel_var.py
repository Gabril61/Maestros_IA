import xml.etree.ElementTree as ET

def fix_lapel_var():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    fixed = False
    for pt in root.findall('.//point'):
        if pt.get('name') == 'A1':
            old_len = pt.get('length')
            if 'Line_F_Cuello_Ancho_B_Boton_1' in old_len:
                pt.set('length', old_len.replace('Line_F_Cuello_Ancho_B_Boton_1', 'Line_B_Boton_1_F_Cuello_Ancho'))
                fixed = True
                
    if fixed:
        tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)
        print("Fixed A1 formula.")
    else:
        print("No change needed.")

if __name__ == '__main__':
    fix_lapel_var()
