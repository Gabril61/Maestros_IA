import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val'

tree = ET.parse(file_path)
root = tree.getroot()

# Add a new draft block for the Cuff (Puno_Ejecutivo)
cuff_draft = ET.Element('draftBlock', {'name': 'Puno_Ejecutivo'})
calc = ET.SubElement(cuff_draft, 'calculation')

# Base points for the Cuff (Puño)
points = [
    # Origin
    {'id': '10300', 'type': 'single', 'name': 'P_Origen', 'x': '150', 'y': '30', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    # Alto del puño (6 cm)
    {'id': '10301', 'type': 'endLine', 'name': 'P_Alto', 'basePoint': '10300', 'angle': '270', 'length': '6', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    # Largo del puño (Contorno de puño + 2 cm de cruce + 2 cm de costura si es necesario, asumiremos @S_CONT_PUNO + 4 de holgura/cruce)
    {'id': '10302', 'type': 'endLine', 'name': 'P_Largo', 'basePoint': '10300', 'angle': '0', 'length': '@S_CONT_PUNO + 4', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
    # Rectángulo
    {'id': '10303', 'type': 'endLine', 'name': 'P_Rectangulo', 'basePoint': '10302', 'angle': '270', 'length': '6', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'},
]

for p in points:
    ET.SubElement(calc, 'point', p)

# Lines
lines = [
    {'id': '10310', 'firstPoint': '10300', 'secondPoint': '10301', 'lineColor': 'black'},
    {'id': '10311', 'firstPoint': '10300', 'secondPoint': '10302', 'lineColor': 'black'},
    {'id': '10312', 'firstPoint': '10301', 'secondPoint': '10303', 'lineColor': 'black'},
    {'id': '10313', 'firstPoint': '10302', 'secondPoint': '10303', 'lineColor': 'black'},
]
for l in lines:
    ET.SubElement(calc, 'line', l)

ET.SubElement(cuff_draft, 'modeling')
ET.SubElement(cuff_draft, 'pieces')

root.append(cuff_draft)

# Write output
tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Cuff block added successfully!")
