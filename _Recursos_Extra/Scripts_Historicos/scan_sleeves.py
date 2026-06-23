import os, glob, re
import xml.etree.ElementTree as ET

val_files = glob.glob('c:/Users/Ricx18/Desktop/Maestros_IA/*.val')
for path in val_files:
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        for db in root.findall('.//draftBlock'):
            name = db.get('name', '').lower()
            if 'manga' in name or 'sleeve' in name or 'corpino' in name:
                calc = db.find('calculation')
                if calc is not None:
                    splines = calc.findall('spline')
                    if splines:
                        for s in splines:
                            l1 = s.get('length1', '')
                            l2 = s.get('length2', '')
                            if re.match(r'^\d+(\.\d+)?$', l1) or re.match(r'^\d+(\.\d+)?$', l2):
                                print(f'File: {os.path.basename(path)} - Spline {s.get("id")}: l1={l1}, l2={l2}')
    except Exception as e:
        print(f'Error reading {path}: {e}')
