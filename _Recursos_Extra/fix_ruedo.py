import xml.etree.ElementTree as ET

def fix_ruedo():
    file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Basico_Maestro.val'
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    draft_block = root.find(".//draftBlock[@name='Scrub_Top_Basico']")
    if draft_block is not None:
        calc = draft_block.find('calculation')
        if calc is not None:
            # Encuentra D_Ruedo_Costado
            d_ruedo = calc.find(".//point[@id='109']")
            if d_ruedo is not None:
                # Cambiar de horizontal a vertical desde la axila (ID 107) usando largo del costado trasero
                d_ruedo.set('basePoint', '107')
                d_ruedo.set('angle', '270')
                d_ruedo.set('length', 'Line_E_Axila_E_Ruedo_Costado')

    ET.indent(tree, space="    ", level=0)
    tree.write(file_path, encoding="UTF-8", xml_declaration=True)
    print("Regla de Extensión de Ruedo aplicada exitosamente.")

if __name__ == '__main__':
    fix_ruedo()
