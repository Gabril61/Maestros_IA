import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Basico_Maestro.val'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if 'id="1120"' in line and 'D_Hombro_Temp' in line:
        new_lines.append('\n            <line firstPoint="104" id="1121" secondPoint="1120" />\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fix applied.")
