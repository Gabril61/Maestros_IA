import os

files_to_fix = [
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val'
]

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    changed = False
    for i, line in enumerate(lines):
        if 'T_Aletilla_Top' in line or 'T_Aletilla_Bot' in line:
            if 'angle="180"' in line:
                lines[i] = line.replace('angle="180"', 'angle="0"')
                changed = True
                print(f"Fixed angle in {file_path}: {line.strip()}")
                
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

print("Process completed.")
