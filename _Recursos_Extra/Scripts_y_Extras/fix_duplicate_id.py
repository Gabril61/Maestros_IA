import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Change the id of the spline from 420 to 500
target_spline = 'id="420" length1="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35"'
replace_spline = 'id="500" length1="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35"'

# Change the modeling node reference from idObject="420" to idObject="500" for modeling id="395"
target_modeling = '<spline id="395" idObject="420" inUse="true" type="modelingSpline"/>'
replace_modeling = '<spline id="395" idObject="500" inUse="true" type="modelingSpline"/>'

if target_spline in content and target_modeling in content:
    content = content.replace(target_spline, replace_spline)
    content = content.replace(target_modeling, replace_modeling)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed duplicate ID successfully.")
else:
    print("Could not find targets to replace.")
