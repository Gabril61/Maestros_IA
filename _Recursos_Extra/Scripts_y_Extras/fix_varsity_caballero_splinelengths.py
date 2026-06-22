import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Insert the missing lines so the spline handle formulas work
new_line_f = ET.Element('line', {'firstPoint': '31', 'id': '80011', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'secondPoint': '5'})
new_line_t = ET.Element('line', {'firstPoint': '120', 'id': '80012', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'secondPoint': '104'})

# Find the splines and insert these lines just before them
insert_index = 0
for i, el in enumerate(list(calc)):
    if el.get('id') == '80001':
        insert_index = i
        break

calc.insert(insert_index, new_line_f)
calc.insert(insert_index + 1, new_line_t)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Invisible lines added for spline handles.")
