import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract the block of code for 202, 20000, 20001, 20002
block_regex = re.compile(
    r'\s*<point angle="270" basePoint="200" id="202".*?/>\s*'
    r'<line firstPoint="200" id="20000" secondPoint="202"/>\s*'
    r'<spline angle1="180" angle2="270" color="black" id="20001".*?/>\s*'
    r'<spline angle1="270" angle2="90" color="black" id="20002".*?/>\s*',
    re.DOTALL
)

match = block_regex.search(content)
if match:
    block_text = match.group(0)
    # 2. Remove it from its current location
    content = content.replace(block_text, '\n')
    
    # 3. Insert it right before 90005
    target_insert = r'<point angle="180" basePoint="209" curve="20002" id="90005"'
    content = content.replace(target_insert, block_text + '            ' + target_insert)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Block moved successfully.")
else:
    print("Could not find the block to move.")
