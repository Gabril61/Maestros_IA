import re

file_path = "Blazer_Dama_Maestro.val"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Instead of replacing up to </nodes>, let's find the start of the sleeve logic
# and replace exactly the sleeve nodes we care about.
# The sleeve logic we want to replace starts at:
# <point angle="270" basePoint="100" id="12000" ... name="MS_Origen"
start_marker = '<point angle="270" basePoint="100" id="12000"'
start_idx = content.find(start_marker)

if start_idx == -1:
    print("Could not find start marker")
    exit(1)

# Now, let's find the end of the nodes. We know the last sleeve node is id="89612" (Ale_Baj_Puno_Ext) or similar,
# but to be totally safe without deleting non-sleeve nodes, we can just replace everything from start_marker
# to the </nodes> tag OF THE CURRENT DRAFTBLOCK.
# Wait, let's find the first </nodes> AFTER start_idx!
end_idx = content.find('</nodes>', start_idx)

# What if there are other nodes after the sleeve in the SAME draftBlock?
# Let's inspect what is between the last known sleeve node and </nodes>
# In my previous print, the last points were:
# 12256: <point firstPoint="12017" id="89610" length="#largo_aletilla_efectivo" ... name="Ale_Baj_Top" ...
# 12352: <point angle="0" basePoint="12017" id="89612" length="#ancho_aletilla" ... name="Ale_Baj_Puno_Ext" ...
# Let's search for "Ale_Baj_Puno_Ext"
last_sleeve_node_idx = content.find('name="Ale_Baj_Puno_Ext"')
if last_sleeve_node_idx != -1:
    # Find the end of this node's tag
    end_of_last_node = content.find('/>', last_sleeve_node_idx) + 2
    
    # Are there any other nodes between end_of_last_node and </nodes>?
    remaining_text = content[end_of_last_node:end_idx].strip()
    if remaining_text:
        print("WARNING: There are other nodes after the sleeve!")
        print(remaining_text[:500])
        # In this case, we ONLY replace up to end_of_last_node
        replace_end_idx = end_of_last_node
    else:
        # It's safe to replace up to end_idx (but not including </nodes>)
        replace_end_idx = end_idx
else:
    # If Ale_Baj_Puno_Ext is not found, maybe the old file didn't have it.
    # Let's just find the last node before </nodes>
    replace_end_idx = end_idx


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
            <point angle="180 - AngleLine_Corte_Frente_Codo_Corte_Frente_Puno" basePoint="30013" id="89502" length="@D_RUEDO_MANGA" mx="0.1" my="0.1" name="Ext_Corte_Frente" showPointName="true" type="endLine"/>
            <point angle="180 - AngleLine_Fold_Espalda_Codo_Fold_Espalda_Puno" basePoint="23003" id="23007" length="@D_RUEDO_MANGA" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="Ext_MS_Aletilla" showPointName="true" type="endLine"/>
            
            <line firstPoint="89501" id="89511" lineColor="black" secondPoint="89500"/>
            <line firstPoint="89500" id="89512" lineColor="black" secondPoint="23007"/>
            <line firstPoint="23003" id="89513" lineColor="black" secondPoint="23007"/>
            <line firstPoint="12014" id="89514" lineColor="black" secondPoint="89501"/>
            <line firstPoint="30013" id="89515" lineColor="blue" lineType="dashLine" secondPoint="89502"/>
"""

new_content = content[:start_idx] + new_sleeve_nodes + "\n        " + content[replace_end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Safe refactor completed successfully!")
