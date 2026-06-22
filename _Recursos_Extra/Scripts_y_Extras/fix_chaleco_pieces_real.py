import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

# Build parent map
parent_map = {c: p for p in tree.iter() for c in p}

pieces_removed = 0
# Remove all pieces
for piece in root.findall('.//piece'):
    parent_map[piece].remove(piece)
    pieces_removed += 1

# Remove all paths
paths_removed = 0
for path in root.findall('.//path'):
    parent_map[path].remove(path)
    paths_removed += 1

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print(f"Removed {pieces_removed} pieces and {paths_removed} paths.")
