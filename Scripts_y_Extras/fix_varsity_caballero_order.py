import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Find the elements to move
ids_to_move = ['80001', '80002', '80003', '80004', '80005', '80006']
elements_to_move = []

for el in list(calc):
    if el.get('id') in ids_to_move:
        elements_to_move.append(el)
        calc.remove(el)

# Find insertion index (after 120, which is around 76)
insert_index = 0
for i, el in enumerate(list(calc)):
    if el.get('id') == '120':
        insert_index = i + 1
        break

# Insert elements at correct position
for el in reversed(elements_to_move):
    calc.insert(insert_index, el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Calculation block reordered correctly.")
