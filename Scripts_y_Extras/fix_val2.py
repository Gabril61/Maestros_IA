import re
import sys

with open(r'C:\Users\Ricx18\Desktop\Prueba_Jogger_Estres\Jogger_Elastica_Dama_Mariarlenys.val', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Front Inseam Spline Angle
content = content.replace(
    'angle1="AngleLine_F_Gavilan_F_Rodilla_Ent - 10"',
    'angle1="AngleLine_F_Rodilla_Ent_F_Gavilan + 180 - 10"'
)

# Fix Back Inseam Spline Angle
content = content.replace(
    'angle1="AngleLine_T_Gavilan_Bajo_T_Rodilla_Ent - 10"',
    'angle1="AngleLine_T_Rodilla_Ent_T_Gavilan_Bajo + 180 - 10"'
)

with open(r'C:\Users\Ricx18\Desktop\Prueba_Jogger_Estres\Jogger_Elastica_Dama_Mariarlenys.val', 'w', encoding='utf-8') as f:
    f.write(content)

print("File successfully modified and written.")
