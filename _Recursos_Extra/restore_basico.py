import xml.etree.ElementTree as ET
import re

with open("C:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove line 1010
content = re.sub(r"\s*<line firstPoint=\"1000\" id=\"1010\" secondPoint=\"1002\"/>", "", content)

# 2. Revert M_Ancho_Izq
content = re.sub(
    r"<point angle=\"180\" basePoint=\"1002\" id=\"1003\" length=\"sqrt[^\"]+\"",
    r'<point angle="180" basePoint="1002" id="1003" length="(@S_CONT_BICEP/2)+2"',
    content
)

# 3. Revert M_Ancho_Der
content = re.sub(
    r"<point angle=\"0\" basePoint=\"1002\" id=\"1004\" length=\"sqrt[^\"]+\"",
    r'<point angle="0" basePoint="1002" id="1004" length="(@S_CONT_BICEP/2)+2"',
    content
)

# 4. Remove ALERTA_MANGA_DESPROPORCIONADA
content = re.sub(r"\s*<point angle=\"0\" basePoint=\"1000\" id=\"9998\"[^>]+name=\"ALERTA_MANGA_DESPROPORCIONADA\"[^>]+/>", "", content)

with open("C:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val", "w", encoding="utf-8") as f:
    f.write(content)
print("File restored successfully.")
