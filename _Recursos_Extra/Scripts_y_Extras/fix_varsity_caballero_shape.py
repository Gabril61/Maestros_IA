import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# 1. Fix Side Seam Boxiness (Straight vertical side seams)
# Get the formula for F_Costado_Sisa
f_sisa_formula = None
t_sisa_formula = None
for p in calc.findall('point'):
    if p.get('name') == 'F_Costado_Sisa':
        f_sisa_formula = p.get('length')
    elif p.get('name') == 'T_Costado_Sisa':
        t_sisa_formula = p.get('length')

pts_to_straighten_f = ['F_Costado_Cintura', 'F_Costado_Cadera_Temp', 'F_Costado_Ruedo_Temp']
pts_to_straighten_t = ['T_Costado_Cintura', 'T_Costado_Cadera', 'T_Costado_Ruedo']

for p in calc.findall('point'):
    if p.get('name') in pts_to_straighten_f:
        p.set('length', f_sisa_formula)
    elif p.get('name') in pts_to_straighten_t:
        p.set('length', t_sisa_formula)
        
    # Also fix Costado_Real which is sometimes an offset
    if p.get('name') in ['F_Costado_Real', 'T_Costado_Real']:
        p.set('length', '0')  # No waist suppression!

# 2 & 3. Fix Armhole Splines (Smooth "J" curve)
for s in calc.findall('spline'):
    if s.get('id') == '80001':
        s.set('angle1', 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa')
        # Tweak control point lengths for smoother curve
        s.set('length1', 'Line_F_Ancho_Pecho_F_Costado_Sisa * 0.3')
        s.set('length2', 'Line_F_Ancho_Pecho_F_Costado_Sisa * 0.4')
    elif s.get('id') == '80002':
        s.set('angle1', 'AngleLine_T_Ancho_Espalda_T_Costado_Sisa')
        s.set('length1', 'Line_T_Ancho_Espalda_T_Costado_Sisa * 0.3')
        s.set('length2', 'Line_T_Ancho_Espalda_T_Costado_Sisa * 0.4')

# 4. Remove curvy side seam splines and replace with straight lines
splines_to_remove = []
for s in calc.findall('spline'):
    # Check if spline connects side points (Costado)
    # E.g. F_Costado_Sisa to F_Costado_Cintura etc
    # Actually, we don't know the exact IDs, but we can look for splines involving Costado_Real
    if s.get('id') in ['307', '407']:
        splines_to_remove.append(s)

for s in splines_to_remove:
    calc.remove(s)
    
# We will just let the user connect the side seam with lines in Details mode, or draw them:
# F_Costado_Sisa (5) to F_Costado_Cintura (6) to F_Costado_Ruedo (303)
# T_Costado_Sisa (104) to T_Costado_Cintura (105) to T_Costado_Ruedo (403)
calc.append(ET.Element('line', {'firstPoint': '5', 'id': '90021', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '6'}))
calc.append(ET.Element('line', {'firstPoint': '6', 'id': '90022', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '303'}))
calc.append(ET.Element('line', {'firstPoint': '104', 'id': '90023', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '105'}))
calc.append(ET.Element('line', {'firstPoint': '105', 'id': '90024', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.7', 'secondPoint': '403'}))


tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Side seams straightened and armhole splines smoothed.")
