import sys
import os

def fix_val(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace id="99002_guia" with id="99004"
    if '99002_guia' in content:
        content = content.replace('id="99002_guia"', 'id="99004"')
        content = content.replace('basePoint="99002_guia"', 'basePoint="99004"')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed numerical ID error successfully.")
    else:
        print("99002_guia not found.")

if __name__ == '__main__':
    fix_val(r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val')
