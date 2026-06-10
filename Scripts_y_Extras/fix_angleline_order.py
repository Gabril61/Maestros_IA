import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """            <point firstPoint="17" id="38" length="Line_D_Punto_Pezon_D_Princesa_Sisa_Estandar * 2" name="D_Princesa_Sisa_Real" secondPoint="37" type="alongLine"/>
            <!-- Pinza de sisa (Apertura de volumen tridimensional) -->
            <point angle="AngleLine_D_Princesa_Sisa_Real_D_Costado_Sisa" basePoint="38" id="3800" length="2.5" name="D_Princesa_Sisa_Inf" type="endLine"/>
            <!-- Líneas Guía para inicializar las variables de longitud -->
            <line firstPoint="12" id="39" secondPoint="38"/>
            <line firstPoint="38" id="40" secondPoint="19"/>
            <line firstPoint="38" id="41" secondPoint="17"/>
            <line firstPoint="3800" id="3801" secondPoint="19"/>
            <line firstPoint="3800" id="3802" secondPoint="17"/>"""

replace = """            <point firstPoint="17" id="38" length="Line_D_Punto_Pezon_D_Princesa_Sisa_Estandar * 2" name="D_Princesa_Sisa_Real" secondPoint="37" type="alongLine"/>
            <!-- Líneas Guía para inicializar las variables de longitud -->
            <line firstPoint="12" id="39" secondPoint="38"/>
            <line firstPoint="38" id="40" secondPoint="19"/>
            <line firstPoint="38" id="41" secondPoint="17"/>
            <!-- Pinza de sisa (Apertura de volumen tridimensional) -->
            <point angle="AngleLine_D_Princesa_Sisa_Real_D_Costado_Sisa" basePoint="38" id="3800" length="2.5" name="D_Princesa_Sisa_Inf" type="endLine"/>
            <line firstPoint="3800" id="3801" secondPoint="19"/>
            <line firstPoint="3800" id="3802" secondPoint="17"/>"""

# we might have windows newlines (\n to \r\n), so replacing by lines is safer, but if python reads it as \n, this match should work.
if target in content:
    content = content.replace(target, replace)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed order successfully using blocks.")
else:
    print("Block not found. Falling back to line search.")
    lines = content.split('\n')
    idx_38 = -1
    idx_3800 = -1
    idx_guia = -1
    
    # Simple line-by-line fix if the block doesn't match perfectly.
    # It's better to read and rewrite it correctly.
    for i, line in enumerate(lines):
        if 'id="3800"' in line and 'name="D_Princesa_Sisa_Inf"' in line:
            idx_3800 = i
        if 'id="41"' in line and 'firstPoint="38"' in line:
            idx_41 = i
            break
            
    if idx_3800 != -1 and idx_41 != -1 and idx_3800 < idx_41:
        # 3800 is before 41, which means it is before the lines.
        # Let's reorder them
        # Lines 39, 40, 41 are currently below 3800. We need them above 3800.
        # Find exactly where 3800 starts (might include the comment above it)
        comment_idx = idx_3800 - 1
        
        # We know exactly the lines. Let's just do a manual swap.
        # Extract the lines:
        # lines[comment_idx] = '            <!-- Pinza de sisa (Apertura de volumen tridimensional) -->'
        # lines[idx_3800] = '            <point angle="AngleLine_D_Princesa_Sisa_Real_D_Costado_Sisa"...'
        # lines[idx_3800+1] = '            <!-- Líneas Guía para inicializar las variables de longitud -->'
        # lines[idx_3800+2] = '            <line firstPoint="12" id="39" secondPoint="38"/>'
        # lines[idx_3800+3] = '            <line firstPoint="38" id="40" secondPoint="19"/>'
        # lines[idx_3800+4] = '            <line firstPoint="38" id="41" secondPoint="17"/>'
        
        # Swapping:
        # new_order = [idx_3800+1, idx_3800+2, idx_3800+3, idx_3800+4, comment_idx, idx_3800]
        temp = [lines[comment_idx], lines[idx_3800]]
        lines[comment_idx] = lines[idx_3800+1]
        lines[idx_3800] = lines[idx_3800+2]
        lines[idx_3800+1] = lines[idx_3800+3]
        lines[idx_3800+2] = lines[idx_3800+4]
        lines[idx_3800+3] = temp[0]
        lines[idx_3800+4] = temp[1]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print("Fixed order successfully using line swapping.")
    else:
        print("Couldn't find the exact lines to swap.")
