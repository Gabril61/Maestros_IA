import re

def calibrate_dart():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix Spline Sup (207)
    # Decrease handle length to 0.25 to reduce length of the longer curve
    # Set angles to bow symmetrically
    find_207 = r'<spline angle1="[^"]*" angle2="[^"]*" color="black" id="207" length1="[^"]*" length2="[^"]*"'
    replace_207 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Sup_F_APEX - 10" angle2="AngleLine_F_Sisa_Pinza_Sup_F_APEX + 180 + 10" color="black" id="207" length1="Line_F_Sisa_Pinza_Sup_F_APEX * 0.25" length2="Line_F_Sisa_Pinza_Sup_F_APEX * 0.25"'
    content = re.sub(find_207, replace_207, content)

    # Fix Spline Inf (209)
    # Increase handle length to 0.45 to increase length of the shorter curve
    # Set angles to bow symmetrically outward
    find_209 = r'<spline angle1="[^"]*" angle2="[^"]*" color="black" id="209" length1="[^"]*" length2="[^"]*"'
    replace_209 = r'<spline angle1="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 15" angle2="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 180 - 15" color="black" id="209" length1="Line_F_Sisa_Pinza_Inf_F_APEX * 0.45" length2="Line_F_Sisa_Pinza_Inf_F_APEX * 0.45"'
    content = re.sub(find_209, replace_209, content)

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Dart calibrated and lengths equalized.")

if __name__ == "__main__":
    calibrate_dart()
