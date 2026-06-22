import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

details = root.find('.//details')
if details is not None:
    for detail in details.findall('detail'):
        nodes = detail.findall('.//node')
        for node in nodes:
            if node.get('idObject') == '436':
                print(f"Detail piece '{detail.get('name')}' uses modeling point 436 (which relies on 141)")
                
        # Also check internal paths
        for path in detail.findall('.//path'):
            for node in path.findall('.//node'):
                if node.get('idObject') == '436':
                    print(f"Detail piece '{detail.get('name')}' has an internal path using 436")
