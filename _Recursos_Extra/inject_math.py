import xml.etree.ElementTree as ET
import re

with open("C:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val", "r", encoding="utf-8") as f:
    content = f.read()

# Replace M_Ancho_Izq
content = re.sub(
    r'<point angle="180" basePoint="1002" id="1003" length="[^"]+"',
    r'<point angle="180" basePoint="1002" id="1003" length="sqrt((Spl_F_Caida_Hombro_F_Ancho_Pecho + Spl_F_Ancho_Pecho_F_Sisa_Pinza_Sup + Spl_F_Sisa_Pinza_Inf_F_Costado_Sisa) * (Spl_F_Caida_Hombro_F_Ancho_Pecho + Spl_F_Ancho_Pecho_F_Sisa_Pinza_Sup + Spl_F_Sisa_Pinza_Inf_F_Costado_Sisa) - (((@S_CONT_BUSTO/10)+3) * ((@S_CONT_BUSTO/10)+3)))"',
    content
)

# Replace M_Ancho_Der
content = re.sub(
    r'<point angle="0" basePoint="1002" id="1004" length="[^"]+"',
    r'<point angle="0" basePoint="1002" id="1004" length="sqrt((Spl_T_Caida_Hombro_T_Ancho_Espalda + Spl_T_Ancho_Espalda_T_Costado_Sisa) * (Spl_T_Caida_Hombro_T_Ancho_Espalda + Spl_T_Ancho_Espalda_T_Costado_Sisa) - (((@S_CONT_BUSTO/10)+3) * ((@S_CONT_BUSTO/10)+3)))"',
    content
)

with open("C:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val", "w", encoding="utf-8") as f:
    f.write(content)
print("Formulas injected successfully.")
