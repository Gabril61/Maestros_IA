import xml.etree.ElementTree as ET

def fix_lineweight():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    fixed_count = 0
    for el in root.findall('.//spline'):
        if el.get('lineWeight') == '1.5':
            el.set('lineWeight', '0.7')
            fixed_count += 1
            
    tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)
    print(f"Fixed {fixed_count} splines with invalid lineWeight.")

if __name__ == '__main__':
    fix_lineweight()
