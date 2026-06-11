import sys

file_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'id="207"' in line and 'type="simpleInteractive"' in line:
        # Left Cap: from Left Armpit (204) to Top (200)
        # angle1 is Armpit, angle2 is Top
        # We want it to leave armpit horizontally towards center (0 degrees)
        # and arrive at Top horizontally from left (angle2=180)
        line = line.replace('angle1="90"', 'angle1="0"')
        line = line.replace('angle2="180"', 'angle2="180"') # unchanged
        line = line.replace('* 0.25"', '* 0.4"')
        line = line.replace('* 0.55"', '* 0.6"')
    elif 'id="208"' in line and 'type="simpleInteractive"' in line:
        # Right Cap: from Top (200) to Right Armpit (205)
        # angle1 is Top, angle2 is Armpit
        # We want it to leave Top horizontally towards right (0 degrees)
        # and arrive at Armpit horizontally from top-left (angle2=180, pointing left)
        line = line.replace('angle1="0"', 'angle1="0"') # unchanged
        line = line.replace('angle2="90"', 'angle2="180"')
        line = line.replace('* 0.55"', '* 0.6"')
        line = line.replace('* 0.25"', '* 0.4"')
        
    new_lines.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Sleeve S-curves (ondas) properly fixed.")
