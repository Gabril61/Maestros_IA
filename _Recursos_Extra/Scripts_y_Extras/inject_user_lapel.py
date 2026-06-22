import xml.etree.ElementTree as ET

blazer_file = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(blazer_file)
root = tree.getroot()

for draft in root.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        calc = draft.find('calculation')
        if calc is not None:
            # Eliminar la solapa anterior que yo había diseñado (IDs 11100 a 11114)
            to_remove = []
            for child in calc:
                if child.attrib.get('id') in ('11100', '11101', '11102', '11103', '11110', '11111', '11112', '11113', '11114'):
                    to_remove.append(child)
            for el in to_remove:
                calc.remove(el)

            # Inyectar la solapa ilustrativa del usuario
            # <line firstPoint="11004" id="12040" lineColor="black" lineType="solidLine" lineWeight="0.35" secondPoint="23"/>
            calc.append(ET.Element('line', {'firstPoint': '11004', 'id': '12040', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 'secondPoint': '23'}))
            
            # <point firstPoint="23" id="12041" length="10" lineColor="black" lineType="none" lineWeight="0.35" mx="0.132292" my="0.264583" name="A1" secondPoint="11004" showPointName="true" type="alongLine"/>
            calc.append(ET.Element('point', {'firstPoint': '23', 'id': '12041', 'length': '10', 'lineColor': 'black', 'lineType': 'none', 'lineWeight': '0.35', 'mx': '0.132292', 'my': '0.264583', 'name': 'A1', 'secondPoint': '11004', 'showPointName': 'true', 'type': 'alongLine'}))
            
            # <point angle="0" firstPoint="12041" id="12042" length="9" lineColor="black" lineType="dashLine" lineWeight="0.35" mx="0.132292" my="0.264583" name="A2" secondPoint="23" showPointName="true" type="normal"/>
            calc.append(ET.Element('point', {'angle': '0', 'firstPoint': '12041', 'id': '12042', 'length': '9', 'lineColor': 'black', 'lineType': 'dashLine', 'lineWeight': '0.35', 'mx': '0.132292', 'my': '0.264583', 'name': 'A2', 'secondPoint': '23', 'showPointName': 'true', 'type': 'normal'}))
            
            # <line firstPoint="12042" id="12044" lineColor="black" lineType="solidLine" lineWeight="0.35" secondPoint="12041"/>
            calc.append(ET.Element('line', {'firstPoint': '12042', 'id': '12044', 'lineColor': 'black', 'lineType': 'solidLine', 'lineWeight': '0.35', 'secondPoint': '12041'}))
            
            # <spline angle1="260" angle2="100" color="black" id="12045" length1="5" length2="5" lineWeight="0.35" penStyle="solidLine" point1="12042" point4="11004" type="simpleInteractive"/>
            calc.append(ET.Element('spline', {'angle1': '260', 'angle2': '100', 'color': 'black', 'id': '12045', 'length1': '5', 'length2': '5', 'lineWeight': '0.35', 'penStyle': 'solidLine', 'point1': '12042', 'point4': '11004', 'type': 'simpleInteractive'}))

            # Asegurarse de que la holgura en F_Costado_Sisa y otros se mantenga en 1.5 cm. 
            # Esto ya se habia seteado en el rebuild_blazer_safe.py y el usuario confirmó "pongamosla en 1,5 cm por lado".
            # No necesito cambiarlo ya que está correcto en el archivo base.

tree.write(blazer_file, encoding='UTF-8', xml_declaration=True)
print("Solapa del usuario inyectada exitosamente.")
