import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Find and remove the leftover ghost lines 43998 and 43999
to_remove = []
for cid in ['43998', '43999']:
    el = calculation.find(f".//*[@id='{cid}']")
    if el is not None:
        to_remove.append(el)

for el in to_remove:
    calculation.remove(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Removed leftover ghost lines 43998 and 43999.")
