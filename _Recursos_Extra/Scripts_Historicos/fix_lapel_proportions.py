import xml.etree.ElementTree as ET

def fix_lapel():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    for pt in root.findall('.//point'):
        name = pt.get('name')
        
        # Make A1 proportional to the lapel break line length
        if name == 'A1':
            pt.set('length', 'Line_F_Cuello_Ancho_B_Boton_1 * 0.35')
            print("Fixed A1 to be proportional.")
            
        # Make A2 use the user-defined variable #ancho_solapa
        elif name == 'A2':
            # In blazer it was 9. We can use #ancho_solapa * 1.3 to keep it around 8.5
            # Or just #ancho_solapa + 2. Let's use proportional to bust or just the variable.
            # Usually the peak lapel is a bit wider than the collar.
            pt.set('length', '#ancho_solapa * 1.35') 
            print("Fixed A2 to use #ancho_solapa.")
            
        # Hide the "ghost line" for C_Boton_1
        elif name == 'C_Boton_1':
            pt.set('lineType', 'none')
            print("Hid the ghost line for C_Boton_1.")
            
        # Make the collar back widths scale with the lapel width
        elif name in ['C_Hombro_Caida', 'C_Medio_Atras_Caida']:
            old = pt.get('length')
            if old == '8':
                pt.set('length', '#ancho_solapa * 1.2')
                print(f"Fixed {name} to use #ancho_solapa.")
                
        # Fix the collar points C_Guia_Punta and C_Frente_Punta which were hardcoded to 7 and 8
        elif name == 'C_Guia_Punta':
            old = pt.get('length')
            if old == '7':
                pt.set('length', '#ancho_solapa * 1.0')
                print("Fixed C_Guia_Punta to use #ancho_solapa.")
                
        elif name == 'C_Frente_Punta':
            old = pt.get('length')
            if old == '8':
                pt.set('length', '#ancho_solapa * 1.2')
                print("Fixed C_Frente_Punta to use #ancho_solapa.")

    tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)

if __name__ == '__main__':
    fix_lapel()
