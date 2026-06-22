import sys

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix Spline 207 (Left Cap)
# Current: length1="Line_M_Nivel_Copa_M_Sisa_Izq * 0.6" length2="Line_M_Nivel_Copa_M_Sisa_Izq * 0.6"
content = content.replace(
    'length1="Line_M_Nivel_Copa_M_Sisa_Izq * 0.6" length2="Line_M_Nivel_Copa_M_Sisa_Izq * 0.6"',
    'length1="Line_M_Nivel_Copa_M_Sisa_Izq * 0.15" length2="Line_M_Nivel_Copa_M_Sisa_Izq * 0.55"'
)

# Fix Spline 208 (Right Cap)
# Current: length1="Line_M_Nivel_Copa_M_Sisa_Der * 0.6" length2="Line_M_Nivel_Copa_M_Sisa_Der * 0.6"
content = content.replace(
    'length1="Line_M_Nivel_Copa_M_Sisa_Der * 0.6" length2="Line_M_Nivel_Copa_M_Sisa_Der * 0.6"',
    'length1="Line_M_Nivel_Copa_M_Sisa_Der * 0.55" length2="Line_M_Nivel_Copa_M_Sisa_Der * 0.15"'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Sleeve cap standardized.")
