import xml.etree.ElementTree as ET
filepath = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(filepath)
s = tree.getroot().find('.//spline[@id="50621"]')
print('length1:', s.get('length1'))
print('length2:', s.get('length2'))
