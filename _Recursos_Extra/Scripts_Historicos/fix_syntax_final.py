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

    # Spline 32 (Hombro -> Ancho Pecho)
    sp_32 = find_by_id('spline', '32')
    if sp_32 is not None:
        # Seamly2D NO permite usar AngleLine_A_B si la línea fue dibujada como B_A.
        # La línea auxiliar dibujada va de F_Hombro a F_Sisa_Pinza_Sup.
        # Reemplazamos AngleLine_F_Sisa_Pinza_Sup_F_Hombro por su equivalente trigonométrico + 180.
        sp_32.set('angle2', 'AngleLine_F_Hombro_F_Sisa_Pinza_Sup + 180')

    tree.write(path, encoding='UTF-8', xml_declaration=True)

for path in paths:
    try:
        fix_splines(path)
        print(f"Sintaxis reparada en: {path}")
    except Exception as e:
        print(f"Error procesando {path}: {e}")
