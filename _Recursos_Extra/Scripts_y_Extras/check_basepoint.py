import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val')
node = tree.getroot().find('.//point[@id="232"]')
if node is not None:
    print(f"Unisex 232: basePoint={node.get('basePoint')} angle={node.get('angle')}")

tree2 = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val')
node2 = tree2.getroot().find('.//point[@id="232"]')
if node2 is not None:
    print(f"Estandar 232: basePoint={node2.get('basePoint')} angle={node2.get('angle')}")
