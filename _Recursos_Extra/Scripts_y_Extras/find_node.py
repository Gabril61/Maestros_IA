import xml.etree.ElementTree as ET

file_path = "Blazer_Dama_Maestro.val"
tree = ET.parse(file_path)
root = tree.getroot()

for draft in root.findall('.//draftBlock'):
    for modeling in draft.findall('.//modeling'):
        for node in modeling:
            if node.get('id') == '89638':
                print(f"Found in draft: {draft.get('name')}")
