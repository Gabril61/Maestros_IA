import os
path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Camisa_Dama_Maestro.val'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Only inject if it's not already in the variables section
if '<variable description="Holgura dinámica y escalable de sisa' not in content:
    var_inject = '        <variable description="Holgura dinámica y escalable de sisa (10%)" formula="@S_CONT_SISA * 0.1" name="#holgura_sisa"/>\n'
    content = content.replace('    </variables>', var_inject + '    </variables>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Variable injected.')
