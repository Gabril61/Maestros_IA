import re
import os

def fix_front_complete(val_path):
    print(f"\nAplicando corrección completa de Regla 14 y 16 en {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # 1. Re-aplicar la longitud matemática a F_Costado_Ruedo
    # Buscar el original F_Costado_Ruedo
    f_ruedo_pattern = r'(<point[^>]*id="121"[^>]*name="F_Costado_Ruedo"[^>]*>)'
    f_match = re.search(f_ruedo_pattern, content)
    
    if f_match and 'F_Costado_Ruedo_Ref' not in content:
        original_f = f_match.group(1)
        
        f_ref = original_f.replace('id="121"', 'id="1210"').replace('name="F_Costado_Ruedo"', 'name="F_Costado_Ruedo_Ref"')
        line_ref = '            <line firstPoint="119" id="12101" lineColor="black" lineType="none" secondPoint="1210"/>'
        
        math_formula = 'length="sqrt((25 * 25) + (((((@S_CONT_BUSTO + #holgura_busto)/4) - ((@S_CONT_BUSTO - @G_CONT_CINTURA)/10)) - ((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)) * ((((@S_CONT_BUSTO + #holgura_busto)/4) - ((@S_CONT_BUSTO - @G_CONT_CINTURA)/10)) - ((@G_CONT_CADERA_BAJA + #holgura_cadera)/4))))"'
        
        f_new = f'            <point angle="AngleLine_F_Costado_Cintura_F_Costado_Ruedo_Ref" basePoint="119" id="121" {math_formula} mx="-3.51557" my="2.07367" name="F_Costado_Ruedo" type="endLine"/>'
        
        replacement_ruedo = f_ref + "\n" + line_ref + "\n" + f_new
        content = content.replace(original_f, replacement_ruedo)
        modified = True
        print("  - F_Costado_Ruedo ajustado matemáticamente (Regla 14).")

    # 2. Corregir F_Costado_Cliente para que nazca de una proyección de F_Costado_Ruedo
    f_cliente_pattern = r'(<point[^>]*id="40403"[^>]*name="F_Costado_Cliente"[^>]*>)'
    c_match = re.search(f_cliente_pattern, content)
    
    if c_match and 'id="40402"' not in content:
        original_c = c_match.group(1)
        
        # Crear un punto de caída vertical exacto desde F_Costado_Ruedo según el ajuste del cliente
        f_nivel_costado = '            <point angle="270" basePoint="121" id="40402" length="#ajuste_largo_prenda" lineColor="black" lineType="none" name="F_Nivel_Costado_Cliente" type="endLine"/>'
        
        # Modificar F_Costado_Cliente para que intersecte con este nuevo nivel elevado, no con el centro delantero
        new_c = original_c.replace('basePoint="40401"', 'basePoint="40402"')
        
        replacement_cliente = f_nivel_costado + "\n" + new_c
        content = content.replace(original_c, replacement_cliente)
        modified = True
        print("  - F_Costado_Cliente anclado a la elevación de F_Costado_Ruedo (Regla 16 y extensión correcta).")

    if modified:
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  - Archivo guardado con éxito.")
    else:
        print("  - No se requirieron modificaciones.")

def main():
    base_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    derived_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val"
    
    if os.path.exists(base_path):
        fix_front_complete(base_path)
    if os.path.exists(derived_path):
        fix_front_complete(derived_path)

if __name__ == "__main__":
    main()
