import xml.etree.ElementTree as ET
import sys
import os

def fix_alerta():
    file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"

    ET.register_namespace('', '')
    tree = ET.parse(file_path)
    root = tree.getroot()

    calc = root.find(".//calculation")
    
    # Find ALERTA_SISA_ESTRECHA
    alerta_el = None
    for el in calc:
        if el.get("name") == "ALERTA_SISA_ESTRECHA":
            alerta_el = el
            break
            
    if alerta_el is not None:
        calc.remove(alerta_el)
        calc.append(alerta_el) # append at the very end

    # Guardar
    tree.write(file_path, encoding="UTF-8", xml_declaration=True)
    print("ALERTA_SISA_ESTRECHA movida al final del bloque calculation.")

if __name__ == "__main__":
    fix_alerta()
