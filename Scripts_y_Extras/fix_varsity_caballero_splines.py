import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Fix armhole spline angles and lengths for a smooth bomber sisa
for s in calc.findall('spline'):
    if s.get('id') == '80001':
        s.set('angle1', '270')
        s.set('angle2', '180')
        s.set('length1', 'Line_F_Ancho_Pecho_F_Costado_Sisa * 0.4')
        s.set('length2', 'Line_F_Ancho_Pecho_F_Costado_Sisa * 0.5')
    elif s.get('id') == '80002':
        s.set('angle1', '270')
        s.set('angle2', '0')
        s.set('length1', 'Line_T_Ancho_Espalda_T_Costado_Sisa * 0.4')
        s.set('length2', 'Line_T_Ancho_Espalda_T_Costado_Sisa * 0.5')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Varsity Caballero splines updated.")
