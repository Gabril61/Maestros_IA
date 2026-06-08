import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()

calc = root.find('.//calculation')

for spline in calc.findall('spline'):
    if spline.get('id') == '207':
        # angle1="AngleLine_F_Sisa_Pinza_Sup_F_APEX+15"
        spline.set('angle1', 'AngleLine_F_APEX_F_Sisa_Pinza_Sup + 180 + 15')
        # angle2="AngleLine_F_Sisa_Pinza_Sup_F_APEX + 180 - 15"
        spline.set('angle2', 'AngleLine_F_APEX_F_Sisa_Pinza_Sup - 15')
        # length1="Line_F_Sisa_Pinza_Sup_F_APEX * 0.4"
        spline.set('length1', 'Line_F_APEX_F_Sisa_Pinza_Sup * 0.4')
        spline.set('length2', 'Line_F_APEX_F_Sisa_Pinza_Sup * 0.4')
        
    elif spline.get('id') == '209':
        # angle1="AngleLine_F_Sisa_Pinza_Inf_F_APEX-15"
        spline.set('angle1', 'AngleLine_F_APEX_F_Sisa_Pinza_Inf + 180 - 15')
        # angle2="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 180 + 15"
        spline.set('angle2', 'AngleLine_F_APEX_F_Sisa_Pinza_Inf + 15')
        # length1="Line_F_Sisa_Pinza_Inf_F_APEX * 0.4"
        spline.set('length1', 'Line_F_APEX_F_Sisa_Pinza_Inf * 0.4')
        spline.set('length2', 'Line_F_APEX_F_Sisa_Pinza_Inf * 0.4')

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Spline direction formulas fixed!")
