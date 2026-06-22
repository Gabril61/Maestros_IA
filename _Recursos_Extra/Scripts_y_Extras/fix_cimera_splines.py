import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# 1. Make 12020 and 12022 invisible
for cid in ['12020', '12022']:
    sp = calculation.find(f".//*[@id='{cid}']")
    if sp is not None:
        sp.set('lineType', 'none')

# 2. Add invisible reference lines
lines = [
    ET.Element('line', {'id': '13101', 'firstPoint': '30031', 'secondPoint': '12000', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35'}),
    ET.Element('line', {'id': '13102', 'firstPoint': '30032', 'secondPoint': '12000', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35'})
]

# 3. Add explicit Cimera splines
splines = [
    ET.Element('spline', {
        'id': '13001', 'type': 'simpleInteractive', 'point1': '12000', 'point4': '30031',
        'angle1': '180', 'angle2': 'AngleLine_Copa_Frente_Pico_MS_Origen - 15',
        'length1': 'Line_Copa_Frente_Pico_MS_Origen * 0.4', 'length2': 'Line_Copa_Frente_Pico_MS_Origen * 0.4',
        'color': 'black', 'lineWeight': '0.35', 'penStyle': 'solidLine'
    }),
    ET.Element('spline', {
        'id': '13002', 'type': 'simpleInteractive', 'point1': '12000', 'point4': '30032',
        'angle1': '0', 'angle2': 'AngleLine_Copa_Espalda_Pico_MS_Origen + 15',
        'length1': 'Line_Copa_Espalda_Pico_MS_Origen * 0.4', 'length2': 'Line_Copa_Espalda_Pico_MS_Origen * 0.4',
        'color': 'black', 'lineWeight': '0.35', 'penStyle': 'solidLine'
    })
]

for el in lines + splines:
    calculation.append(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Explicit Cimera splines created for perimeter extraction.")
