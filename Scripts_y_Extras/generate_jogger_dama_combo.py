import os
import shutil

sola_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\jogger_dama_sola_1781211688307.png"
mod_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\jogger_dama_modelo_1781211729753.png"

dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Pantalon_Dama_Jogger"

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

sola_dest = os.path.join(dest_folder, "sola.png")
mod_dest = os.path.join(dest_folder, "modelo.png")
desc_path = os.path.join(dest_folder, "descripcion.txt")

content = """Nombre: Pantalón Jogger Dama (Athleisure Pant)
Estilo: Urbano / Casual / Deportivo

Características Técnicas de Patronaje:
- Pantalón tipo jogger con silueta relajada y trazado paramétrico.
- Pretina integral diseñada para albergar cinta elástica y cordón de ajuste (drawstring).
- Ruedos inferiores calculados con frunces para banda elástica (puños tipo jogger).
- Inclusión de bolsillos laterales funcionales y profundos.
- Holguras (Protocolo Clo) optimizadas para tejidos de punto (algodón perchado, french terry) o tejidos planos con caída.
"""

try:
    shutil.copy2(sola_src, sola_dest)
    shutil.copy2(mod_src, mod_dest)
    with open(desc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Jogger Dama combo generated successfully!")
except Exception as e:
    print("Error:", e)
