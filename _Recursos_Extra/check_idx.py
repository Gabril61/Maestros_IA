import xml.etree.ElementTree as ET
filepath = 'c:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val'
tree = ET.parse(filepath)
calc = tree.getroot().find('.//calculation')

def get_idx(tag, p_id):
    el = calc.find(f'.//{tag}[@id="{p_id}"]')
    return list(calc).index(el) if el is not None else -1

print('Spline 50116:', get_idx('spline', '50116'))
print('Spline 50209:', get_idx('spline', '50209'))
print('Line 9992:', get_idx('line', '9992'))
print('Line 9981:', get_idx('line', '9981'))
