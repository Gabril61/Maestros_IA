import xml.etree.ElementTree as ET
import shutil

val_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
shutil.copy(val_path, val_path + '.backup_blazer')

tree = ET.parse(val_path)
calc = tree.getroot().find('.//calculation')

# 1. Update Width Formulas
for pt in calc.findall('point'):
    id_val = pt.get('id')
    
    # Bust widths
    if id_val in ['4', '103', '5', '104', '6', '105']:
        pt.set('length', '(@S_CONT_BUSTO / 4) + (@D_HOLGURA_SUPERIOR / 4) + 1.25')
        
    # Hip and Hem widths
    if id_val in ['1302', '402', '1303', '403']:
        pt.set('length', '(@G_CONT_CADERA_BAJA / 4) + (@D_HOLGURA_INFERIOR / 4) + 1.0')
        
    # Waist reduction (Costado Real)
    if id_val in ['1200', '211']:
        pt.set('length', '((@S_CONT_BUSTO + @D_HOLGURA_SUPERIOR) - (@G_CONT_CINTURA + @D_HOLGURA_CINTURA)) / 4 + 0.25 - @D_PINZA_CINT_SUP')

    # 2. Back Princess Seam
    if id_val == '802': # T_Sisa_Pinza_Inf
        pt.set('length', '0')

# Create 820 (T_Mitad_Hombro)
p820 = ET.Element('point', {
    'id': '820', 'name': 'T_Mitad_Hombro', 'type': 'alongLine', 
    'firstPoint': '112', 'secondPoint': '117', 'length': 'Line_T_Cuello_Ancho_T_Hombro / 2',
    'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.1', 'my': '0.1', 'showPointName': 'true'
})

idx_117 = -1
for i, el in enumerate(calc):
    if el.get('id') == '117':
        idx_117 = i
        break
calc.insert(idx_117 + 1, p820)

l821 = ET.Element('line', {'id': '821', 'firstPoint': '820', 'secondPoint': '214', 'lineColor': 'black', 'lineType': 'dashLine', 'lineWeight': '0.35'})
l822 = ET.Element('line', {'id': '822', 'firstPoint': '820', 'secondPoint': '215', 'lineColor': 'black', 'lineType': 'dashLine', 'lineWeight': '0.35'})

idx_splines = -1
for i, el in enumerate(calc):
    if el.get('id') == '612':
        idx_splines = i
        break

if idx_splines != -1:
    calc.insert(idx_splines, l821)
    calc.insert(idx_splines + 1, l822)

# Update splines
for el in calc.findall('spline'):
    id_val = el.get('id')
    if id_val == '612':
        el.set('point1', '820')
        el.set('angle1', '270')
        el.set('angle2', '90')
        el.set('length1', 'Line_T_Mitad_Hombro_T_Pinza_P1 * 0.4')
        el.set('length2', 'Line_T_Mitad_Hombro_T_Pinza_P1 * 0.4')
    if id_val == '613':
        el.set('point1', '820')
        el.set('angle1', '270')
        el.set('angle2', '90')
        el.set('length1', 'Line_T_Mitad_Hombro_T_Pinza_P2 * 0.4')
        el.set('length2', 'Line_T_Mitad_Hombro_T_Pinza_P2 * 0.4')
    if id_val == '207':
        el.set('angle2', 'AngleLine_F_APEX_F_Pinza_P1 - 180')
    if id_val == '209':
        el.set('angle2', 'AngleLine_F_APEX_F_Pinza_P2 - 180')

tree.write(val_path, encoding='UTF-8', xml_declaration=True)
print('Blazer updated successfully!')
