import os
import shutil

sola_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\pantalon_caballero_sola_1781210866827.png"
mod_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\pantalon_caballero_modelo_1781210913203.png"

dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Pantalon_Caballero"

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

sola_dest = os.path.join(dest_folder, "sola.png")
mod_dest = os.path.join(dest_folder, "modelo.png")
desc_path = os.path.join(dest_folder, "descripcion.txt")

content = """Nombre: Pantalón de Vestir Caballero (Classic Dress Pant)
Estilo: Clásico / Formal / Ejecutivo

Características Técnicas de Patronaje:
- Pantalón clásico de caballero con plomo perfecto y trazado paramétrico escalable.
- Ajuste lumbar resuelto mediante pinzas matemáticas en el panel posterior.
- Sistema de cierre con bragueta frontal (fly) y extensión para cremallera.
- Construcción de bolsillos laterales diagonales (slant pockets) de uso fácil.
- Posicionamiento paramétrico para bolsillos traseros tipo ojal (welt pockets).
- Pretina recta estandarizada con pasadores.
"""

try:
    shutil.copy2(sola_src, sola_dest)
    shutil.copy2(mod_src, mod_dest)
    with open(desc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Pantalon Caballero combo generated successfully!")
except Exception as e:
    print("Error:", e)
