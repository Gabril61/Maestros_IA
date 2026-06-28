import re

def fix_spline_angles():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Front Spline: Replace AngleLine_F_Costado_Real_F_Costado_Sisa + 5
    content = content.replace(
        'angle2="AngleLine_F_Costado_Real_F_Costado_Sisa + 5"',
        'angle2="AngleLine_F_Costado_Sisa_F_Costado_Real + 185"'
    )

    # Back Spline: Replace AngleLine_T_Costado_Real_T_Costado_Sisa - 5
    content = content.replace(
        'angle2="AngleLine_T_Costado_Real_T_Costado_Sisa - 5"',
        'angle2="AngleLine_T_Costado_Sisa_T_Costado_Real + 175"'
    )

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Spline angles fixed.")

if __name__ == "__main__":
    fix_spline_angles()
