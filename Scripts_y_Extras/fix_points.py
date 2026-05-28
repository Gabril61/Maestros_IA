import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()
calc = root.find('draftBlock/calculation')

replacements = {
    '109': {'type': 'endLine', 'basePoint': '108', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)'},
    '110': {'type': 'endLine', 'basePoint': '108', 'angle': '270', 'length': '(@I_ENTREPIERNA - @I_ALTO_RODILLA)'},
    '111': {'type': 'endLine', 'basePoint': '108', 'angle': '270', 'length': '@I_ENTREPIERNA'},
    '116': {'type': 'endLine', 'basePoint': '106', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)'},
    '126': {'type': 'endLine', 'basePoint': '106', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)*2/3'},
    '128': {'type': 'endLine', 'basePoint': '127', 'angle': '270', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)/3'},
    '129': {'type': 'endLine', 'basePoint': '106', 'angle': '45', 'length': '(@I_CONTCADBA / 40)'},
    
    '209': {'type': 'endLine', 'basePoint': '208', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)'},
    '210': {'type': 'endLine', 'basePoint': '208', 'angle': '270', 'length': '(@I_ENTREPIERNA - @I_ALTO_RODILLA)'},
    '211': {'type': 'endLine', 'basePoint': '208', 'angle': '270', 'length': '@I_ENTREPIERNA'},
    '216': {'type': 'endLine', 'basePoint': '206', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)'},
    '217': {'type': 'endLine', 'basePoint': '206', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)*2/3'},
    '220': {'type': 'endLine', 'basePoint': '219', 'angle': '270', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)/3'},
    '221': {'type': 'endLine', 'basePoint': '219', 'angle': '90', 'length': '(@I_ALTO_TIRO - @D_ANCHO_PRETINA)*2/3'},
    '222': {'type': 'endLine', 'basePoint': '221', 'angle': '180', 'length': '2'}, # aproximado para T_Cintura_Extremo
    '223': {'type': 'endLine', 'basePoint': '206', 'angle': '135', 'length': '(@I_CONTCADBA / 20)'},
    
    '304': {'type': 'endLine', 'basePoint': '302', 'angle': '270', 'length': '(@D_ANCHO_PRETINA * 2)'},
    '404': {'type': 'endLine', 'basePoint': '402', 'angle': '270', 'length': '10'},
    '504': {'type': 'endLine', 'basePoint': '502', 'angle': '270', 'length': '20'},
    '511': {'type': 'endLine', 'basePoint': '509', 'angle': '270', 'length': '28'}
}

for p in calc.findall('point'):
    pid = p.get('id')
    if pid in replacements:
        for k in list(p.attrib.keys()):
            if k not in ['id', 'name', 'mx', 'my']:
                del p.attrib[k]
        for k, v in replacements[pid].items():
            p.set(k, v)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("pointOfIntersection replaced!")
