import re

def fix_chronology():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract spline 10101 and line 10102
    spline_pattern = r'\s*<spline angle1="270" angle2="90" color="black" id="10101".*?/>'
    line_pattern = r'\s*<line firstPoint="10100" id="10102".*?/>'
    
    spline_match = re.search(spline_pattern, content)
    line_match = re.search(line_pattern, content)
    
    if spline_match and line_match:
        spline_str = spline_match.group(0)
        line_str = line_match.group(0)
        
        # Remove them from current position
        content = content.replace(spline_str, '')
        content = content.replace(line_str, '')
        
        # Insert them right before </calculation>
        insert_str = spline_str + line_str + '\n        '
        content = content.replace('</calculation>', insert_str + '</calculation>')
        
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Chronology fixed.")
    else:
        print("Elements not found.")

if __name__ == "__main__":
    fix_chronology()
