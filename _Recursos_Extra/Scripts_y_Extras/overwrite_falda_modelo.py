import shutil
import os

new_img_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\falda_modelo_nueva_cara_1781210347295.png"
dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Falda_Ejecutiva_Dama"
mod_dest = os.path.join(dest_folder, "modelo.png")

try:
    shutil.copy2(new_img_src, mod_dest)
    print("New model image copied successfully!")
except Exception as e:
    print("Error:", e)
