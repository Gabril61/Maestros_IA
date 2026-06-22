import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Pantalon_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

# Update metadata
desc = root.find('description')
if desc is not None:
    desc.text = "Patrón Maestro - Scrub Pantalón Médico Dama"
notes = root.find('notes')
if notes is not None:
    notes.text = "Pantalón Médico (Scrub) para dama. Basado en la estructura Jogger, cintura elástica completa, bolsillos laterales."

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Scrub Pantalon Dama metadata updated.")
