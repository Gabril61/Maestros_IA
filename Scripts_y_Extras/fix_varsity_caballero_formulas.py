import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Replace old spline variables with new ones
old_f_splines = "Spl_F_Ancho_Pecho_F_Sisa_Pinza_Sup + Spl_F_Sisa_Pinza_Inf_F_Costado_Sisa"
new_f_spline = "Spl_F_Ancho_Pecho_F_Costado_Sisa"

old_t_splines = "Spl_T_Ancho_Espalda_T_Sisa_Pinza_Sup + Spl_T_Sisa_Pinza_Inf_T_Costado_Sisa"
new_t_spline = "Spl_T_Ancho_Espalda_T_Costado_Sisa"

old_f_full = f"Spl_F_Hombro_F_Ancho_Pecho + {old_f_splines}"
new_f_full = f"Spl_F_Hombro_F_Ancho_Pecho + {new_f_spline}"

old_t_full = f"Spl_T_Hombro_T_Ancho_Espalda + {old_t_splines}"
new_t_full = f"Spl_T_Hombro_T_Ancho_Espalda + {new_t_spline}"

for p in calc.findall('point'):
    length = p.get('length', '')
    if not length: continue
    
    # Replace in length formulas
    if old_f_full in length:
        length = length.replace(old_f_full, new_f_full)
    if old_t_full in length:
        length = length.replace(old_t_full, new_t_full)
        
    if "Line_T_Ancho_Espalda_T_Pinza_Centro" in length:
        length = length.replace("Line_T_Ancho_Espalda_T_Pinza_Centro", "Line_T_Ancho_Espalda_T_Cintura")
        
    p.set('length', length)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Formulas in Caballero updated to bypass deleted darts.")
