import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

# The error says piece '424' has a bad record path '439'
# Let's find all pieces and remove the record with path='439'
pieces = root.findall('.//piece')
removed = 0
for piece in pieces:
    ipaths = piece.find('iPaths')
    if ipaths is not None:
        for record in ipaths.findall('record'):
            if record.get('path') == '439':
                ipaths.remove(record)
                removed += 1

# Also, if path 439 is in modeling but missing nodes, let's just remove path 439 completely from modeling
modeling = root.find('.//modeling')
if modeling is not None:
    for path in modeling.findall('path'):
        if path.get('id') == '439':
            modeling.remove(path)
            removed += 1

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print(f"Cleaned up {removed} references to broken path 439.")
