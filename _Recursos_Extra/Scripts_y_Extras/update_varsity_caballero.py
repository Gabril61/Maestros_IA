import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaqueta_Universitaria_Caballero_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

# Update metadata
desc = root.find('description')
if desc is not None:
    desc.text = "Patrón Maestro - Chaqueta Universitaria (Varsity) Caballero"

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Varsity Caballero metadata updated.")
