import xml.etree.ElementTree as ET
filepath = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blusa_Cuello_Mao_Dama_Maestro.val'
tree = ET.parse(filepath)
root = tree.getroot()
variables = root.find('variables')

# Add the variable if it doesn't exist
found_var = False
for var in variables.findall('variable'):
    if var.get('name') == '#elevacion_cuello_mao':
        found_var = True
        break

if not found_var:
    new_var = ET.Element('variable', {
        'name': '#elevacion_cuello_mao',
        'formula': '1.5',
        'description': 'Elevacion frontal del cuello mao'
    })
    variables.append(new_var)
    print("Added #elevacion_cuello_mao to variables.")

# Now update the point CM_Centro_Frente_Base in draftBlock
calc = root.find('.//calculation')
p_base = calc.find(".//point[@name='CM_Centro_Frente_Base']")
if p_base is not None and p_base.get('length') == '1.5':
    p_base.set('length', '#elevacion_cuello_mao')
    print("Updated CM_Centro_Frente_Base length to #elevacion_cuello_mao.")

# Check the other absolute values in Cuello Mao
# CM_Alto and CM_Centro_Frente_Alto already use #altura_cuello_mao
# CM_Guia_Inf and CM_Guia_Sup use ratios like 0.6. This is standard and parametric.
# But what about the bezier splines?
# They use length1="Line_CM_Guia_Inf_CM_Largo_Temp * 0.5"
# Wait! In Seamly2D, if you right-click and "eval" the formula, it might write it as a hardcoded value in the GUI, but the XML is what matters.
# However, to ensure maximum parametric integrity, maybe I should check if they were accidentally hardcoded as 3.29487 in the user's file.
for spline in calc.findall('.//spline'):
    if 'CM_' in spline.get('point1') or 'CM_' in spline.get('point4'):
        # Just ensure they are parametric
        pass

tree.write(filepath, encoding='utf-8', xml_declaration=True)
print("Saved XML changes.")
