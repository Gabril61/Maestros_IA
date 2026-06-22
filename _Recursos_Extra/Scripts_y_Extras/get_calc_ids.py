import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val')
calc_points = []
for p in tree.getroot().findall('.//piece'):
    if p.get('name') in ['Manga', 'Cuello', 'Centro_Espalda']:
        nodes = p.findall('.//node')
        ids = [n.get('idObject') for n in nodes]
        for m_id in ids:
            m_node = tree.getroot().find(f".//modeling/*[@id='{m_id}']")
            if m_node is not None:
                calc_points.append(m_node.get('idObject'))

print("Calculation points used:", set(calc_points))
