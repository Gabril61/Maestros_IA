import xml.etree.ElementTree as ET

xml_file = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val"
tree = ET.parse(xml_file)
root = tree.getroot()

variables_node = root.find("variables")
if variables_node is None:
    variables_node = ET.SubElement(root, "variables")

def add_var(name, formula, desc):
    for v in variables_node.findall("variable"):
        if v.get("name") == name:
            v.set("formula", formula)
            v.set("description", desc)
            return
    v = ET.SubElement(variables_node, "variable")
    v.set("name", name)
    v.set("formula", formula)
    v.set("description", desc)

add_var("#holgura_biceps", "6", "Holgura para el contorno de biceps")
add_var("#holgura_puno", "8", "Holgura para el contorno de puño")
add_var("#largo_aletilla_efectivo", "12", "Largo efectivo aletilla (despues de coser)")
add_var("#ancho_aletilla", "3", "Ancho de la aletilla")

calc_node = root.find("draftBlock/calculation")

def update_point(name, new_length):
    for pt in calc_node.findall("point"):
        if pt.get("name") == name:
            pt.set("length", new_length)

update_point("MS_Copa_Alto", "(@S_CONT_SISA / 3) + 1")
update_point("MS_Ancho_Cimera_Izq", "((@S_CONT_BICEP + #holgura_biceps) / 4) + 1.5")
update_point("MS_Ancho_Cimera_Der", "((@S_CONT_BICEP + #holgura_biceps) / 4) + 1.5")
update_point("MS_Ancho_Bajera_Izq", "((@S_CONT_BICEP + #holgura_biceps) / 4) - 1.5")
update_point("MS_Ancho_Bajera_Der", "((@S_CONT_BICEP + #holgura_biceps) / 4) - 1.5")
update_point("MS_Codo_Cimera_Izq", "(((@S_CONT_BICEP + #holgura_biceps) / 4) + ((@S_CONT_PUNO + #holgura_puno) / 4)) / 2 + 2")
update_point("MS_Codo_Cimera_Der", "(((@S_CONT_BICEP + #holgura_biceps) / 4) + ((@S_CONT_PUNO + #holgura_puno) / 4)) / 2 + 2")
update_point("MS_Codo_Bajera_Izq", "(((@S_CONT_BICEP + #holgura_biceps) / 4) + ((@S_CONT_PUNO + #holgura_puno) / 4)) / 2 - 1.5")
update_point("MS_Codo_Bajera_Der", "(((@S_CONT_BICEP + #holgura_biceps) / 4) + ((@S_CONT_PUNO + #holgura_puno) / 4)) / 2 - 1.5")
update_point("MS_Puno_Cimera_Izq", "((@S_CONT_PUNO + #holgura_puno) / 4) + 1.5")
update_point("MS_Puno_Cimera_Der", "((@S_CONT_PUNO + #holgura_puno) / 4) + 1.5")
update_point("MS_Puno_Bajera_Izq", "((@S_CONT_PUNO + #holgura_puno) / 4) - 1.5")
update_point("MS_Puno_Bajera_Der", "((@S_CONT_PUNO + #holgura_puno) / 4) - 1.5")

