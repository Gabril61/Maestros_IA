import xml.etree.ElementTree as ET

blazer_file = r'c:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val'
tree = ET.parse(blazer_file)
root = tree.getroot()

for draft in root.findall('draftBlock'):
    if draft.attrib.get('name') == 'Corpino_y_Manga':
        calc = draft.find('calculation')
        if calc is not None:
            elements_to_remove = []
            for child in calc:
                # Si es un punto y su nombre empieza con M_ (pertenece a la manga antigua)
                if child.tag == 'point' and child.attrib.get('name', '').startswith('M_'):
                    elements_to_remove.append(child)
                # Si es una línea o spline y hace referencia a puntos M_
                elif child.tag in ('line', 'spline'):
                    first = child.attrib.get('firstPoint', '')
                    second = child.attrib.get('secondPoint', '')
                    pt1 = child.attrib.get('point1', '')
                    pt4 = child.attrib.get('point4', '')
                    if any(x.startswith('M_') for x in [first, second, pt1, pt4]):
                        elements_to_remove.append(child)

            for el in elements_to_remove:
                if el in calc:
                    calc.remove(el)
                    
        # Remove old sleeve pieces from modeling and pieces section in Corpino_y_Manga
        modeling = draft.find('modeling')
        if modeling is not None:
            to_remove = []
            for child in modeling:
                # ID in 2000s are usually the old sleeve
                if child.attrib.get('idObject', '').startswith('20'):
                    to_remove.append(child)
            for el in to_remove:
                modeling.remove(el)

        pieces = draft.find('pieces')
        if pieces is not None:
            to_remove = []
            for piece in pieces:
                if piece.attrib.get('name', '') == 'Manga':
                    to_remove.append(piece)
            for el in to_remove:
                pieces.remove(el)

tree.write(blazer_file, encoding='UTF-8', xml_declaration=True)
print("Old sleeve points and references deleted successfully.")
