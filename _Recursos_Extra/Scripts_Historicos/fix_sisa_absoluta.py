import xml.etree.ElementTree as ET
import os

file_path = r"C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Patrones_Generados\Roxana_Acosta_2026-06-22T213406\Chaleco_Femenino_Maestro.val"
master_file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"

def fix_splines(path):
    tree = ET.parse(path)
    root = tree.getroot()

    def find_by_id(tag, element_id):
        for elem in root.iter(tag):
            if elem.get('id') == element_id:
                return elem
        return None

    # Spline 32 (Hombro -> Ancho Pecho)
    sp_32 = find_by_id('spline', '32')
    if sp_32 is not None:
        # En lugar de depender de la pendiente, forzamos llegada vertical (hacia arriba)
        sp_32.set('angle2', '90')

    # Spline 34 (Ancho Pecho -> Pinza Sup)
    sp_34 = find_by_id('spline', '34')
    if sp_34 is not None:
        # Forzamos salida vertical (hacia abajo)
        sp_34.set('angle1', '270')
        # Reducimos un poco los tensores para que no se abombe demasiado
        sp_34.set('length1', 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup * 0.25')

    tree.write(path, encoding='UTF-8', xml_declaration=True)

# Corregir tanto el archivo de prueba como el maestro
try:
    fix_splines(file_path)
    print("Archivo de prueba (Roxana) corregido.")
except Exception as e:
    print(f"Error en prueba: {e}")

try:
    fix_splines(master_file_path)
    print("Archivo Maestro corregido.")
except Exception as e:
    print(f"Error en maestro: {e}")
