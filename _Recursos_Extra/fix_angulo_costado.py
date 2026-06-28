import re
import os

def fix_angle(val_path):
    print(f"\nReparando {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Buscar el bloque que inyectamos antes
    pattern = r'(<point[^>]*name="F_Costado_Cintura_Ref"[^>]*>)\s*(<point[^>]*name="F_Costado_Cintura"[^>]*>)'
    match = re.search(pattern, content)
    
    if match:
        ref_point = match.group(1)
        new_cintura = match.group(2)
        
        # Insertar la línea invisible entre los dos puntos
        line_element = '            <line firstPoint="111" id="11901" lineColor="black" lineType="none" secondPoint="1190"/>'
        
        replacement = ref_point + "\n" + line_element + "\n" + new_cintura
        
        content = content.replace(match.group(0), replacement)
        
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  - Línea de referencia inyectada para reparar el ángulo.")
    else:
        print("  - No se encontró el bloque a reparar o ya está reparado.")

def main():
    base_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    derived_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val"
    
    if os.path.exists(base_path):
        fix_angle(base_path)
    if os.path.exists(derived_path):
        fix_angle(derived_path)

if __name__ == "__main__":
    main()
