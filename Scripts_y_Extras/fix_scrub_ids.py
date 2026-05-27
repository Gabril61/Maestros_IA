import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

mapping = {
    '40000': '40100',
    '40001': '40101',
    '40002': '40102',
    '40003': '40103',
    '40004': '40104'
}

for tag in ['line', 'spline']:
    for el in root.findall(f'.//{tag}'):
        el_id = el.get('id')
        if el_id in mapping:
            el.set('id', mapping[el_id])

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Fixed ID collisions for lines in Scrub Top Dama.")
