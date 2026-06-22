import xml.etree.ElementTree as ET

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Camisa_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

drafts = root.findall('draftBlock')

main_draft = None
for d in drafts:
    if d.get('name') == 'Corpino_y_Manga':
        main_draft = d
        break

if main_draft is not None:
    main_calc = main_draft.find('calculation')
    main_model = main_draft.find('modeling')
    main_pieces = main_draft.find('pieces')

    for d in drafts:
        if d != main_draft:
            # Move calculation elements
            calc = d.find('calculation')
            if calc is not None:
                for elem in list(calc):
                    main_calc.append(elem)
                    
            # Move modeling elements
            model = d.find('modeling')
            if model is not None:
                for elem in list(model):
                    main_model.append(elem)
                    
            # Move pieces elements
            pieces = d.find('pieces')
            if pieces is not None:
                for elem in list(pieces):
                    main_pieces.append(elem)
            
            # Remove the extra draftBlock
            root.remove(d)
            
    # Adjust origins so they don't overlap
    for p in main_calc.findall('point'):
        if p.get('type') == 'single':
            name = p.get('name')
            if name == 'T_Origen':
                p.set('x', '120')  # Increased separation for back
            elif name == 'M_A':
                p.set('x', '220')  # Increased separation for sleeve
            elif name == 'C_Origen':
                p.set('x', '0')
                p.set('y', '120')  # Below front
            elif name == 'P_Origen':
                p.set('x', '120')
                p.set('y', '120')  # Below back

    # Adjust splines for sleeve side seams (20500 and 20501)
    # Reducing length1 and length2 makes the curve softer
    for s in main_calc.findall('spline'):
        if s.get('id') in ['20500', '20501']:
            s.set('length1', '3')
            s.set('length2', '3')

    tree.write(file_path, encoding='UTF-8', xml_declaration=True)
    print("Refactoring applied to Camisa_Dama_Maestro.val!")
else:
    print("Main draft block 'Corpino_y_Manga' not found.")
