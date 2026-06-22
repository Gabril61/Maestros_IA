import xml.etree.ElementTree as ET

def inject_vista(val_path):
    tree = ET.parse(val_path)
    root = tree.getroot()
    
    # Buscar el draftBlock -> calculation
    calculation = root.find('.//calculation')
    if calculation is None:
        print("No se encontró calculation.")
        return
        
    point_28 = None
    for p in calculation.iter('point'):
        if p.get('id') == '28':
            point_28 = p
            break
            
    if point_28 is None:
        print("No se encontró el punto F_Hombro (28).")
        return
        
    # Crear nuevos nodos
    # 1. Punto mitad de hombro
    # ID: 90001
    new_point = ET.Element('point', {
        'id': '90001',
        'name': 'F_Vista_Hombro_Mitad',
        'type': 'alongLine',
        'firstPoint': '23',
        'secondPoint': '28',
        'length': 'Line_F_Cuello_Ancho_F_Hombro / 2',
        'lineColor': 'black'
    })
    
    # Insertar el punto justo después del punto 28 para respetar orden cronológico
    index_28 = list(calculation).index(point_28)
    calculation.insert(index_28 + 1, new_point)
    
    # 2. Línea hasta B_Ruedo_Curva_V (89001)
    # Insertar al final del bloque de calculation
    new_line = ET.Element('line', {
        'id': '90002',
        'firstPoint': '90001',
        'secondPoint': '89001',
        'lineColor': 'black',
        'lineStyle': 'solid',
        'type': 'normal'
    })
    
    calculation.append(new_line)
        
    # Guardar
    tree.write(val_path, encoding='UTF-8', xml_declaration=True)
    print("Vista inyectada con éxito.")

if __name__ == "__main__":
    inject_vista("C:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val")
