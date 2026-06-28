import re
import os

def fix_ruedo_costado(val_path):
    print(f"\nReparando Ruedos en {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Buscar T_Costado_Ruedo original
    # Ejemplo: <point angle="180" basePoint="218" id="221" length="((@G_CONT_CADERA_BAJA + #holgura_cadera)/4)" name="T_Costado_Ruedo" type="endLine"/>
    ruedo_pattern = r'(<point[^>]*id="221"[^>]*name="T_Costado_Ruedo"[^>]*>)'
    match = re.search(ruedo_pattern, content)
    
    modified = False
    
    if match and 'T_Costado_Ruedo_Ref' not in content:
        original_ruedo = match.group(1)
        
        # Crear T_Costado_Ruedo_Ref
        ref_ruedo = original_ruedo.replace('id="221"', 'id="2210"').replace('name="T_Costado_Ruedo"', 'name="T_Costado_Ruedo_Ref"')
        
        # Línea de referencia para el ángulo
        line_ref = '            <line firstPoint="219" id="22101" lineColor="black" lineType="none" secondPoint="2210"/>'
        
        # Crear el nuevo T_Costado_Ruedo que absorbe el largo del delantero
        new_ruedo = '            <point angle="AngleLine_T_Costado_Cintura_T_Costado_Ruedo_Ref" basePoint="219" id="221" length="Line_F_Costado_Cintura_F_Costado_Ruedo" mx="-11.2183" my="-0.809662" name="T_Costado_Ruedo" type="endLine"/>'
        
        replacement = ref_ruedo + "\n" + line_ref + "\n" + new_ruedo
        
        content = content.replace(original_ruedo, replacement)
        modified = True
        print("  - T_Costado_Ruedo modificado para absorber Line_F_Costado_Cintura_F_Costado_Ruedo (Regla 14).")

    if modified:
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  - Archivo guardado con éxito.")
    else:
        print("  - No se requirieron modificaciones o ya estaba reparado.")

def main():
    base_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    derived_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val"
    
    if os.path.exists(base_path):
        fix_ruedo_costado(base_path)
    if os.path.exists(derived_path):
        fix_ruedo_costado(derived_path)

if __name__ == "__main__":
    main()
