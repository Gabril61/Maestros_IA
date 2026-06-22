import xml.etree.ElementTree as ET

def clean():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    # Points to delete
    pts_to_del = {'F_Solapa_Punta', 'F_Cran_Base', 'F_Pie_Cuello', 'F_Caja_Cuello', 'B_Boton_5'}
    # Splines to delete
    spl_to_del = {'16013'}
    
    # Find IDs of points to delete
    pt_ids_to_del = set()
    for pt in root.findall('.//point'):
        if pt.get('name') in pts_to_del:
            pt_ids_to_del.add(pt.get('id'))
            
    print(f"Deleting point IDs: {pt_ids_to_del}")
    
    # Remove lines using these points
    for calculation in root.findall('.//calculation'):
        for line in calculation.findall('.//line'):
            if line.get('firstPoint') in pt_ids_to_del or line.get('secondPoint') in pt_ids_to_del:
                print(f"Deleting line {line.get('id')}")
                calculation.remove(line)
                
    # Remove the points
    for calculation in root.findall('.//calculation'):
        for pt in calculation.findall('.//point'):
            if pt.get('id') in pt_ids_to_del:
                print(f"Deleting point {pt.get('name')} (ID: {pt.get('id')})")
                calculation.remove(pt)
                
    # Remove the splines
    for calculation in root.findall('.//calculation'):
        for spl in calculation.findall('.//spline'):
            if spl.get('id') in spl_to_del:
                print(f"Deleting spline {spl.get('id')}")
                calculation.remove(spl)
                
    # Also remove from <modeling> <detail> sections?
    # Usually we just remove from calculation for now. 
    # If they are in a piece, we might need to remove them from <piece> but they were clones not used yet.
    
    tree.write('Chaleco_Femenino_Maestro_cleaned.val', encoding='UTF-8', xml_declaration=True)

if __name__ == '__main__':
    clean()
