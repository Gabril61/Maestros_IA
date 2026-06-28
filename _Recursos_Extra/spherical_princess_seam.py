import re

def spherical_princess_seam():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Sup Spline (207)
    find_207 = r'<spline angle1="[^"]*" angle2="[^"]*" color="black" id="207" length1="[^"]*" length2="[^"]*"'
    replace_207 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Sup_F_APEX - 18" angle2="AngleLine_F_Sisa_Pinza_Sup_F_APEX + 180 + 18" color="black" id="207" length1="Line_F_Sisa_Pinza_Sup_F_APEX * 0.35" length2="Line_F_Sisa_Pinza_Sup_F_APEX * 0.35"'
    content = re.sub(find_207, replace_207, content)

    # Inf Spline (209)
    find_209 = r'<spline angle1="[^"]*" angle2="[^"]*" color="black" id="209" length1="[^"]*" length2="[^"]*"'
    replace_209 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 18" angle2="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 180 - 18" color="black" id="209" length1="Line_F_Sisa_Pinza_Inf_F_APEX * 0.38" length2="Line_F_Sisa_Pinza_Inf_F_APEX * 0.38"'
    content = re.sub(find_209, replace_209, content)

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Spherical princess seam applied.")

if __name__ == "__main__":
    spherical_princess_seam()
