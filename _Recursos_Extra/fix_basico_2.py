import xml.etree.ElementTree as ET

def fix_basico():
    file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    ET.register_namespace('', '')
    tree = ET.parse(file_path)
    root = tree.getroot()
    calc = root.find(".//calculation")

    # 1. Eliminar Fósiles (136, 137, 9001, 9005)
    to_delete = {"136", "137", "9001", "9005"}
    elements_to_remove = []
    for el in calc:
        if el.get("id") in to_delete:
            elements_to_remove.append(el)
    for el in elements_to_remove:
        calc.remove(el)

    # 2. Arreglar Sisa (107, 207)
    for el in calc:
        if el.get("id") in ("107", "207"):
            el.set("length", "(@S_CONT_SISA / 2) + (#holgura_sisa / 2)")

    # 3. Arreglar Entalle Espalda (250)
    for el in calc:
        if el.get("id") == "250":
            el.set("length", "1.5")

    # 4. Arreglar Manga (1001)
    for el in calc:
        if el.get("id") == "1001":
            el.set("length", "@S_LARGO_MANGA + #ajuste_largo_manga")

    # 5. Agregar #ajuste_largo_manga a variables
    vars_node = root.find("variables")
    if vars_node is not None:
        # Check if it already exists
        exists = False
        for v in vars_node:
            if v.get("name") == "#ajuste_largo_manga":
                exists = True
        if not exists:
            ET.SubElement(vars_node, "variable", {"name": "#ajuste_largo_manga", "formula": "0", "description": "Ajuste al largo de manga (+ o -)"})

    # 6. Agregar Extensión de Ruedo
    # Ext_F_Nivel_Largo (de 118)
    # Ext_F_Costado_Ruedo (de 121)
    # Ext_T_Costado_Ruedo (de 221)
    # Ext_T_Nivel_Largo (de 218)
    # Base points: 118, 121, 221, 218
    # Insert them before the ALERTA point or just append before ALERTA
    
    # We find ALERTA point, remove it, append everything, append ALERTA
    alerta_el = None
    for el in calc:
        if el.get("name") == "ALERTA_SISA_ESTRECHA":
            alerta_el = el
            break
            
    if alerta_el is not None:
        calc.remove(alerta_el)

    p1 = ET.Element("point", {"angle": "270", "basePoint": "118", "id": "40201", "length": "#ruedo_prenda", "mx": "0.1", "my": "0.1", "name": "Ext_F_Nivel_Largo", "showPointName": "true", "type": "endLine"})
    p2 = ET.Element("point", {"angle": "270", "basePoint": "121", "id": "40202", "length": "#ruedo_prenda", "mx": "0.1", "my": "0.1", "name": "Ext_F_Costado_Ruedo", "showPointName": "true", "type": "endLine"})
    p3 = ET.Element("point", {"angle": "270", "basePoint": "221", "id": "40203", "length": "#ruedo_prenda", "mx": "0.1", "my": "0.1", "name": "Ext_T_Costado_Ruedo", "showPointName": "true", "type": "endLine"})
    p4 = ET.Element("point", {"angle": "270", "basePoint": "218", "id": "40204", "length": "#ruedo_prenda", "mx": "0.1", "my": "0.1", "name": "Ext_T_Nivel_Largo", "showPointName": "true", "type": "endLine"})
    
    l1 = ET.Element("line", {"firstPoint": "118", "id": "40301", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40201"})
    l2 = ET.Element("line", {"firstPoint": "121", "id": "40302", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40202"})
    l3 = ET.Element("line", {"firstPoint": "221", "id": "40303", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40203"})
    l4 = ET.Element("line", {"firstPoint": "218", "id": "40304", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40204"})
    
    l5 = ET.Element("line", {"firstPoint": "40201", "id": "40306", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.7", "secondPoint": "40202"})
    l6 = ET.Element("line", {"firstPoint": "40203", "id": "40307", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.7", "secondPoint": "40204"})

    for ext_el in [p1, p2, p3, p4, l1, l2, l3, l4, l5, l6]:
        calc.append(ext_el)

    if alerta_el is not None:
        calc.append(alerta_el)

    tree.write(file_path, encoding="UTF-8", xml_declaration=True)
    print("Modificaciones ejecutadas exitosamente.")

if __name__ == "__main__":
    fix_basico()
