import re

def add_side_curves():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Front Line 201 to dashLine and add Spline 20100
    find_201 = r'(<line firstPoint="5" id="201" lineColor="black" lineType=")solidLine(" lineWeight=")0.7(" secondPoint="200" />)'
    replace_201 = (
        r'\1dashLine\g<2>0.35\g<3>\n'
        r'            <spline angle1="AngleLine_F_Costado_Sisa_F_Costado_Real - 5" angle2="AngleLine_F_Costado_Real_F_Costado_Sisa + 5" color="black" id="20100" length1="Line_F_Costado_Sisa_F_Costado_Real * 0.33" length2="Line_F_Costado_Sisa_F_Costado_Real * 0.33" lineWeight="0.7" point1="5" point4="200" type="simpleInteractive" />'
    )
    content = re.sub(find_201, replace_201, content)

    # 2. Update Back Line 212 to dashLine and add Spline 21200
    find_212 = r'(<line firstPoint="104" id="212" lineColor="black" lineType=")solidLine(" lineWeight=")0.7(" secondPoint="211" />)'
    replace_212 = (
        r'\1dashLine\g<2>0.35\g<3>\n'
        r'            <spline angle1="AngleLine_T_Costado_Sisa_T_Costado_Real + 5" angle2="AngleLine_T_Costado_Real_T_Costado_Sisa - 5" color="black" id="21200" length1="Line_T_Costado_Sisa_T_Costado_Real * 0.33" length2="Line_T_Costado_Sisa_T_Costado_Real * 0.33" lineWeight="0.7" point1="104" point4="211" type="simpleInteractive" />'
    )
    content = re.sub(find_212, replace_212, content)

    # 3. Update Modeling for Front (90121)
    find_mod_front = r'(<point id="90121" idObject="200".*?/>)'
    replace_mod_front = (
        r'<spline id="901210" idObject="20100" inUse="true" type="modelingSpline" />\n            \1'
    )
    content = re.sub(find_mod_front, replace_mod_front, content)

    # 4. Update Modeling for Back (90145)
    find_mod_back = r'(<point id="90145" idObject="104".*?/>)'
    replace_mod_back = (
        r'<spline id="901450" idObject="21200" inUse="true" type="modelingSpline" />\n            \1'
    )
    content = re.sub(find_mod_back, replace_mod_back, content)

    # 5. Update Nodes for Front Piece 90123
    find_nodes_front = r'(<node idObject="90121" type="NodePoint" />)'
    replace_nodes_front = (
        r'<node idObject="901210" reverse="0" type="NodeSpline" />\n                    \1'
    )
    content = re.sub(find_nodes_front, replace_nodes_front, content)

    # 6. Update Nodes for Back Piece 90150
    find_nodes_back = r'(<node idObject="90145" type="NodePoint" />)'
    replace_nodes_back = (
        r'<node idObject="901450" reverse="1" type="NodeSpline" />\n                    \1'
    )
    content = re.sub(find_nodes_back, replace_nodes_back, content)

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Side curves added successfully.")

if __name__ == "__main__":
    add_side_curves()
