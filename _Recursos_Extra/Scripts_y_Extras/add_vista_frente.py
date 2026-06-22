import sys
import os

def modify_val(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    calc_nodes = """
            <point firstPoint="23" id="99001" length="Line_F_Cuello_Ancho_F_Hombro / 2" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Mitad_Hombro" secondPoint="28" showPointName="true" type="alongLine"/>
            <point curve="89003" id="99002" length="Spl_B_Ruedo_Curva_V_F_Ruedo_Pinza * 0.4" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Vista_Hem" showPointName="true" type="alongCurve"/>
            <spline angle1="270" angle2="90" color="black" id="99003" length1="Line_F_Mitad_Hombro_F_Vista_Hem * 0.3" length2="Line_F_Mitad_Hombro_F_Vista_Hem * 0.3" lineWeight="0.7" penStyle="solidLine" point1="99001" point4="99002" type="simpleInteractive"/>
"""
    modeling_nodes = """
            <point id="99103" idObject="99002" inUse="true" mx="0.1" my="0.1" showPointName="true" type="modeling"/>
            <spline id="99104" idObject="89003" inUse="true" type="modelingSpline"/>
            <point id="99105" idObject="11004" inUse="true" mx="0.1" my="0.1" showPointName="true" type="modeling"/>
            <spline id="99106" idObject="12045" inUse="true" type="modelingSpline"/>
            <point id="99107" idObject="12041" inUse="true" mx="0.132292" my="0.264583" showPointName="true" type="modeling"/>
            <point id="99108" idObject="23" inUse="true" mx="0.1" my="0.1" showPointName="true" type="modeling"/>
            <point id="99101" idObject="99001" inUse="true" mx="0.1" my="0.1" showPointName="true" type="modeling"/>
            <spline id="99102" idObject="99003" inUse="true" type="modelingSpline"/>
"""
    piece_node = """
            <piece color="#ffffff" fill="nobrush" forbidFlipping="true" hideMainPath="false" id="99201" inLayout="true" locked="false" mx="50" my="0" name="Vista_Frente" seamAllowance="true" united="false" version="2" width="1">
                <data annotation="" foldPosition="Indefinido" fontSize="18" height="2" letter="V" mx="10" my="10" onFold="false" orientation="Indefinido" quantity="2" rotation="45" rotationWay="Ninguno" tilt="Ninguno" visible="true" width="5">
                    <line alignment="0" bold="false" italic="false" sfIncrement="18" text="Vista Delantera"/>
                </data>
                <patternInfo fontSize="67" height="4" mx="30" my="50" rotation="0" visible="true" width="15"/>
                <grainline arrowLength="1.27" arrows="0" length="2.667" mx="50" my="50" rotation="90" visible="true"/>
                <nodes>
                    <node idObject="99103" type="NodePoint"/>
                    <node idObject="99104" reverse="1" type="NodeSpline"/>
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
            </piece>
"""

    if 'id="99001"' not in content:
        content = content.replace("        </calculation>", calc_nodes.lstrip('\n') + "        </calculation>")
        content = content.replace("        </modeling>", modeling_nodes.lstrip('\n') + "        </modeling>")
        content = content.replace("        </pieces>", piece_node.lstrip('\n') + "        </pieces>")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Vista_Frente successfully injected.")
    else:
        print("Vista_Frente already present.")

if __name__ == '__main__':
    modify_val(r'C:\\Users\\Ricx18\\Desktop\\Maestros_IA\\Blazer_Dama_Maestro.val')
