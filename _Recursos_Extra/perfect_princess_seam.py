import re

def perfect_princess_seam():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Sup Spline (207) - Convex Up/Left
    find_207 = r'<spline angle1="[^"]*" angle2="[^"]*" color="black" id="207" length1="[^"]*" length2="[^"]*"'
    replace_207 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Sup_F_APEX - 15" angle2="AngleLine_F_APEX_F_Sisa_Pinza_Sup + 15" color="black" id="207" length1="Line_F_Sisa_Pinza_Sup_F_APEX * 0.3" length2="Line_F_Sisa_Pinza_Sup_F_APEX * 0.3"'
    content = re.sub(find_207, replace_207, content)

    # Inf Spline (209) - Convex Down/Right, with longer handles to equalize length
    find_209 = r'<spline angle1="[^"]*" angle2="[^"]*" color="black" id="209" length1="[^"]*" length2="[^"]*"'
    replace_209 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 15" angle2="AngleLine_F_APEX_F_Sisa_Pinza_Inf - 15" color="black" id="209" length1="Line_F_Sisa_Pinza_Inf_F_APEX * 0.45" length2="Line_F_Sisa_Pinza_Inf_F_APEX * 0.45"'
    content = re.sub(find_209, replace_209, content)

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Princess seam fixed.")

if __name__ == "__main__":
    perfect_princess_seam()
