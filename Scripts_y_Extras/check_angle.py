import xml.etree.ElementTree as ET

file_path = 'Camisa_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('.//calculation')

s207 = None
for s in calc.findall('.//spline'):
    if s.get('id') == '207':
        s207 = s
        break

print('207 angle1:', s207.get('angle1'))
print('207 angle2:', s207.get('angle2'))

s209 = None
for s in calc.findall('.//spline'):
    if s.get('id') == '209':
        s209 = s
        break

print('209 angle1:', s209.get('angle1'))
print('209 angle2:', s209.get('angle2'))
