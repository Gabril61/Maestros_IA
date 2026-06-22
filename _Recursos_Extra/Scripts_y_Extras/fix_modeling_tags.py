import re

file_path = "Blazer_Dama_Maestro.val"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '<point id="30014" idObject="30002" inUse="false" mx="0.1" my="0.1" name="Corte_Espalda_Bicep" showPointName="true" type="modeling"/>',
    '<point angle="0" basePoint="30002" id="30014" length="0" mx="0.1" my="0.1" name="Corte_Espalda_Bicep" showPointName="true" type="endLine"/>'
)
content = content.replace(
    '<point id="30015" idObject="30004" inUse="false" mx="0.1" my="0.1" name="Corte_Espalda_Codo" showPointName="true" type="modeling"/>',
    '<point angle="0" basePoint="30004" id="30015" length="0" mx="0.1" my="0.1" name="Corte_Espalda_Codo" showPointName="true" type="endLine"/>'
)
content = content.replace(
    '<point id="30016" idObject="30006" inUse="false" mx="0.1" my="0.1" name="Corte_Espalda_Puno" showPointName="true" type="modeling"/>',
    '<point angle="0" basePoint="30006" id="30016" length="0" mx="0.1" my="0.1" name="Corte_Espalda_Puno" showPointName="true" type="endLine"/>'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Tags fixed!")
