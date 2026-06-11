import sys
import ezdxf

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Médico_Clo.dxf"
target_piece = "2_M"
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
max_y = max(p[1] for p in points)
norm_points = [(p[0] - min_x, p[1] - min_y) for p in points]

center_x = 29.01
center_points = [p for p in norm_points if abs(p[0] - center_x) < 0.5]
sorted_center = sorted(center_points, key=lambda p: p[1])

print(f"--- Analisis Profundo: Pieza {target_piece} ---")
print(f"Eje Central detectado en X = {center_x:.2f}")

if sorted_center:
    print(f"Ruedo Centro: ({sorted_center[0][0]:.2f}, {sorted_center[0][1]:.2f})")
    print(f"Escote Centro: ({sorted_center[-1][0]:.2f}, {sorted_center[-1][1]:.2f})")
    neck_drop = max_y - sorted_center[-1][1]
    print(f"-> Profundidad de Escote (Caida desde Hombro Alto): {neck_drop:.2f} cm")
else:
    print("No se detectaron puntos exactos en el eje central.")

top_half = [p for p in norm_points if p[1] > 50]
shoulder_left = min(top_half, key=lambda p: p[0])
shoulder_right = max(top_half, key=lambda p: p[0])

print("\n--- Analisis de Hombros ---")
print(f"Punto mas alto (Nacimiento de Cuello Izq): ({17.73:.2f}, {73.53:.2f})")
print(f"Punta de Hombro (Sisa Izq): ({shoulder_left[0]:.2f}, {shoulder_left[1]:.2f})")
shoulder_slope = 73.53 - shoulder_left[1]
print(f"-> Caida de Hombro: {shoulder_slope:.2f} cm")
shoulder_width = 29.01 - shoulder_left[0]
print(f"-> Ancho de Hombro (Desde Centro a Punta): {shoulder_width:.2f} cm")

armpit_left = [p for p in norm_points if p[0] < 1.0 and 30 < p[1] < 60]
if armpit_left:
    armpit = min(armpit_left, key=lambda p: p[0])
    print(f"\n--- Analisis de Sisa ---")
    print(f"Punto mas externo (Axila Izq): ({armpit[0]:.2f}, {armpit[1]:.2f})")
    armhole_drop = shoulder_left[1] - armpit[1]
    print(f"-> Profundidad de Sisa (Desde Punta de Hombro a Axila): {armhole_drop:.2f} cm")
    armhole_width = 29.01 - armpit[0]
    print(f"-> Ancho de Sisa Total (Desde Centro Frente): {armhole_width:.2f} cm")
