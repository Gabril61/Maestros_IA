import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calculation = root.find('.//calculation')

# Exact topological order required:
ordered_ids = [
    # 1. Origin and Vectors
    '41000', '41001', '41002',
    
    # 2. Shifted Points Front
    '42001', '42002', '42003', '42004', '42005',
    '42006', '42007', '42008', '42009', '42010',
    
    # 3. Shifted Points Back
    '43001', '43002', '43003', '43004',
    '43006', '43007', '43008', '43010',
    
    # 4. Lines used as Angle References
    '44101', '44102', '44103', '45100', '44017',
    
    # 5. Splines
    '44001', '44002', '44003',
    
    # 6. Aletillon Base (along line)
    '45001',
    
    # 7. Extended Hem and Placket Points
    '45005', '45006', '45002', '45003', '45004',
    
    # 8. Remaining Outline Lines
    '44010', '44011', '44012', '44013', '44014',
    '44015', '44016', '44026', '44022', '44023',
    '44024', '44025', '44019', '44020', '44021'
]

# Extract them from calculation
elements_to_append = []

for cid in ordered_ids:
    el = calculation.find(f".//*[@id='{cid}']")
    if el is not None:
        elements_to_append.append(el)
        calculation.remove(el)

# Append them back in exact order at the end
for el in elements_to_append:
    calculation.append(el)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Bajera nodes successfully reordered topologically.")
