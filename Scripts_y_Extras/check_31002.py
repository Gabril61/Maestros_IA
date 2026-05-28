import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
node = tree.getroot().find('.//point[@id="31002"]')
if node is not None:
    print(f"31002 basePoint={node.get('basePoint')} angle={node.get('angle')}")
