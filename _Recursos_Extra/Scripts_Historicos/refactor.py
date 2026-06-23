import os
import glob
import re
import xml.etree.ElementTree as ET

smis_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Maestro_Variables_IA.smis'

tree = ET.parse(smis_path)
root = tree.getroot()
body_meas = root.find('body-measurements')

extracted_vars = {}

for m in body_meas.findall('m'):
    name = m.get('name')
    if name and (name.startswith('@D_') or name.startswith('@M_')):
        val = m.get('value', '0')
        desc = m.get('full_name', '')
        if not desc:
            desc = m.get('description', '')
        if not desc:
            desc = name[3:].replace('_', ' ').capitalize()
        
        # generate new name
        new_name = '#' + name[3:].lower()
        extracted_vars[name] = {
            'new_name': new_name,
            'value': val,
            'desc': desc,
            'elem': m
        }

# Remove from smis
for k, v in extracted_vars.items():
    body_meas.remove(v['elem'])

# Write smis back (with proper encoding and header)
with open(smis_path, 'wb') as f:
    f.write(b"<?xml version='1.0' encoding='UTF-8'?>\n")
    ET.ElementTree(root).write(f, encoding='utf-8', xml_declaration=False)
    
print(f"Extracted {len(extracted_vars)} variables and updated .smis")

# Process .val files
val_files = glob.glob('c:/Users/Ricx18/Desktop/Maestros_IA/*.val')
for val_path in val_files:
    with open(val_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    vars_to_inject = []
    modified = False
    
    # Check for variables
    for old_name, v in extracted_vars.items():
        if old_name in content:
            vars_to_inject.append(v)
            content = content.replace(old_name, v['new_name'])
            modified = True
            
    if modified:
        # Create variable tags string
        inject_str = ''
        for v in vars_to_inject:
            inject_str += f'        <variable description="{v["desc"]}" formula="{v["value"]}" name="{v["new_name"]}"/>\n'
            
        # Insert into content
        if '<variables/>' in content:
            content = content.replace('<variables/>', f'<variables>\n{inject_str}    </variables>')
        elif '    </variables>' in content:
            # We want to put these BEFORE #holgura_sisa if it exists, or just at the end.
            # But putting it right before </variables> is safe.
            # Actually, #holgura_sisa might depend on something? No, it depends on @S_CONT_SISA.
            content = content.replace('    </variables>', f'{inject_str}    </variables>')
            
        with open(val_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(val_path)} with {len(vars_to_inject)} new variables.")
