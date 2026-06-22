import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# Find the start of splines block
idx_spline_start = -1
for i, line in enumerate(lines):
    if '<!-- COMPOSICIÓN DE SISA EN 2 SPLINES' in line:
        idx_spline_start = i
        break

# Find the start of dart block
idx_dart_start = -1
for i, line in enumerate(lines):
    if '<!-- Pinza y PICO PRINCESA -->' in line:
        idx_dart_start = i
        break

# Find the end of dart block
idx_dart_end = -1
for i, line in enumerate(lines):
    if '<!-- UBICACIÓN BOLSILLO DELANTERO' in line:
        idx_dart_end = i
        break

if idx_spline_start != -1 and idx_dart_start != -1 and idx_dart_end != -1 and idx_spline_start < idx_dart_start:
    splines_block = lines[idx_spline_start:idx_dart_start]
    dart_block = lines[idx_dart_start:idx_dart_end]
    
    # Remove old blocks
    new_lines = lines[:idx_spline_start] + dart_block + splines_block + lines[idx_dart_end:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    print("Fixed dependency order by swapping splines and dart blocks.")
else:
    print("Could not find the correct indices.")
