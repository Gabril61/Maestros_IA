import os
import re

path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blusa_Dama_CortePrincesa_Maestro.val'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix F_Linea_Sisa and T_Linea_Sisa robustly
# We find the <point ... name="F_Linea_Sisa" ... /> element using a robust regex that doesn't care about attribute order
def replace_sisa_length(match):
    tag = match.group(0)
    # Replace the length attribute inside this tag
    new_tag = re.sub(r'length="[^"]+"', r'length="(@S_CONT_SISA / 2) + #holgura_sisa"', tag)
    return new_tag

content = re.sub(r'<point[^>]+name="F_Linea_Sisa"[^>]*/>', replace_sisa_length, content)
content = re.sub(r'<point[^>]+name="T_Linea_Sisa"[^>]*/>', replace_sisa_length, content)

# 2. Hide ALERTA_SISA_ESTRECHA
def hide_alert(match):
    tag = match.group(0)
    new_tag = tag.replace('showPointName="true"', 'showPointName="false"')
    return new_tag

content = re.sub(r'<point[^>]+name="ALERTA_SISA_ESTRECHA"[^>]*/>', hide_alert, content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# 3. VERIFICATION PROTOCOL (The Polish)
errors = []
if 'length="(@S_CONT_SISA / 2) + #holgura_sisa"' not in content:
    errors.append("Fallo crítico: El M.A.S. no se inyectó correctamente en las curvas de sisa.")
if 'ALERTA_SISA_ESTRECHA' not in content:
    errors.append("Fallo crítico: No se encontró la alerta de sisa.")

if errors:
    print("VERIFICACIÓN FALLIDA:")
    for e in errors:
        print(" -", e)
else:
    print("VERIFICACIÓN EXITOSA: La regla de sisas se ha aplicado correctamente.")
