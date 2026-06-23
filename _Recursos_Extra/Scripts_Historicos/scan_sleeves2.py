import os, glob
import xml.etree.ElementTree as ET

val_files = glob.glob('c:/Users/Ricx18/Desktop/Maestros_IA/*.val')
for path in val_files:
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        for db in root.findall('.//draftBlock'):
            name = db.get('name', '').lower()
            if 'manga' in name or 'sleeve' in name:
                calc = db.find('calculation')
                if calc is not None:
                    splines = calc.findall('spline')
                    if splines:
                        print(f'\\nFile: {os.path.basename(path)} - Block: {name}')
                        for s in splines:
                            l1 = s.get('length1', '')
                            l2 = s.get('length2', '')
                            id_val = s.get('id', '')
                            print(f'  Spline {id_val}: l1={l1}, l2={l2}')
    except Exception as e:
        pass
