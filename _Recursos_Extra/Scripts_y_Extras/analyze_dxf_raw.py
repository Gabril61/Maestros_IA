import os

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Médico_Clo.dxf"

def analyze_dxf(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        
    lines = [line.strip() for line in lines]
    
    in_blocks = False
    in_block = False
    current_block_name = ""
    blocks = {}
    
    in_entities = False
    
    for i in range(len(lines)):
        if lines[i] == "SECTION":
            if i+2 < len(lines) and lines[i+2] == "BLOCKS":
                in_blocks = True
            elif i+2 < len(lines) and lines[i+2] == "ENTITIES":
                in_entities = True
        elif lines[i] == "ENDSEC":
            in_blocks = False
            in_entities = False
            
        if in_blocks:
            if lines[i] == "BLOCK":
                in_block = True
            elif in_block and lines[i] == "2": # Block name follows "2"
                if i+1 < len(lines):
                    current_block_name = lines[i+1]
                    blocks[current_block_name] = {'lines': 0, 'polylines': 0}
            elif in_block and lines[i] == "ENDBLK":
                in_block = False
                current_block_name = ""
            elif in_block and current_block_name != "":
                if lines[i] == "LINE":
                    blocks[current_block_name]['lines'] += 1
                elif lines[i] == "POLYLINE" or lines[i] == "LWPOLYLINE":
                    blocks[current_block_name]['polylines'] += 1
                    
    print("Found Pieces (Blocks) in DXF:")
    for b_name, data in blocks.items():
        if not b_name.startswith("*"): # Ignore anonymous blocks
            print(f" - Piece Name: {b_name} | Lines: {data['lines']} | Polylines: {data['polylines']}")
            
    if not blocks:
        print("No blocks found. The DXF might define pieces as direct entities in the ENTITIES section. Scanning TEXT/LAYER entries...")
        layers = set()
        for i in range(len(lines)):
            if lines[i] == "8": # Layer name follows "8"
                if i+1 < len(lines):
                    layers.add(lines[i+1])
        print("Found Layers:")
        for l in layers:
            print(f" - {l}")

if __name__ == "__main__":
    analyze_dxf(file_path)
