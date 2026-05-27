import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Medica_Dama_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# Add line from T_Centro_Cintura (250) to T_Nivel_Largo (218)
new_line = ET.Element('line', {
    'id': '40500',
    'firstPoint': '250',
    'secondPoint': '218',
    'lineColor': 'black',
    'lineType': 'solidLine',
    'lineWeight': '0.35'
})

calc.append(new_line)
tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Back line added to Blouse.")
