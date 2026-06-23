import os

path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Camisa_Dama_Maestro.val'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Change holgura_sisa to 15%
content = content.replace('formula="@S_CONT_SISA * 0.1" name="#holgura_sisa"',
                          'formula="@S_CONT_SISA * 0.15" name="#holgura_sisa"')
content = content.replace('description="Holgura dinámica y escalable de sisa (10%)"',
                          'description="Holgura dinámica y escalable de sisa (15%)"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Camisa updated to 15% ease.')
