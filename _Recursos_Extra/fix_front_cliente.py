import re
import os

def fix_front_cliente(val_path):
    print(f"\nCorrigiendo anclaje de F_Costado_Cliente en {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Corregir F_Costado_Cliente para que nazca de una proyección de F_Costado_Ruedo
    f_cliente_pattern = r'(<point[^>]*id="40403"[^>]*name="F_Costado_Cliente"[^>]*>)'
    c_match = re.search(f_cliente_pattern, content)
    
    if c_match and 'id="404020"' not in content:
        original_c = c_match.group(1)
        
        # Crear un punto de caída vertical exacto desde F_Costado_Ruedo (121) según el ajuste del cliente
        f_nivel_costado = '            <point angle="270" basePoint="121" id="404020" length="#ajuste_largo_prenda" lineColor="black" lineType="none" name="F_Nivel_Costado_Cliente" type="endLine"/>'
        
        # Modificar F_Costado_Cliente para que intersecte con este nuevo nivel elevado (404020), no con el centro delantero (40401)
        new_c = original_c.replace('basePoint="40401"', 'basePoint="404020"')
        
        replacement_cliente = f_nivel_costado + "\n" + new_c
        content = content.replace(original_c, replacement_cliente)
        modified = True
        print("  - F_Costado_Cliente anclado a la elevación de F_Costado_Ruedo mediante id=404020.")

    if modified:
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  - Archivo guardado con éxito.")
    else:
        print("  - No se requirieron modificaciones.")

def main():
    base_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Basico_Superior_Dama_Maestro.val"
    derived_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Blusa_Cuello_Mao_Dama_Maestro.val"
    
    if os.path.exists(base_path):
        fix_front_cliente(base_path)
    if os.path.exists(derived_path):
        fix_front_cliente(derived_path)

if __name__ == "__main__":
    main()
