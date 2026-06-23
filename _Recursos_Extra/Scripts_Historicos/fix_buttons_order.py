import xml.etree.ElementTree as ET

def fix_buttons():
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    
    # We need to find the <calculation> block
    calc = root.find('.//calculation')
    
    # Find the button points
    btn1 = None
    btn2 = None
    btn3 = None
    btn4 = None
    
    for el in calc:
        name = el.get('name')
        if name == 'B_Boton_1':
            btn1 = el
        elif name == 'B_Boton_2':
            btn2 = el
        elif name == 'B_Boton_3':
            btn3 = el
        elif name == 'B_Boton_4':
            btn4 = el
            
    if all([btn1, btn2, btn3, btn4]):
        # Update btn4 length for scalability
        btn4.set('length', 'Line_B_Cruce_Cintura_B_Cruce_Ruedo * 0.15')
        
        # Remove them from calc
        calc.remove(btn1)
        calc.remove(btn2)
        calc.remove(btn3)
        calc.remove(btn4)
        
        # Find index of where to insert them. 
        # They should be inserted after the points they depend on:
        # btn1 depends on 14 (F_APEX), 11000 (B_Cruce_Cuello), 11001 (B_Cruce_Cintura).
        # btn4 depends on 11001, 11002 (B_Cruce_Ruedo).
        # We can just insert them at the very end of the <calculation> block, right before the collar nodes,
        # or simply append them at the end of the calculation block. Since they don't have dependents (other than themselves),
        # appending them to the end of calculation is perfectly safe.
        
        # Actually, let's just insert them before the first collar node (14100) to keep them grouped, 
        # or append at the end of calculation.
        # Wait, if any other points (like lines) depended on buttons, they need to be after buttons.
        # Let's insert them right where the original btn1 was.
        
    tree = ET.parse('Chaleco_Femenino_Maestro.val')
    root = tree.getroot()
    calc = root.find('.//calculation')
    
    # Let's do it cleanly:
    # First, collect all children
    children = list(calc)
    
    # Remove the 4 buttons
    b1_idx = -1
    for i, child in enumerate(children):
        if child.get('name') == 'B_Boton_1':
            b1_idx = i
            break
            
    buttons = []
    for name in ['B_Boton_1', 'B_Boton_4', 'B_Boton_2', 'B_Boton_3']:
        for child in list(calc):
            if child.get('name') == name:
                buttons.append(child)
                calc.remove(child)
                break
                
    # Update btn4
    for b in buttons:
        if b.get('name') == 'B_Boton_4':
            b.set('length', 'Line_B_Cruce_Cintura_B_Cruce_Ruedo * 0.15')
            
    # Insert them back at b1_idx
    for b in reversed(buttons):
        calc.insert(b1_idx, b)
        
    tree.write('Chaleco_Femenino_Maestro.val', encoding='UTF-8', xml_declaration=True)
    print("Buttons reordered and scalability fixed.")

if __name__ == '__main__':
    fix_buttons()
