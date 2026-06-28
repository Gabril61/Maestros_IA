import re

def fix_chaleco():
    val_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Femenino_Maestro.val"
    
    with open(val_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. F_Costado_Temp (1200)
    content = re.sub(
        r'id="1200" length="\(\(@S_CONT_BUSTO - @G_CONT_CINTURA\) / 4\) - #pinza_cint_sup"',
        r'id="1200" length="((@S_CONT_BUSTO - @G_CONT_CINTURA) / 4) * 0.5"',
        content
    )

    # 2. F_Pinza_P1 (203) and F_Pinza_P2 (204)
    content = re.sub(
        r'id="203" length="#pinza_cint_sup / 2"',
        r'id="203" length="(((@S_CONT_BUSTO - @G_CONT_CINTURA) / 4) * 0.5) / 2"',
        content
    )
    content = re.sub(
        r'id="204" length="#pinza_cint_sup / 2"',
        r'id="204" length="(((@S_CONT_BUSTO - @G_CONT_CINTURA) / 4) * 0.5) / 2"',
        content
    )

    # 3. T_Costado_Real (211)
    content = re.sub(
        r'id="211" length="\(\(@S_CONT_BUSTO - @G_CONT_CINTURA\) / 4\) - #pinza_cint_sup"',
        r'id="211" length="(((@S_CONT_BUSTO - @G_CONT_CINTURA) / 4) * 0.7) * 0.5"',
        content
    )

    # 4. T_Pinza_P1 (214) and T_Pinza_P2 (215)
    content = re.sub(
        r'id="214" length="#pinza_cint_sup / 2"',
        r'id="214" length="((((@S_CONT_BUSTO - @G_CONT_CINTURA) / 4) * 0.7) * 0.5) / 2"',
        content
    )
    content = re.sub(
        r'id="215" length="#pinza_cint_sup / 2"',
        r'id="215" length="((((@S_CONT_BUSTO - @G_CONT_CINTURA) / 4) * 0.7) * 0.5) / 2"',
        content
    )

    # 5. Insert T_Cintura_Entalle (10100) and Ext_T_Ruedo_Entalle (150060)
    find_101 = r'(<point angle="270" basePoint="100" id="101".*?/>)'
    replace_101 = (
        r'\1\n'
        r'            <point angle="180" basePoint="101" id="10100" length="((@S_CONT_BUSTO - @G_CONT_CINTURA) / 4) * 0.3" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Cintura_Entalle" showPointName="true" type="endLine" />\n'
        r'            <point angle="270" basePoint="10100" id="150060" length="#bajada_ruedo + #ruedo_prenda" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="Ext_T_Ruedo_Entalle" showPointName="true" type="endLine" />'
    )
    content = re.sub(find_101, replace_101, content)

    # 6. Base T_Pinza_Centro on 10100
    content = re.sub(
        r'basePoint="101" id="213"',
        r'basePoint="10100" id="213"',
        content
    )

    # 7. Replace Line 106 with Spline 10101 and Line 10102
    find_106 = r'<line firstPoint="100" id="106".*?/>'
    replace_106 = (
        r'<spline angle1="270" angle2="90" color="black" id="10101" length1="15" length2="15" lineWeight="0.7" point1="113" point4="10100" type="simpleInteractive" />\n'
        r'            <line firstPoint="10100" id="10102" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="150060" />'
    )
    content = re.sub(find_106, replace_106, content)

    # 8. Update Piece Espalda Nodes
    find_nodes = r'<node after="0" idObject="90141" type="NodePoint" />\s*<node after="0" before="0" idObject="90142" type="NodePoint" />'
    replace_nodes = (
        r'<node after="0" idObject="90141" type="NodePoint" />\n'
        r'                    <node idObject="901410" reverse="0" type="NodeSpline" />\n'
        r'                    <node idObject="901411" type="NodePoint" />\n'
        r'                    <node after="0" before="0" idObject="90142" type="NodePoint" />'
    )
    content = re.sub(find_nodes, replace_nodes, content)

    # 9. Update Piece Espalda Modeling
    find_mod = r'<point id="90141" idObject="113".*?/>\s*<point id="90142" idObject="15006".*?/>'
    replace_mod = (
        r'<point id="90141" idObject="113" inUse="true" mx="0.1" my="0.1" showPointName="true" type="modeling" />\n'
        r'            <spline id="901410" idObject="10101" inUse="true" type="modelingSpline" />\n'
        r'            <point id="901411" idObject="10100" inUse="true" mx="0.1" my="0.1" showPointName="true" type="modeling" />\n'
        r'            <point id="90142" idObject="150060" inUse="true" mx="-6.87652" my="-2.88994" showPointName="true" type="modeling" />'
    )
    content = re.sub(find_mod, replace_mod, content)

    with open(val_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("XML updated successfully.")

if __name__ == "__main__":
    fix_chaleco()
