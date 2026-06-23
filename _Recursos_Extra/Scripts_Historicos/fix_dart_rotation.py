import xml.etree.ElementTree as ET

paths = [
    r"C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Patrones_Generados\Roxana_Acosta_2026-06-22T213406\Chaleco_Femenino_Maestro.val",
    r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
]

def fix_splines(path):
    tree = ET.parse(path)
    root = tree.getroot()

    def find_by_id(tag, element_id):
        for elem in root.iter(tag):
            if elem.get('id') == element_id:
                return elem
        return None

    # Spline 34 (Ancho Pecho -> Pinza Sup)
    sp_34 = find_by_id('spline', '34')
    if sp_34 is not None:
        # La pinza superior está rotada -15 grados respecto a la línea base.
        # Para que al coser la pinza (rotación de +15 grados) la curva quede continua,
        # la tangente en el patrón plano DEBE tener ese -15.
        # Anteriormente era: AngleLine_F_Ancho_Pecho_F_Costado_Sisa + 180
        sp_34.set('angle2', 'AngleLine_F_Ancho_Pecho_F_Costado_Sisa - 15 + 180')
        
        # Ajustamos los tensores para que fluya más natural y evite S-curves
        sp_34.set('length2', 'Line_F_Ancho_Pecho_F_Sisa_Pinza_Sup * 0.3')

    tree.write(path, encoding='UTF-8', xml_declaration=True)

for path in paths:
    try:
        fix_splines(path)
        print(f"Rotación de pinza corregida en: {path}")
    except Exception as e:
        print(f"Error procesando {path}: {e}")
