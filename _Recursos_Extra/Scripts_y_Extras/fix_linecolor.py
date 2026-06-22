import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Find all elements with lineColor="none" and change to "black"
for el in calculation.iter():
    if el.get('lineColor') == 'none':
        el.set('lineColor', 'black')

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Fixed lineColor='none' issue.")
