import re

file_path = "Blazer_Dama_Maestro.val"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the invalid AngleLine variables and adjust the math to maintain the same direction (+90 instead of -90)
content = content.replace("AngleLine_MS_Puno_Cimera_Der_MS_Codo_Cimera_Der - 90", "AngleLine_MS_Codo_Cimera_Der_MS_Puno_Cimera_Der + 90")
content = content.replace("AngleLine_MS_Puno_Bajera_Der_MS_Codo_Bajera_Der - 90", "AngleLine_MS_Codo_Bajera_Der_MS_Puno_Bajera_Der + 90")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("AngleLine formulas fixed successfully!")
