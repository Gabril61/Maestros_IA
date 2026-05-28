import os
import re
import shutil

DAMA = r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val'
ESTANDAR = r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val'
UNISEX = r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val'

# Backup first
shutil.copy(ESTANDAR, ESTANDAR + '.bak_pieces')
shutil.copy(UNISEX, UNISEX + '.bak_pieces')

with open(DAMA, 'r', encoding='utf-8') as f:
    dama_content = f.read()

# Extract the block from </calculation> to </draftBlock> in Dama
# We want the text strictly *after* </calculation> and *before* </draftBlock>
match = re.search(r'(</calculation>)(.*?)(</draftBlock>)', dama_content, re.DOTALL)
if not match:
    print("Could not find the block in Dama!")
    exit(1)

extracted_block = match.group(2)

def inject_block(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace everything between </calculation> and </draftBlock>
    new_content = re.sub(r'(</calculation>)(.*?)(</draftBlock>)', r'\1' + extracted_block + r'\3', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully injected into {os.path.basename(filepath)}")

inject_block(ESTANDAR)
inject_block(UNISEX)
print("Sync complete.")
