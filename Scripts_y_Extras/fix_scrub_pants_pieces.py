import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Pantalon_Medico_Caballero_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

paths_to_remove = []
path_ids_to_remove = []

# Find internal paths that refer to Pinza
for path in root.findall('.//path'):
    if 'Pinza' in path.get('name', ''):
        paths_to_remove.append(path)
        path_ids_to_remove.append(path.get('id'))

# Remove the path elements from their parent (draw)
for path in paths_to_remove:
    # We need to find the parent of the path. It's usually <draw>
    # Since iter() doesn't give parents, we can do:
    for draw in root.findall('.//draw'):
        if path in list(draw):
            draw.remove(path)

# Find and remove records in iPaths
for ipaths in root.findall('.//iPaths'):
    records_to_remove = []
    for record in ipaths.findall('record'):
        if record.get('path') in path_ids_to_remove:
            records_to_remove.append(record)
    for r in records_to_remove:
        ipaths.remove(r)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print(f"Removed {len(path_ids_to_remove)} internal paths for darts.")
