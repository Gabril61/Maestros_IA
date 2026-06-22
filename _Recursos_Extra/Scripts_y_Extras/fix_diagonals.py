import re

def fix_diagonals(path, old_pt, new_pt):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace <line ... firstPoint="old_pt" ... secondPoint="232" ...>
    # with firstPoint="new_pt".
    # Or secondPoint="old_pt" firstPoint="232"
    
    # Actually, let's just do a string replace if we know the exact string.
    # In Estandar: <line firstPoint="221" id="243" secondPoint="232" />
    content = content.replace(f'firstPoint="{old_pt}" id="243" secondPoint="232"', f'firstPoint="{new_pt}" id="243" secondPoint="232"')
    
    # What about Unisex? Maybe it's not line 243. Let's search for any line connecting old_pt and 232.
    content = re.sub(rf'firstPoint="{old_pt}"([^>]*)secondPoint="232"', rf'firstPoint="{new_pt}"\1secondPoint="232"', content)
    content = re.sub(rf'secondPoint="{old_pt}"([^>]*)firstPoint="232"', rf'secondPoint="{new_pt}"\1firstPoint="232"', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_diagonals(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val', '221', '30036')
fix_diagonals(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val', '221', '31003')

print("Diagonals fixed.")
