import xml.etree.ElementTree as ET
import sys
import os

def build_basico():
    file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
    out_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"

    ET.register_namespace('', '')
    tree = ET.parse(file_path)
    root = tree.getroot()

    # 1. Metadatos
    root.find("description").text = "Patrón Maestro - Básico Superior Dama"
    notes = root.find("notes")
    if notes is not None:
        notes.text = "Bloque fundacional para prendas superiores de dama. Estructura anatómica pura sin vistas, bolsillos ni cruces. Contiene Corte Princesa M.A.S."

    # 2. Mediciones
    meas = root.find("measurements")
    if meas is not None:
        meas.text = "Maestro_Variables_IA.smis"

    # 3. Variables
    variables_node = root.find("variables")
    if variables_node is not None:
        variables_node.clear()
        vars_to_add = [
            {"name": "#holgura_busto", "formula": "4", "description": "Holgura de busto"},
            {"name": "#holgura_cintura", "formula": "6", "description": "Holgura de cintura"},
            {"name": "#holgura_cadera", "formula": "8", "description": "Holgura de cadera"},
            {"name": "#holgura_espalda", "formula": "2", "description": "Holgura de espalda"},
            {"name": "#holgura_pecho", "formula": "2", "description": "Holgura de pecho"},
            {"name": "#holgura_bicep", "formula": "4", "description": "Holgura de bicep"},
            {"name": "#holgura_sisa", "formula": "10", "description": "Holgura de sisa"},
            {"name": "#ruedo_prenda", "formula": "0", "description": "Ruedo de prenda"}
        ]
        for v in vars_to_add:
            ET.SubElement(variables_node, "variable", v)

    # 4. Limpieza del DraftBlock
    calc = root.find(".//calculation")
    
    ids_to_delete = {
        "180", "186", "280", "284",  # Splines redundantes
        "3013" # Línea basura
    }
    
    # Agregar rangos a ids_to_delete
    for i in range(40000, 40308): ids_to_delete.add(str(i))
    for i in range(89100, 89115): ids_to_delete.add(str(i))
    for i in range(95000, 95018): ids_to_delete.add(str(i))

    elements_to_remove = []
    for el in calc:
        el_id = el.get("id")
        if el_id in ids_to_delete:
            elements_to_remove.append(el)

    for el in elements_to_remove:
        calc.remove(el)

    # 5. Modificar Splines del Corte Princesa Delantero (Universal Protocol)
    for spline in calc.findall("spline"):
        sid = spline.get("id")
        if sid == "50207":
            spline.set("angle1", "AngleLine_F_Ancho_Pecho_F_Costado_Sisa - 90")
            spline.set("angle2", "AngleLine_F_Centro_Busto_F_Pinza_Izq - 180")
            # Dejamos length1 y length2 como están (* 0.25)
        elif sid == "50209":
            spline.set("angle1", "AngleLine_F_Ancho_Pecho_F_Costado_Sisa - 90")
            spline.set("angle2", "AngleLine_F_Centro_Busto_F_Pinza_Der - 180")

    # 6. Insertar ALERTA_SISA_ESTRECHA justo después del origen (F_Origen tiene id "100")
    alerta = ET.Element("point", {
        "angle": "0",
        "basePoint": "100",
        "id": "9999",
        "length": "((@S_CONT_SISA + 4) > (Spl_F_Caida_Hombro_F_Ancho_Pecho + Spl_F_Ancho_Pecho_F_Sisa_Pinza_Sup + Spl_F_Sisa_Pinza_Inf_F_Costado_Sisa + Spl_T_Caida_Hombro_T_Ancho_Espalda + Spl_T_Ancho_Espalda_T_Costado_Sisa)) ? 20 : 0",
        "lineColor": "black",
        "lineType": "solidLine",
        "lineWeight": "0.7",
        "mx": "0",
        "my": "-5",
        "name": "ALERTA_SISA_ESTRECHA",
        "showPointName": "true",
        "type": "endLine"
    })
    calc.insert(1, alerta) # Index 1 is after F_Origen

    # 7. Renombrar el DraftBlock
    draft = root.find("draftBlock")
    if draft is not None:
        draft.set("name", "Cuerpo_Principal")

    # Guardar
    tree.write(out_path, encoding="UTF-8", xml_declaration=True)
    print(f"Archivo guardado exitosamente en: {out_path}")

if __name__ == "__main__":
    build_basico()
