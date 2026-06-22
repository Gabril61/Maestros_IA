import os
import shutil

sola_src = r"C:\Users\Ricx18\.gemini\antigravity\brain\7e07b8ac-7484-4fd5-ab9a-6904fc4eb57a\scrub_top_sola_1781212232400.png"

dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Scrub_Top_Medico"

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

sola_dest = os.path.join(dest_folder, "sola.png")
desc_path = os.path.join(dest_folder, "descripcion.txt")

content = """Nombre: Top Médico / Scrub (Medical Scrub Top)
Estilo: Clínico / Uniforme / Unisex

Características Técnicas de Patronaje:
- Camisa médica (Scrub Top) con trazado paramétrico escalable y holguras estandarizadas.
- Escote en V (V-neck) reforzado con vista/falso interno.
- Construcción de manga corta clásica montada con altura de copa calibrada.
- Sistema de 3 bolsillos funcionales: un bolsillo de pecho izquierdo y dos bolsillos tipo parche inferiores de gran capacidad.
- Diseño de costura limpia en hombros y sisas para máxima resistencia en el entorno hospitalario.
"""

try:
    shutil.copy2(sola_src, sola_dest)
    with open(desc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Scrub Top sola and desc generated successfully!")
except Exception as e:
    print("Error:", e)
