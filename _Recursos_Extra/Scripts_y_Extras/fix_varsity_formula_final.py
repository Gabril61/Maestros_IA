import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
calc = tree.getroot().find('.//calculation')

target_f = "Spl_F_Ancho_Pecho_F_Sisa_Pinza_Sup + Spl_F_Sisa_Pinza_Inf_F_Costado_Sisa"
repl_f = "Spl_F_Ancho_Pecho_F_Costado_Sisa"

target_t = "Spl_T_Ancho_Espalda_T_Sisa_Pinza_Sup + Spl_T_Sisa_Pinza_Inf_T_Costado_Sisa"
repl_t = "Spl_T_Ancho_Espalda_T_Costado_Sisa"

for p in calc.findall('point'):
    length = p.get('length', '')
    if not length:
        continue
        
    new_length = length
    if target_f in new_length:
        new_length = new_length.replace(target_f, repl_f)
    if target_t in new_length:
        new_length = new_length.replace(target_t, repl_t)
        
    if new_length != length:
        p.set('length', new_length)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Formulas scrubbed and fixed.")
