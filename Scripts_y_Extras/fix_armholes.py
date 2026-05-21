import os
import re

files_to_fix = [
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Dama_CortePrincesa_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA2\Blusa_Dama_CortePrincesa_Maestro.val'
]

replacements = {
    # Front Armhole Splines
    'angle1="260" angle2="90" color="black" id="32"': 'angle1="AngleLine_F_Cuello_Ancho_F_Hombro - 90" angle2="AngleLine_F_Hombro_F_Ancho_Pecho" color="black" id="32"',
    'angle1="270" angle2="140" color="black" id="34"': 'angle1="AngleLine_F_Hombro_F_Ancho_Pecho + 180" angle2="AngleLine_F_Ancho_Pecho_F_Costado_Sisa + 180" color="black" id="34"',
    'angle1="300" angle2="180" color="black" id="33"': 'angle1="AngleLine_F_Ancho_Pecho_F_Costado_Sisa" angle2="180" color="black" id="33"',
    
    # Back Armhole Splines
    'angle1="250" angle2="90" color="black" id="121"': 'angle1="AngleLine_T_Cuello_Ancho_T_Hombro - 90" angle2="AngleLine_T_Hombro_T_Ancho_Espalda" color="black" id="121"',
    'angle1="270" angle2="90" color="black" id="124"': 'angle1="AngleLine_T_Hombro_T_Ancho_Espalda + 180" angle2="AngleLine_T_Ancho_Espalda_T_Costado_Sisa + 180" color="black" id="124"',
    'angle1="270" angle2="0" color="black" id="122" length1="Line_T_Sisa_Pinza_Inf_T_Costado_Sisa * 0.5" length2="Line_T_Sisa_Pinza_Inf_T_Costado_Sisa * 0.5"': 'angle1="AngleLine_T_Ancho_Espalda_T_Costado_Sisa" angle2="0" color="black" id="122" length1="Line_T_Sisa_Pinza_Inf_T_Costado_Sisa * 0.4" length2="Line_T_Sisa_Pinza_Inf_T_Costado_Sisa * 0.4"'
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
            print(f"Replaced string in {file_path}")
        else:
            print(f"String not found in {file_path}:\n{old_str[:50]}...")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Process completed.")
