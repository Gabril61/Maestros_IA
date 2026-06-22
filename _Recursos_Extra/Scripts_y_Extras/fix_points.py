import xml.etree.ElementTree as ET

file_path = "Blazer_Dama_Maestro.val"
tree = ET.parse(file_path)
root = tree.getroot()

calculation_node = None
for draft in root.findall('.//draftBlock'):
    if draft.get('name') == 'Corpino_y_Manga':
        calculation_node = draft.find('calculation')
        break

# Find where to insert them. Right before line 30033.
insert_idx = -1
for i, node in enumerate(list(calculation_node)):
    if node.get('id') == '30033':
        insert_idx = i
        break

if insert_idx != -1:
    pt1 = ET.Element('point', angle="90", basePoint="30011", curve="12020", id="30031", lineColor="black", lineType="none", mx="0.1", my="0.1", name="Copa_Frente_Pico", showPointName="true", type="curveIntersectAxis")
    pt2 = ET.Element('point', angle="0", basePoint="12007", id="30032", length="0", lineColor="black", lineType="none", mx="0.1", my="0.1", name="Copa_Espalda_Pico", showPointName="true", type="endLine")
    calculation_node.insert(insert_idx, pt1)
    calculation_node.insert(insert_idx + 1, pt2)

tree.write(file_path, encoding="utf-8", xml_declaration=True)
print("Points restored correctly.")
