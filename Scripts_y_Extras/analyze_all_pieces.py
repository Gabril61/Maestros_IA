import sys
import ezdxf

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Médico_Clo.dxf"
try:
    doc = ezdxf.readfile(file_path)
except Exception as e:
    print(f"Error reading DXF: {e}")
    sys.exit(1)

def analyze_piece(block_name, piece_type):
    piece_block = None
    for block in doc.blocks:
        if block.name == block_name:
            piece_block = block
            break

    if not piece_block:
        return f"Piece {block_name} not found."

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

    if not points:
        return f"No geometry in {block_name}"

    min_x = min(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    
    width = max_x - min_x
    height = max_y - min_y
    norm_points = [(p[0] - min_x, p[1] - min_y) for p in points]
    
    res = f"\n### Pieza {block_name} ({piece_type})\n"
    res += f"- **Dimensiones Totales:** {width:.2f} cm (Ancho) x {height:.2f} cm (Alto)\n"

    # Determinar si es centro izquierdo o derecho
    left_edge_points = [p for p in norm_points if p[0] < 1.0]
    right_edge_points = [p for p in norm_points if p[0] > width - 1.0]
    
    y_range_left = max((p[1] for p in left_edge_points), default=0) - min((p[1] for p in left_edge_points), default=0)
    y_range_right = max((p[1] for p in right_edge_points), default=0) - min((p[1] for p in right_edge_points), default=0)

    center_x = 0 if y_range_left > y_range_right else width
    center_points = [p for p in norm_points if abs(p[0] - center_x) < 1.0]
    sorted_center = sorted(center_points, key=lambda p: p[1])
    
    if sorted_center:
        res += f"- **Largo por el Centro:** {sorted_center[-1][1] - sorted_center[0][1]:.2f} cm\n"
        neck_drop = max_y - sorted_center[-1][1]
        res += f"- **Caída/Profundidad Centro Superior (Escote/Canesú):** {neck_drop:.2f} cm\n"

    top_half = [p for p in norm_points if p[1] > height * 0.5]
    if top_half:
        if center_x == 0:
            shoulder_point = max(top_half, key=lambda p: p[0])
        else:
            shoulder_point = min(top_half, key=lambda p: p[0])
            
        shoulder_drop = max_y - shoulder_point[1]
        shoulder_width = abs(center_x - shoulder_point[0])
        res += f"- **Caída de Extremo (Hombro):** {shoulder_drop:.2f} cm\n"
        res += f"- **Ancho hasta el Extremo:** {shoulder_width:.2f} cm\n"
        
    return res

pieces_to_analyze = [
    ("4_M", "Delantero"),
    ("2_M", "Espalda"),
    ("3_M", "Manga"),
    ("5_M", "Bolsillo"),
    ("6_M", "Canesú / Vista")
]

report = "# Desglose Geométrico de CLO 3D (Scrub Médico M)\n"
for p_name, p_type in pieces_to_analyze:
    report += analyze_piece(p_name, p_type)

with open(r"c:\Users\Ricx18\Desktop\Maestros_IA\Scripts_y_Extras\clo_breakdown.md", 'w', encoding='utf-8') as f:
    f.write(report)
    
print("Breakdown generated in clo_breakdown.md")
