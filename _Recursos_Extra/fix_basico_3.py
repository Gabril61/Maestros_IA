import xml.etree.ElementTree as ET

def fix_basico():
    file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    ET.register_namespace('', '')
    tree = ET.parse(file_path)
    root = tree.getroot()
    calc = root.find(".//calculation")

    # 1. Agregar #ajuste_largo_prenda a variables si no existe
    vars_node = root.find("variables")
    if vars_node is not None:
        exists = False
        for v in vars_node:
            if v.get("name") == "#ajuste_largo_prenda":
                exists = True
        if not exists:
            ET.SubElement(vars_node, "variable", {"name": "#ajuste_largo_prenda", "formula": "0", "description": "Ajuste al largo total (+ o -)"})

    # 2. Eliminar la extensión de ruedo fallida
    to_delete = {"40201", "40202", "40203", "40204", "40301", "40302", "40303", "40304", "40306", "40307"}
    elements_to_remove = []
    for el in calc:
        if el.get("id") in to_delete:
            elements_to_remove.append(el)
    for el in elements_to_remove:
        calc.remove(el)

    # 3. Mover ALERTA_SISA_ESTRECHA
    alerta_el = None
    for el in calc:
        if el.get("name") == "ALERTA_SISA_ESTRECHA":
            alerta_el = el
            break
            
    if alerta_el is not None:
        calc.remove(alerta_el)

    # FRONT CLIENT LENGTH & EXTENSION
    # F_Largo_Cliente_Ref (base=100)
    p_f_ref = ET.Element("point", {"angle": "270", "basePoint": "100", "id": "40401", "length": "@S_TALLE_DELANTERO + 25 + #ajuste_largo_prenda", "mx": "0.1", "my": "0.1", "name": "F_Largo_Cliente_Ref", "showPointName": "true", "type": "endLine"})
    p_f_temp = ET.Element("point", {"angle": "0", "basePoint": "40401", "id": "40402", "length": "50", "mx": "0.1", "my": "0.1", "name": "F_Largo_Temp", "showPointName": "false", "type": "endLine", "lineType": "none"})
    # F_Costado_Cliente (Intersect 119-121 with 40401-40402)
    p_f_costado = ET.Element("point", {"id": "40403", "mx": "0.1", "my": "0.1", "name": "F_Costado_Cliente", "p1Line1": "119", "p1Line2": "121", "p2Line1": "40401", "p2Line2": "40402", "showPointName": "true", "type": "lineIntersect"})
    
    l_f_bottom = ET.Element("line", {"firstPoint": "40401", "id": "40404", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40403"})
    l_f_side = ET.Element("line", {"firstPoint": "121", "id": "40405", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40403"})
    
    # Extensions
    e_f_ref = ET.Element("point", {"angle": "270", "basePoint": "40401", "id": "40406", "length": "#ruedo_prenda", "mx": "0.1", "my": "0.1", "name": "Ext_F_Largo_Cliente", "showPointName": "true", "type": "endLine"})
    e_f_costado = ET.Element("point", {"angle": "540 - AngleLine_F_Costado_Cintura_F_Costado_Ruedo", "basePoint": "40403", "id": "40407", "length": "#ruedo_prenda", "mx": "0.1", "my": "0.1", "name": "Ext_F_Costado_Cliente", "showPointName": "true", "type": "endLine"})
    
    l_ef_bottom = ET.Element("line", {"firstPoint": "40406", "id": "40408", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.7", "secondPoint": "40407"})
    l_ef_c = ET.Element("line", {"firstPoint": "40401", "id": "40409", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40406"})
    l_ef_s = ET.Element("line", {"firstPoint": "40403", "id": "40410", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40407"})

    # BACK CLIENT LENGTH & EXTENSION
    # T_Largo_Cliente_Ref (base=200)
    p_t_ref = ET.Element("point", {"angle": "270", "basePoint": "200", "id": "40501", "length": "@S_TALLE_TRASERO + 25 + #ajuste_largo_prenda", "mx": "0.1", "my": "0.1", "name": "T_Largo_Cliente_Ref", "showPointName": "true", "type": "endLine"})
    p_t_temp = ET.Element("point", {"angle": "0", "basePoint": "40501", "id": "40502", "length": "50", "mx": "0.1", "my": "0.1", "name": "T_Largo_Temp", "showPointName": "false", "type": "endLine", "lineType": "none"})
    # T_Centro_Cliente (Intersect 250-218 with 40501-40502)
    p_t_centro = ET.Element("point", {"id": "40503", "mx": "0.1", "my": "0.1", "name": "T_Centro_Cliente", "p1Line1": "250", "p1Line2": "218", "p2Line1": "40501", "p2Line2": "40502", "showPointName": "true", "type": "lineIntersect"})
    # T_Costado_Cliente (Intersect 219-221 with 40501-40502)
    p_t_costado = ET.Element("point", {"id": "40504", "mx": "0.1", "my": "0.1", "name": "T_Costado_Cliente", "p1Line1": "219", "p1Line2": "221", "p2Line1": "40501", "p2Line2": "40502", "showPointName": "true", "type": "lineIntersect"})
    
    l_t_bottom = ET.Element("line", {"firstPoint": "40503", "id": "40505", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40504"})
    l_t_center = ET.Element("line", {"firstPoint": "218", "id": "40506", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40503"})
    l_t_side = ET.Element("line", {"firstPoint": "221", "id": "40507", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40504"})

    # Extensions
    e_t_centro = ET.Element("point", {"angle": "540 - AngleLine_T_Centro_Cintura_T_Nivel_Largo", "basePoint": "40503", "id": "40508", "length": "#ruedo_prenda", "mx": "0.1", "my": "0.1", "name": "Ext_T_Centro_Cliente", "showPointName": "true", "type": "endLine"})
    e_t_costado = ET.Element("point", {"angle": "540 - AngleLine_T_Costado_Cintura_T_Costado_Ruedo", "basePoint": "40504", "id": "40509", "length": "#ruedo_prenda", "mx": "0.1", "my": "0.1", "name": "Ext_T_Costado_Cliente", "showPointName": "true", "type": "endLine"})
    
    l_et_bottom = ET.Element("line", {"firstPoint": "40508", "id": "40510", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.7", "secondPoint": "40509"})
    l_et_c = ET.Element("line", {"firstPoint": "40503", "id": "40511", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40508"})
    l_et_s = ET.Element("line", {"firstPoint": "40504", "id": "40512", "lineColor": "black", "lineType": "solidLine", "lineWeight": "0.35", "secondPoint": "40509"})

    front_elements = [p_f_ref, p_f_temp, p_f_costado, l_f_bottom, l_f_side, e_f_ref, e_f_costado, l_ef_bottom, l_ef_c, l_ef_s]
    back_elements = [p_t_ref, p_t_temp, p_t_centro, p_t_costado, l_t_bottom, l_t_center, l_t_side, e_t_centro, e_t_costado, l_et_bottom, l_et_c, l_et_s]

    for ext_el in front_elements + back_elements:
        calc.append(ext_el)

    if alerta_el is not None:
        calc.append(alerta_el)

    tree.write(file_path, encoding="UTF-8", xml_declaration=True)
    print("Modificaciones de ruedo y largos ejecutadas exitosamente.")

if __name__ == "__main__":
    fix_basico()
