import os

rules_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/.antigravityrules'
with open(rules_path, 'r', encoding='utf-8') as f:
    content = f.read()

if '19. PROTOCOLO DE COPA DE MANGA' not in content:
    manga_block = """
19. PROTOCOLO DE COPA DE MANGA (Estandarización Bezier):
Toda curva que construya la copa de una manga debe ser matemáticamente escalable a su sisa perimetral. Queda ESTRICTAMENTE PROHIBIDO usar valores fijos (ej. length="10") en los tiradores Bezier de la copa. Se deben usar vectores relacionales con multiplicadores estándar:
- Para la curva de la Cimera (Copa Superior): Multiplicadores de * 0.55 y * 0.05.
- Para la curva de la Bajera (Sisa Inferior): Multiplicadores de * 0.4 (o 0.3) y * 0.2.
Esto asegura que el perímetro de la copa siempre sea superior y proporcional a la sisa, permitiendo la costura de embebido natural en sastrería sin desproporcionarse al escalar tallas.
"""
    with open(rules_path, 'a', encoding='utf-8') as f:
        f.write(manga_block)
    print("Protocolo de Copa de Manga añadido.")
else:
    print("El protocolo ya estaba presente.")
