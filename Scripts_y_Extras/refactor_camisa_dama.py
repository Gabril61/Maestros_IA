import xml.etree.ElementTree as ET
import shutil
import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val'
backup_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val.backup'

shutil.copy2(file_path, backup_path)
print(f"Backup created at {backup_path}")

tree = ET.parse(file_path)
root = tree.getroot()

# 1. Update existing Ruedo lengths
ruedo_points = {
    '301': '@G_LARGO_PRENDA - @S_TALLE_TRASERO', # F_Ruedo
    '502': '@G_LARGO_PRENDA - @S_TALLE_TRASERO', # F_Ruedo_Pinza
    '401': '@G_LARGO_PRENDA - @S_TALLE_TRASERO', # T_Ruedo
    '602': '@G_LARGO_PRENDA - @S_TALLE_TRASERO'  # T_Ruedo_Pinza
}

for point in root.findall('.//point'):
    pid = point.get('id')
    if pid in ruedo_points:
        point.set('length', ruedo_points[pid])
        print(f"Updated point {pid} length to {ruedo_points[pid]}")

# 2. Update Splines 207 and 209
for spline in root.findall('.//spline'):
    sid = spline.get('id')
    if sid == '207':
        spline.set('angle1', 'AngleLine_F_Sisa_Pinza_Sup_F_APEX + 10')
        spline.set('length1', 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.3')
        spline.set('angle2', 'AngleLine_F_Sisa_Pinza_Sup_F_APEX + 180')
        spline.set('length2', 'Line_F_Sisa_Pinza_Sup_F_APEX * 0.15')
        print("Updated spline 207")
    elif sid == '209':
        spline.set('angle1', 'AngleLine_F_Sisa_Pinza_Inf_F_APEX - 10')
        spline.set('length1', 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.3')
        spline.set('angle2', 'AngleLine_F_Sisa_Pinza_Inf_F_APEX + 180')
        spline.set('length2', 'Line_F_Sisa_Pinza_Inf_F_APEX * 0.15')
        print("Updated spline 209")

# 3. Add new points
calc = root.find('.//calculation')

def add_point(calc_node, pid, name, base, length, angle="270"):
    elem = ET.Element('point')
    elem.set('id', pid)
    elem.set('name', name)
    elem.set('basePoint', base)
    elem.set('length', length)
    elem.set('angle', angle)
    elem.set('type', 'endLine')
    elem.set('lineColor', 'black')
    elem.set('lineType', 'none')
    elem.set('lineWeight', '0.35')
    elem.set('mx', '0.1')
    elem.set('my', '0.1')
    elem.set('showPointName', 'true')
    calc_node.append(elem)
    print(f"Added point {pid} ({name})")

def add_line(calc_node, lid, p1, p2):
    elem = ET.Element('line')
    elem.set('id', lid)
    elem.set('firstPoint', p1)
    elem.set('secondPoint', p2)
    elem.set('lineColor', 'black')
    elem.set('lineType', 'dashLine')
    elem.set('lineWeight', '0.35')
    calc_node.append(elem)
    print(f"Added line {lid} ({p1} -> {p2})")

# Check if points already exist to prevent duplicates
existing_ids = [p.get('id') for p in root.findall('.//point')]

if '50001' not in existing_ids:
    add_point(calc, '50001', 'F_Cadera_Pinza', '202', '@G_ALTO_CADERA')
    add_point(calc, '50002', 'T_Cadera_Pinza', '213', '@G_ALTO_CADERA')
    add_point(calc, '50003', 'F_Dobladillo', '2', '@G_LARGO_PRENDA - @S_TALLE_TRASERO + @D_RUEDO_PRENDA')
    add_point(calc, '50004', 'T_Dobladillo', '101', '@G_LARGO_PRENDA - @S_TALLE_TRASERO + @D_RUEDO_PRENDA')
    add_point(calc, '50005', 'F_Dobladillo_Pinza', '202', '@G_LARGO_PRENDA - @S_TALLE_TRASERO + @D_RUEDO_PRENDA')
    add_point(calc, '50006', 'T_Dobladillo_Pinza', '213', '@G_LARGO_PRENDA - @S_TALLE_TRASERO + @D_RUEDO_PRENDA')

    add_line(calc, '50011', '501', '50001') # Fin_Pinza -> Cadera_Pinza
    add_line(calc, '50012', '50001', '502') # Cadera_Pinza -> Ruedo_Pinza
    add_line(calc, '50013', '502', '50005') # Ruedo_Pinza -> Dobladillo_Pinza
    
    add_line(calc, '50014', '601', '50002') # Fin_Pinza -> Cadera_Pinza
    add_line(calc, '50015', '50002', '602') # Cadera_Pinza -> Ruedo_Pinza
    add_line(calc, '50016', '602', '50006') # Ruedo_Pinza -> Dobladillo_Pinza
    
    add_line(calc, '50017', '301', '50003') # F_Ruedo -> F_Dobladillo
    add_line(calc, '50018', '401', '50004') # T_Ruedo -> T_Dobladillo

# Pretty print XML (simple indentation)
ET.indent(tree, space="    ", level=0)
tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Changes successfully written to Camisa_Dama_Maestro.val")
