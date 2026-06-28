import re
import os

def process_file(val_path):
    print(f"\nProcesando {os.path.basename(val_path)}...")
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # 1. Inyectar #altura_cadera en <variables> si no existe
    if '#altura_cadera' not in content:
        variables_match = re.search(r'(<variables>.*?)(\s*</variables>)', content, re.DOTALL)
        if variables_match:
            new_variable = '\n        <variable description="Altura de Cadera" formula="20" name="#altura_cadera"/>'
            new_variables_block = variables_match.group(1) + new_variable + variables_match.group(2)
            content = content.replace(variables_match.group(0), new_variables_block)
            modified = True
            print("  - Variable #altura_cadera inyectada.")
        else:
            print("  - ERROR: No se encontró el bloque <variables>.")

    # 2. Reemplazar "20" por "#altura_cadera" en F_Nivel_Cadera y T_Nivel_Cadera
    # Buscar F_Nivel_Cadera (teniendo en cuenta que length puede estar antes de name)
    f_cadera_pattern = r'(<point[^>]*length=")20("[^>]*name="F_Nivel_Cadera"[^>]*>)'
    if re.search(f_cadera_pattern, content):
        content = re.sub(f_cadera_pattern, r'\1#altura_cadera\2', content)
        modified = True
        print("  - F_Nivel_Cadera actualizado con #altura_cadera.")
    else:
        # Fallback if name is before length
        f_cadera_pattern2 = r'(<point[^>]*name="F_Nivel_Cadera"[^>]*length=")20("[^>]*>)'
        if re.search(f_cadera_pattern2, content):
            content = re.sub(f_cadera_pattern2, r'\1#altura_cadera\2', content)
            modified = True
            print("  - F_Nivel_Cadera actualizado con #altura_cadera (name antes de length).")

    # Buscar T_Nivel_Cadera
    t_cadera_pattern = r'(<point[^>]*length=")20("[^>]*name="T_Nivel_Cadera"[^>]*>)'
    if re.search(t_cadera_pattern, content):
        content = re.sub(t_cadera_pattern, r'\1#altura_cadera\2', content)
        modified = True
        print("  - T_Nivel_Cadera actualizado con #altura_cadera.")
    else:
        t_cadera_pattern2 = r'(<point[^>]*name="T_Nivel_Cadera"[^>]*length=")20("[^>]*>)'
        if re.search(t_cadera_pattern2, content):
            content = re.sub(t_cadera_pattern2, r'\1#altura_cadera\2', content)
            modified = True
            print("  - T_Nivel_Cadera actualizado con #altura_cadera (name antes de length).")

    # 3. Igualar longitudes de costados
    # Buscar F_Costado_Cintura original
    cintura_pattern = r'(<point[^>]*id="119"[^>]*name="F_Costado_Cintura"[^>]*>)'
    cintura_match = re.search(cintura_pattern, content)
    
    if cintura_match and 'F_Costado_Cintura_Ref' not in content:
        original_cintura = cintura_match.group(1)
        # Crear F_Costado_Cintura_Ref (cambiando id a 1190 y name a F_Costado_Cintura_Ref)
        ref_cintura = original_cintura.replace('id="119"', 'id="1190"').replace('name="F_Costado_Cintura"', 'name="F_Costado_Cintura_Ref"')
        
        # Crear el nuevo F_Costado_Cintura
        new_cintura = '            <point angle="AngleLine_F_Costado_Sisa_F_Costado_Cintura_Ref" basePoint="111" id="119" length="Line_T_Costado_Sisa_T_Costado_Cintura" mx="-10.2213" my="-2.59643" name="F_Costado_Cintura" type="endLine"/>'
        
        replacement = ref_cintura + "\n" + new_cintura
        content = content.replace(original_cintura, replacement)
        modified = True
        print("  - F_Costado_Cintura igualado al costado trasero (creado punto Ref).")

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
        process_file(base_path)
    else:
        print(f"Error: No se encontró el archivo base {base_path}")
        
    if os.path.exists(derived_path):
        process_file(derived_path)
    else:
        print(f"Error: No se encontró el archivo derivado {derived_path}")

if __name__ == "__main__":
    main()
