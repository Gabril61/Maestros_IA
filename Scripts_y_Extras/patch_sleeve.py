import sys

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if 'id="206"' in line and 'secondPoint="205"' in line:
        new_lines.append('            <line firstPoint="200" id="299" secondPoint="204"/>\n')
        new_lines.append('            <line firstPoint="200" id="298" secondPoint="205"/>\n')

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Sleeve fully patched.")
