import os
import shutil

sola_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\varsity_sola_1781204820927.png"
mod_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\varsity_modelo_1781204859547.png"

dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Chaqueta_Universitaria_Caballero_Maestro"

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

sola_dest = os.path.join(dest_folder, "sola.png")
mod_dest = os.path.join(dest_folder, "modelo.png")

try:
    shutil.copy2(sola_src, sola_dest)
    shutil.copy2(mod_src, mod_dest)
    print("Varsity images copied successfully!")
except Exception as e:
    print("Error:", e)
