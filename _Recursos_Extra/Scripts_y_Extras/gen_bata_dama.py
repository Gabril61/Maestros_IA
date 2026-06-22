with open(r"C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val", "w", encoding="utf-8") as file:
    file.write("""<?xml version="1.0" encoding="UTF-8"?>
<pattern>
    <version>0.7.3</version>
    <unit>cm</unit>
    <description>Bata Medica Dama - Corte Princesa</description>
    <notes>Corte princesa desde sisa. Sin cruce externo. Escote trasero profundo.</notes>
    <measurements/>
    <variables>
        <variable description="Contorno de cuello" formula="36.5" name="@S_CONTCUELLO"/>
        <variable description="Ancho de espalda" formula="36" name="@S_ANCHOESP"/>
        <variable description="Talle delantero" formula="44" name="@S_TALLEDEL"/>
        <variable description="Talle trasero" formula="42" name="@S_TALLETRA"/>
        <variable description="Contorno de busto" formula="92" name="@S_CONTBUSTO"/>
        <variable description="Contorno de cadera baja" formula="98" name="@I_CONTCADBA"/>
        <variable description="Largo total de la bata" formula="100" name="@G_LARGOPRENDA"/>
        <variable description="Contorno del brazo" formula="28" name="@S_CONTBRAZO"/>
        <variable description="Largo de manga" formula="60" name="@G_LARGOMANGA"/>
        <variable description="Holgura industrial bata" formula="8" name="@M_HOLGURA_BATA"/>
    </variables>
    <draftBlock name="Bata_Dama">
        <calculation>
            <!-- ========================================================= -->
            <!-- DELANTERO (Origen X=0)                                    -->
            <!-- ========================================================= -->
            <point id="100" mx="0.1" my="0.1" name="F_Origen" type="single" x="0" y="0"/>
            
            <point angle="270" basePoint="100" id="102" length="(@S_CONTCUELLO/6) + 2" name="F_Escote_Alto" type="endLine"/>
            <point angle="270" basePoint="100" id="107" length="(@S_ANCHOESP/2) + 4" name="F_Nivel_Sisa" type="endLine"/>
            <point angle="270" basePoint="100" id="109" length="((@S_ANCHOESP/2)+4)/2" name="F_Nivel_Pecho" type="endLine"/>
            <point angle="270" basePoint="100" id="116" length="@S_TALLEDEL" name="F_Nivel_Cintura" type="endLine"/>
            <point angle="270" basePoint="100" id="118" length="@G_LARGOPRENDA" name="F_Nivel_Largo" type="endLine"/>
            
            <!-- Cuello y Solapa (Sin Cruce) -->
            <point angle="0" basePoint="100" id="101" length="(@S_CONTCUELLO/6) + 1" name="F_Escote_Ancho" type="endLine"/>
            <point angle="125" basePoint="102" id="153" length="7" name="F_Punta_Solapa" type="endLine"/>
            
            <!-- Hombro -->
            <point angle="0" basePoint="100" id="104" length="(@S_ANCHOESP/2)" name="F_Guia_Espalda" type="endLine"/>
            <point angle="270" basePoint="104" id="105" length="4" name="F_Caida_Hombro" type="endLine"/>
            <line firstPoint="101" id="106" secondPoint="105"/>
            
            <!-- Sisa Parametrica -->
            <point angle="0" basePoint="109" id="110" length="(@S_ANCHOESP/2) - 1.5" name="F_Ancho_Pecho" type="endLine"/>
            <point angle="0" basePoint="107" id="111" length="((@S_CONTBUSTO + @M_HOLGURA_BATA)/4)" name="F_Costado_Sisa" type="endLine"/>
            <line firstPoint="105" id="112" secondPoint="110"/>
            <line firstPoint="110" id="113" secondPoint="111"/>
            <spline angle1="AngleLine_F_Escote_Ancho_F_Caida_Hombro - 90" angle2="AngleLine_F_Caida_Hombro_F_Ancho_Pecho + 200" color="black" id="114" length1="Line_F_Caida_Hombro_F_Ancho_Pecho * 0.4" length2="Line_F_Caida_Hombro_F_Ancho_Pecho * 0.4" point1="105" point4="110" type="simpleInteractive"/>
            <spline angle1="AngleLine_F_Caida_Hombro_F_Ancho_Pecho + 20" angle2="180" color="black" id="115" length1="Line_F_Ancho_Pecho_F_Costado_Sisa * 0.4" length2="Line_F_Ancho_Pecho_F_Costado_Sisa * 0.3" point1="110" point4="111" type="simpleInteractive"/>
            
            <!-- Entalle de Costado (Shaping Lateral) -->
            <point angle="0" basePoint="116" id="119" length="((@S_CONTBUSTO + @M_HOLGURA_BATA)/4) - 2" name="F_Costado_Cintura" type="endLine"/>
            <point angle="0" basePoint="118" id="121" length="((@I_CONTCADBA + @M_HOLGURA_BATA)/4) + 4" name="F_Costado_Ruedo" type="endLine"/>
            <line firstPoint="111" id="120" secondPoint="119"/>
            <line firstPoint="119" id="122" secondPoint="121"/>
            <spline angle1="270" angle2="90" color="black" id="130" length1="Line_F_Costado_Sisa_F_Costado_Cintura * 0.5" length2="Line_F_Costado_Sisa_F_Costado_Cintura * 0.5" point1="111" point4="119" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="131" length1="Line_F_Costado_Cintura_F_Costado_Ruedo * 0.5" length2="Line_F_Costado_Cintura_F_Costado_Ruedo * 0.5" point1="119" point4="121" type="simpleInteractive"/>
            
            <!-- Lineas de Solapa -->
            <spline angle1="270" angle2="10" color="black" id="135" length1="3" length2="3" point1="101" point4="153" type="simpleInteractive"/>
            <line firstPoint="153" id="134" secondPoint="102"/>

            <!-- ========================================================= -->
            <!-- CORTE PRINCESA DELANTERO                                  -->
            <!-- ========================================================= -->
            <!-- Puntos de Busto y Pinzas -->
            <point angle="0" basePoint="109" id="160" length="(@S_CONTBUSTO / 10)" name="F_Centro_Busto" type="endLine"/>
            <point angle="0" basePoint="116" id="161" length="(@S_CONTBUSTO / 10)" name="F_Pinza_Centro" type="endLine"/>
            <point angle="180" basePoint="161" id="162" length="1.5" name="F_Pinza_Izq" type="endLine"/>
            <point angle="0" basePoint="161" id="163" length="1.5" name="F_Pinza_Der" type="endLine"/>
            <point angle="0" basePoint="118" id="164" length="(@S_CONTBUSTO / 10)" name="F_Pinza_Ruedo_Centro" type="endLine"/>
            <point angle="180" basePoint="164" id="165" length="2.5" name="F_Pinza_Ruedo_Izq" type="endLine"/>
            <point angle="0" basePoint="164" id="166" length="2.5" name="F_Pinza_Ruedo_Der" type="endLine"/>
            
            <!-- Lineas Base Princesa Frontal -->
            <line firstPoint="110" id="170" secondPoint="160"/>
            <line firstPoint="160" id="171" secondPoint="162"/>
            <line firstPoint="162" id="172" secondPoint="165"/>
            <line firstPoint="160" id="173" secondPoint="163"/>
            <line firstPoint="163" id="174" secondPoint="166"/>
            
            <!-- Curvas Princesa Frontal -->
            <spline angle1="AngleLine_F_Caida_Hombro_F_Ancho_Pecho + 20" angle2="90" color="black" id="180" length1="3" length2="3" point1="110" point4="160" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="181" length1="3" length2="3" point1="160" point4="162" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="182" length1="3" length2="3" point1="162" point4="165" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="183" length1="3" length2="3" point1="160" point4="163" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="184" length1="3" length2="3" point1="163" point4="166" type="simpleInteractive"/>

            <!-- ========================================================= -->
            <!-- TRASERO (Origen X=80)                                     -->
            <!-- ========================================================= -->
            <point id="200" mx="0.1" my="0.1" name="T_Origen" type="single" x="80" y="0"/>
            
            <!-- Ejes y Entalle Central -->
            <point angle="270" basePoint="200" id="216" length="@S_TALLETRA" name="T_Nivel_Cintura" type="endLine"/>
            <point angle="270" basePoint="200" id="218" length="@G_LARGOPRENDA" name="T_Nivel_Largo" type="endLine"/>
            <point angle="180" basePoint="216" id="250" length="2.5" name="T_Centro_Cintura" type="endLine"/>
            
            <!-- Abertura Central Trasera -->
            <point angle="90" basePoint="218" id="230" length="20" name="T_Abertura_Top" type="endLine"/>
            <point angle="180" basePoint="230" id="231" length="5" name="T_Aletilla_Top" type="endLine"/>
            <point angle="180" basePoint="218" id="232" length="5" name="T_Aletilla_Bot" type="endLine"/>
            <line firstPoint="200" id="248" secondPoint="250"/>
            <spline angle1="270" angle2="90" color="black" id="247" length1="Line_T_Origen_T_Nivel_Cintura * 0.5" length2="Line_T_Origen_T_Nivel_Cintura * 0.5" point1="200" point4="250" type="simpleInteractive"/>
            <line firstPoint="250" id="246" secondPoint="230"/>
            <line firstPoint="230" id="245" secondPoint="231"/>
            <line firstPoint="231" id="244" secondPoint="232"/>
            <line firstPoint="232" id="249" secondPoint="218"/>
            
            <!-- Escote Trasero Profundo -->
            <point angle="270" basePoint="200" id="202" length="2.5" name="T_Escote_Profundidad" type="endLine"/>
            <point angle="180" basePoint="200" id="201" length="(@S_CONTCUELLO/6) + 1.5" name="T_Escote_Ancho" type="endLine"/>
            <spline angle1="180" angle2="90" color="black" id="240" length1="2" length2="2" point1="202" point4="201" type="simpleInteractive"/>
            
            <!-- Hombro -->
            <point angle="180" basePoint="200" id="204" length="(@S_ANCHOESP/2)" name="T_Guia_Espalda" type="endLine"/>
            <point angle="270" basePoint="204" id="205" length="3" name="T_Caida_Hombro" type="endLine"/>
            <line firstPoint="201" id="206" secondPoint="205"/>
            
            <!-- Sisa Parametrica Ajustada a 280 grados -->
            <point angle="270" basePoint="200" id="207" length="(@S_ANCHOESP/2) + 4" name="T_Nivel_Sisa" type="endLine"/>
            <point angle="270" basePoint="200" id="209" length="((@S_ANCHOESP/2)+4)/2" name="T_Nivel_Pecho" type="endLine"/>
            <point angle="180" basePoint="209" id="210" length="(@S_ANCHOESP/2) - 0.5" name="T_Ancho_Espalda" type="endLine"/>
            <point angle="180" basePoint="207" id="211" length="((@S_CONTBUSTO + @M_HOLGURA_BATA)/4)" name="T_Costado_Sisa" type="endLine"/>
            <line firstPoint="205" id="212" secondPoint="210"/>
            <line firstPoint="210" id="213" secondPoint="211"/>
            <spline angle1="280" angle2="AngleLine_T_Caida_Hombro_T_Ancho_Espalda + 165" color="black" id="214" length1="Line_T_Caida_Hombro_T_Ancho_Espalda * 0.4" length2="Line_T_Caida_Hombro_T_Ancho_Espalda * 0.4" point1="205" point4="210" type="simpleInteractive"/>
            <spline angle1="AngleLine_T_Caida_Hombro_T_Ancho_Espalda + 345" angle2="0" color="black" id="215" length1="Line_T_Ancho_Espalda_T_Costado_Sisa * 0.4" length2="Line_T_Ancho_Espalda_T_Costado_Sisa * 0.3" point1="210" point4="211" type="simpleInteractive"/>
            
            <!-- Entalle de Costado Trasero -->
            <point angle="180" basePoint="216" id="219" length="((@S_CONTBUSTO + @M_HOLGURA_BATA)/4) - 2" name="T_Costado_Cintura" type="endLine"/>
            <point angle="180" basePoint="218" id="221" length="((@I_CONTCADBA + @M_HOLGURA_BATA)/4) + 4" name="T_Costado_Ruedo" type="endLine"/>
            <line firstPoint="211" id="220" secondPoint="219"/>
            <line firstPoint="219" id="222" secondPoint="221"/>
            <spline angle1="270" angle2="90" color="black" id="241" length1="Line_T_Costado_Sisa_T_Costado_Cintura * 0.5" length2="Line_T_Costado_Sisa_T_Costado_Cintura * 0.5" point1="211" point4="219" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="242" length1="Line_T_Costado_Cintura_T_Costado_Ruedo * 0.5" length2="Line_T_Costado_Cintura_T_Costado_Ruedo * 0.5" point1="219" point4="221" type="simpleInteractive"/>
            <line firstPoint="221" id="243" secondPoint="218"/>
            
            <!-- ========================================================= -->
            <!-- CORTE PRINCESA TRASERO                                    -->
            <!-- ========================================================= -->
            <point angle="180" basePoint="209" id="260" length="(@S_ANCHOESP/4)" name="T_Centro_Escapula" type="endLine"/>
            <point angle="180" basePoint="216" id="261" length="(@S_ANCHOESP/4) + 1.5" name="T_Pinza_Centro" type="endLine"/>
            <point angle="0" basePoint="261" id="262" length="1.5" name="T_Pinza_Der" type="endLine"/>
            <point angle="180" basePoint="261" id="263" length="1.5" name="T_Pinza_Izq" type="endLine"/>
            <point angle="180" basePoint="218" id="264" length="(@S_ANCHOESP/4) + 1.5" name="T_Pinza_Ruedo_Centro" type="endLine"/>
            <point angle="0" basePoint="264" id="265" length="2.5" name="T_Pinza_Ruedo_Der" type="endLine"/>
            <point angle="180" basePoint="264" id="266" length="2.5" name="T_Pinza_Ruedo_Izq" type="endLine"/>
            
            <!-- Lineas Base Princesa Trasero -->
            <line firstPoint="210" id="270" secondPoint="260"/>
            <line firstPoint="260" id="271" secondPoint="262"/>
            <line firstPoint="262" id="272" secondPoint="265"/>
            <line firstPoint="260" id="273" secondPoint="263"/>
            <line firstPoint="263" id="274" secondPoint="266"/>
            
            <!-- Curvas Princesa Trasero -->
            <spline angle1="270" angle2="90" color="black" id="280" length1="3" length2="3" point1="210" point4="260" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="281" length1="3" length2="3" point1="260" point4="262" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="282" length1="3" length2="3" point1="262" point4="265" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="283" length1="3" length2="3" point1="260" point4="263" type="simpleInteractive"/>
            <spline angle1="270" angle2="90" color="black" id="284" length1="3" length2="3" point1="263" point4="266" type="simpleInteractive"/>

        </calculation>
        
        <modeling>
            <!-- Centro Delantero -->
            <point id="401" idObject="101" inUse="true" type="modeling"/>
            <point id="402" idObject="105" inUse="true" type="modeling"/>
            <spline id="403" idObject="114" inUse="true" type="modelingSpline"/>
            <point id="404" idObject="110" inUse="true" type="modeling"/>
            <spline id="405" idObject="180" inUse="true" type="modelingSpline"/>
            <point id="406" idObject="160" inUse="true" type="modeling"/>
            <spline id="407" idObject="181" inUse="true" type="modelingSpline"/>
            <point id="408" idObject="162" inUse="true" type="modeling"/>
            <spline id="409" idObject="182" inUse="true" type="modelingSpline"/>
            <point id="410" idObject="165" inUse="true" type="modeling"/>
            <point id="411" idObject="118" inUse="true" type="modeling"/>
            <point id="412" idObject="116" inUse="true" type="modeling"/>
            <point id="413" idObject="102" inUse="true" type="modeling"/>
            <point id="414" idObject="153" inUse="true" type="modeling"/>
            <spline id="415" idObject="135" inUse="true" type="modelingSpline"/>
            
            <!-- Costadillo Delantero -->
            <point id="420" idObject="110" inUse="true" type="modeling"/>
            <spline id="421" idObject="115" inUse="true" type="modelingSpline"/>
            <point id="422" idObject="111" inUse="true" type="modeling"/>
            <spline id="423" idObject="130" inUse="true" type="modelingSpline"/>
            <point id="424" idObject="119" inUse="true" type="modeling"/>
            <spline id="425" idObject="131" inUse="true" type="modelingSpline"/>
            <point id="426" idObject="121" inUse="true" type="modeling"/>
            <point id="427" idObject="166" inUse="true" type="modeling"/>
            <spline id="428" idObject="184" inUse="true" type="modelingSpline"/>
            <point id="429" idObject="163" inUse="true" type="modeling"/>
            <spline id="430" idObject="183" inUse="true" type="modelingSpline"/>
            
            <!-- Centro Trasero -->
            <point id="440" idObject="201" inUse="true" type="modeling"/>
            <point id="441" idObject="205" inUse="true" type="modeling"/>
            <spline id="442" idObject="214" inUse="true" type="modelingSpline"/>
            <point id="443" idObject="210" inUse="true" type="modeling"/>
            <spline id="444" idObject="280" inUse="true" type="modelingSpline"/>
            <point id="445" idObject="260" inUse="true" type="modeling"/>
            <spline id="446" idObject="281" inUse="true" type="modelingSpline"/>
            <point id="447" idObject="262" inUse="true" type="modeling"/>
            <spline id="448" idObject="282" inUse="true" type="modelingSpline"/>
            <point id="449" idObject="265" inUse="true" type="modeling"/>
            <point id="450" idObject="218" inUse="true" type="modeling"/>
            <point id="451" idObject="232" inUse="true" type="modeling"/>
            <point id="452" idObject="231" inUse="true" type="modeling"/>
            <point id="453" idObject="230" inUse="true" type="modeling"/>
            <point id="454" idObject="250" inUse="true" type="modeling"/>
            <spline id="455" idObject="247" inUse="true" type="modelingSpline"/>
            <point id="456" idObject="200" inUse="true" type="modeling"/>
            <point id="457" idObject="202" inUse="true" type="modeling"/>
            <spline id="458" idObject="240" inUse="true" type="modelingSpline"/>
            
            <!-- Costadillo Trasero -->
            <point id="460" idObject="210" inUse="true" type="modeling"/>
            <spline id="461" idObject="215" inUse="true" type="modelingSpline"/>
            <point id="462" idObject="211" inUse="true" type="modeling"/>
            <spline id="463" idObject="241" inUse="true" type="modelingSpline"/>
            <point id="464" idObject="219" inUse="true" type="modeling"/>
            <spline id="465" idObject="242" inUse="true" type="modelingSpline"/>
            <point id="466" idObject="221" inUse="true" type="modeling"/>
            <point id="467" idObject="266" inUse="true" type="modeling"/>
            <spline id="468" idObject="284" inUse="true" type="modelingSpline"/>
            <point id="469" idObject="263" inUse="true" type="modeling"/>
            <spline id="470" idObject="283" inUse="true" type="modelingSpline"/>
        </modeling>
        <pieces>
            <piece id="600" name="Centro_Delantero">
                <nodes>
                    <node idObject="401" type="NodePoint"/>
                    <node idObject="402" type="NodePoint"/>
                    <node idObject="403" reverse="0" type="NodeSpline"/>
                    <node idObject="404" type="NodePoint"/>
                    <node idObject="405" reverse="0" type="NodeSpline"/>
                    <node idObject="406" type="NodePoint"/>
                    <node idObject="407" reverse="0" type="NodeSpline"/>
                    <node idObject="408" type="NodePoint"/>
                    <node idObject="409" reverse="0" type="NodeSpline"/>
                    <node idObject="410" type="NodePoint"/>
                    <node idObject="411" type="NodePoint"/>
                    <node idObject="412" type="NodePoint"/>
                    <node idObject="413" type="NodePoint"/>
                    <node idObject="414" type="NodePoint"/>
                    <node idObject="415" reverse="0" type="NodeSpline"/>
                </nodes>
            </piece>
            <piece id="601" name="Costadillo_Delantero">
                <nodes>
                    <node idObject="420" type="NodePoint"/>
                    <node idObject="421" reverse="0" type="NodeSpline"/>
                    <node idObject="422" type="NodePoint"/>
                    <node idObject="423" reverse="0" type="NodeSpline"/>
                    <node idObject="424" type="NodePoint"/>
                    <node idObject="425" reverse="0" type="NodeSpline"/>
                    <node idObject="426" type="NodePoint"/>
                    <node idObject="427" type="NodePoint"/>
                    <node idObject="428" reverse="1" type="NodeSpline"/>
                    <node idObject="429" type="NodePoint"/>
                    <node idObject="430" reverse="1" type="NodeSpline"/>
                </nodes>
            </piece>
            <piece id="602" name="Centro_Trasero">
                <nodes>
                    <node idObject="440" type="NodePoint"/>
                    <node idObject="441" type="NodePoint"/>
                    <node idObject="442" reverse="0" type="NodeSpline"/>
                    <node idObject="443" type="NodePoint"/>
                    <node idObject="444" reverse="0" type="NodeSpline"/>
                    <node idObject="445" type="NodePoint"/>
                    <node idObject="446" reverse="0" type="NodeSpline"/>
                    <node idObject="447" type="NodePoint"/>
                    <node idObject="448" reverse="0" type="NodeSpline"/>
                    <node idObject="449" type="NodePoint"/>
                    <node idObject="450" type="NodePoint"/>
                    <node idObject="451" type="NodePoint"/>
                    <node idObject="452" type="NodePoint"/>
                    <node idObject="453" type="NodePoint"/>
                    <node idObject="454" type="NodePoint"/>
                    <node idObject="455" reverse="1" type="NodeSpline"/>
                    <node idObject="456" type="NodePoint"/>
                    <node idObject="457" type="NodePoint"/>
                    <node idObject="458" reverse="0" type="NodeSpline"/>
                </nodes>
            </piece>
            <piece id="603" name="Costadillo_Trasero">
                <nodes>
                    <node idObject="460" type="NodePoint"/>
                    <node idObject="461" reverse="0" type="NodeSpline"/>
                    <node idObject="462" type="NodePoint"/>
                    <node idObject="463" reverse="0" type="NodeSpline"/>
                    <node idObject="464" type="NodePoint"/>
                    <node idObject="465" reverse="0" type="NodeSpline"/>
                    <node idObject="466" type="NodePoint"/>
                    <node idObject="467" type="NodePoint"/>
                    <node idObject="468" reverse="1" type="NodeSpline"/>
                    <node idObject="469" type="NodePoint"/>
                    <node idObject="470" reverse="1" type="NodeSpline"/>
                </nodes>
            </piece>
        </pieces>
        <groups/>
    </draftBlock>
</pattern>
""")
print("Bata Dama generated")
