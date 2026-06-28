import re
import os

def fix_chronology(val_path):
    print(f"\nReparando {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The exact string to replace in length
    target_string = 'length="Line_T_Costado_Sisa_T_Costado_Cintura"'
    
    # Mathematical formula substituting the line length
    # dy = @S_TALLE_TRASERO - ((@S_CONT_SISA / 2) + (#holgura_sisa / 2))
    # dx = (@S_CONT_BUSTO - @G_CONT_CINTURA)/10
    math_formula = 'length="sqrt(((@S_TALLE_TRASERO - ((@S_CONT_SISA / 2) + (#holgura_sisa / 2))) * (@S_TALLE_TRASERO - ((@S_CONT_SISA / 2) + (#holgura_sisa / 2)))) + (((@S_CONT_BUSTO - @G_CONT_CINTURA)/10) * ((@S_CONT_BUSTO - @G_CONT_CINTURA)/10)))"'
    
    if target_string in content:
        content = content.replace(target_string, math_formula)
        
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  - Reparada la dependencia cronológica con fórmula matemática exacta.")
    else:
        print("  - No se encontró la cadena objetivo.")

def main():
    base_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    derived_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val"
    
    if os.path.exists(base_path):
        fix_chronology(base_path)
    if os.path.exists(derived_path):
        fix_chronology(derived_path)

if __name__ == "__main__":
    main()
