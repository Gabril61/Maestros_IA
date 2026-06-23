import xml.etree.ElementTree as ET

file_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Chaleco_Femenino_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

updated = False
for spline in root.iter('spline'):
    id_val = spline.get('id')
    if id_val == '207':
        spline.set('angle1', 'AngleLine_F_APEX_F_Sisa_Pinza_Sup + 165')
        spline.set('angle2', 'AngleLine_F_APEX_F_Pinza_P1 - 180')
        spline.set('length1', 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.25')
        spline.set('length2', 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.25')
        updated = True
        print("Spline 207 updated.")
    elif id_val == '209':
        spline.set('angle1', 'AngleLine_F_APEX_F_Sisa_Pinza_Inf + 165')
        spline.set('angle2', 'AngleLine_F_APEX_F_Pinza_P2 - 180')
        spline.set('length1', 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.25')
        spline.set('length2', 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.25')
        updated = True
        print("Spline 209 updated.")

if updated:
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Archivo Chaleco_Femenino_Maestro.val guardado con éxito.")
else:
    print("No se encontraron los splines 207 o 209.")
