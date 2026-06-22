import sys

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if 'id="15"' in line and 'secondPoint="14"' in line:
        new_lines.append('            <line firstPoint="14" id="999" secondPoint="8"/>\n')
    if 'id="114"' in line and 'secondPoint="113"' in line:
        new_lines.append('            <line firstPoint="113" id="998" secondPoint="107"/>\n')

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Lines injected.")
