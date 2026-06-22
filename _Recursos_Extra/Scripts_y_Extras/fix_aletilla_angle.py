import re

file_path = "Blazer_Dama_Maestro.val"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the AngleLine of the non-existent Aletilla line with the parallel seam line angle
content = content.replace("AngleLine_MS_Aletilla_Top_Cimera_MS_Aletilla_Cimera_Bot_Ext", "AngleLine_MS_Codo_Cimera_Der_MS_Puno_Cimera_Der")
content = content.replace("AngleLine_MS_Aletilla_Top_Bajera_MS_Aletilla_Bajera_Bot_Ext", "AngleLine_MS_Codo_Bajera_Der_MS_Puno_Bajera_Der")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Aletilla Hem Extension angles fixed successfully!")
