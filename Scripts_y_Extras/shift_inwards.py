import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

p701 = calc.find('point[@id="701"]')
if p701 is not None:
    p701.set('angle', 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa - 15')

p702 = calc.find('point[@id="702"]')
if p702 is not None:
    p702.set('angle', 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa - 15')

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Puntos desplazados hacia adentro!")
