import re
import os

def fix_altura_cadera(val_path):
    print(f"\nCorrigiendo variable de altura cadera en {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # 1. Eliminar la declaración de la variable #altura_cadera
    var_pattern = r'\s*<variable description="Altura de Cadera" formula="20" name="#altura_cadera"/>\r?\n?'
    if re.search(var_pattern, content):
        content = re.sub(var_pattern, '\n', content)
        modified = True
        print("  - Variable #altura_cadera purgada del bloque <variables>.")

    # 2. Reemplazar #altura_cadera por @G_ALTO_CADERA en los puntos
    if '#altura_cadera' in content:
        content = content.replace('#altura_cadera', '@G_ALTO_CADERA')
        modified = True
        print("  - Referencias actualizadas a @G_ALTO_CADERA.")

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
        fix_altura_cadera(base_path)
    if os.path.exists(derived_path):
        fix_altura_cadera(derived_path)

if __name__ == "__main__":
    main()
