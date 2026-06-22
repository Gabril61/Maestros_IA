import os
import glob
import re

def to_increment(match):
    # match.group(1) is the part after @M_HOLGURA_
    suffix = match.group(1).lower()
    return f"#holgura_{suffix}"

def refactor_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar si el archivo contiene la variable
    if "@M_HOLGURA_" not in content:
        return False
        
    # Expresión regular para capturar el sufijo y pasarlo a minúsculas
    pattern = r'@M_HOLGURA_([a-zA-Z0-9_]+)'
    new_content = re.sub(pattern, to_increment, content)
    
    # Si hubo cambios, sobrescribir el archivo
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    target_dir = r"c:\Users\Ricx18\Desktop\Maestros_IA"
    val_files = glob.glob(os.path.join(target_dir, "*.val"))
    
    modified_count = 0
    for file in val_files:
        if refactor_file(file):
            print(f"Refactored: {os.path.basename(file)}")
            modified_count += 1
            
    print(f"\nTotal de archivos modificados: {modified_count}")

if __name__ == "__main__":
    main()
