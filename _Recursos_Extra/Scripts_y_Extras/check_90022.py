import xml.etree.ElementTree as ET

tree = ET.parse(r'c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Caballero_Maestro.val')
modeling = tree.getroot().find('.//modeling')

for path_id in ['90022', '90023', '90034', '90047', '890100']:
    path = modeling.find(f'.//path[@id="{path_id}"]')
    print(f"Path {path_id}:")
    if path is not None:
        nodes = path.find('nodes')
        if nodes is not None:
            for node in nodes.findall('node'):
                print(node.attrib)
        else:
            print("No nodes")
    else:
        print("Path not found")
