import re

val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
with open(val_path, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'<spline[^>]+id="209"[^>]*>', content)
if match:
    print(match.group(0))
