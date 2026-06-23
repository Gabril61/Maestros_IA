import xml.etree.ElementTree as ET

file_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

updated = False
for spline in root.iter('spline'):
    id_val = spline.get('id')
    if id_val == '12020':
        spline.set('length1', 'Line_MS_Origen_MS_Guia_Izq * 0.55')
        spline.set('length2', 'Line_MS_Origen_MS_Guia_Izq * 0.05')
        updated = True
    elif id_val == '12021':
        spline.set('length1', 'Line_MS_Guia_Izq_MS_Ancho_Izq * 0.15')
        spline.set('length2', 'Line_MS_Guia_Izq_MS_Ancho_Izq * 0.15')
        updated = True
    elif id_val == '12022':
        spline.set('length1', 'Line_MS_Origen_MS_Guia_Der * 0.55')
        spline.set('length2', 'Line_MS_Origen_MS_Guia_Der * 0.05')
        updated = True
    elif id_val == '12023':
        spline.set('length1', 'Line_MS_Guia_Der_MS_Ancho_Der * 0.15')
        spline.set('length2', 'Line_MS_Guia_Der_MS_Ancho_Der * 0.15')
        updated = True

if updated:
    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Splines de manga actualizados en Blazer_Dama_Maestro.val")
