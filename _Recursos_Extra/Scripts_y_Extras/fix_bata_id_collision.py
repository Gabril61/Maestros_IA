import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the duplicated IDs
content = content.replace('id="20005" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Inter_Pecho"', 'id="90005" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Inter_Pecho"')
content = content.replace('id="20006" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Inter_Sisa"', 'id="90006" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Inter_Sisa"')

content = content.replace('basePoint="20005" id="210"', 'basePoint="90005" id="210"')
content = content.replace('basePoint="20006" id="211"', 'basePoint="90006" id="211"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("ID collision patched successfully.")
