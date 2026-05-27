import xml.etree.ElementTree as ET

def redefine_pockets(calc):
    to_remove = []
    for el in calc:
        if el.get('id') in ['90050', '90051', '90052', '90053']:
            to_remove.append(el)
    for el in to_remove:
        calc.remove(el)

    calc.append(ET.Element('point', {'angle': '0', 'basePoint': '2', 'id': '90050', 'length': '11', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Ref', 'showPointName': 'false', 'type': 'endLine'}))
    calc.append(ET.Element('point', {'angle': '90', 'basePoint': '90050', 'id': '90051', 'length': '6', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Sup', 'showPointName': 'true', 'type': 'endLine'}))
    calc.append(ET.Element('point', {'angle': '300', 'basePoint': '90051', 'id': '90052', 'length': '15', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'name': 'F_Bolsillo_Inf', 'showPointName': 'true', 'type': 'endLine'}))
    calc.append(ET.Element('line', {'firstPoint': '90051', 'id': '90053', 'lineColor': 'blue', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '90052'}))

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')
redefine_pockets(calc)
tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Pockets added to Caballero.")
