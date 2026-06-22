import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Remove invalid 'lineType' attribute from splines
for cid in ['12020', '12022']:
    sp = calculation.find(f".//*[@id='{cid}']")
    if sp is not None:
        if 'lineType' in sp.attrib:
            del sp.attrib['lineType']

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Removed invalid lineType from splines.")
