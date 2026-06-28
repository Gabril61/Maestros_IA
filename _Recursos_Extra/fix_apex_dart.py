import re

def fix_apex_dart():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix Spline Sup (207)
    find_207 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Sup_F_APEX - 5" angle2="AngleLine_F_Sisa_Pinza_Sup_F_APEX \+ 180 \+ 5" color="black" id="207" length1="Line_F_Sisa_Pinza_Sup_F_APEX \* 0\.3" length2="Line_F_Sisa_Pinza_Sup_F_APEX \* 0\.3" lineWeight="0\.7" point1="701" point4="14" type="simpleInteractive" />'
    replace_207 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Sup_F_APEX - 12" angle2="AngleLine_F_Pinza_P1_F_APEX" color="black" id="207" length1="Line_F_Sisa_Pinza_Sup_F_APEX * 0.35" length2="Line_F_Sisa_Pinza_Sup_F_APEX * 0.35" lineWeight="0.7" point1="701" point4="14" type="simpleInteractive" />'
    content = re.sub(find_207, replace_207, content)

    # Fix Spline Inf (209)
    find_209 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Inf_F_APEX - 5" angle2="AngleLine_F_Sisa_Pinza_Inf_F_APEX \+ 180 \+ 5" color="black" id="209" length1="Line_F_Sisa_Pinza_Inf_F_APEX \* 0\.3" length2="Line_F_Sisa_Pinza_Inf_F_APEX \* 0\.3" lineWeight="0\.7" point1="702" point4="14" type="simpleInteractive" />'
    replace_209 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 12" angle2="AngleLine_F_Pinza_P2_F_APEX" color="black" id="209" length1="Line_F_Sisa_Pinza_Inf_F_APEX * 0.35" length2="Line_F_Sisa_Pinza_Inf_F_APEX * 0.35" lineWeight="0.7" point1="702" point4="14" type="simpleInteractive" />'
    content = re.sub(find_209, replace_209, content)

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Apex dart splines fixed.")

if __name__ == "__main__":
    fix_apex_dart()
