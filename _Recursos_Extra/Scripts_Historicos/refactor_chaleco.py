import os
import re

path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Chaleco_Femenino_Maestro.val'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Expand variables block
injections = [
    '<variable description="Holgura superior" formula="3" name="#holgura_superior"/>',
    '<variable description="Holgura inferior" formula="4" name="#holgura_inferior"/>',
    '<variable description="Holgura cintura" formula="2" name="#holgura_cintura"/>',
    '<variable description="Pinza cintura" formula="3" name="#pinza_cint_sup"/>',
    '<variable description="Ruedo prenda" formula="3" name="#ruedo_prenda"/>',
    '<variable description="Holgura dinámica y escalable de sisa (15%)" formula="@S_CONT_SISA * 0.15" name="#holgura_sisa"/>'
]

vars_str = "\n".join([f"        {i}" for i in injections])
vars_block = f"<variables>\n{vars_str}\n    </variables>"

if '<variables />' in content:
    content = content.replace('<variables />', vars_block)
elif '<variables/>' in content:
    content = content.replace('<variables/>', vars_block)

# 2. Fix F_Linea_Sisa and T_Linea_Sisa robustly
def replace_sisa_length(match):
    tag = match.group(0)
    new_tag = re.sub(r'length="[^"]+"', r'length="(@S_CONT_SISA / 2) + #holgura_sisa"', tag)
    return new_tag

content = re.sub(r'<point[^>]+name="F_Linea_Sisa"[^>]*/>', replace_sisa_length, content)
content = re.sub(r'<point[^>]+name="T_Linea_Sisa"[^>]*/>', replace_sisa_length, content)

# 3. Hide ALERTA_SISA_ESTRECHA
def hide_alert(match):
    tag = match.group(0)
    new_tag = tag.replace('showPointName="true"', 'showPointName="false"')
    return new_tag

content = re.sub(r'<point[^>]+name="ALERTA_SISA_ESTRECHA"[^>]*/>', hide_alert, content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

# 4. VERIFICATION
errors = []
if '<variable description="Holgura superior"' not in content:
    errors.append("Fallo: No se inyectaron las variables.")
if 'length="(@S_CONT_SISA / 2) + #holgura_sisa"' not in content:
    errors.append("Fallo crítico: El M.A.S. no se inyectó en las curvas de sisa.")
if 'ALERTA_SISA_ESTRECHA' not in content:
    errors.append("Fallo crítico: No se encontró la alerta de sisa.")

if errors:
    print("VERIFICACIÓN FALLIDA:")
    for e in errors:
        print(" -", e)
else:
    print("VERIFICACIÓN EXITOSA: Chaleco refactorizado y regla M.A.S. aplicada correctamente.")
