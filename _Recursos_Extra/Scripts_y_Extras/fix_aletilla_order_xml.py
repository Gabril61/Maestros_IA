import xml.etree.ElementTree as ET
import os

files = [
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val'
]

for filepath in files:
    if not os.path.exists(filepath): continue
    
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        calc = root.find('.//calculation')
        
        if calc is not None:
            extracted = []
            to_remove = []
            
            for child in calc:
                if child.get('id') == '232' or child.get('firstPoint') == '232' or child.get('secondPoint') == '232' or child.get('point1') == '232' or child.get('point2') == '232' or child.get('point3') == '232' or child.get('point4') == '232':
                    to_remove.append(child)
            
            for child in to_remove:
                calc.remove(child)
                extracted.append(child)
                
            for child in extracted:
                calc.append(child)
                
            tree.write(filepath, encoding='UTF-8', xml_declaration=True)
            print(f"Fixed order in {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
