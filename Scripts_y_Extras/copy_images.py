import shutil

sola_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\halter_vest_sola_1781204399651.png"
mod_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\halter_vest_modelo_1781204420557.png"

sola_dest = r"C:\Users\Ricx18\Desktop\Catalogo\Chaleco_Halter_Dama\sola.png"
mod_dest = r"C:\Users\Ricx18\Desktop\Catalogo\Chaleco_Halter_Dama\modelo.png"

try:
    shutil.copy2(sola_src, sola_dest)
    shutil.copy2(mod_src, mod_dest)
    print("Images copied successfully!")
except Exception as e:
    print("Error:", e)
