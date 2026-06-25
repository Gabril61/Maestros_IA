import xml.etree.ElementTree as ET

val_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(val_path)
root = tree.getroot()
calc = root.find('.//calculation')

# Helper to find max ID
max_id = max([int(e.attrib.get('id', 0)) for e in root.iter() if 'id' in e.attrib])
def next_id():
    global max_id
    max_id += 1
    return str(max_id)

# 1. Add Hem Extensions for Darts
dart_points = ['F_Pinza_Ruedo_Der', 'F_Pinza_Ruedo_Izq', 'T_Pinza_Ruedo_Der', 'T_Pinza_Ruedo_Izq']
for dp_name in dart_points:
    dp = calc.find(f".//point[@name='{dp_name}']")
    if dp is not None:
        dp_id = dp.attrib.get('id')
        ext_id = next_id()
        ET.SubElement(calc, 'point', {
            'id': ext_id, 
            'name': 'Ext_' + dp_name, 
            'type': 'endLine', 
            'basePoint': dp_id, 
            'angle': '270', 
            'length': '#ruedo_prenda', 
            'mx': '0', 'my': '0'
        })
        ET.SubElement(calc, 'line', {
            'id': next_id(), 
            'firstPoint': dp_id, 
            'secondPoint': ext_id
        })

# 2. Remove Pocket Design, keep only mouth
b_inf_der = calc.find(".//point[@name='B_Inf_Der']")
b_inf_izq = calc.find(".//point[@name='B_Inf_Izq']")
if b_inf_der is not None: calc.remove(b_inf_der)
if b_inf_izq is not None: calc.remove(b_inf_izq)

# Remove lines related to the bottom of the pocket
# We only want to keep the line between B_Sup_Der and B_Sup_Izq
b_sup_der = calc.find(".//point[@name='B_Sup_Der']")
b_sup_izq = calc.find(".//point[@name='B_Sup_Izq']")
b_sup_der_id = b_sup_der.attrib.get('id') if b_sup_der is not None else None
b_sup_izq_id = b_sup_izq.attrib.get('id') if b_sup_izq is not None else None

for l in calc.findall('.//line'):
    p1 = l.attrib.get('firstPoint')
    p2 = l.attrib.get('secondPoint')
    if (p1 == b_sup_der_id and p2 == b_sup_izq_id) or (p2 == b_sup_der_id and p1 == b_sup_izq_id):
        pass # Keep the mouth line
    elif b_inf_der is not None and (p1 == b_inf_der.attrib.get('id') or p2 == b_inf_der.attrib.get('id')):
        calc.remove(l)
    elif b_inf_izq is not None and (p1 == b_inf_izq.attrib.get('id') or p2 == b_inf_izq.attrib.get('id')):
        calc.remove(l)

tree.write(val_path, encoding='UTF-8', xml_declaration=True)
print("Detalles corregidos exitosamente.")
