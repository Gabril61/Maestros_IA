import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Update Spline 44002 (Top Left)
sp2 = calculation.find(".//spline[@id='44002']")
if sp2 is not None:
    sp2.set('angle1', 'AngleLine_B_Copa_Frente_Pico_B_F_Guia_Izq_Flip - 20')
    sp2.set('angle2', 'AngleLine_B_Copa_Frente_Pico_B_F_Guia_Izq_Flip + 180 + 30')
    sp2.set('length1', 'Line_B_Copa_Frente_Pico_B_F_Guia_Izq_Flip * 0.4')
    sp2.set('length2', 'Line_B_Copa_Frente_Pico_B_F_Guia_Izq_Flip * 0.4')

# Update Spline 44001 (Mid Left to Center)
sp1 = calculation.find(".//spline[@id='44001']")
if sp1 is not None:
    sp1.set('angle1', 'AngleLine_B_F_Guia_Izq_Flip_B_F_Ancho_Izq_Flip - 20')
    sp1.set('angle2', '180')
    sp1.set('length1', 'Line_B_F_Guia_Izq_Flip_B_F_Ancho_Izq_Flip * 0.4')
    sp1.set('length2', 'Line_B_F_Guia_Izq_Flip_B_F_Ancho_Izq_Flip * 0.4')

# Update Spline 44003 (Top Right to Center)
sp3 = calculation.find(".//spline[@id='44003']")
if sp3 is not None:
    sp3.set('angle1', 'AngleLine_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip + 20')
    sp3.set('angle2', '0')
    sp3.set('length1', 'Line_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip * 0.4')
    sp3.set('length2', 'Line_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip * 0.4')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Spline angles calibrated perfectly.")
