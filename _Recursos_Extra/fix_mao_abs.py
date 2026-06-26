import xml.etree.ElementTree as ET

filepath = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Update the elevation point
p_base = calc.find(".//point[@name='CM_Centro_Frente_Base']")
if p_base is not None and p_base.get('length') == '1.5':
    p_base.set('length', '#elevacion_cuello_mao')
    print("Updated CM_Centro_Frente_Base to use #elevacion_cuello_mao")

# 2. Add the increment if it doesn't exist
increments = root.find('.//increments')
if increments is None:
    # insert before draw
    increments = ET.Element('increments')
    draw_idx = list(root).index(root.find('.//draw'))
    root.insert(draw_idx, increments)

found_inc = False
for inc in increments.findall('increment'):
    if inc.get('name') == '#elevacion_cuello_mao':
        found_inc = True
        break

if not found_inc:
    new_inc = ET.Element('increment', {
        'name': '#elevacion_cuello_mao',
        'formula': '1.5',
        'description': 'Elevacion frontal del cuello mao'
    })
    increments.append(new_inc)
    print("Added #elevacion_cuello_mao to increments.")

tree.write(filepath, encoding='utf-8', xml_declaration=True)
print("Done modifying Cuello Mao.")
