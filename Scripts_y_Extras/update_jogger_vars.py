import xml.etree.ElementTree as ET
import re

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Reemplazar variables antiguas por las de Maestro_Variables_IA.smis
text = text.replace('@I_CONTCINBA', '@G_CONT_CINTURA')
text = text.replace('@I_CONTCADBA', '@G_CONT_CADERA_BAJA')

# Actualizar el nombre del draftBlock
text = re.sub(r'<draftBlock name=\"[^\"]+\">', '<draftBlock name=\"Pantalon_Jogger_Clinico\">', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Variables and draft name updated')
