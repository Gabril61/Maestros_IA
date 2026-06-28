import re

def fix_inversion():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Sup Spline (207) - Must bulge UP-LEFT (Away from dart)
    # Using + 18 for angle1, - 18 for angle2
    find_207 = r'<spline angle1="[^"]*" angle2="[^"]*" color="black" id="207" length1="[^"]*" length2="[^"]*"'
    replace_207 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Sup_F_APEX + 15" angle2="AngleLine_F_Sisa_Pinza_Sup_F_APEX + 180 - 15" color="black" id="207" length1="Line_F_Sisa_Pinza_Sup_F_APEX * 0.3" length2="Line_F_Sisa_Pinza_Sup_F_APEX * 0.3"'
    content = re.sub(find_207, replace_207, content)

    # Inf Spline (209) - Must bulge DOWN-RIGHT (Away from dart)
    # Using - 18 for angle1, + 18 for angle2
    find_209 = r'<spline angle1="[^"]*" angle2="[^"]*" color="black" id="209" length1="[^"]*" length2="[^"]*"'
    replace_209 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Inf_F_APEX - 15" angle2="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 180 + 15" color="black" id="209" length1="Line_F_Sisa_Pinza_Inf_F_APEX * 0.3" length2="Line_F_Sisa_Pinza_Inf_F_APEX * 0.3"'
    content = re.sub(find_209, replace_209, content)

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Inversion fixed. Eye shape restored.")

if __name__ == "__main__":
    fix_inversion()
