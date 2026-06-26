import xml.etree.ElementTree as ET
filepath = 'c:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val'
tree = ET.parse(filepath)
calc = tree.getroot().find('.//calculation')

p50672 = calc.find('.//point[@id="50672"]')
l9991 = calc.find('.//line[@id="9991"]')

if p50672 is not None and l9991 is not None:
    calc.remove(p50672)
    # find the new index of l9991 after removing p50672
    new_idx_9991 = list(calc).index(l9991)
    calc.insert(new_idx_9991 + 1, p50672)
    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print("Point 50672 successfully moved after Line 9991.")
else:
    print("Could not find the elements.")
