import re

files = ['Basico_Superior_Dama_Maestro.val', 'Blusa_Cuello_Mao_Dama_Maestro.val']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # The string to search and replace
    target = 'sqrt((25 * 25) +'
    replacement = 'sqrt((@G_ALTO_CADERA * @G_ALTO_CADERA) +'
    
    if target in content:
        content = content.replace(target, replacement)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {filename}')
    else:
        print(f'Target not found in {filename}')
