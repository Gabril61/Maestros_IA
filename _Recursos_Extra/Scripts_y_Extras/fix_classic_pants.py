import re
import os

backup_path = r'C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Maestros\Maestro_Pantalón_Dama_IA01.val'
out_path1 = r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Dama_Clasico_Maestro.val'
out_path2 = r'C:\Users\Ricx18\Desktop\Maestros_IA2\Pantalon_Dama_Clasico_Maestro.val'

with open(backup_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Outseam lines with splines (change lineType to 'none' and add spline)
# For line 23 (Delantero)
content = content.replace(
    '<line firstPoint="13" id="23" lineColor="black" lineType="solidLine" lineWeight="0.35" secondPoint="18"/>',
    '<line firstPoint="13" id="23" lineColor="black" lineType="none" lineWeight="0.35" secondPoint="18"/>\n            <spline angle1="270" angle2="90" color="black" id="2300" length1="Line_F_Costado_Tiro_F_Rodilla_Cost * 0.3" length2="Line_F_Costado_Tiro_F_Rodilla_Cost * 0.3" lineWeight="0.35" penStyle="solidLine" point1="13" point4="18" type="simpleInteractive"/>'
)
# For line 46 (Trasero)
content = content.replace(
    '<line firstPoint="42" id="46" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="35"/>',
    '<line firstPoint="42" id="46" lineColor="black" lineType="none" lineWeight="0.7" secondPoint="35"/>\n            <spline angle1="270" angle2="90" color="black" id="4600" length1="Line_T_Costado_Tiro_T_Rodilla_Cost * 0.3" length2="Line_T_Costado_Tiro_T_Rodilla_Cost * 0.3" lineWeight="0.7" penStyle="solidLine" point1="42" point4="35" type="simpleInteractive"/>'
)

# 2. Modify Inseam splines 211 and 212
content = content.replace(
    'angle1="AngleLine_F_Rodilla_Ent_F_Gavilan + 180 + 10" angle2="AngleLine_F_Rodilla_Ent_F_Gavilan - 10" color="black" id="211" length1="Line_F_Rodilla_Ent_F_Gavilan * 0.3" length2="Line_F_Rodilla_Ent_F_Gavilan * 0.3"',
    'angle1="AngleLine_F_Gavilan_F_Rodilla_Ent - 10" angle2="90" color="black" id="211" length1="Line_F_Rodilla_Ent_F_Gavilan * 0.2" length2="Line_F_Rodilla_Ent_F_Gavilan * 0.3"'
)
content = content.replace(
    'angle1="AngleLine_T_Rodilla_Ent_T_Gavilan_Bajo + 180 + 10" angle2="AngleLine_T_Rodilla_Ent_T_Gavilan_Bajo - 10" color="black" id="212" length1="Line_T_Rodilla_Ent_T_Gavilan_Bajo * 0.3" length2="Line_T_Rodilla_Ent_T_Gavilan_Bajo * 0.3"',
    'angle1="AngleLine_T_Gavilan_Bajo_T_Rodilla_Ent - 10" angle2="90" color="black" id="212" length1="Line_T_Rodilla_Ent_T_Gavilan_Bajo * 0.2" length2="Line_T_Rodilla_Ent_T_Gavilan_Bajo * 0.3"'
)

# 3. Add to modeling section
content = content.replace('</modeling>', '    <spline id="12300" idObject="2300" inUse="true" type="modelingSpline"/>\n            <spline id="14600" idObject="4600" inUse="true" type="modelingSpline"/>\n        </modeling>')

# 4. Add nodes to Delantero piece (insert after node 1068)
content = content.replace(
    '<node idObject="1068" reverse="0" type="NodeSpline"/>\n                    <node idObject="1069" type="NodePoint"/>',
    '<node idObject="1068" reverse="0" type="NodeSpline"/>\n                    <node idObject="12300" reverse="0" type="NodeSpline"/>\n                    <node idObject="1069" type="NodePoint"/>'
)

# 5. Add nodes to Trasero piece (insert after node 1080)
content = content.replace(
    '<node idObject="1080" reverse="0" type="NodeSpline"/>\n                    <node idObject="1081" type="NodePoint"/>',
    '<node idObject="1080" reverse="0" type="NodeSpline"/>\n                    <node idObject="14600" reverse="0" type="NodeSpline"/>\n                    <node idObject="1081" type="NodePoint"/>'
)

for out in [out_path1, out_path2]:
    if os.path.exists(os.path.dirname(out)):
        try:
            with open(out, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Saved to {out}")
        except Exception as e:
            print(f"Error saving to {out}: {e}")
    else:
        print(f"Directory {os.path.dirname(out)} does not exist, skipping.")
