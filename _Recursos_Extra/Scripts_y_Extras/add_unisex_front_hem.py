import xml.etree.ElementTree as ET
import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val'

tree = ET.parse(file_path)
calc = tree.getroot().find('draftBlock/calculation')

pts = [
    {'id': '31011', 'name': 'F_Solapa_Doblez_Bot', 'base': '10002'},
    {'id': '31012', 'name': 'V_Doblez_Bot_Doblez_Extremo', 'base': '3004'}
]

for pt in pts:
    el = ET.Element('point', {
        'id': pt['id'],
        'name': pt['name'],
        'type': 'endLine',
        'basePoint': pt['base'],
        'angle': '270',
        'length': '3',
        'lineColor': 'black',
        'lineType': 'none'
    })
    calc.append(el)

lines = [
    {'id': '31013', 'first': '3004', 'second': '31012', 'color': 'blue'},
    {'id': '31014', 'first': '10002', 'second': '31011', 'color': 'blue'},
    {'id': '31015', 'first': '31012', 'second': '31011', 'color': 'black'},
    {'id': '31016', 'first': '31011', 'second': '31000', 'color': 'black'},
    {'id': '31017', 'first': '31000', 'second': '31001', 'color': 'black'}
]

for ln in lines:
    el = ET.Element('line', {
        'id': ln['id'],
        'firstPoint': ln['first'],
        'secondPoint': ln['second'],
        'lineColor': ln['color'],
        'lineType': 'solidLine'
    })
    calc.append(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Added front hem extension to Unisex!")
