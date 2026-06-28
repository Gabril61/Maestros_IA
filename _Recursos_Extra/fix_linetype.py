import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Basico_Maestro.val'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the broken line definition
broken_line = '<line firstPoint="200" id="2001" lineColor="black" lineType="dottedLine" lineWeight="0.8" secondPoint="2000" />'
fixed_line = '<line firstPoint="200" id="2001" secondPoint="2000" />'

content = content.replace(broken_line, fixed_line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fix applied.")
