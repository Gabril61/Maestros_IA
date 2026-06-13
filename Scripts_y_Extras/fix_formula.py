import xml.etree.ElementTree as ET

file_path = r'C:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

calc = root.find('.//calculation')

# Points 151 and 153 used the invalid formula
# 'Line_E_Nivel_Cintura_E_Dobladillo_Centro'
correct_formula = 'Line_E_Nivel_Cintura_E_Centro_Ruedo + Line_E_Centro_Ruedo_E_Dobladillo_Centro'

for pt in calc.findall('point'):
    if pt.get('id') in ['151', '153']:
        pt.set('length', correct_formula)

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Formula repaired.")
