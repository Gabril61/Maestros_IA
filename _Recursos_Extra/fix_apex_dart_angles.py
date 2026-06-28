import re

def fix_apex_dart_angles():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix AngleLine_F_Pinza_P1_F_APEX
    content = content.replace(
        'angle2="AngleLine_F_Pinza_P1_F_APEX"',
        'angle2="AngleLine_F_APEX_F_Pinza_P1 + 180"'
    )

    # Fix AngleLine_F_Pinza_P2_F_APEX
    content = content.replace(
        'angle2="AngleLine_F_Pinza_P2_F_APEX"',
        'angle2="AngleLine_F_APEX_F_Pinza_P2 + 180"'
    )

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Apex dart angles fixed.")

if __name__ == "__main__":
    fix_apex_dart_angles()
