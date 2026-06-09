import re

file_path = "Blazer_Dama_Maestro.val"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<point angle="270" basePoint="100" id="12000"'
end_marker = '</nodes>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

# To be safe, I will ONLY replace up to the last known point we added: Ext_MS_Aletilla_Bajera or Ale_Baj_Puno_Ext
# Let's see what the last line before </nodes> actually is.
last_node_block = content[start_idx:end_idx]

new_sleeve_nodes = """<point angle="270" basePoint="100" id="12000" length="0" mx="0.1" my="0.1" name="MS_Origen" showPointName="true" type="endLine"/>
            <point angle="270" basePoint="12000" id="12001" length="@S_LARGO_MANGA" mx="0.1" my="0.1" name="MS_Largo" showPointName="true" type="endLine"/>
            <point angle="270" basePoint="12000" id="12002" length="(@S_LARGO_MANGA/2)+2" mx="0.1" my="0.1" name="MS_Codo" showPointName="true" type="endLine"/>
            <point firstPoint="12000" id="12003" length="(@S_CONT_BUSTO / 10) + 4" mx="0.1" my="0.1" name="MS_Copa_Alto" secondPoint="12001" showPointName="true" type="alongLine"/>
            
            <point angle="180" basePoint="12003" id="12004" length="(@S_CONT_BICEP + #holgura_biceps) / 2" mx="0.1" my="0.1" name="MS_Ancho_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12003" id="12005" length="(@S_CONT_BICEP + #holgura_biceps) / 2" mx="0.1" my="0.1" name="MS_Ancho_Der" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="12002" id="12010" length="(((@S_CONT_BICEP + #holgura_biceps) / 2) + ((@S_CONT_PUNO + #holgura_puno) / 2)) / 2" mx="0.1" my="0.1" name="MS_Codo_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12002" id="12011" length="(((@S_CONT_BICEP + #holgura_biceps) / 2) + ((@S_CONT_PUNO + #holgura_puno) / 2)) / 2" mx="0.1" my="0.1" name="MS_Codo_Der" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="12001" id="12014" length="(@S_CONT_PUNO + #holgura_puno) / 2" mx="0.721382" my="-5.59601" name="MS_Puno_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12001" id="12015" length="(@S_CONT_PUNO + #holgura_puno) / 2" mx="0.1" my="0.1" name="MS_Puno_Der" showPointName="true" type="endLine"/>
            
            <line firstPoint="12004" id="12031" lineColor="black" secondPoint="12010"/>
            <line firstPoint="12010" id="12032" lineColor="black" secondPoint="12014"/>
            <line firstPoint="12005" id="12033" lineColor="black" secondPoint="12011"/>
            <line firstPoint="12011" id="12034" lineColor="black" secondPoint="12015"/>
            
            <spline angle1="90" angle2="180" color="black" id="12020" length1="Line_MS_Ancho_Izq_MS_Origen * 0.55" length2="Line_MS_Ancho_Izq_MS_Origen * 0.55" point1="12004" point4="12000" type="simpleInteractive"/>
            <spline angle1="0" angle2="270" color="black" id="12021" length1="Line_MS_Origen_MS_Ancho_Der * 0.55" length2="Line_MS_Origen_MS_Ancho_Der * 0.55" point1="12000" point4="12005" type="simpleInteractive"/>
            
            <point angle="180" basePoint="12003" id="30001" length="((@S_CONT_BICEP + #holgura_biceps) / 2) / 2" mx="0.1" my="0.1" name="Fold_Frente_Bicep" showPointName="false" type="endLine"/>
            <point angle="0" basePoint="12003" id="30002" length="((@S_CONT_BICEP + #holgura_biceps) / 2) / 2" mx="0.1" my="0.1" name="Fold_Espalda_Bicep" showPointName="false" type="endLine"/>
            <point angle="180" basePoint="12002" id="30003" length="Line_MS_Codo_MS_Codo_Izq / 2" mx="0.1" my="0.1" name="Fold_Frente_Codo" showPointName="false" type="endLine"/>
            <point angle="0" basePoint="12002" id="30004" length="Line_MS_Codo_MS_Codo_Der / 2" mx="0.1" my="0.1" name="Fold_Espalda_Codo" showPointName="false" type="endLine"/>
            <point angle="180" basePoint="12001" id="30005" length="Line_MS_Largo_MS_Puno_Izq / 2" mx="0.1" my="0.1" name="Fold_Frente_Puno" showPointName="false" type="endLine"/>
            <point angle="0" basePoint="12001" id="30006" length="Line_MS_Largo_MS_Puno_Der / 2" mx="0.1" my="0.1" name="Fold_Espalda_Puno" showPointName="false" type="endLine"/>
            
            <point angle="180" basePoint="30001" id="30011" length="-3" mx="0.1" my="0.1" name="Corte_Frente_Bicep" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="30003" id="30012" length="-3" mx="0.1" my="0.1" name="Corte_Frente_Codo" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="30005" id="30013" length="-3" mx="0.1" my="0.1" name="Corte_Frente_Puno" showPointName="true" type="endLine"/>
            
            <point id="30014" idObject="30002" inUse="false" mx="0.1" my="0.1" name="Corte_Espalda_Bicep" showPointName="true" type="modeling"/>
            <point id="30015" idObject="30004" inUse="false" mx="0.1" my="0.1" name="Corte_Espalda_Codo" showPointName="true" type="modeling"/>
            <point id="30016" idObject="30006" inUse="false" mx="0.1" my="0.1" name="Corte_Espalda_Puno" showPointName="true" type="modeling"/>
            
            <line firstPoint="30011" id="30021" lineColor="blue" lineType="dashLine" secondPoint="30012"/>
            <line firstPoint="30012" id="30022" lineColor="blue" lineType="dashLine" secondPoint="30013"/>
            <line firstPoint="30002" id="30023" lineColor="blue" lineType="dashLine" secondPoint="30004"/>
            <line firstPoint="30004" id="30024" lineColor="blue" lineType="dashLine" secondPoint="30006"/>
            
            <point angle="90" basePoint="30011" curve="12020" id="30031" mx="0.1" my="0.1" name="Copa_Frente_Pico" showPointName="true" type="curveIntersectAxis"/>
            <point angle="90" basePoint="30002" curve="12021" id="30032" mx="0.1" my="0.1" name="Copa_Espalda_Pico" showPointName="true" type="curveIntersectAxis"/>
            
            <line firstPoint="30011" id="30033" lineColor="blue" lineType="dashLine" secondPoint="30031"/>
            <line firstPoint="30002" id="30034" lineColor="blue" lineType="dashLine" secondPoint="30032"/>
            
            <point firstPoint="30006" id="23001" length="12" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Top" secondPoint="30004" showPointName="false" type="alongLine"/>
            <point angle="AngleLine_Fold_Espalda_Codo_Fold_Espalda_Puno + 90" basePoint="23001" id="23002" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Top_Ext" showPointName="true" type="endLine"/>
            <point angle="AngleLine_Fold_Espalda_Codo_Fold_Espalda_Puno + 90" basePoint="30006" id="23003" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Bot_Ext" showPointName="true" type="endLine"/>
            <line firstPoint="23002" id="23004" lineColor="blue" secondPoint="23003"/>
            <line firstPoint="23001" id="23005" lineColor="blue" secondPoint="23002"/>
            <line firstPoint="30006" id="23006" lineColor="blue" secondPoint="23003"/>
            
            <point angle="270" basePoint="12001" id="89500" length="@D_RUEDO_MANGA" mx="0.1" my="0.1" name="Ext_MS_Largo" showPointName="true" type="endLine"/>
            <point angle="180 - AngleLine_MS_Codo_Izq_MS_Puno_Izq" basePoint="12014" id="89501" length="@D_RUEDO_MANGA" mx="-4.7675" my="1.34276" name="Ext_MS_Puno_Izq" showPointName="true" type="endLine"/>
            <point angle="180 - AngleLine_Fold_Frente_Codo_Corte_Frente_Puno" basePoint="30013" id="89502" length="@D_RUEDO_MANGA" mx="0.1" my="0.1" name="Ext_Corte_Frente" showPointName="true" type="endLine"/>
            <point angle="180 - AngleLine_Fold_Espalda_Codo_Fold_Espalda_Puno" basePoint="23003" id="23007" length="@D_RUEDO_MANGA" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="Ext_MS_Aletilla" showPointName="true" type="endLine"/>
            
            <line firstPoint="89501" id="89511" lineColor="black" secondPoint="89500"/>
            <line firstPoint="89500" id="89512" lineColor="black" secondPoint="23007"/>
            <line firstPoint="23003" id="89513" lineColor="black" secondPoint="23007"/>
            <line firstPoint="12014" id="89514" lineColor="black" secondPoint="89501"/>
            <line firstPoint="30013" id="89515" lineColor="blue" lineType="dashLine" secondPoint="89502"/>
"""

# Wait, the line angle 180 - AngleLine_Fold_Frente_Codo_Corte_Frente_Puno is invalid!
# I used "Corte_Frente_Puno" which is 30013. The line is "Corte_Frente_Codo_Corte_Frente_Puno".
# The line is between 30012 and 30013. So it should be AngleLine_Corte_Frente_Codo_Corte_Frente_Puno.
# Let me fix that.
new_sleeve_nodes = new_sleeve_nodes.replace("AngleLine_Fold_Frente_Codo_Corte_Frente_Puno", "AngleLine_Corte_Frente_Codo_Corte_Frente_Puno")

new_content = content[:start_idx] + new_sleeve_nodes + "\n        " + content[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Sleeve overlay refactor completed successfully!")
