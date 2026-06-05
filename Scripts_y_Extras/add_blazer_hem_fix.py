import xml.etree.ElementTree as ET
import shutil

val_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
shutil.copy(val_path, val_path + '.backup_redondeo')

tree = ET.parse(val_path)
calc = tree.getroot().find('.//calculation')

# 1. Hide unused buttons
for pt in calc.findall('point'):
    if pt.get('id') in ['11004', '11005']:
        pt.set('length', '0')

# 2. Add Rounded Hem (using unique IDs to avoid conflicts)
# Check if they exist first, just in case
existing_ids = [el.get('id') for el in calc]
if '89001' not in existing_ids:
    p_curva_v = ET.Element('point', {
        'id': '89001', 'name': 'B_Ruedo_Curva_V', 'type': 'alongLine',
        'firstPoint': '15000', 'secondPoint': '11003', 'length': '5',
        'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'showPointName': 'true'
    })
    p_curva_h = ET.Element('point', {
        'id': '89002', 'name': 'B_Ruedo_Curva_H', 'type': 'alongLine',
        'firstPoint': '15000', 'secondPoint': '15001', 'length': '5',
        'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'showPointName': 'true'
    })
    s_curva = ET.Element('spline', {
        'id': '89003', 'color': 'black', 'lineWeight': '0.35', 'penStyle': 'solidLine', 'type': 'simpleInteractive',
        'point1': '89001', 'point4': '89002',
        'angle1': '270', 'angle2': '180',
        'length1': '3', 'length2': '3'
    })

    calc.append(p_curva_v)
    calc.append(p_curva_h)
    calc.append(s_curva)

tree.write(val_path, encoding='UTF-8', xml_declaration=True)
print('Applied rounded hem and hid buttons successfully!')
