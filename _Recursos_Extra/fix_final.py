import xml.etree.ElementTree as ET

val_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(val_path)
root = tree.getroot()
calc = root.find('.//calculation')

changed = False
for p in calc.findall('.//point'):
    name = p.attrib.get('name', '')
    
    # Fix Sleeve Asymmetry (Restore proportional tracking of bicep lines)
    if name == 'M_Puno_Izq':
        p.attrib['length'] = 'Line_M_Origen_M_Ancho_Izq * 0.85 + (#holgura_manga_corta / 2)'
        changed = True
    elif name == 'M_Puno_Der':
        p.attrib['length'] = 'Line_M_Origen_M_Ancho_Der * 0.85 + (#holgura_manga_corta / 2)'
        changed = True
        
    # Fix Pocket Anchor (Place ON the spline instead of straight line projection)
    elif name == 'B_Sup_Der':
        p.attrib.clear() # Clear all attributes to rebuild as cutSpline
        p.attrib['id'] = p.attrib.get('id', '9999') # will overwrite below
        p.attrib['name'] = 'B_Sup_Der'
        p.attrib['type'] = 'cutSpline'
        p.attrib['spline'] = '131' # ID of Spl_F_Costado_Cintura_F_Costado_Ruedo
        p.attrib['length'] = 'Spl_F_Costado_Cintura_F_Costado_Ruedo - #alto_bolsillo'
        p.attrib['mx'] = '0'
        p.attrib['my'] = '0'
        p.attrib['lineColor'] = 'black'
        changed = True

# We need to restore the original ID to B_Sup_Der to not break line connections
b_sup_der_original_id = None
for p in root.iter('point'):
    if p.attrib.get('name') == 'B_Sup_Der':
        b_sup_der_original_id = p.attrib.get('id')

if changed:
    tree.write(val_path, encoding='UTF-8', xml_declaration=True)
    print("Correcciones aplicadas: Asimetria de punos y anclaje cutSpline.")
else:
    print("No se encontraron los puntos a corregir.")
