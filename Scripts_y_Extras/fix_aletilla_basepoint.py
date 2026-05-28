import os

files = {
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val': '30007',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val': '30035',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val': '31002'
}

for filepath, new_base in files.items():
    if not os.path.exists(filepath): continue
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    changed = False
    for i, line in enumerate(lines):
        if 'name="T_Aletilla_Bot"' in line and 'basePoint="218"' in line:
            lines[i] = line.replace('basePoint="218"', f'basePoint="{new_base}"')
            changed = True
            print(f'Fixed {os.path.basename(filepath)}: {lines[i].strip()}')
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)

print("Proceso completado.")
