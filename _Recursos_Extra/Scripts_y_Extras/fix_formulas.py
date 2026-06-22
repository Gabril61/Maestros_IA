import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Update 40003
pt = calculation.find(".//point[@id='40003']")
if pt is not None:
    pt.set('angle', '(AngleLine_Corte_Frente_Bicep_Corte_Frente_Codo * 2) - AngleLine_Corte_Frente_Codo_MS_Codo_Izq')

# Update 40004
pt = calculation.find(".//point[@id='40004']")
if pt is not None:
    pt.set('angle', '(AngleLine_Corte_Frente_Codo_Corte_Frente_Puno * 2) - AngleLine_Corte_Frente_Puno_MS_Puno_Izq')

# Update 40005
pt = calculation.find(".//point[@id='40005']")
if pt is not None:
    pt.set('angle', '(AngleLine_Corte_Frente_Codo_Corte_Frente_Puno * 2) - AngleLine_Corte_Frente_Puno_Ext_MS_Puno_Izq')

# Update 40011
pt = calculation.find(".//point[@id='40011']")
if pt is not None:
    pt.set('angle', '(AngleLine_Fold_Espalda_Bicep_Fold_Espalda_Codo * 2) - AngleLine_Corte_Espalda_Bicep_MS_Ancho_Der')

# Update 40012
pt = calculation.find(".//point[@id='40012']")
if pt is not None:
    pt.set('angle', '(AngleLine_Fold_Espalda_Bicep_Fold_Espalda_Codo * 2) - AngleLine_Corte_Espalda_Bicep_MS_Guia_Der')

# Update 40013
pt = calculation.find(".//point[@id='40013']")
if pt is not None:
    pt.set('angle', '(AngleLine_Fold_Espalda_Bicep_Fold_Espalda_Codo * 2) - AngleLine_Corte_Espalda_Codo_MS_Codo_Der')

# Update 40014
pt = calculation.find(".//point[@id='40014']")
if pt is not None:
    pt.set('angle', '(AngleLine_Fold_Espalda_Codo_Fold_Espalda_Puno * 2) - AngleLine_Corte_Espalda_Puno_MS_Puno_Der')

# Update 40015 (Spline)
sp = calculation.find(".//spline[@id='40015']")
if sp is not None:
    sp.set('angle1', '(AngleLine_Fold_Espalda_Bicep_Fold_Espalda_Codo * 2) - (AngleLine_MS_Origen_MS_Ancho_Der - 20)')
    sp.set('angle2', '(AngleLine_Fold_Espalda_Bicep_Fold_Espalda_Codo * 2) - 180')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Formula variable names fixed!")
