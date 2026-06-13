import os
import shutil

catalogo_dir = r"C:\Users\Ricx18\Desktop\Catalogo"
maestros_dir = r"C:\Users\Ricx18\Desktop\Maestros_IA"

# 1. Fix the folder names I messed up earlier
try:
    if os.path.exists(os.path.join(catalogo_dir, "Chaleco_Halter_Dama_Maestro")):
        shutil.move(os.path.join(catalogo_dir, "Chaleco_Halter_Dama_Maestro"), os.path.join(catalogo_dir, "Chaleco_Halter_Dama"))
    if os.path.exists(os.path.join(catalogo_dir, "Chaqueta_Universitaria_Caballero_Maestro")):
        shutil.move(os.path.join(catalogo_dir, "Chaqueta_Universitaria_Caballero_Maestro"), os.path.join(catalogo_dir, "Chaqueta_Universitaria_Caballero"))
except Exception as e:
    print(f"Error renaming: {e}")

# 2. Audit
val_files = [f for f in os.listdir(maestros_dir) if f.endswith(".val") and "old" not in f and "antes" not in f]

missing_folders = []
incomplete_folders = []
complete_folders = []
untracked_folders = os.listdir(catalogo_dir)

required_files = ['sola.png', 'modelo.png', 'descripcion.txt']

for val_file in val_files:
    # Strip .val and _Maestro to get base name
    base_name = val_file.replace(".val", "")
    if base_name.endswith("_Maestro"):
        base_name = base_name[:-8] # remove exactly "_Maestro"
    
    # Wait, some might have _Maestro_Clo
    if base_name.endswith("_Maestro_Clo"):
        base_name = base_name[:-12]
        
    cat_path = os.path.join(catalogo_dir, base_name)
    
    if base_name in untracked_folders:
        untracked_folders.remove(base_name)
        
    if not os.path.exists(cat_path):
        missing_folders.append(base_name)
    else:
        missing_files = []
        for req in required_files:
            if not os.path.exists(os.path.join(cat_path, req)):
                missing_files.append(req)
        
        if missing_files:
            incomplete_folders.append((base_name, missing_files))
        else:
            complete_folders.append(base_name)

print("=== PRENDAS COMPLETAMENTE LISTAS (COMBO OK) ===")
for g in complete_folders:
    print(f" - {g}")

print("\n=== CARPETAS INCOMPLETAS (FALTAN ARCHIVOS) ===")
if not incomplete_folders:
    print(" (Ninguna)")
for g, missing in incomplete_folders:
    print(f" - {g} (Falta: {', '.join(missing)})")

print("\n=== PRENDAS SIN CATÁLOGO (CARPETA INEXISTENTE) ===")
if not missing_folders:
    print(" (Ninguna)")
for g in missing_folders:
    print(f" - {g}")

print("\n=== CARPETAS EN CATALOGO SIN PATRON MAESTRO ASOCIADO ===")
if not untracked_folders:
    print(" (Ninguna)")
for g in untracked_folders:
    print(f" - {g}")
