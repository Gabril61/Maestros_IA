import xml.etree.ElementTree as ET

file_path = "Blazer_Dama_Maestro.val"
tree = ET.parse(file_path)
root = tree.getroot()

calculation_ids = set()
for draft in root.findall('.//draftBlock'):
    calc = draft.find('calculation')
    if calc is not None:
        for node in calc:
            node_id = node.get('id')
            if node_id:
                calculation_ids.add(node_id)

removed = 0
for draft in root.findall('.//draftBlock'):
    modeling = draft.find('modeling')
    if modeling is not None:
        for node in list(modeling):
            id_obj = node.get('idObject')
            # If idObject does not exist in calculation, it's an orphan!
            if id_obj and id_obj not in calculation_ids:
                modeling.remove(node)
                removed += 1

tree.write(file_path, encoding="utf-8", xml_declaration=True)
print(f"Removed {removed} orphaned modeling nodes.")
