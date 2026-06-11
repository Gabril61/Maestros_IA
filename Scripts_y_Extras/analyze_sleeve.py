import sys
import ezdxf

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Médico_Clo.dxf"
target_piece = "3_M" # Manga
doc = ezdxf.readfile(file_path)

piece_block = None
for block in doc.blocks:
    if block.name == target_piece:
        piece_block = block
        break

points = []
for entity in piece_block:
    if entity.dxftype() == 'LWPOLYLINE':
        for point in entity.get_points('xy'):
            points.append((point[0], point[1]))
    elif entity.dxftype() == 'POLYLINE':
        for vertex in entity.vertices:
            points.append((vertex.dxf.location.x, vertex.dxf.location.y))

if not points:
    print("No geometry.")
    sys.exit()

min_x = min(p[0] for p in points)
min_y = min(p[1] for p in points)
max_x = max(p[0] for p in points)
max_y = max(p[1] for p in points)

norm_points = [(p[0] - min_x, p[1] - min_y) for p in points]
width = max_x - min_x
height = max_y - min_y

print(f"--- Análisis Profundo: Manga (Pieza {target_piece}) ---")
print(f"Ancho Total: {width:.2f} cm")
print(f"Alto Total: {height:.2f} cm")

# Identificar Copa (Apex)
highest_points = [p for p in norm_points if p[1] > height - 1.0]
if highest_points:
    apex = sum(p[0] for p in highest_points)/len(highest_points)
    print(f"\nCúspide de la Copa (Centro Manga): X = {apex:.2f}")

# Extremos de Sisa (Izquierda y Derecha)
left_points = [p for p in norm_points if p[0] < 1.0]
right_points = [p for p in norm_points if p[0] > width - 1.0]

if left_points and right_points:
    left_armpit = max(left_points, key=lambda p: p[1])
    right_armpit = max(right_points, key=lambda p: p[1])
    
    print(f"\nExtremos de Sisa (Conexión con axila):")
    print(f"- Axila Izquierda: Y = {left_armpit[1]:.2f} cm (Altura desde ruedo)")
    print(f"- Axila Derecha: Y = {right_armpit[1]:.2f} cm (Altura desde ruedo)")
    
    cap_height = height - left_armpit[1]
    print(f"-> Altura real de Copa (Desde línea axilar al Apex): {cap_height:.2f} cm")

# Análisis de Ruedo Manga
bottom_points = [p for p in norm_points if p[1] < 1.0]
if bottom_points:
    b_left = min(bottom_points, key=lambda p: p[0])
    b_right = max(bottom_points, key=lambda p: p[0])
    print(f"\nExtremos del Ruedo de Manga (Puño/Apertura):")
    hem_width = b_right[0] - b_left[0]
    print(f"- Ancho de Ruedo: {hem_width:.2f} cm (Media manga: {hem_width/2:.2f} cm)")
    
# Análisis Bolsillo 5_M
piece_block_5 = None
for block in doc.blocks:
    if block.name == "5_M":
        piece_block_5 = block
        break

if piece_block_5:
    points_5 = []
    for entity in piece_block_5:
        if entity.dxftype() == 'LWPOLYLINE':
            for point in entity.get_points('xy'):
                points_5.append((point[0], point[1]))
    if points_5:
        m_x = min(p[0] for p in points_5)
        m_y = min(p[1] for p in points_5)
        mx_y = max(p[1] for p in points_5)
        mx_x = max(p[0] for p in points_5)
        np_5 = [(p[0] - m_x, p[1] - m_y) for p in points_5]
        
        print(f"\n--- Análisis Profundo: Bolsillo (Pieza 5_M) ---")
        print(f"Dimensiones: {mx_x - m_x:.2f} cm Ancho x {mx_y - m_y:.2f} cm Alto")
        bottom_5 = [p for p in np_5 if p[1] < 1.0]
        if bottom_5:
            if len(bottom_5) > 1 and max(p[0] for p in bottom_5) - min(p[0] for p in bottom_5) > (mx_x - m_x) * 0.8:
                print("-> Forma: Fondo Plano (Cuadrado/Rectangular)")
            else:
                print("-> Forma: Fondo en Pico (V) o Curvo")
