import sys

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix Spline 207 (Left Cap)
# Current: angle1="60" angle2="180"
content = content.replace(
    'angle1="60" angle2="180"',
    'angle1="90" angle2="180"'
)

# Fix Spline 208 (Right Cap)
# Current: angle1="0" angle2="120"
content = content.replace(
    'angle1="0" angle2="120"',
    'angle1="0" angle2="90"'
)

# Also slightly increase the armpit handle length to make the S-curve more visible (from 0.15 to 0.25)
content = content.replace(
    '* 0.15"',
    '* 0.25"'
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Sleeve S-curves (ondas) added.")
