import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Extract all newly added points and lines
points = []
lines = []

to_remove = []
for el in list(calc):
    el_id = el.get('id')
    if el_id and (el_id.startswith('400') or el_id.startswith('401')):
        if el.tag == 'point':
            points.append(el)
        else:
            lines.append(el)
        to_remove.append(el)

# Remove them from calc
for el in to_remove:
    calc.remove(el)

# Re-append in the correct order: points first, then lines
for p in points:
    calc.append(p)
for l in lines:
    calc.append(l)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Fixed calculation order: points are now before lines.")
