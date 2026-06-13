import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Invert Spline 44003 direction
sp3 = calculation.find(".//spline[@id='44003']")
if sp3 is not None:
    # Swap points
    sp3.set('point1', '43001') # B_T_Ancho_Der_Flip (Center)
    sp3.set('point4', '43010') # B_Copa_Espalda_Pico (Top Right)
    
    # Swap angles
    # Old angle1 was AngleLine_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip + 15
    # Old angle2 was 0
    sp3.set('angle1', '0')
    sp3.set('angle2', 'AngleLine_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip + 15')
    
    # Lengths are the same
    sp3.set('length1', 'Line_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip * 0.4')
    sp3.set('length2', 'Line_B_Copa_Espalda_Pico_B_T_Ancho_Der_Flip * 0.4')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Spline 44003 successfully inverted.")
