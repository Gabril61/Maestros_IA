import xml.etree.ElementTree as ET

xml_file = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val"
tree = ET.parse(xml_file)
root = tree.getroot()

calc_node = root.find("draftBlock/calculation")

replacements = {
    "360 - AngleLine_MS_Puno_Cimera_Izq_MS_Codo_Cimera_Izq": "180 - AngleLine_MS_Codo_Cimera_Izq_MS_Puno_Cimera_Izq",
    "360 - AngleLine_MS_Puno_Cimera_Der_MS_Codo_Cimera_Der": "180 - AngleLine_MS_Codo_Cimera_Der_MS_Puno_Cimera_Der",
    "360 - AngleLine_MS_Puno_Bajera_Izq_MS_Codo_Bajera_Izq": "180 - AngleLine_MS_Codo_Bajera_Izq_MS_Puno_Bajera_Izq",
    "360 - AngleLine_MS_Puno_Bajera_Der_MS_Codo_Bajera_Der": "180 - AngleLine_MS_Codo_Bajera_Der_MS_Puno_Bajera_Der"
}

modified = False
for pt in calc_node.findall("point"):
    angle = pt.get("angle")
    if angle in replacements:
        pt.set("angle", replacements[angle])
        modified = True

if modified:
    tree.write(xml_file, encoding="UTF-8", xml_declaration=True)
    print("Fixed angles successfully")
else:
    print("No angles matched to replace")
