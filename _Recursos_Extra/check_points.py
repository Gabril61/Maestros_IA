import re

val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
with open(val_path, "r", encoding="utf-8") as f:
    content = f.read()

for pt_id in ["5", "200", "104", "211"]:
    match = re.search(r'<point[^>]+id="' + pt_id + r'"[^>]*>', content)
    if match:
        print(f"Point {pt_id}: {match.group(0)}")
    else:
        print(f"Point {pt_id} not found")
