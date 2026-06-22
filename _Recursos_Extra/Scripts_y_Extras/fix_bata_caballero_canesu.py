import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Change the Canesu reference point length from 12 to 9
content = content.replace('id="90030" length="12"', 'id="90030" length="9"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Canesu depth.")
