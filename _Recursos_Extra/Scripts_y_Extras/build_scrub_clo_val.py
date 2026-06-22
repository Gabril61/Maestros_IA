import os

xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<pattern>
    <version>0.7.3</version>
    <unit>cm</unit>
    <description>Scrub Top Medico (Estilo CLO 3D) - TextilFit M.A.S.</description>
    <notes>Patron maestro generado desde cero basado en las proporciones paramétricas de CLO 3D.</notes>
    <measurements>Maestro_Variables_IA.smis</measurements>
    <variables>
        <variable description="Holgura pecho por cuarto" formula="5.0" name="#holgura_pecho"/>
        <variable description="Caida de Hombro Drop" formula="10.0" name="#caida_hombro_extra"/>
        <variable description="Largo de Manga" formula="24.0" name="#largo_manga_corta"/>
    </variables>
    <draftBlock name="Scrub_Top_Clo">
        <calculation>
            <!-- ESPALDA -->
            <point id="1" mx="0" my="0" name="E_Origen" type="single" x="0" y="0"/>
            <point angle="270" basePoint="1" id="2" length="@S_TALLE_TRASERO + 25" name="E_Largo_Total" type="endLine"/>
            <line firstPoint="1" id="3" secondPoint="2"/>
            
            <point angle="270" basePoint="1" id="4" length="4.3" name="E_Cuello_Prof" type="endLine"/>
            <point angle="0" basePoint="1" id="5" length="(@S_CONT_CUELLO / 6) + 2" name="E_Cuello_Ancho" type="endLine"/>
            <spline angle1="270" angle2="180" id="6" length1="Line_E_Origen_E_Cuello_Prof * 0.5" length2="Line_E_Origen_E_Cuello_Ancho * 0.5" point1="4" point4="5" type="simpleInteractive"/>
            
            <point angle="0" basePoint="1" id="7" length="(@S_CONT_BUSTO / 4) + #holgura_pecho" name="E_Ancho_Pecho" type="endLine"/>
            <point angle="0" basePoint="2" id="8" length="(@S_CONT_BUSTO / 4) + #holgura_pecho" name="E_Ruedo_Costado" type="endLine"/>
            <line firstPoint="7" id="9" secondPoint="8"/>
            <line firstPoint="2" id="10" secondPoint="8"/>
            
            <point angle="270" basePoint="7" id="11" length="(@S_TALLE_TRASERO / 2) - 5" name="E_Axila" type="endLine"/>
            
            <point angle="0" basePoint="1" id="12" length="(@S_ANCHO_ESPALDA / 2) + #caida_hombro_extra" name="E_Hombro_Guia" type="endLine"/>
            <point angle="270" basePoint="12" id="13" length="(@S_TALLE_TRASERO / 10)" name="E_Hombro_Punta" type="endLine"/>
            <line firstPoint="5" id="14" secondPoint="13"/>
            
            <spline angle1="AngleLine_E_Cuello_Ancho_E_Hombro_Punta - 90" angle2="90" id="15" length1="Line_E_Hombro_Punta_E_Axila * 0.5" length2="Line_E_Hombro_Punta_E_Axila * 0.5" point1="13" point4="11" type="simpleInteractive"/>
            <line firstPoint="11" id="16" secondPoint="8"/>
            <line firstPoint="4" id="17" secondPoint="2"/>

            <!-- DELANTERO -->
            <point id="100" mx="0" my="0" name="D_Origen" type="single" x="100" y="0"/>
            <point angle="270" basePoint="100" id="101" length="Line_E_Origen_E_Largo_Total" name="D_Largo_Total" type="endLine"/>
            <line firstPoint="100" id="102" secondPoint="101"/>
            
            <point angle="270" basePoint="100" id="103" length="@S_TALLE_DELANTERO * 0.45" name="D_Cuello_Prof" type="endLine"/>
            <point angle="180" basePoint="100" id="104" length="Line_E_Origen_E_Cuello_Ancho" name="D_Cuello_Ancho" type="endLine"/>
            <line firstPoint="104" id="105" secondPoint="103"/>
            
            <point angle="180" basePoint="100" id="106" length="Line_E_Origen_E_Ancho_Pecho" name="D_Ancho_Pecho" type="endLine"/>
            <point angle="180" basePoint="101" id="107" length="Line_E_Largo_Total_E_Ruedo_Costado" name="D_Ruedo_Costado" type="endLine"/>
            <line firstPoint="106" id="108" secondPoint="107"/>
            <line firstPoint="101" id="109" secondPoint="107"/>
            
            <point angle="270" basePoint="106" id="110" length="Line_E_Ancho_Pecho_E_Axila" name="D_Axila" type="endLine"/>
            
            <point angle="180" basePoint="100" id="111" length="Line_E_Origen_E_Hombro_Guia" name="D_Hombro_Guia" type="endLine"/>
            <point angle="270" basePoint="111" id="112" length="Line_E_Hombro_Guia_E_Hombro_Punta" name="D_Hombro_Punta" type="endLine"/>
            <line firstPoint="104" id="113" secondPoint="112"/>
            
            <spline angle1="AngleLine_D_Cuello_Ancho_D_Hombro_Punta + 90" angle2="90" id="114" length1="Line_D_Hombro_Punta_D_Axila * 0.5" length2="Line_D_Hombro_Punta_D_Axila * 0.5" point1="112" point4="110" type="simpleInteractive"/>
            <line firstPoint="110" id="115" secondPoint="107"/>
            <line firstPoint="103" id="116" secondPoint="101"/>

            <!-- MANGA -->
            <point id="200" mx="0" my="0" name="M_Origen" type="single" x="200" y="0"/>
            <point angle="270" basePoint="200" id="201" length="#largo_manga_corta" name="M_Largo_Total" type="endLine"/>
            <line firstPoint="200" id="202" secondPoint="201"/>
            
            <point angle="270" basePoint="200" id="203" length="(@S_ANCHO_ESPALDA / 4)" name="M_Nivel_Copa" type="endLine"/>
            <point angle="180" basePoint="203" id="204" length="Line_E_Hombro_Punta_E_Axila * 1.2" name="M_Sisa_Izq" type="endLine"/>
            <point angle="0" basePoint="203" id="205" length="Line_D_Hombro_Punta_D_Axila * 1.2" name="M_Sisa_Der" type="endLine"/>
            <line firstPoint="204" id="206" secondPoint="205"/>
            
            <spline angle1="90" angle2="0" id="207" length1="Line_M_Origen_M_Sisa_Izq * 0.4" length2="Line_M_Origen_M_Sisa_Izq * 0.4" point1="204" point4="200" type="simpleInteractive"/>
            <spline angle1="180" angle2="90" id="208" length1="Line_M_Origen_M_Sisa_Der * 0.4" length2="Line_M_Origen_M_Sisa_Der * 0.4" point1="200" point4="205" type="simpleInteractive"/>
            
            <point angle="180" basePoint="201" id="209" length="Line_M_Nivel_Copa_M_Sisa_Izq * 0.8" name="M_Ruedo_Izq" type="endLine"/>
            <point angle="0" basePoint="201" id="210" length="Line_M_Nivel_Copa_M_Sisa_Der * 0.8" name="M_Ruedo_Der" type="endLine"/>
            <line firstPoint="209" id="211" secondPoint="210"/>
            <line firstPoint="204" id="212" secondPoint="209"/>
            <line firstPoint="205" id="213" secondPoint="210"/>

            <!-- BOLSILLO -->
            <point id="300" mx="0" my="0" name="B_Origen" type="single" x="300" y="0"/>
            <point angle="270" basePoint="300" id="301" length="(@S_TALLE_DELANTERO / 2) - 3" name="B_Alto" type="endLine"/>
            <point angle="0" basePoint="300" id="302" length="(@S_CONT_BUSTO / 6)" name="B_Ancho_Top" type="endLine"/>
            <point angle="0" basePoint="301" id="303" length="(@S_CONT_BUSTO / 6)" name="B_Ancho_Bot" type="endLine"/>
            <line firstPoint="300" id="304" secondPoint="301"/>
            <line firstPoint="300" id="305" secondPoint="302"/>
            <line firstPoint="301" id="306" secondPoint="303"/>
            <line firstPoint="302" id="307" secondPoint="303"/>
            
        </calculation>
        <modeling>
            <point id="400" idObject="4" inUse="true" type="modeling"/>
            <point id="401" idObject="2" inUse="true" type="modeling"/>
            <point id="402" idObject="8" inUse="true" type="modeling"/>
            <point id="403" idObject="11" inUse="true" type="modeling"/>
            <spline id="405" idObject="15" inUse="true" type="modelingSpline"/>
            <point id="406" idObject="13" inUse="true" type="modeling"/>
            <point id="407" idObject="5" inUse="true" type="modeling"/>
            <spline id="408" idObject="6" inUse="true" type="modelingSpline"/>
            
            <point id="500" idObject="101" inUse="true" type="modeling"/>
            <point id="501" idObject="103" inUse="true" type="modeling"/>
            <point id="503" idObject="104" inUse="true" type="modeling"/>
            <point id="504" idObject="112" inUse="true" type="modeling"/>
            <spline id="505" idObject="114" inUse="true" type="modelingSpline"/>
            <point id="506" idObject="110" inUse="true" type="modeling"/>
            <point id="507" idObject="107" inUse="true" type="modeling"/>
            
            <point id="600" idObject="204" inUse="true" type="modeling"/>
            <spline id="601" idObject="207" inUse="true" type="modelingSpline"/>
            <point id="602" idObject="200" inUse="true" type="modeling"/>
            <spline id="603" idObject="208" inUse="true" type="modelingSpline"/>
            <point id="604" idObject="205" inUse="true" type="modeling"/>
            <point id="605" idObject="210" inUse="true" type="modeling"/>
            <point id="606" idObject="209" inUse="true" type="modeling"/>
            
            <point id="700" idObject="300" inUse="true" type="modeling"/>
            <point id="701" idObject="301" inUse="true" type="modeling"/>
            <point id="702" idObject="303" inUse="true" type="modeling"/>
            <point id="703" idObject="302" inUse="true" type="modeling"/>
        </modeling>
        <pieces>
            <piece id="410" inLayout="true" name="Espalda" seamAllowance="true" version="2">
                <nodes>
                    <node idObject="400" type="NodePoint"/>
                    <node idObject="401" type="NodePoint"/>
                    <node idObject="402" type="NodePoint"/>
                    <node idObject="403" type="NodePoint"/>
                    <node idObject="405" reverse="1" type="NodeSpline"/>
                    <node idObject="406" type="NodePoint"/>
                    <node idObject="407" type="NodePoint"/>
                    <node idObject="408" reverse="1" type="NodeSpline"/>
                </nodes>
            </piece>
            <piece id="510" inLayout="true" name="Delantero" seamAllowance="true" version="2">
                <nodes>
                    <node idObject="500" type="NodePoint"/>
                    <node idObject="501" type="NodePoint"/>
                    <node idObject="503" type="NodePoint"/>
                    <node idObject="504" type="NodePoint"/>
                    <node idObject="505" reverse="0" type="NodeSpline"/>
                    <node idObject="506" type="NodePoint"/>
                    <node idObject="507" type="NodePoint"/>
                </nodes>
            </piece>
            <piece id="610" inLayout="true" name="Manga" seamAllowance="true" version="2">
                <nodes>
                    <node idObject="600" type="NodePoint"/>
                    <node idObject="601" reverse="0" type="NodeSpline"/>
                    <node idObject="602" type="NodePoint"/>
                    <node idObject="603" reverse="0" type="NodeSpline"/>
                    <node idObject="604" type="NodePoint"/>
                    <node idObject="605" type="NodePoint"/>
                    <node idObject="606" type="NodePoint"/>
                </nodes>
            </piece>
            <piece id="710" inLayout="true" name="Bolsillo" seamAllowance="true" version="2">
                <nodes>
                    <node idObject="700" type="NodePoint"/>
                    <node idObject="701" type="NodePoint"/>
                    <node idObject="702" type="NodePoint"/>
                    <node idObject="703" type="NodePoint"/>
                </nodes>
            </piece>
        </pieces>
    </draftBlock>
</pattern>
"""

out_path = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(xml_content)
print("Archivo generado exitosamente:", out_path)
