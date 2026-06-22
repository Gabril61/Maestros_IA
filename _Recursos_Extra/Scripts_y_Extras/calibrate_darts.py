import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Add missing lines for F_APEX to F_Pinza_P1 / F_Pinza_P2 if they don't exist
# They already exist as 208 and 210, so AngleLine_F_APEX_F_Pinza_P1 is safe.

for spline in calc.findall('spline'):
    # 2. Fix Front Splines 207 and 209 (Connect to 14, use Blazer formulas)
    if spline.get('id') == '207':
        spline.set('point4', '14')
        spline.set('angle1', 'AngleLine_F_APEX_F_Sisa_Pinza_Sup + 165')
        spline.set('angle2', 'AngleLine_F_APEX_F_Pinza_P1 - 180')
        spline.set('length1', 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.25')
        spline.set('length2', 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.25')
    elif spline.get('id') == '209':
        spline.set('point4', '14')
        spline.set('angle1', 'AngleLine_F_APEX_F_Sisa_Pinza_Inf + 165')
        spline.set('angle2', 'AngleLine_F_APEX_F_Pinza_P2 - 180')
        spline.set('length1', 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.25')
        spline.set('length2', 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.25')
        
    # 3. Fix Back Splines 612 and 613 (Disconnect from Apex 610, connect 800 to Waist)
    elif spline.get('id') == '612':
        spline.set('point1', '800')  # 800 is T_Hombro_Medio in this file
        spline.set('point4', '214')  # T_Pinza_P1
        spline.set('angle1', '270')
        spline.set('angle2', '90')
        spline.set('length1', 'Line_T_Hombro_Medio_T_Pinza_P1 * 0.4')
        spline.set('length2', 'Line_T_Hombro_Medio_T_Pinza_P1 * 0.4')
    elif spline.get('id') == '613':
        spline.set('point1', '800')
        spline.set('point4', '215')  # T_Pinza_P2
        spline.set('angle1', '270')
        spline.set('angle2', '90')
        spline.set('length1', 'Line_T_Hombro_Medio_T_Pinza_P2 * 0.4')
        spline.set('length2', 'Line_T_Hombro_Medio_T_Pinza_P2 * 0.4')

# We also need to ensure Line_T_Hombro_Medio_T_Pinza_P1 and P2 exist!
# If they don't exist, AngleLine and Line functions will fail.
# Let's create invisible lines 800 to 214 and 800 to 215 just to be safe.
line_back_p1 = ET.Element('line', {'firstPoint': '800', 'id': '9993', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'secondPoint': '214'})
line_back_p2 = ET.Element('line', {'firstPoint': '800', 'id': '9994', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'secondPoint': '215'})

for i, elem in enumerate(calc):
    if elem.get('id') == '613':
        calc.insert(i + 1, line_back_p1)
        calc.insert(i + 2, line_back_p2)
        break

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Darts calibration applied!")
