import xml.etree.ElementTree as ET
import shutil
import os

val_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val'
smis_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Maestro_Variables_IA.smis'

# Backup
shutil.copy(val_path, val_path + '.backup_final_fixes')
shutil.copy(smis_path, smis_path + '.backup_final_fixes')

# 1. Update SMIS
tree_smis = ET.parse(smis_path)
root_smis = tree_smis.getroot()
bm = root_smis.find('body-measurements')

for m in bm.findall('m'):
    if m.get('name') == '@D_HOLGURA_SUPERIOR':
        m.set('value', '3')
    if m.get('name') == '@D_HOLGURA_INFERIOR':
        m.set('value', '4')

# Check if @D_HOLGURA_CINTURA exists, if not create it
cintura_exists = False
for m in bm.findall('m'):
    if m.get('name') == '@D_HOLGURA_CINTURA':
        m.set('value', '2')
        cintura_exists = True
if not cintura_exists:
    ET.SubElement(bm, 'm', {'full_name': 'Holgura cintura', 'name': '@D_HOLGURA_CINTURA', 'value': '2'})

tree_smis.write(smis_path, encoding='UTF-8', xml_declaration=True)

# 2. Update VAL
tree_val = ET.parse(val_path)
root_val = tree_val.getroot()
calc = root_val.find('.//calculation')

for pt in calc.findall('point'):
    id = pt.get('id')
    name = pt.get('name')
    
    # Holguras de Cintura
    if id in ['1200', '211']:
        pt.set('length', '((@S_CONT_BUSTO + @D_HOLGURA_SUPERIOR) - (@G_CONT_CINTURA + @D_HOLGURA_CINTURA)) / 4 - @D_PINZA_CINT_SUP')
    
    # Sisa Trasera
    if id == '802' and name == 'T_Sisa_Pinza_Inf':
        pt.set('length', '0')
    
    # Manga
    if id == '2026' and name == 'M_A3_Izq':
        pt.set('type', 'endLine')
        pt.set('angle', '180')
        pt.set('basePoint', '2025')
        pt.set('length', '(Line_M_A_M_A1_Real < 35) ? (Line_M_A2_M_F * 0.85) : (Line_M_A2_M_F - (Line_M_A2_M_F - (@S_CONT_PUNO/2)) * ((Line_M_A_M_A1_Real - Line_M_A_M_A2) / (Line_M_A_M_A_Master - Line_M_A_M_A2)))')
        if 'p1Line' in pt.attrib: del pt.attrib['p1Line']
        if 'p2Line' in pt.attrib: del pt.attrib['p2Line']
        
    if id == '2027' and name == 'M_A4_Der':
        pt.set('type', 'endLine')
        pt.set('angle', '0')
        pt.set('basePoint', '2025')
        pt.set('length', '(Line_M_A_M_A1_Real < 35) ? (Line_M_A2_M_T * 0.85) : (Line_M_A2_M_T - (Line_M_A2_M_T - (@S_CONT_PUNO/2)) * ((Line_M_A_M_A1_Real - Line_M_A_M_A2) / (Line_M_A_M_A_Master - Line_M_A_M_A2)))')
        if 'p1Line' in pt.attrib: del pt.attrib['p1Line']
        if 'p2Line' in pt.attrib: del pt.attrib['p2Line']

    # F_Vista_Inf y F_Aletilla_Inf (Corrección de ángulo a 270 exactos)
    if id == '10002' and name == 'F_Aletilla_Inf':
        pt.set('type', 'lineIntersectAxis')
        pt.set('angle', '270')
        pt.set('basePoint', '10001')
        pt.set('p1Line', '301')
        pt.set('p2Line', '303')
        if 'length' in pt.attrib: del pt.attrib['length']
        if 'mx' in pt.attrib: del pt.attrib['mx']
        if 'my' in pt.attrib: del pt.attrib['my']

    if id == '10004' and name == 'F_Vista_Inf':
        pt.set('type', 'lineIntersectAxis')
        pt.set('angle', '270')
        pt.set('basePoint', '10003')
        pt.set('p1Line', '301')
        pt.set('p2Line', '303')
        if 'length' in pt.attrib: del pt.attrib['length']
        if 'mx' in pt.attrib: del pt.attrib['mx']
        if 'my' in pt.attrib: del pt.attrib['my']

    # F_Aletilla_Dobladillo y F_Vista_Dobladillo
    if id == '50100' and name == 'F_Aletilla_Dobladillo':
        pt.set('type', 'lineIntersectAxis')
        pt.set('angle', '270')
        pt.set('basePoint', '10001') # Sigue el eje vertical desde arriba
        pt.set('p1Line', '50003')
        pt.set('p2Line', '50102')
        if 'length' in pt.attrib: del pt.attrib['length']
        if 'mx' in pt.attrib: del pt.attrib['mx']
        if 'my' in pt.attrib: del pt.attrib['my']

    if id == '50101' and name == 'F_Vista_Dobladillo':
        pt.set('type', 'lineIntersectAxis')
        pt.set('angle', '270')
        pt.set('basePoint', '10003') # Sigue el eje vertical desde arriba
        pt.set('p1Line', '50003')
        pt.set('p2Line', '50102')
        if 'length' in pt.attrib: del pt.attrib['length']
        if 'mx' in pt.attrib: del pt.attrib['mx']
        if 'my' in pt.attrib: del pt.attrib['my']

tree_val.write(val_path, encoding='UTF-8', xml_declaration=True)
print("Changes applied successfully!")
