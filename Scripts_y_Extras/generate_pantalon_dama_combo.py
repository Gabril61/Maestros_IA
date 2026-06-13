import os
import shutil

sola_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\pantalon_dama_clasico_sola_1781211406453.png"
mod_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\pantalon_dama_clasico_modelo_1781211444440.png"

dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Pantalon_Dama_Clasico"

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

sola_dest = os.path.join(dest_folder, "sola.png")
mod_dest = os.path.join(dest_folder, "modelo.png")
desc_path = os.path.join(dest_folder, "descripcion.txt")

content = """Nombre: Pantalón Clásico Dama (Classic Dress Pant)
Estilo: Corporativo / Formal / Ejecutivo

Características Técnicas de Patronaje:
- Pantalón clásico de vestir para mujer con trazado paramétrico escalable.
- Entalle anatómico preciso calculado mediante pinzas frontales y posteriores.
- Sistema de cierre central con bragueta frontal.
- Corte de pierna recto clásico (Straight leg), elegante y atemporal.
- Pretina anatómica estandarizada para mayor confort en la cintura.
- Diseño minimalista, libre de bolsillos abultados para mantener una silueta limpia.
"""

try:
    shutil.copy2(sola_src, sola_dest)
    shutil.copy2(mod_src, mod_dest)
    with open(desc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Pantalon Dama Clasico combo generated successfully!")
except Exception as e:
    print("Error:", e)
