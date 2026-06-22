import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace non-numeric IDs 'm900' with '8900'
content = content.replace('"m900', '"8900')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed non-numeric IDs.")
