import xml.etree.ElementTree as ET

tree = ET.parse('c:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val')
calc = tree.getroot().find('.//calculation')

p702 = calc.find(".//point[@id='702']")
p702.set('name', 'F_Sisa_Pinza_Inf_Ref')

# Add the new F_Sisa_Pinza_Inf
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

# We must insert this point AFTER 702 and 160, but BEFORE it's used in Splines and Lines.
# It is used in Spline 50116, Spline 50209, Line 9992, Line 9981.
# Let's find the index of 702.
index_702 = list(calc).index(p702)

# Wait, F_Centro_Busto (160) is created at index:
p160 = calc.find(".//point[@id='160']")
index_160 = list(calc).index(p160)

insert_index = max(index_702, index_160) + 1

calc.insert(insert_index, new_point)

# Now we must update any reference to F_Sisa_Pinza_Inf in Splines/Lines to use 50634 if it references id '702'
for el in calc:
    if el.tag == 'line':
        if el.get('firstPoint') == '702': el.set('firstPoint', '50634')
        if el.get('secondPoint') == '702': el.set('secondPoint', '50634')
    if el.tag == 'spline':
        if el.get('point1') == '702': el.set('point1', '50634')
        if el.get('point4') == '702': el.set('point4', '50634')
    if el.tag == 'point' and el.get('type') != 'alongLine':
        if el.get('basePoint') == '702': el.set('basePoint', '50634')

tree.write('c:/Users/Ricx18/Desktop/Maestros_IA/_Recursos_Extra/test_fix.val', encoding='utf-8', xml_declaration=True)
print("Done writing test file.")
