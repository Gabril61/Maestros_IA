import sys

def fix_line_formula(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The line to inject
    invisible_line = '<line firstPoint="99001" id="99005" lineColor="black" lineType="none" lineWeight="0.35" secondPoint="99002"/>\n            '
    
    # We want to insert it right before spline 99003
    target_spline = '<spline angle1="270" angle2="90" color="black" id="99003"'
    
    if target_spline in content and invisible_line not in content:
        content = content.replace(target_spline, invisible_line + target_spline)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Invisible line added to satisfy formula.")
    elif invisible_line in content:
        print("Line already added.")
    else:
        print("Target spline not found.")

if __name__ == '__main__':
    fix_line_formula(r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val')
