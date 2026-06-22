import re

file_path = "Blazer_Dama_Maestro.val"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<point id="12000" mx="0.1" my="0.1" name="MS_Origen" showPointName="true" type="single" x="150" y="0"/>'
end_marker = '<point firstPoint="12042" id="14005" length="CurrentLength/2" mx="0.1" my="0.1" name="A7_Piquete" secondPoint="12041" showPointName="true" type="alongLine"/>'

replacement_block = """<point angle="270" basePoint="12000" id="12001" length="@S_LARGO_MANGA" mx="0.1" my="0.1" name="MS_Largo" showPointName="true" type="endLine"/>
            <point angle="270" basePoint="12000" id="12002" length="(@S_LARGO_MANGA/2)+2" mx="0.1" my="0.1" name="MS_Codo" showPointName="true" type="endLine"/>
            <point angle="270" basePoint="12000" id="12003" length="(@S_CONT_SISA / 3) + 1" mx="0.1" my="0.1" name="MS_Copa_Alto" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="12003" id="12004" length="((@S_CONT_BICEP + #holgura_biceps) / 4) + 1.5" mx="0.1" my="0.1" name="MS_Ancho_Cimera_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12003" id="12005" length="((@S_CONT_BICEP + #holgura_biceps) / 4) + 1.5" mx="0.1" my="0.1" name="MS_Ancho_Cimera_Der" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="12003" id="12006" length="((@S_CONT_BICEP + #holgura_biceps) / 4) - 1.5" mx="0.1" my="0.1" name="MS_Ancho_Bajera_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12003" id="12007" length="((@S_CONT_BICEP + #holgura_biceps) / 4) - 1.5" mx="0.1" my="0.1" name="MS_Ancho_Bajera_Der" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="12002" id="12010" length="(((@S_CONT_BICEP + #holgura_biceps) / 4) + ((@S_CONT_PUNO + #holgura_puno) / 4)) / 2 + 2" mx="0.1" my="0.1" name="MS_Codo_Cimera_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12002" id="12011" length="(((@S_CONT_BICEP + #holgura_biceps) / 4) + ((@S_CONT_PUNO + #holgura_puno) / 4)) / 2 + 2" mx="0.1" my="0.1" name="MS_Codo_Cimera_Der" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="12002" id="12012" length="(((@S_CONT_BICEP + #holgura_biceps) / 4) + ((@S_CONT_PUNO + #holgura_puno) / 4)) / 2 - 1.5" mx="0.1" my="0.1" name="MS_Codo_Bajera_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12002" id="12013" length="(((@S_CONT_BICEP + #holgura_biceps) / 4) + ((@S_CONT_PUNO + #holgura_puno) / 4)) / 2 - 1.5" mx="0.1" my="0.1" name="MS_Codo_Bajera_Der" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="12001" id="12014" length="((@S_CONT_PUNO + #holgura_puno) / 4) + 1.5" mx="0.721382" my="-5.59601" name="MS_Puno_Cimera_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12001" id="12015" length="((@S_CONT_PUNO + #holgura_puno) / 4) + 1.5" mx="0.1" my="0.1" name="MS_Puno_Cimera_Der" showPointName="true" type="endLine"/>
            <point angle="180" basePoint="12001" id="12016" length="((@S_CONT_PUNO + #holgura_puno) / 4) - 1.5" mx="-9.84212" my="-5.59601" name="MS_Puno_Bajera_Izq" showPointName="true" type="endLine"/>
            <point angle="0" basePoint="12001" id="12017" length="((@S_CONT_PUNO + #holgura_puno) / 4) - 1.5" mx="0.410691" my="-5.28531" name="MS_Puno_Bajera_Der" showPointName="true" type="endLine"/>
            <spline angle1="90" angle2="180" color="black" id="12020" length1="Line_MS_Ancho_Cimera_Izq_MS_Origen * 0.55" length2="Line_MS_Ancho_Cimera_Izq_MS_Origen * 0.55" point1="12004" point4="12000" type="simpleInteractive"/>
            <spline angle1="0" angle2="90" color="black" id="12021" length1="Line_MS_Origen_MS_Ancho_Cimera_Der * 0.55" length2="Line_MS_Origen_MS_Ancho_Cimera_Der * 0.55" point1="12000" point4="12005" type="simpleInteractive"/>
            <spline angle1="270" angle2="270" color="blue" id="12022" length1="Line_MS_Ancho_Bajera_Izq_MS_Ancho_Bajera_Der * 0.15" length2="Line_MS_Ancho_Bajera_Izq_MS_Ancho_Bajera_Der * 0.15" point1="12006" point4="12007" type="simpleInteractive"/>
            <line firstPoint="12010" id="12031" lineColor="black" secondPoint="12014"/>
            <line firstPoint="12011" id="12033" lineColor="black" secondPoint="12015"/>
            <line firstPoint="12014" id="12034" lineColor="black" secondPoint="12015"/>
            <line firstPoint="12012" id="12036" lineColor="blue" secondPoint="12016"/>
            <line firstPoint="12007" id="12037" lineColor="blue" secondPoint="12013"/>
            <line firstPoint="12013" id="12038" lineColor="blue" secondPoint="12017"/>
            <line firstPoint="12016" id="12039" lineColor="blue" secondPoint="12017"/>
            <point firstPoint="23" id="12041" length="10" lineColor="black" lineType="none" lineWeight="0.35" mx="0.132292" my="0.264583" name="A1" secondPoint="11004" showPointName="true" type="alongLine"/>
            <point angle="0" firstPoint="12041" id="12042" length="9" lineColor="black" lineType="dashLine" lineWeight="0.35" mx="-3.60182" my="0.151428" name="A2" secondPoint="23" showPointName="true" type="normal"/>
            <line firstPoint="12042" id="12044" lineColor="black" lineType="solidLine" lineWeight="0.35" secondPoint="12041"/>
            <spline angle1="260" angle2="100" color="black" id="12045" length1="5" length2="5" lineWeight="0.35" penStyle="solidLine" point1="12042" point4="11004" type="simpleInteractive"/>"""

pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)

if pattern.search(content):
    new_content = pattern.sub(start_marker + "\n" + replacement_block + "\n            " + end_marker, content)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully restored lines")
else:
    print("Could not find the block to replace!")
