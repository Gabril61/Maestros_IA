import xml.etree.ElementTree as ET
import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'

tree = ET.parse(file_path)
root = tree.getroot()

mapping = {
    '11002': '12000',
    '301': '12001',
    '502': '12002',
    '303': '12003',
    '403': '12004',
    '602': '12005',
    '401': '12006'
}

count = 0
for pt in root.findall('.//modeling//point'):
    old_id = pt.get('idObject')
    if old_id in mapping:
        pt.set('idObject', mapping[old_id])
        count += 1

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print(f"Updated {count} modeling points to use the hem extensions.")
