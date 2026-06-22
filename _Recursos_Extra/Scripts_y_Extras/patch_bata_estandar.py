import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update T_Ancho_Espalda and T_Costado_Sisa, and insert points before them
# Target 1:
t1_search = r'<point angle="180" basePoint="209" id="210" length="\(@S_ANCHO_ESPALDA/2\) - 0\.5" name="T_Ancho_Espalda" type="endLine"/>'
t1_replace = r'''<point angle="180" basePoint="209" curve="20002" id="20005" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Inter_Pecho" showPointName="false" type="curveIntersectAxis"/>
            <point angle="180" basePoint="20005" id="210" length="(@S_ANCHO_ESPALDA/2) - 0.5" name="T_Ancho_Espalda" type="endLine"/>'''
content = re.sub(t1_search, t1_replace, content)

# Target 2:
t2_search = r'<point angle="180" basePoint="207" id="211" length="\(\(@S_CONT_BUSTO \+ #holgura_bata\)/4\)" name="T_Costado_Sisa" type="endLine"/>'
t2_replace = r'''<point angle="180" basePoint="207" curve="20002" id="20006" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Inter_Sisa" showPointName="false" type="curveIntersectAxis"/>
            <point angle="180" basePoint="20006" id="211" length="((@S_CONT_BUSTO + #holgura_bata)/4)" name="T_Costado_Sisa" type="endLine"/>'''
content = re.sub(t2_search, t2_replace, content)

# 3. Update T_Costado_Cintura basePoint
t3_search = r'<point angle="180" basePoint="216" id="219" length="\(\(@S_CONT_BUSTO \+ #holgura_bata\)/4\) - 2" name="T_Costado_Cintura" type="endLine"/>'
t3_replace = r'<point angle="180" basePoint="250" id="219" length="((@S_CONT_BUSTO + #holgura_bata)/4) - 2" name="T_Costado_Cintura" type="endLine"/>'
content = re.sub(t3_search, t3_replace, content)

# 4. Update spline idObject in modeling
t4_search = r'<spline id="30084" idObject="247" inUse="true" type="modelingSpline"/>'
t4_replace = r'<spline id="30084" idObject="20002" inUse="true" type="modelingSpline"/>'
content = re.sub(t4_search, t4_replace, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully.")
