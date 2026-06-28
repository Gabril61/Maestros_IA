import re
import os

def fix_ruedos(val_path):
    print(f"\nReparando Ruedos (Regla 14 y 16) en {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # 1. Revertir T_Costado_Ruedo
    t_revert_pattern = r'(<point[^>]*name="T_Costado_Ruedo_Ref"[^>]*>)\s*(<line[^>]*id="22101"[^>]*>)\s*(<point[^>]*name="T_Costado_Ruedo"[^>]*>)'
    t_match = re.search(t_revert_pattern, content)
    
    if t_match:
        ref_point = t_match.group(1)
        # Extraer el length original del Ref para reconstruir el original
        # id="2210" name="T_Costado_Ruedo_Ref"
        original_ruedo = ref_point.replace('id="2210"', 'id="221"').replace('name="T_Costado_Ruedo_Ref"', 'name="T_Costado_Ruedo"')
        content = content.replace(t_match.group(0), original_ruedo)
        modified = True
        print("  - T_Costado_Ruedo restaurado a su anclaje horizontal original (Regla 16).")
    else:
        print("  - No se encontró T_Costado_Ruedo_Ref, asumiendo que ya estaba limpio.")

    # 2. Modificar F_Costado_Ruedo
    f_pattern = r'(<point[^>]*id="121"[^>]*name="F_Costado_Ruedo"[^>]*>)'
    f_match = re.search(f_pattern, content)
    
    if f_match and 'F_Costado_Ruedo_Ref' not in content:
        original_f = f_match.group(1)
        
        # Crear F_Costado_Ruedo_Ref
        f_ref = original_f.replace('id="121"', 'id="1210"').replace('name="F_Costado_Ruedo"', 'name="F_Costado_Ruedo_Ref"')
        
        # Línea de referencia
        line_ref = '            <line firstPoint="119" id="12101" lineColor="black" lineType="none" secondPoint="1210"/>'
        
        # Fórmula matemática para absorber el largo del trasero
        # length = sqrt((25 * 25) + (dx * dx))
        # dx = (((@S_CONT_BUSTO + #holgura_busto)/4) - ((@S_CONT_BUSTO - @G_CONT_CINTURA)/10)) - ((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)
        math_formula = 'length="sqrt((25 * 25) + (((((@S_CONT_BUSTO + #holgura_busto)/4) - ((@S_CONT_BUSTO - @G_CONT_CINTURA)/10)) - ((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)) * ((((@S_CONT_BUSTO + #holgura_busto)/4) - ((@S_CONT_BUSTO - @G_CONT_CINTURA)/10)) - ((@G_CONT_CADERA_BAJA + #holgura_cadera)/4))))"'
        
        # Crear el nuevo F_Costado_Ruedo
        f_new = f'            <point angle="AngleLine_F_Costado_Cintura_F_Costado_Ruedo_Ref" basePoint="119" id="121" {math_formula} mx="-3.51557" my="2.07367" name="F_Costado_Ruedo" type="endLine"/>'
        
        replacement = f_ref + "\n" + line_ref + "\n" + f_new
        content = content.replace(original_f, replacement)
        modified = True
        print("  - F_Costado_Ruedo modificado matemáticamente para absorber el largo trasero (Regla 14).")

    if modified:
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  - Archivo guardado con éxito.")
    else:
        print("  - No se requirieron modificaciones en el archivo.")

def main():
    base_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    derived_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val"
    
    if os.path.exists(base_path):
        fix_ruedos(base_path)
    if os.path.exists(derived_path):
        fix_ruedos(derived_path)

if __name__ == "__main__":
    main()
