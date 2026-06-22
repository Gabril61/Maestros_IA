import sys
import os

def fix_val(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    bad_node = '<point curve="89003" id="99002" length="Spl_B_Ruedo_Curva_V_F_Ruedo_Pinza * 0.4" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Vista_Hem" showPointName="true" type="alongCurve"/>'
    
    good_nodes = """<point firstPoint="301" id="99002_guia" length="Line_F_Ruedo_F_Ruedo_Pinza * 0.4" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Vista_Hem_Guia" secondPoint="502" showPointName="false" type="alongLine"/>
            <point angle="270" basePoint="99002_guia" curve="89003" id="99002" lineColor="black" lineType="none" mx="0.1" my="0.1" name="F_Vista_Hem" showPointName="true" type="curveIntersectAxis"/>"""

    if bad_node in content:
        content = content.replace(bad_node, good_nodes)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed alongCurve error successfully.")
    else:
        print("bad_node not found. Maybe already fixed or formatting differs.")

if __name__ == '__main__':
    fix_val(r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val')
