import os

files_to_fix = [
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Dama_CortePrincesa_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA2\Blusa_Dama_CortePrincesa_Maestro.val'
]

replacements = {
    # Fix Spline 32
    'angle2="AngleLine_F_Ancho_Pecho_F_Hombro + 20"': 'angle2="AngleLine_F_Hombro_F_Ancho_Pecho + 200"',
    # Fix Spline 34
    'angle1="AngleLine_F_Ancho_Pecho_F_Hombro + 200"': 'angle1="AngleLine_F_Hombro_F_Ancho_Pecho + 20"',
    # Fix Spline 121
    'angle2="AngleLine_T_Ancho_Espalda_T_Hombro - 15"': 'angle2="AngleLine_T_Hombro_T_Ancho_Espalda + 165"',
    # Fix Spline 124
    'angle1="AngleLine_T_Ancho_Espalda_T_Hombro + 165"': 'angle1="AngleLine_T_Hombro_T_Ancho_Espalda + 345"'
}

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old_str, new_str in replacements.items():
        if old_str in content:
            content = content.replace(old_str, new_str)
            print(f"Fixed string in {file_path}:\n -> {new_str}")
        else:
            print(f"String not found in {file_path}:\n{old_str}")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Process completed.")
