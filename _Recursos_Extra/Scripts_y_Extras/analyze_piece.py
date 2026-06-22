import sys
try:
    import ezdxf
except ImportError:
    print("ezdxf not found. Please install it with 'pip install ezdxf'")
    sys.exit(1)

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Médico_Clo.dxf"
target_piece = "2_M"

try:
    doc = ezdxf.readfile(file_path)
except Exception as e:
    print(f"Error reading DXF: {e}")
    sys.exit(1)

blocks = doc.blocks

piece_block = None
for block in blocks:
    if block.name == target_piece:
        piece_block = block
        break

if not piece_block:
    print(f"Piece {target_piece} not found in the DXF.")
    sys.exit(1)

points = []

# Extract all points
for entity in piece_block:
    if entity.dxftype() == 'LWPOLYLINE':
        for point in entity.get_points('xy'):
            points.append((point[0], point[1]))
    elif entity.dxftype() == 'POLYLINE':
        for vertex in entity.vertices:
            points.append((vertex.dxf.location.x, vertex.dxf.location.y))
    elif entity.dxftype() == 'LINE':
        points.append((entity.dxf.start.x, entity.dxf.start.y))
        points.append((entity.dxf.end.x, entity.dxf.end.y))

if not points:
    print("No geometry found in this piece.")
    sys.exit(1)

# Find extrema
min_x = min(p[0] for p in points)
max_x = max(p[0] for p in points)
min_y = min(p[1] for p in points)
max_y = max(p[1] for p in points)

# Normalize points so that bottom-left is (0,0)
norm_points = [(p[0] - min_x, p[1] - min_y) for p in points]

# Find specific landmarks (normalized)
# Highest point (Shoulder/Neck)
highest = max(norm_points, key=lambda p: p[1])
# Lowest point (Hem)
lowest = min(norm_points, key=lambda p: p[1])
# Leftmost point (Center or Side)
leftmost = min(norm_points, key=lambda p: p[0])
# Rightmost point (Side or Center)
rightmost = max(norm_points, key=lambda p: p[0])

# To differentiate left and right, let's find the armpit (usually the widest point but not at the bottom or top)
# Let's print the top 5 highest points to analyze neck and shoulder
sorted_by_y = sorted(norm_points, key=lambda p: p[1], reverse=True)
top_points = sorted_by_y[:10]

print(f"--- ANÁLISIS GEOMÉTRICO PIEZA {target_piece} ---")
print(f"Ancho Total: {max_x - min_x:.2f} cm")
print(f"Alto Total: {max_y - min_y:.2f} cm")
print("\n--- Puntos Clave Normalizados (X, Y) ---")
print(f"Punto más alto (Escote/Hombro): ({highest[0]:.2f}, {highest[1]:.2f})")
print(f"Punto más bajo (Ruedo): ({lowest[0]:.2f}, {lowest[1]:.2f})")
print(f"Punto más a la izquierda: ({leftmost[0]:.2f}, {leftmost[1]:.2f})")
print(f"Punto más a la derecha: ({rightmost[0]:.2f}, {rightmost[1]:.2f})")

# Check if center is on left or right. A straight line over Y indicates center fold.
# We look for points with x near 0 and x near max_width
left_edge_points = [p for p in norm_points if p[0] < 1.0] # within 1cm of left
right_edge_points = [p for p in norm_points if p[0] > (max_x - min_x) - 1.0] # within 1cm of right

y_range_left = max(p[1] for p in left_edge_points) - min(p[1] for p in left_edge_points) if left_edge_points else 0
y_range_right = max(p[1] for p in right_edge_points) - min(p[1] for p in right_edge_points) if right_edge_points else 0

if y_range_left > y_range_right:
    print("-> El Eje Central (Centro Frente) parece estar en el lado IZQUIERDO.")
    center_x = 0
    armpit_x_candidates = [p for p in norm_points if p[0] > (max_x - min_x)/2 and 30 < p[1] < 60]
    if armpit_x_candidates:
        armpit = max(armpit_x_candidates, key=lambda p: p[0])
        print(f"Punto estimado de Sisa (Axila): ({armpit[0]:.2f}, {armpit[1]:.2f})")
        print(f"  * Profundidad de Sisa desde lo más alto: {highest[1] - armpit[1]:.2f} cm")
else:
    print("-> El Eje Central (Centro Frente) parece estar en el lado DERECHO.")
    center_x = max_x - min_x
    armpit_x_candidates = [p for p in norm_points if p[0] < (max_x - min_x)/2 and 30 < p[1] < 60]
    if armpit_x_candidates:
        armpit = min(armpit_x_candidates, key=lambda p: p[0])
        print(f"Punto estimado de Sisa (Axila): ({armpit[0]:.2f}, {armpit[1]:.2f})")
        print(f"  * Profundidad de Sisa desde lo más alto: {highest[1] - armpit[1]:.2f} cm")

print("\nTop 10 puntos más altos (Para ver caída de escote y hombro):")
unique_top = []
for p in top_points:
    # Filter very close points
    if not any(abs(p[0]-up[0]) < 1.0 and abs(p[1]-up[1]) < 1.0 for up in unique_top):
        unique_top.append(p)
        print(f"({p[0]:.2f}, {p[1]:.2f})")
