import xml.etree.ElementTree as ET

def inject():
    # Parse Blazer
    tree_b = ET.parse('Blazer_Dama_Maestro.val')
    root_b = tree_b.getroot()
    
    # Extract collar nodes
    collar_nodes = []
    for calc_b in root_b.findall('.//calculation'):
        for node in calc_b:
            node_id = node.get('id')
            if node_id and node_id.isdigit():
                nid = int(node_id)
                if 14100 <= nid <= 14199:
                    # Deep copy just to be safe
                    import copy
                    n_copy = copy.deepcopy(node)
                    if nid == 14100:
                        n_copy.set('basePoint', '200') # F_Costado_Real
                        # We might want to move it further to the right or change angle
                        # Blazer had angle="0" length="30" basePoint="12005"
                        n_copy.set('length', '40') 
                    collar_nodes.append(n_copy)
                    
    print(f"Extracted {len(collar_nodes)} nodes for the collar.")
    
    # Parse Chaleco
    tree_c = ET.parse('Chaleco_Femenino_Maestro.val')
    root_c = tree_c.getroot()
    
    # Inject nodes
    calc_c = root_c.find('.//calculation')
    for n in collar_nodes:
        calc_c.append(n)
        
    tree_c.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)
    print("Collar injected successfully.")

if __name__ == '__main__':
    inject()
