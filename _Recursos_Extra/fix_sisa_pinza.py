import xml.etree.ElementTree as ET

filepath = 'c:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val'
tree = ET.parse(filepath)
calc = tree.getroot().find('.//calculation')

p702 = calc.find(".//point[@id='702']")
p702.set('name', 'F_Sisa_Pinza_Inf_Ref')

new_point = ET.Element('point', {
    'id': '50634',
    'name': 'F_Sisa_Pinza_Inf',
    'type': 'alongLine',
    'firstPoint': '160',  # F_Centro_Busto
    'secondPoint': '702', # F_Sisa_Pinza_Inf_Ref
    'length': 'Line_F_Centro_Busto_F_Sisa_Pinza_Sup',
    'lineColor': 'black',
    'lineType': 'none',
    'lineWeight': '0.35'
})

p160 = calc.find(".//point[@id='160']")
index_702 = list(calc).index(p702)
index_160 = list(calc).index(p160)
insert_index = max(index_702, index_160) + 1

calc.insert(insert_index, new_point)

# Add a line connecting the new point to F_Centro_Busto for visual completeness (Line 9992 already does this, but let's check)
# Actually, the user already had lines: Line 9992: F_Centro_Busto -> F_Sisa_Pinza_Inf
# We just need to update the references from 702 to 50634 in lines, splines, etc.
for el in calc:
    if el.tag == 'line':
        if el.get('firstPoint') == '702': el.set('firstPoint', '50634')
        if el.get('secondPoint') == '702': el.set('secondPoint', '50634')
    if el.tag == 'spline':
        if el.get('point1') == '702': el.set('point1', '50634')
        if el.get('point4') == '702': el.set('point4', '50634')
    if el.tag == 'point' and el.get('type') != 'alongLine':
        if el.get('basePoint') == '702': el.set('basePoint', '50634')

# Save directly over the original file
tree.write(filepath, encoding='utf-8', xml_declaration=True)
print("Dart equalization complete. F_Sisa_Pinza_Inf length is now exactly tied to F_Sisa_Pinza_Sup.")
