import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Caballero_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Update metadata
desc = root.find('description')
if desc is not None:
    desc.text = "Patrón Maestro - Scrub Top Médico Caballero (Boxy)"

# 2. Flatten Side Seams
for p in calc.findall('point'):
    name = p.get('name', '')
    if name in ['F_Costado_Cintura', 'T_Costado_Cintura']:
        p.set('length', '((@S_CONTBUSTO + @M_HOLGURA_BATA)/4)')
    elif name in ['F_Costado_Ruedo', 'T_Costado_Ruedo']:
        p.set('length', '((@I_CONTCADBA + @M_HOLGURA_BATA)/4)')
    elif name == 'T_Centro_Cintura':
        # Remove the 2.5cm inward waist dart on the center back
        p.set('length', '0')

# 3. Clean up the back spline to make it a straight line
# The user wants the back to be straight. The spline 20002 goes from 202 to 250.
# The line 40500 goes from 250 to 218.
# By setting T_Centro_Cintura to 0, 202 -> 250 -> 218 will all fall on the vertical axis X=0.
# However, 202 is T_Escote_Profundidad which is down 2.5 from T_Origen.
# Since T_Centro_Cintura is now X=0, the spline and line will just form a perfectly straight vertical line!
# I don't even need to delete the spline, it will just draw straight. But to be clean, I can replace the spline with a line.
splines_to_remove = []
for s in calc.findall('spline'):
    if s.get('id') == '20002':
        splines_to_remove.append(s)

for s in splines_to_remove:
    calc.remove(s)

# Add a straight line from 202 to 250 to replace the spline
calc.append(ET.Element('line', {
    'id': '40501',
    'firstPoint': '202',
    'secondPoint': '250',
    'lineColor': 'black',
    'lineType': 'solidLine',
    'lineWeight': '0.35'
}))

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Scrub Top Caballero masculinized successfully.")
