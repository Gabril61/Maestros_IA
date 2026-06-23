import xml.etree.ElementTree as ET

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
        # angle1: Ligeramente abierto hacia afuera respecto a la lÃ­nea recta
        sp_32.set('angle1', 'AngleLine_F_Hombro_F_Ancho_Pecho - 15')
        
        # angle2: Tangente de llegada paralela a la lÃ­nea larga (Hombro -> Pinza Sup)
        # Como es tangente hacia ATRÃS, apuntamos desde Pinza Sup hacia Hombro
        sp_32.set('angle2', 'AngleLine_F_Sisa_Pinza_Sup_F_Hombro')
        
        sp_32.set('length1', 'Line_F_Hombro_F_Ancho_Pecho * 0.4')
        sp_32.set('length2', 'Line_F_Hombro_F_Ancho_Pecho * 0.3') # Reducido un poco para evitar abombamiento excesivo

    # Spline 34 (Ancho Pecho -> Pinza Sup)
    sp_34 = find_by_id('spline', '34')
    if sp_34 is not None:
        # angle1: Tangente de salida paralela a la lÃ­nea larga (Hombro -> Pinza Sup)
        sp_34.set('angle1', 'AngleLine_F_Hombro_F_Sisa_Pinza_Sup')
        
        # angle2: Llegada a la pinza (Se mantiene igual, anclada a la lÃ­nea de rotaciÃ³n)
        sp_34.set('angle2', 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa + 180')
        
        sp_34.set('length1', 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup * 0.3')
        sp_34.set('length2', 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup * 0.35')

    tree.write(path, encoding='UTF-8', xml_declaration=True)

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
