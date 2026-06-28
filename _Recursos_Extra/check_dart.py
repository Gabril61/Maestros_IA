import re

val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
with open(val_path, "r", encoding="utf-8") as f:
    content = f.read()

# Spline from 701 to 14
match1 = re.search(r'<spline[^>]+point1="701"[^>]+point4="14"[^>]*>', content)
if match1:
    print(f"Spline Sup: {match1.group(0)}")

# Spline from 702 to 14
match2 = re.search(r'<spline[^>]+point1="702"[^>]+point4="14"[^>]*>', content)
if match2:
    print(f"Spline Inf: {match2.group(0)}")
