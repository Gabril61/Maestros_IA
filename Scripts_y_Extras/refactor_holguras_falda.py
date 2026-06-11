import re

filepath = r'C:\Users\Ricx18\Desktop\Maestros_IA\Falda_Ejecutiva_Dama_Maestro.val'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace variables tag
old_vars = '<m description="Holgura inferior total" name="#holgura_inferior" value="4"/>'
new_vars = '<m description="Holgura de cintura" name="#holgura_cintura" value="2"/>\n        <m description="Holgura de cadera" name="#holgura_cadera" value="4"/>'
content = content.replace(old_vars, new_vars)

# Replace in Waist formulas
content = content.replace('(@G_CONT_CINTURA/4) + (#holgura_inferior/4)', '(@G_CONT_CINTURA/4) + (#holgura_cintura/4)')
content = content.replace('(@G_CONT_CINTURA/2) + (#holgura_inferior/2)', '(@G_CONT_CINTURA/2) + (#holgura_cintura/2)')

# Replace in Hip/Caja formulas
content = content.replace('(@G_CONT_CADERA_BAJA/4) + (#holgura_inferior/4)', '(@G_CONT_CADERA_BAJA/4) + (#holgura_cadera/4)')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Separated holgura_cintura and holgura_cadera.')
