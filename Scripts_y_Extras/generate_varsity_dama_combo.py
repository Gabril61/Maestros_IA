import os
import shutil

sola_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\varsity_dama_sola_1781206637572.png"
mod_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\varsity_dama_modelo_1781206674775.png"

dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Chaqueta_Universitaria_Dama"

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

sola_dest = os.path.join(dest_folder, "sola.png")
mod_dest = os.path.join(dest_folder, "modelo.png")
desc_path = os.path.join(dest_folder, "descripcion.txt")

content = """Nombre: Chaqueta Universitaria Dama (Varsity Jacket)
Estilo: Universitario / Clásico Deportivo Femenino

Características Técnicas de Patronaje:
- Chaqueta estilo universitario con entalle femenino y trazado paramétrico escalable.
- Cierre frontal diseñado para botones a presión (snaps).
- Terminaciones en cuello, puños y ruedo calculadas para tejido de punto elástico (rib).
- Bolsillos frontales diagonales tipo ojal / ribeteados.
- Área reservada en el pecho izquierdo para aplicación de parches o bordados institucionales.
"""

try:
    shutil.copy2(sola_src, sola_dest)
    shutil.copy2(mod_src, mod_dest)
    with open(desc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Varsity Dama combo generated successfully!")
except Exception as e:
    print("Error:", e)
