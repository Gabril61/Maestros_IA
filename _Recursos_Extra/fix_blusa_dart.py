import xml.etree.ElementTree as ET

filepath = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(filepath)
calc = tree.getroot().find('.//calculation')

p_inf = calc.find(".//point[@name='F_Sisa_Pinza_Inf']")
if p_inf is None:
    print("Already fixed or point not found.")
    exit()

old_bad_id = p_inf.get('id')
print(f"Found F_Sisa_Pinza_Inf with ID: {old_bad_id}")

p_inf.set('name', 'F_Sisa_Pinza_Inf_Ref')

# find the true max ID
max_id = 0
for el in tree.getroot().iter():
    if 'id' in el.attrib:
        try:
            val = int(el.get('id'))
            if val > max_id: max_id = val
        except: pass

new_unique_id = str(max_id + 1)
print(f"New ID will be: {new_unique_id}")

# Find F_Centro_Busto
p160 = calc.find(".//point[@name='F_Centro_Busto']")
id_busto = p160.get('id') if p160 is not None else '160'

new_point = ET.Element('point', {
    'id': new_unique_id,
    'name': 'F_Sisa_Pinza_Inf',
    'type': 'alongLine',
    'firstPoint': id_busto,
    'secondPoint': old_bad_id,
    'length': 'Line_F_Centro_Busto_F_Sisa_Pinza_Sup',
    'lineColor': 'black',
    'lineType': 'none',
    'lineWeight': '0.35'
})

# Find where to insert it: After Line_F_Centro_Busto_F_Sisa_Pinza_Sup is created!
# That line is usually created by a <line> element between Bust and Sup.
p_sup = calc.find(".//point[@name='F_Sisa_Pinza_Sup']")
id_sup = p_sup.get('id') if p_sup is not None else '701'

line_sup = None
for el in calc.findall('.//line'):
    if (el.get('firstPoint') == id_busto and el.get('secondPoint') == id_sup) or \
       (el.get('firstPoint') == id_sup and el.get('secondPoint') == id_busto):
        line_sup = el
        break

if line_sup is not None:
    idx_insert = list(calc).index(line_sup) + 1
else:
    # If no line element, just put it after p_inf
    idx_insert = list(calc).index(p_inf) + 1

calc.insert(idx_insert, new_point)

for el in calc:
    if el.tag == 'line':
        if el.get('firstPoint') == old_bad_id: el.set('firstPoint', new_unique_id)
        if el.get('secondPoint') == old_bad_id: el.set('secondPoint', new_unique_id)
    if el.tag == 'spline':
        if el.get('point1') == old_bad_id: el.set('point1', new_unique_id)
        if el.get('point4') == old_bad_id: el.set('point4', new_unique_id)
    if el.tag == 'point' and el.get('type') != 'alongLine':
        if el.get('basePoint') == old_bad_id: el.set('basePoint', new_unique_id)

tree.write(filepath, encoding='utf-8', xml_declaration=True)
print("Blusa Cuello Mao: Dart equalization complete.")
