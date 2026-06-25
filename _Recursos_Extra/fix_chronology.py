import xml.etree.ElementTree as ET

val_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(val_path)
calc = tree.find('.//calculation')

p_izq = calc.find(".//point[@name='M_Puno_Izq']")
idx = list(calc).index(p_izq)

# 1024 and 1025 are the lines we need to move
# Wait, let's just find the lines that use 1000 and 1020/1021
# M_Ancho_Izq is 1021
# M_Ancho_Der is 1020
l_izq = calc.find(".//line[@firstPoint='1000'][@secondPoint='1021']")
l_der = calc.find(".//line[@firstPoint='1000'][@secondPoint='1020']")

if l_izq is not None and l_der is not None:
    calc.remove(l_izq)
    calc.remove(l_der)
    calc.insert(idx, l_izq)
    calc.insert(idx, l_der)
    
tree.write(val_path, encoding='UTF-8', xml_declaration=True)
print("Lineas movidas exitosamente antes de M_Puno_Izq.")
