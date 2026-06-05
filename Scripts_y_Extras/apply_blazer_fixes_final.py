import xml.etree.ElementTree as ET
import shutil

val_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
shutil.copy(val_path, val_path + '.backup_blazer_final')

tree = ET.parse(val_path)
calc = tree.getroot().find('.//calculation')

# 1. Back Dart Position
for pt in calc.findall('point'):
    if pt.get('name') == 'T_Pinza_Centro':
        pt.set('length', '@S_SEP_BUSTO / 2')

# 2. Front Princess Seam (Sisa) Splines
for el in calc.findall('spline'):
    if el.get('id') == '207':
        el.set('angle1', 'AngleLine_F_APEX_F_Sisa_Pinza_Sup + 165')
        el.set('length1', 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.25')
        el.set('length2', 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.25')
    if el.get('id') == '209':
        el.set('angle1', 'AngleLine_F_APEX_F_Sisa_Pinza_Inf + 165')
        el.set('length1', 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.25')
        el.set('length2', 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.25')

# 3. 1-Button Lapel & Quiebre
for el in calc.findall('line'):
    # Lapel break point
    if el.get('id') == '12040' and el.get('firstPoint') == '11004':
        el.set('firstPoint', '11003')
    # Vertical placket edge
    if el.get('id') == '16002' and el.get('firstPoint') == '11004':
        el.set('firstPoint', '11003')

# 4. Rounded Hem (Canto Redondeado)
# Create new points for the curve
p_curva_v = ET.Element('point', {
    'id': '16003', 'name': 'B_Ruedo_Curva_V', 'type': 'alongLine',
    'firstPoint': '15000', 'secondPoint': '11003', 'length': '4',
    'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'showPointName': 'true'
})
p_curva_h = ET.Element('point', {
    'id': '16004', 'name': 'B_Ruedo_Curva_H', 'type': 'alongLine',
    'firstPoint': '15000', 'secondPoint': '15001', 'length': '4',
    'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'showPointName': 'true'
})
s_curva = ET.Element('spline', {
    'id': '16005', 'color': 'black', 'lineWeight': '0.35', 'penStyle': 'solidLine', 'type': 'simpleInteractive',
    'point1': '16003', 'point4': '16004',
    'angle1': '270', 'angle2': '180',
    'length1': '2.5', 'length2': '2.5'
})

# Insert them at the end of the calculation block
calc.append(p_curva_v)
calc.append(p_curva_h)
calc.append(s_curva)

tree.write(val_path, encoding='UTF-8', xml_declaration=True)
print('Blazer fixes applied successfully!')
