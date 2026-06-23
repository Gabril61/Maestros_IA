import os
import re

# 1. Update .antigravityrules
rules_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/.antigravityrules'
with open(rules_path, 'r', encoding='utf-8') as f:
    rules_content = f.read()

if 'BLOQUE V: PROTOCOLOS DE ACTIVACIÓN DE IA' not in rules_content:
    new_block = """

### BLOQUE V: PROTOCOLOS DE ACTIVACIÓN DE IA
17. PROTOCOLO DE REFACTORIZACIÓN (Limpieza y Sometimiento): Al invocar este protocolo sobre un archivo, el agente debe ejecutar obligatoriamente la siguiente rutina:
- A) Rastrear y purgar toda variable @D_ o @M_, reemplazándolas por #incrementos y declarándolas en <variables>.
- B) Inyectar #holgura_sisa según el tipo de prenda (10% estándar, 15% entallada).
- C) Validar o inyectar el nodo ALERTA_SISA_ESTRECHA auditando la regla M.A.S.
- D) Verificar que el atributo color sea siempre black y limpiar redundancias (como <increments/>).
"""
    with open(rules_path, 'a', encoding='utf-8') as f:
        f.write(new_block)
    print('.antigravityrules actualizado con Bloque V.')

# 2. Refactor Blusa
val_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blusa_Dama_CortePrincesa_Maestro.val'
with open(val_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define default values for injected variables
injections = [
    '<variable description="Holgura superior" formula="3" name="#holgura_superior"/>',
    '<variable description="Holgura inferior" formula="4" name="#holgura_inferior"/>',
    '<variable description="Holgura cintura" formula="2" name="#holgura_cintura"/>',
    '<variable description="Pinza cintura" formula="3" name="#pinza_cint_sup"/>',
    '<variable description="Modificacion copa" formula="0" name="#mod_copa"/>',
    '<variable description="Largo corte manga" formula="25" name="#largo_corte_manga"/>',
    '<variable description="Ruedo manga" formula="3" name="#ruedo_manga"/>',
    '<variable description="Ruedo prenda" formula="3" name="#ruedo_prenda"/>',
    '<variable description="Holgura dinámica y escalable de sisa (15%)" formula="@S_CONT_SISA * 0.15" name="#holgura_sisa"/>'
]

# Expand variables tag
vars_str = "\n".join([f"        {i}" for i in injections])
vars_block = f"<variables>\n{vars_str}\n    </variables>"

if '<variables/>' in content:
    content = content.replace('<variables/>', vars_block)
else:
    # If it's already an open tag, we inject at the end. But the script said it was missing or empty.
    content = content.replace('    <variables>', f'    <variables>\n{vars_str}')

# Replace old variables
replacements = {
    '@D_HOLGURA_SUPERIOR': '#holgura_superior',
    '@D_HOLGURA_INFERIOR': '#holgura_inferior',
    '@D_HOLGURA_CINTURA': '#holgura_cintura',
    '@D_PINZA_CINT_SUP': '#pinza_cint_sup',
    '@D_MOD_COPA': '#mod_copa',
    '@D_LARGO_CORTE_MANGA': '#largo_corte_manga',
    '@D_RUEDO_MANGA': '#ruedo_manga',
    '@D_RUEDO_PRENDA': '#ruedo_prenda'
}

for old_v, new_v in replacements.items():
    content = content.replace(old_v, new_v)

# Apply M.A.S to Sisa points
# Find the exact F_Linea_Sisa and T_Linea_Sisa lines and replace their lengths
import re
content = re.sub(r'name="F_Linea_Sisa"\s+showPointName="true"\s+type="endLine"/>',
                 r'name="F_Linea_Sisa" showPointName="true" type="endLine"/>', content)

# But they might be proportional right now. Let's do a regex to replace length="..." for these two points
content = re.sub(r'(name="F_Linea_Sisa".*?length=")[^"]+(")', r'\1(@S_CONT_SISA / 2) + #holgura_sisa\2', content)
content = re.sub(r'(name="T_Linea_Sisa".*?length=")[^"]+(")', r'\1(@S_CONT_SISA / 2) + #holgura_sisa\2', content)

# Make alert invisible
content = content.replace('name="ALERTA_SISA_ESTRECHA" showPointName="true"', 'name="ALERTA_SISA_ESTRECHA" showPointName="false"')

# Fix any red colors just in case
content = content.replace('lineColor="red"', 'lineColor="black"')

with open(val_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Blusa refactorizada impecablemente.')
