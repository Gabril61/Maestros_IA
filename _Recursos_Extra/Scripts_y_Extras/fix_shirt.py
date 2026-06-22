import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val'

tree = ET.parse(file_path)
root = tree.getroot()

# Fix sleeve length and curves
for draft in root.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        calc = draft.find('calculation')
        if calc is not None:
            # Change sleeve length variable
            for pt in calc.findall('point'):
                if pt.attrib.get('name') == 'M_A1_Real':
                    # Change to S_LARGO_MANGA (minus cuff width which is 6)
                    pt.attrib['length'] = '@S_LARGO_MANGA - 6'
            
            # Find the sleeve side lines and change them to splines if they exist, or add them if not
            # In typical TextilFit files, M_F to M_A3_Izq and M_T to M_A4_Der are the side seams.
            # But the points here are 2004 M_T and 2005 M_F (biceps), and hem points are 2026 M_A3_Izq and 2027 M_A4_Der.
            # The line ids are usually 2018, 2019 etc. Let's just create splines for them.
            # I will inject splines directly for M_T to M_A3_Izq and M_F to M_A4_Der.
            
            # M_T (2004) to M_A3_Izq (2026) -> back seam
            s1 = ET.Element('spline', {'id': '20500', 'type': 'simpleInteractive', 'point1': '2004', 'point4': '2026', 'angle1': '260', 'angle2': '90', 'length1': '15', 'length2': '15', 'color': 'black'})
            # M_F (2005) to M_A4_Der (2027) -> front seam
            s2 = ET.Element('spline', {'id': '20501', 'type': 'simpleInteractive', 'point1': '2005', 'point4': '2027', 'angle1': '280', 'angle2': '90', 'length1': '15', 'length2': '15', 'color': 'black'})
            
            calc.append(s1)
            calc.append(s2)

    # Fix Collar Stand distance
    if draft.attrib.get('name') == 'Cuello_y_Tirilla':
        calc = draft.find('calculation')
        if calc is not None:
            for pt in calc.findall('point'):
                if pt.attrib.get('name') == 'C_Cuello_Base':
                    # Increase the length to separate it more from the stand (e.g. from 0.5 to 2.5)
                    pt.attrib['length'] = '2.5'

tree.write(file_path, encoding='UTF-8', xml_declaration=True)
print("Camisa corrections applied successfully!")
