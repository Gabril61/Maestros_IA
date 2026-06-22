import re
import sys

with open(r'C:\Users\Ricx18\Desktop\Maestros_IA\Jogger_Temp.val', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update measurements file
content = content.replace('<measurements>Maestro_Variables_IA.smis</measurements>', '<measurements>Mariarlenys_Jogger_Estres.smis</measurements>')

# 2. Update Bota points to use @I_CONT_TOBILLO
content = re.sub(r'(id="19".*?)@I_CONT_RODILLA', r'\1@I_CONT_TOBILLO', content)
content = re.sub(r'(id="20".*?)@I_CONT_RODILLA', r'\1@I_CONT_TOBILLO', content)
content = re.sub(r'(id="36".*?)@I_CONT_RODILLA', r'\1@I_CONT_TOBILLO', content)
content = re.sub(r'(id="37".*?)@I_CONT_RODILLA', r'\1@I_CONT_TOBILLO', content)

# 3. Replace Outseam lines with splines
content = content.replace(
    '<line firstPoint="13" id="23" lineColor="black" lineType="solidLine" lineWeight="0.35" secondPoint="18"/>',
    '<spline angle1="270" angle2="90" color="black" id="23" length1="Line_F_Costado_Tiro_F_Rodilla_Cost * 0.3" length2="Line_F_Costado_Tiro_F_Rodilla_Cost * 0.3" lineWeight="0.35" penStyle="solidLine" point1="13" point4="18" type="simpleInteractive"/>'
)
content = content.replace(
    '<line firstPoint="42" id="46" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="35"/>',
    '<spline angle1="270" angle2="90" color=\"black\" id="46" length1="Line_T_Costado_Tiro_T_Rodilla_Cost * 0.3" length2="Line_T_Costado_Tiro_T_Rodilla_Cost * 0.3" lineWeight="0.7" penStyle="solidLine" point1="42" point4="35" type="simpleInteractive"/>'
)

# 4. Modify Inseam splines 211 and 212
content = content.replace(
    'angle1="AngleLine_F_Rodilla_Ent_F_Gavilan + 180 + 10" angle2="AngleLine_F_Rodilla_Ent_F_Gavilan - 10" color="black" id="211" length1="Line_F_Rodilla_Ent_F_Gavilan * 0.3" length2="Line_F_Rodilla_Ent_F_Gavilan * 0.3" lineWeight="0.35" penStyle="solidLine" point1="11" point4="17"',
    'angle1="AngleLine_F_Gavilan_F_Rodilla_Ent - 10" angle2="90" color="black" id="211" length1="Line_F_Rodilla_Ent_F_Gavilan * 0.2" length2="Line_F_Rodilla_Ent_F_Gavilan * 0.3" lineWeight="0.35" penStyle="solidLine" point1="11" point4="17"'
)
content = content.replace(
    'angle1="AngleLine_T_Rodilla_Ent_T_Gavilan_Bajo + 180 + 10" angle2="AngleLine_T_Rodilla_Ent_T_Gavilan_Bajo - 10" color="black" id="212" length1="Line_T_Rodilla_Ent_T_Gavilan_Bajo * 0.3" length2="Line_T_Rodilla_Ent_T_Gavilan_Bajo * 0.3" lineWeight="0.7" penStyle="solidLine" point1="39" point4="34"',
    'angle1="AngleLine_T_Gavilan_Bajo_T_Rodilla_Ent - 10" angle2="90" color="black" id="212" length1="Line_T_Rodilla_Ent_T_Gavilan_Bajo * 0.2" length2="Line_T_Rodilla_Ent_T_Gavilan_Bajo * 0.3" lineWeight="0.7" penStyle="solidLine" point1="39" point4="34"'
)

# 5. Add to modeling section
content = content.replace('</modeling>', '    <spline id="10121100" idObject="23" inUse="true" type="modelingSpline"/>\n            <spline id="10121101" idObject="46" inUse="true" type="modelingSpline"/>\n        </modeling>')

# 6. Add nodes to Delantero (10121023)
content = content.replace(
    '<node idObject="10121021" reverse="0" type="NodeSpline"/>\n                    <node idObject="10121022"',
    '<node idObject="10121021" reverse="0" type="NodeSpline"/>\n                    <node idObject="10121100" reverse="0" type="NodeSpline"/>\n                    <node idObject="10121022"'
)

# 7. Add nodes to Trasero (10121035)
content = content.replace(
    '<node idObject="10121033" reverse="0" type="NodeSpline"/>\n                    <node idObject="10121034"',
    '<node idObject="10121033" reverse="0" type="NodeSpline"/>\n                    <node idObject="10121101" reverse="0" type="NodeSpline"/>\n                    <node idObject="10121034"'
)

with open(r'C:\Users\Ricx18\Desktop\Prueba_Jogger_Estres\Jogger_Elastica_Dama_Mariarlenys.val', 'w', encoding='utf-8') as f:
    f.write(content)

print("File successfully modified and written.")
