import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calc = root.find('.//calculation')

fixed_count = 0
for line in calc.findall('line'):
    if 'type' in line.attrib:
        del line.attrib['type']
        fixed_count += 1

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print(f"Fixed {fixed_count} lines by removing invalid 'type' attribute.")