nodes_to_add = [
    {'tag': 'point', 'angle': "270", 'basePoint': "12001", 'id': "89500", 'length': "@D_RUEDO_MANGA", 'mx': "0.1", 'my': "0.1", 'name': "Ext_MS_Largo", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'point', 'angle': "360 - AngleLine_MS_Puno_Cimera_Izq_MS_Codo_Cimera_Izq", 'basePoint': "12014", 'id': "89501", 'length': "@D_RUEDO_MANGA", 'mx': "0.1", 'my': "0.1", 'name': "Ext_MS_Puno_Cimera_Izq", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'point', 'angle': "360 - AngleLine_MS_Puno_Cimera_Der_MS_Codo_Cimera_Der", 'basePoint': "12015", 'id': "89502", 'length': "@D_RUEDO_MANGA", 'mx': "0.1", 'my': "0.1", 'name': "Ext_MS_Puno_Cimera_Der", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'point', 'angle': "360 - AngleLine_MS_Puno_Bajera_Izq_MS_Codo_Bajera_Izq", 'basePoint': "12016", 'id': "89503", 'length': "@D_RUEDO_MANGA", 'mx': "0.1", 'my': "0.1", 'name': "Ext_MS_Puno_Bajera_Izq", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'point', 'angle': "360 - AngleLine_MS_Puno_Bajera_Der_MS_Codo_Bajera_Der", 'basePoint': "12017", 'id': "89504", 'length': "@D_RUEDO_MANGA", 'mx': "0.1", 'my': "0.1", 'name': "Ext_MS_Puno_Bajera_Der", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'line', 'firstPoint': "89500", 'id': "89505", 'lineColor': "black", 'secondPoint': "89501"},
    {'tag': 'line', 'firstPoint': "89500", 'id': "89506", 'lineColor': "black", 'secondPoint': "89502"},
    {'tag': 'line', 'firstPoint': "89501", 'id': "89507", 'lineColor': "black", 'secondPoint': "12014"},
    {'tag': 'line', 'firstPoint': "89502", 'id': "89508", 'lineColor': "black", 'secondPoint': "12015"},
    {'tag': 'line', 'firstPoint': "89503", 'id': "89509", 'lineColor': "blue", 'secondPoint': "12016"},
    {'tag': 'line', 'firstPoint': "89504", 'id': "89510", 'lineColor': "blue", 'secondPoint': "12017"},
    {'tag': 'line', 'firstPoint': "89503", 'id': "89511", 'lineColor': "blue", 'secondPoint': "89504"},
    {'tag': 'point', 'firstPoint': "12015", 'id': "89600", 'length': "#largo_aletilla_efectivo", 'lineColor': "black", 'lineType': "none", 'lineWeight': "0.35", 'mx': "0.1", 'my': "0.1", 'name': "Ale_Cim_Top", 'secondPoint': "12011", 'showPointName': "true", 'type': "alongLine"},
    {'tag': 'point', 'angle': "0", 'basePoint': "89600", 'id': "89601", 'length': "#ancho_aletilla", 'mx': "0.1", 'my': "0.1", 'name': "Ale_Cim_Top_Ext", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'point', 'angle': "0", 'basePoint': "12015", 'id': "89602", 'length': "#ancho_aletilla", 'mx': "0.1", 'my': "0.1", 'name': "Ale_Cim_Puno_Ext", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'point', 'angle': "0", 'basePoint': "89502", 'id': "89603", 'length': "#ancho_aletilla", 'mx': "0.1", 'my': "0.1", 'name': "Ale_Cim_Bot_Ext", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'line', 'firstPoint': "89600", 'id': "89604", 'lineColor': "black", 'secondPoint': "89601"},
    {'tag': 'line', 'firstPoint': "89601", 'id': "89605", 'lineColor': "black", 'secondPoint': "89602"},
    {'tag': 'line', 'firstPoint': "89602", 'id': "89606", 'lineColor': "black", 'secondPoint': "89603"},
    {'tag': 'line', 'firstPoint': "89603", 'id': "89607", 'lineColor': "black", 'secondPoint': "89502"},
    {'tag': 'point', 'firstPoint': "12017", 'id': "89610", 'length': "#largo_aletilla_efectivo", 'lineColor': "blue", 'lineType': "none", 'lineWeight': "0.35", 'mx': "0.1", 'my': "0.1", 'name': "Ale_Baj_Top", 'secondPoint': "12013", 'showPointName': "true", 'type': "alongLine"},
    {'tag': 'point', 'angle': "0", 'basePoint': "89610", 'id': "89611", 'length': "#ancho_aletilla", 'mx': "0.1", 'my': "0.1", 'name': "Ale_Baj_Top_Ext", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'point', 'angle': "0", 'basePoint': "12017", 'id': "89612", 'length': "#ancho_aletilla", 'mx': "0.1", 'my': "0.1", 'name': "Ale_Baj_Puno_Ext", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'point', 'angle': "0", 'basePoint': "89504", 'id': "89613", 'length': "#ancho_aletilla", 'mx': "0.1", 'my': "0.1", 'name': "Ale_Baj_Bot_Ext", 'showPointName': "true", 'type': "endLine"},
    {'tag': 'line', 'firstPoint': "89610", 'id': "89614", 'lineColor': "blue", 'secondPoint': "89611"},
    {'tag': 'line', 'firstPoint': "89611", 'id': "89615", 'lineColor': "blue", 'secondPoint': "89612"},
    {'tag': 'line', 'firstPoint': "89612", 'id': "89616", 'lineColor': "blue", 'secondPoint': "89613"},
    {'tag': 'line', 'firstPoint': "89613", 'id': "89617", 'lineColor': "blue", 'secondPoint': "89504"}
]

existing_ids = set()
for child in calc_node:
    if 'id' in child.attrib:
        existing_ids.add(child.get('id'))

for node_data in nodes_to_add:
    if node_data['id'] not in existing_ids:
        tag = node_data.pop('tag')
        elem = ET.SubElement(calc_node, tag)
        for k, v in node_data.items():
            elem.set(k, v)

ET.indent(tree, space="    ", level=0)
tree.write(xml_file, encoding="UTF-8", xml_declaration=True)
print("Updated successfully")
