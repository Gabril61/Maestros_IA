import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

# F_Bolsillo_Temp1
p89101 = calc.find('point[@id="89101"]')
if p89101 is not None: p89101.set('length', '5')

# F_Bolsillo_Temp2
p89102 = calc.find('point[@id="89102"]')
if p89102 is not None: p89102.set('length', '5')

# F_Bolsillo_Izq
p89105 = calc.find('point[@id="89105"]')
if p89105 is not None: p89105.set('length', '((@S_CONT_BUSTO / 10) + 4) / 2')

# F_Bolsillo_Der
p89106 = calc.find('point[@id="89106"]')
if p89106 is not None: p89106.set('length', '((@S_CONT_BUSTO / 10) + 4) / 2')

# F_Bolsillo_BotIzq
p89107 = calc.find('point[@id="89107"]')
if p89107 is not None: p89107.set('length', '(@S_CONT_BUSTO / 10) + 6')

# F_Bolsillo_BotDer
p89108 = calc.find('point[@id="89108"]')
if p89108 is not None: p89108.set('length', '(@S_CONT_BUSTO / 10) + 6')


xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Bolsillo más angosto y proporcionado!")
