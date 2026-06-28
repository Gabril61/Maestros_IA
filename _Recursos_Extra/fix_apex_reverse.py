import re

def fix_apex_dart_reverse_angles():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix AngleLine_F_APEX_F_Sisa_Pinza_Sup
    content = content.replace(
        'angle2="AngleLine_F_APEX_F_Sisa_Pinza_Sup + 15"',
        'angle2="AngleLine_F_Sisa_Pinza_Sup_F_APEX + 180 + 15"'
    )

    # Fix AngleLine_F_APEX_F_Sisa_Pinza_Inf
    content = content.replace(
        'angle2="AngleLine_F_APEX_F_Sisa_Pinza_Inf - 15"',
        'angle2="AngleLine_F_Sisa_Pinza_Inf_F_APEX + 180 - 15"'
    )

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("Apex dart reverse angles fixed.")

if __name__ == "__main__":
    fix_apex_dart_reverse_angles()
