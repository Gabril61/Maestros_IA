import os, glob, re

val_files = glob.glob('c:/Users/Ricx18/Desktop/Maestros_IA/*.val')
for path in val_files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'<spline[^>]+length[12]="\d+(?:\.\d+)?"[^>]*>', content)
    if matches:
        print(f'File: {os.path.basename(path)}')
        for m in matches:
            # check if it belongs to Manga
            # we can guess by looking at point references or just print them all
            name_match = re.search(r'id="([^"]+)"', m)
            id_val = name_match.group(1) if name_match else 'unknown'
            # limit output size
            print(f'  Spline ID {id_val}')
