import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# 1. Assign names to shifted points
names_map = {
    '42001': 'B_F_Ancho_Izq_Flip',
    '42002': 'B_F_Guia_Izq_Flip',
    '42003': 'B_F_Codo_Izq_Flip',
    '42004': 'B_F_Puno_Izq_Flip',
    '42005': 'B_F_Ext_Puno_Izq_Flip',
    '42006': 'B_Corte_Frente_Bicep',
    '42007': 'B_Corte_Frente_Codo',
    '42008': 'B_Corte_Frente_Puno',
    '42009': 'B_Ext_Corte_Frente_Puno',
    '42010': 'B_Copa_Frente_Pico',
    '43001': 'B_T_Ancho_Der_Flip',
    '43002': 'B_T_Guia_Der_Flip',
    '43003': 'B_T_Codo_Der_Flip',
    '43004': 'B_T_Puno_Der_Flip',
    '43006': 'B_Corte_Espalda_Bicep',
    '43007': 'B_Corte_Espalda_Codo',
    '43008': 'B_Corte_Espalda_Puno',
    '43010': 'B_Copa_Espalda_Pico'
}

for pid, pname in names_map.items():
    pt = calculation.find(f".//point[@id='{pid}']")
    if pt is not None:
        pt.set('name', pname)

# 2. Fix Spline 44002
sp2 = calculation.find(".//spline[@id='44002']")
if sp2 is not None:
    sp2.set('angle1', 'AngleLine_B_Copa_Frente_Pico_B_F_Guia_Izq_Flip + 10')
    sp2.set('angle2', 'AngleLine_B_Copa_Frente_Pico_B_F_Guia_Izq_Flip + 190')
    sp2.set('length1', 'Line_B_Copa_Frente_Pico_B_F_Guia_Izq_Flip * 0.4')
    sp2.set('length2', 'Line_B_Copa_Frente_Pico_B_F_Guia_Izq_Flip * 0.4')

# 3. Fix Spline 44001
sp1 = calculation.find(".//spline[@id='44001']")
if sp1 is not None:
    sp1.set('angle1', 'AngleLine_B_F_Guia_Izq_Flip_B_F_Ancho_Izq_Flip + 10')
    sp1.set('angle2', 'AngleLine_B_F_Guia_Izq_Flip_B_F_Ancho_Izq_Flip + 190')
    sp1.set('length1', 'Line_B_F_Guia_Izq_Flip_B_F_Ancho_Izq_Flip * 0.4')
    sp1.set('length2', 'Line_B_F_Guia_Izq_Flip_B_F_Ancho_Izq_Flip * 0.4')

# 4. Fix Spline 44003
sp3 = calculation.find(".//spline[@id='44003']")
if sp3 is not None:
    sp3.set('angle1', 'AngleLine_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip - 10')
    sp3.set('angle2', 'AngleLine_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip + 170')
    sp3.set('length1', 'Line_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip * 0.4')
    sp3.set('length2', 'Line_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip * 0.4')

# 5. Fix Hem Points and Aletillon angles
# 45005: Bajera_Underarm_Hem. Base is 42004. Angle straight down. Line 44017 is 42003 to 42004.
pt5 = calculation.find(".//point[@id='45005']")
if pt5 is not None:
    pt5.set('angle', 'AngleLine_B_F_Codo_Izq_Flip_B_F_Puno_Izq_Flip')

# 45006: Bajera_Corte_Espalda_Hem. Base is 43008. Angle straight down. Line 45100 is 43008 to 43007 (UP).
pt6 = calculation.find(".//point[@id='45006']")
if pt6 is not None:
    pt6.set('angle', 'AngleLine_B_Corte_Espalda_Puno_B_Corte_Espalda_Codo + 180')

# 45002: Bajera_Aletillon_Top_Ext. Angle to the right. Line 45100 goes UP.
pt2 = calculation.find(".//point[@id='45002']")
if pt2 is not None:
    pt2.set('angle', 'AngleLine_B_Corte_Espalda_Puno_B_Corte_Espalda_Codo - 90')

# 45003: Bajera_Aletillon_Bot_Ext. Angle to the right.
pt3 = calculation.find(".//point[@id='45003']")
if pt3 is not None:
    pt3.set('angle', 'AngleLine_B_Corte_Espalda_Puno_B_Corte_Espalda_Codo - 90')

# 45004: Bajera_Aletillon_Hem_Ext. Angle straight down.
pt4 = calculation.find(".//point[@id='45004']")
if pt4 is not None:
    pt4.set('angle', 'AngleLine_B_Corte_Espalda_Puno_B_Corte_Espalda_Codo + 180')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Bajera formulas and names fully repaired.")
