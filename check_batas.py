import os, glob, xml.etree.ElementTree as ET

val_files = glob.glob('c:/Users/Ricx18/Desktop/Maestros_IA/Bata*.val')
for path in val_files:
    try:
        tree = ET.parse(path)
        print(f'\n{os.path.basename(path)}:')
        for s in tree.findall('.//spline'):
            l1 = s.get('length1', '')
            if '0.55' in l1 or '0.4' in l1 or 'Line_' in l1:
                pass
            else:
                if 'length1' in s.attrib and l1.replace('.','',1).isdigit():
                    print(f'  Spline {s.get("id")}: {l1}')
    except Exception as e:
        pass
