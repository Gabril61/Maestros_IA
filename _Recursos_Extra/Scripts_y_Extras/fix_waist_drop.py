import re
import os

files_to_fix = [
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Dama_Clasico_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Dama_Jogger_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA2\Pantalon_Dama_Clasico_Maestro.val'
]

for file_path in files_to_fix:
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}, does not exist.")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace basePoint="15" with basePoint="14" ONLY for id="16"
    # Find the line defining point 16
    pattern = r'(<point angle="0" basePoint=")15(" id="16".*?name="F_Guia_Cintura_Cost".*?>)'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, r'\g<1>14\g<2>', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed waist drop in {file_path}")
    else:
        print(f"Could not find point 16 with basePoint 15 in {file_path}")
