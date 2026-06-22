import os

dest_folder = r"C:\Users\Ricx18\Desktop\Catalogo\Chaqueta_Universitaria_Caballero_Maestro"
desc_path = os.path.join(dest_folder, "descripcion.txt")

content = """Nombre: Chaqueta Universitaria Caballero (Varsity Jacket)
Estilo: Universitario / Clásico Deportivo

Características Técnicas de Patronaje:
- Chaqueta estilo universitario con trazado paramétrico escalable.
- Cierre frontal diseñado para botones a presión (snaps).
- Terminaciones en cuello, puños y ruedo calculadas para tejido de punto elástico (rib).
- Bolsillos frontales diagonales tipo ojal / ribeteados.
- Área reservada en el pecho izquierdo para aplicación de parches o bordados institucionales.
"""

with open(desc_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("descripcion.txt generated successfully!")
