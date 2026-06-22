import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target_42 = 'angle2="AngleLine_D_Punto_Pezon_D_Pinza_Izq - 180" id="42"'
replace_42 = 'angle2="90" id="42"'

target_500 = 'angle2="AngleLine_D_Punto_Pezon_D_Pinza_Der - 180" id="500"'
replace_500 = 'angle2="90" id="500"'

if target_42 in content and target_500 in content:
    content = content.replace(target_42, replace_42)
    content = content.replace(target_500, replace_500)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed angles to 90 degrees.")
else:
    print("Targets not found.")
