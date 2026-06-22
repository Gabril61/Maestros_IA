import sys

def fix_val(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new line and spline
    new_nodes = """<line firstPoint="89001" id="99011" lineColor="black" lineType="none" lineWeight="0.35" secondPoint="99002"/>
            <spline angle1="270" angle2="AngleLine_F_Ruedo_Pinza_F_Costado_Ruedo + 180" color="black" id="99010" length1="Line_B_Ruedo_Curva_V_F_Vista_Hem * 0.3" length2="Line_B_Ruedo_Curva_V_F_Vista_Hem * 0.3" lineWeight="0.35" penStyle="solidLine" point1="89001" point4="99002" type="simpleInteractive"/>
"""
    # Insert new nodes into calculation if not present
    if 'id="99010"' not in content:
        content = content.replace("        </calculation>", new_nodes + "        </calculation>")

    # Define the modeling nodes for 99010
    mod_nodes = """<spline id="99110" idObject="99010" inUse="true" type="modelingSpline"/>
"""
    if 'id="99110"' not in content:
        content = content.replace("        </modeling>", mod_nodes + "        </modeling>")

    # The piece definition
    piece_def = """<piece color="#ffffff" fill="nobrush" forbidFlipping="true" hideMainPath="false" id="99201" inLayout="true" locked="false" mx="50" my="0" name="Vista_Frente" seamAllowance="true" united="false" version="2" width="1">
                <data annotation="" foldPosition="Indefinido" fontSize="18" height="2" letter="V" mx="10" my="10" onFold="false" orientation="Indefinido" quantity="2" rotation="45" rotationWay="Ninguno" tilt="Ninguno" visible="true" width="5">
                    <line alignment="0" bold="false" italic="false" sfIncrement="18" text="Vista Delantera"/>
                </data>
                <patternInfo fontSize="67" height="4" mx="30" my="50" rotation="0" visible="true" width="15"/>
                <grainline arrowLength="1.27" arrows="0" length="2.667" mx="50" my="50" rotation="90" visible="true"/>
                <nodes>
                    <node idObject="99103" type="NodePoint"/>
                    <node idObject="99110" reverse="1" type="NodeSpline"/>
                    <node idObject="99105" type="NodePoint"/>
                    <node idObject="99106" reverse="1" type="NodeSpline"/>
                    <node idObject="99107" type="NodePoint"/>
                    <node idObject="99108" type="NodePoint"/>
                    <node idObject="99101" type="NodePoint"/>
                    <node idObject="99102" reverse="0" type="NodeSpline"/>
                </nodes>
                <iPaths>
                    <record path="89155"/>
                </iPaths>
            </piece>"""

    # If the user deleted the piece, it won't be in content. 
    # If it is in content, replace it.
    if 'name="Vista_Frente"' in content:
        import re
        content = re.sub(r'<piece[^>]*name="Vista_Frente"[\s\S]*?</piece>', piece_def, content)
    else:
        content = content.replace("        </pieces>", "            " + piece_def + "\n        </pieces>")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed Vista_Frente spline successfully.")

if __name__ == '__main__':
    fix_val(r'C:\Users\Ricx18\Desktop\Maestros_IA\Blazer_Dama_Maestro.val')
