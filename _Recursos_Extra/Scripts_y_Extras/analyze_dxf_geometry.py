import sys
try:
    import ezdxf
except ImportError:
    print("ezdxf not found. Please install it with 'pip install ezdxf'")
    sys.exit(1)

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Médico_Clo.dxf"

try:
    doc = ezdxf.readfile(file_path)
except Exception as e:
    print(f"Error reading DXF: {e}")
    sys.exit(1)

blocks = doc.blocks

print(f"{'Piece Name':<15} | {'Width':<10} | {'Height':<10} | {'Possible Type'}")
print("-" * 60)

for block in blocks:
    name = block.name
    if name.startswith('*') or name in ['0', '10']:
        continue
        
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')
    
    has_geometry = False
    
    for entity in block:
        if entity.dxftype() == 'LWPOLYLINE':
            for point in entity.get_points('xy'):
                x, y = point[0], point[1]
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                has_geometry = True
        elif entity.dxftype() == 'POLYLINE':
            for vertex in entity.vertices:
                x, y = vertex.dxf.location.x, vertex.dxf.location.y
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                has_geometry = True
        elif entity.dxftype() == 'LINE':
            x1, y1 = entity.dxf.start.x, entity.dxf.start.y
            x2, y2 = entity.dxf.end.x, entity.dxf.end.y
            for x, y in [(x1, y1), (x2, y2)]:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                has_geometry = True
                
    if has_geometry:
        width = max_x - min_x
        height = max_y - min_y
        
        # Simple heuristic to guess what the piece is
        guess = "Unknown"
        if 400 <= height <= 800 and 150 <= width <= 350:
            guess = "Delantero/Espalda (Mitad)"
        elif 100 <= height <= 300 and 100 <= width <= 400:
            guess = "Manga corta / Bolsillo grande"
        elif 50 <= height <= 150 and 50 <= width <= 150:
            guess = "Bolsillo"
        elif height < 50 or width < 50:
            guess = "Cuello / Vista / Refuerzo"
            
        print(f"{name:<15} | {width:<10.1f} | {height:<10.1f} | {guess}")
