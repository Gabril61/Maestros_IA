import xml.etree.ElementTree as ET

def update_buttons():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    # We need to find the points and replace their attributes.
    for calculation in root.findall('.//calculation'):
        for pt in calculation.findall('.//point'):
            name = pt.get('name')
            if name == 'B_Boton_1':
                pt.clear()
                pt.attrib = {
                    'type': 'lineIntersectAxis', 'id': '11004', 'name': 'B_Boton_1',
                    'basePoint': '14', 'angle': '0', 'p1Line': '11000', 'p2Line': '11001',
                    'lineColor': 'black', 'lineType': 'none', 'showPointName': 'true'
                }
            elif name == 'B_Boton_4':
                pt.clear()
                pt.attrib = {
                    'type': 'alongLine', 'id': '11006', 'name': 'B_Boton_4',
                    'firstPoint': '11001', 'secondPoint': '11002', 'length': '4',
                    'lineColor': 'black', 'lineType': 'none', 'showPointName': 'true'
                }
            elif name == 'B_Boton_2':
                pt.clear()
                pt.attrib = {
                    'type': 'alongLine', 'id': '11003', 'name': 'B_Boton_2',
                    'firstPoint': '11004', 'secondPoint': '11006', 'length': 'Line_B_Boton_1_B_Boton_4 * 0.3333',
                    'lineColor': 'black', 'lineType': 'none', 'showPointName': 'true'
                }
            elif name == 'B_Boton_3':
                pt.clear()
                pt.attrib = {
                    'type': 'alongLine', 'id': '11005', 'name': 'B_Boton_3',
                    'firstPoint': '11004', 'secondPoint': '11006', 'length': 'Line_B_Boton_1_B_Boton_4 * 0.6667',
                    'lineColor': 'black', 'lineType': 'none', 'showPointName': 'true'
                }
                
    tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)
    print("Buttons updated successfully.")

if __name__ == '__main__':
    update_buttons()
