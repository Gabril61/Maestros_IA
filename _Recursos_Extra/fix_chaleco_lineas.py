import xml.etree.ElementTree as ET

val_path = r"C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
tree = ET.parse(val_path)
root = tree.getroot()

calculation = root.find('.//calculation')

def add_line(first_point, second_point, id_str, insert_after_id):
    # Check if line already exists
    for el in calculation:
        if el.tag == 'line' and el.attrib.get('firstPoint') == first_point and el.attrib.get('secondPoint') == second_point:
            return False
            
    # Find the index to insert
    index = -1
    for i, el in enumerate(calculation):
        if el.attrib.get('id') == insert_after_id:
            index = i + 1
            break
            
    if index != -1:
        line_el = ET.Element('line', {
            'firstPoint': first_point,
            'id': id_str,
            'lineColor': 'black',
            'lineType': 'none',
            'lineWeight': '0.35',
            'secondPoint': second_point
        })
        calculation.insert(index, line_el)
        print(f"Inserted line {first_point}_{second_point}")
        return True
    return False

# F_Costado_Sisa is usually ID 5, F_Hombro is ID 28
# F_Sisa_Pinza_Sup is ID 701, F_APEX is 14
modified = False
if add_line('28', '5', '19999', '28'):
    modified = True
if add_line('701', '14', '19998', '701'):
    modified = True

if modified:
    tree.write(val_path, encoding="UTF-8", xml_declaration=True)
    print("Archivo guardado con las lineas faltantes.")
else:
    print("No se requirieron modificaciones.")
