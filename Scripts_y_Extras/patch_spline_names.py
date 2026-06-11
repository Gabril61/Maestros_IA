import sys

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    'length="Spline_19"',
    'length="Spline_E_Hombro_Punta_E_Axila"'
)

content = content.replace(
    'length="Spline_115"',
    'length="Spline_D_Hombro_Punta_D_Axila"'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Spline names patched.")
