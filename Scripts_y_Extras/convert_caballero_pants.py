import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Pantalon_Medico_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

# 1. Update Metadata
desc = tree.getroot().find('description')
if desc is not None:
    desc.text = "Patrón Maestro - Scrub Pantalón Médico Caballero"
notes = tree.getroot().find('notes')
if notes is not None:
    notes.text = "Pantalón Médico (Scrub) para caballero. Estructura Jogger: cintura elástica completa alineada a la cadera, sin pinzas."

# 2. Update Waist Formulas for Elastic (Align to Hip Width)
for p in calc.findall('point'):
    name = p.get('name', '')
    if name == 'F_Guia_Cintura_Cost':
        p.set('length', '(@G_CONT_CADERA_BAJA / 4) - 1')
    elif name == 'T_Guia_Cintura_Cost':
        p.set('length', '(@G_CONT_CADERA_BAJA / 4) + 1')

# 3. Remove Darts
dart_pts = ['T_Pinza_Centro', 'T_Pinza_Punta', 'T_Pinza_P1', 'T_Pinza_P2', 'T_Pinza_Tejadillo']
pts_to_remove = []
pt_ids_to_remove = []

for p in calc.findall('point'):
    if p.get('name') in dart_pts:
        pts_to_remove.append(p)
        pt_ids_to_remove.append(p.get('id'))

for p in pts_to_remove:
    calc.remove(p)

# Remove lines and splines connected to the dart
elements_to_remove = []
for l in calc.findall('line'):
    if l.get('firstPoint') in pt_ids_to_remove or l.get('secondPoint') in pt_ids_to_remove:
        elements_to_remove.append(l)
for s in calc.findall('spline'):
    if s.get('point1') in pt_ids_to_remove or s.get('point4') in pt_ids_to_remove:
        elements_to_remove.append(s)

for el in elements_to_remove:
    calc.remove(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Pants adapted to Scrub Jogger Caballero successfully.")
