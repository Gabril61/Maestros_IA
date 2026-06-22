import os
import shutil

sola_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\falda_sola_1781207124186.png"
mod_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\falda_modelo_1781207160129.png"

dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Falda_Ejecutiva_Dama"

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

sola_dest = os.path.join(dest_folder, "sola.png")
mod_dest = os.path.join(dest_folder, "modelo.png")
desc_path = os.path.join(dest_folder, "descripcion.txt")

content = """Nombre: Falda Ejecutiva Dama (Pencil Skirt)
Estilo: Corporativo / Formal

Características Técnicas de Patronaje:
- Falda ejecutiva estilo tubo o lápiz, con trazado paramétrico.
- Entalle anatómico resuelto mediante pinzas matemáticas en el panel frontal y posterior.
- Largo estandarizado a la rodilla (ajustable dinámicamente).
- Construcción preparada para pretina y cierre invisible en la parte trasera.
- Abertura inferior trasera (kick pleat) calculada para permitir confort y movilidad.
"""

try:
    shutil.copy2(sola_src, sola_dest)
    shutil.copy2(mod_src, mod_dest)
    with open(desc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Falda Ejecutiva combo generated successfully!")
except Exception as e:
    print("Error:", e)
