import sys
import ezdxf

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Médico_Clo.dxf"
target_piece = "4_M"
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
    elif entity.dxftype() == 'LINE':
        points.append((entity.dxf.start.x, entity.dxf.start.y))
        points.append((entity.dxf.end.x, entity.dxf.end.y))

min_x = min(p[0] for p in points)
min_y = min(p[1] for p in points)
max_x = max(p[0] for p in points)
max_y = max(p[1] for p in points)

norm_points = [(p[0] - min_x, p[1] - min_y) for p in points]
width = max_x - min_x
height = max_y - min_y

left_edge_points = [p for p in norm_points if p[0] < 1.0]
right_edge_points = [p for p in norm_points if p[0] > width - 1.0]

y_range_left = max((p[1] for p in left_edge_points), default=0) - min((p[1] for p in left_edge_points), default=0)
y_range_right = max((p[1] for p in right_edge_points), default=0) - min((p[1] for p in right_edge_points), default=0)

center_x = 0 if y_range_left > y_range_right else width
center_points = [p for p in norm_points if abs(p[0] - center_x) < 1.0]
sorted_center = sorted(center_points, key=lambda p: p[1])

print(f"--- Análisis Profundo: Pieza {target_piece} (Delantero) ---")
print(f"Ancho Total: {width:.2f} cm | Alto Total: {height:.2f} cm")
print(f"Eje Central detectado en X = {center_x:.2f}")

if sorted_center:
    print(f"Ruedo Centro: ({sorted_center[0][0]:.2f}, {sorted_center[0][1]:.2f})")
    print(f"Escote Centro V (Punta del V): ({sorted_center[-1][0]:.2f}, {sorted_center[-1][1]:.2f})")
    neck_drop = height - sorted_center[-1][1]
    print(f"-> Profundidad de Escote V (Caída desde Hombro Alto): {neck_drop:.2f} cm")

top_half = [p for p in norm_points if p[1] > height * 0.5]
if center_x == 0:
    shoulder_tip = max(top_half, key=lambda p: p[0])
    highest_shoulder = max([p for p in top_half if p[0] < shoulder_tip[0] - 5], key=lambda p: p[1], default=None)
else:
    shoulder_tip = min(top_half, key=lambda p: p[0])
    highest_shoulder = max([p for p in top_half if p[0] > shoulder_tip[0] + 5], key=lambda p: p[1], default=None)

if highest_shoulder:
    print("\n--- Análisis de Hombros ---")
    print(f"Punto más alto (Nacimiento de Cuello): ({highest_shoulder[0]:.2f}, {highest_shoulder[1]:.2f})")
    print(f"Punta de Hombro Caído: ({shoulder_tip[0]:.2f}, {shoulder_tip[1]:.2f})")
    shoulder_slope = highest_shoulder[1] - shoulder_tip[1]
    print(f"-> Caída de Hombro: {shoulder_slope:.2f} cm")
    shoulder_width = abs(center_x - shoulder_tip[0])
    print(f"-> Ancho de Hombro (Desde Centro a Punta): {shoulder_width:.2f} cm")

if center_x == 0:
    armpit_candidates = [p for p in norm_points if p[0] > width * 0.5 and 20 < p[1] < 60]
    if armpit_candidates:
        armpit = max(armpit_candidates, key=lambda p: p[0])
else:
    armpit_candidates = [p for p in norm_points if p[0] < width * 0.5 and 20 < p[1] < 60]
    if armpit_candidates:
        armpit = min(armpit_candidates, key=lambda p: p[0])

if armpit_candidates:
    print(f"\n--- Análisis de Sisa ---")
    print(f"Punto de Axila: ({armpit[0]:.2f}, {armpit[1]:.2f})")
    armhole_drop = shoulder_tip[1] - armpit[1]
    print(f"-> Profundidad de Sisa (Desde Punta de Hombro a Axila): {armhole_drop:.2f} cm")
    armhole_width = abs(center_x - armpit[0])
    print(f"-> Ancho de Sisa Total (Desde Centro Frente): {armhole_width:.2f} cm")

