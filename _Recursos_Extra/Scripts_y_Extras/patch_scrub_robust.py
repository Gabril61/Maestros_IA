import sys

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if 'id="13"' in line and 'name="E_Hombro_Punta"' in line:
        new_lines.append('            <line firstPoint="13" id="999" secondPoint="11"/>\n')
    if 'id="112"' in line and 'name="D_Hombro_Punta"' in line:
        new_lines.append('            <line firstPoint="112" id="998" secondPoint="110"/>\n')

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("File fully patched.")
