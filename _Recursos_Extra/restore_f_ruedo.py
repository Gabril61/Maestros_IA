import re
import os

def restore_f_ruedo(val_path):
    print(f"\nRestaurando F_Costado_Ruedo en {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Buscar el bloque que inyectamos antes
    pattern = r'(<point[^>]*name="F_Costado_Ruedo_Ref"[^>]*>)\s*(<line[^>]*id="12101"[^>]*>)\s*(<point[^>]*name="F_Costado_Ruedo"[^>]*>)'
    match = re.search(pattern, content)
    
    if match:
        ref_point = match.group(1)
        # Reconstruir el F_Costado_Ruedo original desde el Ref
        original_ruedo = ref_point.replace('id="1210"', 'id="121"').replace('name="F_Costado_Ruedo_Ref"', 'name="F_Costado_Ruedo"')
        
        content = content.replace(match.group(0), original_ruedo)
        modified = True
        print("  - F_Costado_Ruedo restaurado a su anclaje horizontal en F_Nivel_Largo.")

    if modified:
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  - Archivo guardado con éxito.")
    else:
        print("  - No se requirieron modificaciones o ya estaba restaurado.")

def main():
    base_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    derived_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val"
    
    if os.path.exists(base_path):
        restore_f_ruedo(base_path)
    if os.path.exists(derived_path):
        restore_f_ruedo(derived_path)

if __name__ == "__main__":
    main()
