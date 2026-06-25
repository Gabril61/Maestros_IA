import xml.etree.ElementTree as ET

# Register namespaces to prevent 'ns0' prefixes
ET.register_namespace('', 'http://www.w3.org/2000/svg') # not actually svg but just in case
# Seamly2D doesn't typically use namespaces, but let's be safe.

tree = ET.parse('C:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val')
root = tree.getroot()
calc = root.find('.//calculation')

sleeve_elements = []

# Collect elements that belong to the sleeve (names starting with M_ or IDs between 1000 and 1099)
for elem in list(calc):
    name = elem.attrib.get('name', '')
    id_str = elem.attrib.get('id', '0')
    
    if name.startswith('M_') or (id_str.isdigit() and 1000 <= int(id_str) < 1100):
        sleeve_elements.append(elem)

# Remove them from their current position
for elem in sleeve_elements:
    calc.remove(elem)

# Append them to the end of the calculation block
for elem in sleeve_elements:
    calc.append(elem)

tree.write('C:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val', encoding='utf-8', xml_declaration=True)
print(f"Moved {len(sleeve_elements)} elements to the end of the calculation block.")
