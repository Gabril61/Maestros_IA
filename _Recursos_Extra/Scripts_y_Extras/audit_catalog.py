import os

maestros_dir = r"C:\Users\Ricx18\Desktop\Maestros_IA"
catalogo_dir = r"C:\Users\Ricx18\Desktop\Catalogo"

# Get all .val files
garments = []
for f in os.listdir(maestros_dir):
    if f.endswith(".val"):
        # Strip .val extension
        garments.append(f[:-4])

print("--- AUDITORÍA DEL CATÁLOGO ---")
print(f"Total de patrones maestros encontrados: {len(garments)}\n")

missing_folders = []
incomplete_folders = []
complete_folders = []

required_files = ['sola.png', 'modelo.png', 'descripcion.txt']

for garment in garments:
    cat_path = os.path.join(catalogo_dir, garment)
    if not os.path.exists(cat_path):
        missing_folders.append(garment)
    else:
        # Check for combo
        missing_files = []
        for req in required_files:
            if not os.path.exists(os.path.join(cat_path, req)):
                missing_files.append(req)
        
        if missing_files:
            incomplete_folders.append((garment, missing_files))
        else:
            complete_folders.append(garment)

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
