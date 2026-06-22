import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'

original_content = """<?xml version="1.0" encoding="UTF-8"?>
<pattern>
    <version>0.7.3</version>
    <unit>cm</unit>
    <description>Chaleco Halter Dama - TextilFit M.A.S.</description>
    <notes>Chaleco halter con corte princesa frontal y espalda Racerback</notes>
    <measurements>Maestro_Variables_IA.smis</measurements>
    <variables>
        <variable description="Holgura para chaleco ajustado" formula="2" name="#holgura_chaleco"/>
    </variables>
    <draftBlock name="Chaleco_Halter_Dama">
        <calculation>
            <!-- ============================== -->
            <!-- DELANTERO HALTER -->
            <!-- ============================== -->
            <point id="2" mx="0" my="0" name="D_Origen" type="single" x="0" y="0"/>
            <point angle="270" basePoint="2" id="3" length="@S_ALTO_BUSTO" name="D_Nivel_Busto" type="endLine"/>
            <line firstPoint="2" id="4" secondPoint="3"/>
            <point angle="270" basePoint="2" id="5" length="@S_TALLE_DELANTERO" name="D_Nivel_Cintura" type="endLine"/>
            <line firstPoint="3" id="6" secondPoint="5"/>
            <!-- Eje Central Frontal (Botonera) -->
            <point angle="90" basePoint="5" id="9" length="@S_TALLE_DELANTERO * 0.18" name="D_Boton_Inicio" type="endLine"/>
            <point angle="270" basePoint="5" id="7" length="@S_TALLE_DELANTERO * 0.2" name="D_Botonera_Fin" type="endLine"/>
            <line firstPoint="9" id="8" secondPoint="7"/>
            <!-- Hombro / Tirante Halter (Escala proporcional) -->
            <point angle="0" basePoint="2" id="10" length="(@S_CONT_CUELLO / 6) + 1" name="D_Cuello_Int" type="endLine"/>
            <line firstPoint="2" id="11" secondPoint="10"/>
            <point angle="345" basePoint="10" id="12" length="(@S_ANCHO_ESPALDA / 10) + 0.4" name="D_Cuello_Ext" type="endLine"/>
            <line firstPoint="10" id="13" secondPoint="12"/>
            <!-- Curva Escote Halter -->
            <line firstPoint="10" id="14" secondPoint="9"/>
            <spline angle1="260" angle2="75" id="15" length1="Line_D_Cuello_Int_D_Boton_Inicio * 0.35" length2="Line_D_Cuello_Int_D_Boton_Inicio * 0.35" point1="10" point4="9" type="simpleInteractive"/>
            <!-- Niveles de Sisa Tradicional (Usado solo como anclaje de orientacion fantasma) -->
            <point angle="270" basePoint="2" id="16" length="(@S_ANCHO_ESPALDA / 2) + 4" name="D_Nivel_Sisa" type="endLine"/>
            <!-- ROTURA DEL ANCLAJE DE SISA: El costado ahora cae hasta el nivel de busto -->
            <point angle="0" basePoint="3" id="19" length="(@S_CONT_BUSTO + #holgura_chaleco) / 4" name="D_Costado_Sisa" type="endLine"/>
            <!-- Costado y Ruedo -->
            <point angle="0" basePoint="5" id="22" length="((@G_CONT_CINTURA + #holgura_chaleco) / 4) + @D_PINZA_CINT_SUP" name="D_Costado_Cintura" type="endLine"/>
            <line firstPoint="19" id="23" secondPoint="22"/>
            <point angle="270" basePoint="22" id="24" length="4" name="D_Costado_Ruedo" type="endLine"/>
            <line firstPoint="22" id="25" secondPoint="24"/>
            <!-- Puntos Base para el Corte Princesa -->
            <point angle="0" basePoint="3" id="17" length="@S_SEP_BUSTO / 2" name="D_Punto_Pezon" type="endLine"/>
            <line firstPoint="3" id="18" secondPoint="17"/>
            <!-- Punto Fantasma para la trayectoria normal del corte princesa -->
            <point angle="0" basePoint="16" id="37" length="(@S_SEP_BUSTO / 2) + 1.5" name="D_Princesa_Sisa_Estandar" type="endLine"/>
            <line firstPoint="17" id="370" secondPoint="37"/>
            <!-- ANCLAJE BOOLEANO PROYECTADO (Aprobado por Taller) -->
            <!-- Proyectamos la línea princesa "más arriba y afuera" sin romper su trayectoria original (factor 2) -->
            <point firstPoint="17" id="38" length="Line_D_Punto_Pezon_D_Princesa_Sisa_Estandar * 2" name="D_Princesa_Sisa_Real" secondPoint="37" type="alongLine"/>
            <!-- Líneas Guía para inicializar las variables de longitud -->
            <line firstPoint="12" id="39" secondPoint="38"/>
            <line firstPoint="38" id="40" secondPoint="19"/>
            <line firstPoint="38" id="41" secondPoint="17"/>
            <!-- Pinza de sisa (Apertura de volumen tridimensional) -->
            <point angle="AngleLine_D_Princesa_Sisa_Real_D_Costado_Sisa" basePoint="38" id="3800" length="2.5" name="D_Princesa_Sisa_Inf" type="endLine"/>
            <line firstPoint="3800" id="3801" secondPoint="19"/>
            <line firstPoint="3800" id="3802" secondPoint="17"/>
            <!-- COMPOSICIÓN DE SISA EN 2 SPLINES (Calibración Visual Definitiva del Taller) -->
            <spline angle1="265" angle2="115" id="28" length1="Line_D_Cuello_Ext_D_Princesa_Sisa_Real * 0.3" length2="Line_D_Cuello_Ext_D_Princesa_Sisa_Real * 0.5" point1="12" point4="38" type="simpleInteractive"/>
            <spline angle1="260" angle2="180" id="29" length1="Line_D_Princesa_Sisa_Inf_D_Costado_Sisa * 0.1" length2="(@S_ANCHO_ESPALDA / 10) + 1" point1="3800" point4="19" type="simpleInteractive"/>
            <!-- Curva del Corte Princesa hacia el Busto -->
            <spline angle1="AngleLine_D_Princesa_Sisa_Real_D_Punto_Pezon - 15" angle2="AngleLine_D_Punto_Pezon_D_Pinza_Izq - 180" id="42" length1="Line_D_Princesa_Sisa_Real_D_Punto_Pezon * 0.35" length2="Line_D_Princesa_Sisa_Real_D_Punto_Pezon * 0.35" point1="38" point4="17" type="simpleInteractive"/>
            <spline angle1="AngleLine_D_Princesa_Sisa_Inf_D_Punto_Pezon + 15" angle2="AngleLine_D_Punto_Pezon_D_Pinza_Der - 180" id="420" length1="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35" length2="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35" point1="3800" point4="17" type="simpleInteractive"/>
            <!-- Pinza y PICO PRINCESA -->
            <point angle="270" basePoint="17" id="43" length="@S_TALLE_DELANTERO - @S_ALTO_BUSTO" name="D_Centro_Pinza" type="endLine"/>
            <point angle="180" basePoint="43" id="44" length="@D_PINZA_CINT_SUP / 2" name="D_Pinza_Izq" type="endLine"/>
            <point angle="0" basePoint="43" id="45" length="@D_PINZA_CINT_SUP / 2" name="D_Pinza_Der" type="endLine"/>
            <point angle="270" basePoint="43" id="46" length="@S_TALLE_DELANTERO * 0.3" name="D_Pico_Princesa" type="endLine"/>
            <line firstPoint="17" id="47" secondPoint="44"/>
            <line firstPoint="17" id="48" secondPoint="45"/>
            <line firstPoint="44" id="49" secondPoint="46"/>
            <line firstPoint="45" id="50" secondPoint="46"/>
            <!-- UBICACIÓN BOLSILLO DELANTERO (Bolsillo de ribete) -->
            <!-- Anclado paramétricamente debajo de la cintura y escalado según el busto -->
            <point angle="270" basePoint="43" id="61" length="@S_TALLE_DELANTERO * 0.15" name="D_Bolsillo_Centro" type="endLine"/>
            <point angle="180" basePoint="61" id="62" length="(@S_CONT_BUSTO / 20) + 1" name="D_Bolsillo_Izq" type="endLine"/>
            <point angle="0" basePoint="61" id="63" length="(@S_CONT_BUSTO / 20) + 1" name="D_Bolsillo_Der" type="endLine"/>
            <line firstPoint="62" id="64" secondPoint="63"/>
            <!-- Conectar Ruedo Delantero -->
            <line firstPoint="7" id="51" secondPoint="46"/>
            <line firstPoint="46" id="52" secondPoint="24"/>
            <!-- DOBLADILLOS DELANTERO -->
            <point angle="270" basePoint="7" id="53" length="3" name="D_Dobladillo_Botonera" type="endLine"/>
            <point angle="270" basePoint="46" id="54" length="3" name="D_Dobladillo_Pico" type="endLine"/>
            <line firstPoint="7" id="55" secondPoint="53"/>
            <line firstPoint="46" id="56" secondPoint="54"/>
            <line firstPoint="53" id="57" secondPoint="54"/>
            <point angle="540 - AngleLine_D_Costado_Cintura_D_Costado_Ruedo" basePoint="24" id="58" length="3" name="D_Dobladillo_Costado" type="endLine"/>
            <line firstPoint="24" id="59" secondPoint="58"/>
            <line firstPoint="54" id="60" secondPoint="58"/>
            <!-- ============================== -->
            <!-- ESPALDA RACERBACK -->
            <!-- ============================== -->
            <point id="100" mx="0" my="0" name="E_Origen" type="single" x="100" y="0"/>
            <point angle="270" basePoint="100" id="101" length="@S_TALLE_TRASERO" name="E_Nivel_Cintura" type="endLine"/>
            <line firstPoint="100" id="102" secondPoint="101"/>
            <!-- La Sisa de la Espalda se alarga drasticamente para igualar el nivel del delantero -->
            <point angle="90" basePoint="101" id="104" length="@S_TALLE_DELANTERO - @S_ALTO_BUSTO" name="E_Nivel_Busto_Lateral" type="endLine"/>
            <point angle="180" basePoint="104" id="105" length="(@S_CONT_BUSTO + #holgura_chaleco) / 4" name="E_Costado_Sisa" type="endLine"/>
            <line firstPoint="104" id="106" secondPoint="105"/>
            <point angle="180" basePoint="101" id="108" length="((@G_CONT_CINTURA + #holgura_chaleco) / 4) + @D_PINZA_CINT_SUP" name="E_Costado_Cintura" type="endLine"/>
            <line firstPoint="101" id="109" secondPoint="108"/>
            <line firstPoint="105" id="110" secondPoint="108"/>
            <!-- Ruedo Espalda -->
            <point angle="270" basePoint="101" id="111" length="4" name="E_Centro_Ruedo" type="endLine"/>
            <line firstPoint="101" id="112" secondPoint="111"/>
            <point angle="270" basePoint="108" id="113" length="4" name="E_Costado_Ruedo" type="endLine"/>
            <line firstPoint="108" id="114" secondPoint="113"/>
            <line firstPoint="111" id="115" secondPoint="113"/>
            <!-- DOBLADILLO ESPALDA -->
            <point angle="270" basePoint="111" id="116" length="3" name="E_Dobladillo_Centro" type="endLine"/>
            <line firstPoint="111" id="117" secondPoint="116"/>
            <point angle="540 - AngleLine_E_Costado_Cintura_E_Costado_Ruedo" basePoint="113" id="118" length="3" name="E_Dobladillo_Costado" type="endLine"/>
            <line firstPoint="113" id="119" secondPoint="118"/>
            <line firstPoint="116" id="120" secondPoint="118"/>
            <!-- Escote Trasero -->
            <point angle="180" basePoint="100" id="121" length="(@S_CONT_CUELLO / 6) + 1.5" name="E_Ancho_Escote" type="endLine"/>
            <point angle="270" basePoint="100" id="122" length="0.5" name="E_Prof_Escote" type="endLine"/>
            <line firstPoint="100" id="123" secondPoint="121"/>
            <line firstPoint="100" id="124" secondPoint="122"/>
            <line firstPoint="121" id="125" secondPoint="122"/>
            <spline angle1="280" angle2="180" id="126" length1="Line_E_Ancho_Escote_E_Prof_Escote * 0.1" length2="Line_E_Ancho_Escote_E_Prof_Escote * 0.35" point1="121" point4="122" type="simpleInteractive"/>
            <!-- Tirante Espalda -->
            <point angle="195" basePoint="121" id="128" length="(@S_ANCHO_ESPALDA / 10) + 0.4" name="E_Cuello_Ext" type="endLine"/>
            <line firstPoint="121" id="129" secondPoint="128"/>
            <!-- Sisa Cavada Racerback (Escalable: 16cm en talla M) -->
            <point angle="270" basePoint="100" id="130" length="(@S_TALLE_TRASERO / 2) - 3" name="E_Mitad_Espalda" type="endLine"/>
            <point angle="180" basePoint="130" id="131" length="(@S_ANCHO_ESPALDA / 4) - 1" name="E_Cavado_Racer" type="endLine"/>
            <!-- Líneas Guía para inicializar las variables de longitud de espalda -->
            <line firstPoint="128" id="133" secondPoint="131"/>
            <line firstPoint="131" id="134" secondPoint="105"/>
            <spline angle1="300" angle2="80" id="135" length1="Line_E_Cuello_Ext_E_Cavado_Racer * 0.4" length2="Line_E_Cuello_Ext_E_Cavado_Racer * 0.4" point1="128" point4="131" type="simpleInteractive"/>
            <spline angle1="250" angle2="0" id="136" length1="Line_E_Cavado_Racer_E_Costado_Sisa * 0.4" length2="Line_E_Cavado_Racer_E_Costado_Sisa * 0.4" point1="131" point4="105" type="simpleInteractive"/>
            <!-- Pinza de Espalda -->
            <point angle="180" basePoint="101" id="137" length="(@G_CONT_CINTURA / 10) + 1" name="E_Centro_Pinza" type="endLine"/>
            <point angle="180" basePoint="137" id="138" length="@D_PINZA_CINT_SUP / 2" name="E_Pinza_Der" type="endLine"/>
            <point angle="0" basePoint="137" id="139" length="@D_PINZA_CINT_SUP / 2" name="E_Pinza_Izq" type="endLine"/>
            <point angle="90" basePoint="137" id="140" length="12" name="E_Pinza_Top" type="endLine"/>
            <point angle="270" basePoint="137" id="141" length="4" name="E_Pinza_Bot" type="endLine"/>
            <line firstPoint="140" id="142" secondPoint="138"/>
            <line firstPoint="140" id="143" secondPoint="139"/>
            <line firstPoint="138" id="144" secondPoint="141"/>
            <line firstPoint="139" id="145" secondPoint="141"/>
        </calculation>
        <modeling>
            <point id="371" idObject="58" inUse="false" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="372" idObject="54" inUse="false" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="373" idObject="53" inUse="false" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="374" idObject="9" inUse="false" mx="10" my="15" showPointName="true" type="modeling"/>
            <spline id="375" idObject="15" inUse="false" type="modelingSpline"/>
            <point id="376" idObject="12" inUse="false" mx="10" my="15" showPointName="true" type="modeling"/>
            <spline id="377" idObject="28" inUse="false" type="modelingSpline"/>
            <spline id="378" idObject="29" inUse="false" type="modelingSpline"/>
            <point id="379" idObject="22" inUse="false" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="380" idObject="54" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="381" idObject="53" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="382" idObject="9" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <spline id="383" idObject="15" inUse="true" type="modelingSpline"/>
            <point id="384" idObject="12" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <spline id="385" idObject="28" inUse="true" type="modelingSpline"/>
            <spline id="386" idObject="42" inUse="true" type="modelingSpline"/>
            <point id="387" idObject="44" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="388" idObject="46" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="390" idObject="58" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="391" idObject="54" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="392" idObject="46" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="393" idObject="45" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="394" idObject="17" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <spline id="395" idObject="420" inUse="true" type="modelingSpline"/>
            <spline id="396" idObject="29" inUse="true" type="modelingSpline"/>
            <point id="397" idObject="22" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="399" idObject="7" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="400" idObject="46" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="401" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="F_CENTRO_Ruedo" type="2">
                <nodes>
                    <node idObject="399" type="NodePoint"/>
                    <node idObject="400" type="NodePoint"/>
                </nodes>
            </path>
            <point id="402" idObject="5" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="403" idObject="44" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="404" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="F_L_Cintura" type="2">
                <nodes>
                    <node idObject="402" type="NodePoint"/>
                    <node idObject="403" type="NodePoint"/>
                </nodes>
            </path>
            <point id="405" idObject="62" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="406" idObject="61" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="407" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="F_C_Bols" type="2">
                <nodes>
                    <node idObject="405" type="NodePoint"/>
                    <node idObject="406" type="NodePoint"/>
                </nodes>
            </path>
            <point id="408" idObject="17" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="409" idObject="19" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="410" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="Costado_L_Sisa" type="2">
                <nodes>
                    <node idObject="408" type="NodePoint"/>
                    <node idObject="409" type="NodePoint"/>
                </nodes>
            </path>
            <point id="411" idObject="45" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="412" idObject="22" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="413" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="Cost_L_Cintur" type="2">
                <nodes>
                    <node idObject="411" type="NodePoint"/>
                    <node idObject="412" type="NodePoint"/>
                </nodes>
            </path>
            <point id="414" idObject="46" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="415" idObject="24" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="416" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="Cost_Ruedo" type="2">
                <nodes>
                    <node idObject="414" type="NodePoint"/>
                    <node idObject="415" type="NodePoint"/>
                </nodes>
            </path>
            <point id="417" idObject="122" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="418" idObject="116" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="419" idObject="118" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="420" idObject="108" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="421" idObject="105" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <spline id="422" idObject="136" inUse="true" type="modelingSpline"/>
            <spline id="423" idObject="135" inUse="true" type="modelingSpline"/>
            <point id="425" idObject="105" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="426" idObject="104" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="427" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="ESP_L_Sisa" type="2">
                <nodes>
                    <node idObject="425" type="NodePoint"/>
                    <node idObject="426" type="NodePoint"/>
                </nodes>
            </path>
            <point id="428" idObject="108" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="429" idObject="101" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="430" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="Esp_L_Cintur" type="2">
                <nodes>
                    <node idObject="428" type="NodePoint"/>
                    <node idObject="429" type="NodePoint"/>
                </nodes>
            </path>
            <point id="431" idObject="113" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="432" idObject="111" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="433" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="Esp_Ruedo" type="2">
                <nodes>
                    <node idObject="431" type="NodePoint"/>
                    <node idObject="432" type="NodePoint"/>
                </nodes>
            </path>
            <point id="434" idObject="140" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="435" idObject="139" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="436" idObject="141" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="437" idObject="138" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <point id="438" idObject="140" inUse="true" mx="10" my="15" showPointName="true" type="modeling"/>
            <path cut="false" extendEndPoint="false" extendStartPoint="false" id="439" inUse="true" lineColor="black" lineType="dashLine" lineWeight="0.35" name="Esp_Pinza" type="2">
                <nodes>
                    <node idObject="434" type="NodePoint"/>
                    <node idObject="435" type="NodePoint"/>
                    <node idObject="436" type="NodePoint"/>
                    <node idObject="437" type="NodePoint"/>
                    <node idObject="438" type="NodePoint"/>
                </nodes>
            </path>
        </modeling>
        <pieces>
            <piece color="#ffffff" fill="nobrush" forbidFlipping="true" hideMainPath="false" id="389" inLayout="true" locked="false" mx="-24.1368" my="-7.92552" name="F_Centro" seamAllowance="true" united="false" version="2" width="1">
                <data annotation="" foldPosition="Indefinido" fontSize="0" height="2" letter="" mx="297.638" my="1124.41" onFold="false" orientation="Indefinido" quantity="1" rotation="0" rotationWay="Ninguno" tilt="Ninguno" visible="true" width="3"/>
                <patternInfo fontSize="0" height="2" mx="61.4173" my="1124.41" rotation="0" visible="true" width="3"/>
                <grainline arrowLength="1.27" arrows="0" length="2.667" mx="236.22" my="1212.6" rotation="90" visible="true"/>
                <nodes>
                    <node idObject="380" type="NodePoint"/>
                    <node idObject="381" type="NodePoint"/>
                    <node idObject="382" type="NodePoint"/>
                    <node idObject="383" reverse="1" type="NodeSpline"/>
                    <node idObject="384" type="NodePoint"/>
                    <node idObject="385" reverse="0" type="NodeSpline"/>
                    <node idObject="386" reverse="0" type="NodeSpline"/>
                    <node idObject="387" type="NodePoint"/>
                    <node idObject="388" type="NodePoint"/>
                </nodes>
                <iPaths>
                    <record path="401"/>
                    <record path="404"/>
                    <record path="407"/>
                </iPaths>
            </piece>
            <piece color="#ffffff" fill="nobrush" forbidFlipping="true" hideMainPath="false" id="398" inLayout="true" locked="false" mx="-19.2734" my="-7.02489" name="F_Costado" seamAllowance="true" united="false" version="2" width="1">
                <data annotation="" foldPosition="Indefinido" fontSize="0" height="2" letter="C" mx="699.213" my="1464.57" onFold="false" orientation="Indefinido" quantity="1" rotation="0" rotationWay="Ninguno" tilt="Ninguno" visible="true" width="3"/>
                <patternInfo fontSize="0" height="2" mx="434.646" my="1464.57" rotation="0" visible="true" width="3"/>
                <grainline arrowLength="1.27" arrows="0" length="2.667" mx="623.622" my="1552.76" rotation="90" visible="true"/>
                <nodes>
                    <node idObject="390" type="NodePoint"/>
                    <node idObject="391" type="NodePoint"/>
                    <node idObject="392" type="NodePoint"/>
                    <node idObject="393" type="NodePoint"/>
                    <node idObject="394" type="NodePoint"/>
                    <node idObject="395" reverse="1" type="NodeSpline"/>
                    <node idObject="396" reverse="0" type="NodeSpline"/>
                    <node idObject="397" type="NodePoint"/>
                </nodes>
                <iPaths>
                    <record path="410"/>
                    <record path="413"/>
                    <record path="416"/>
                </iPaths>
            </piece>
            <piece color="#ffffff" fill="nobrush" forbidFlipping="true" hideMainPath="false" id="424" inLayout="true" locked="false" mx="-70.4291" my="6.30439" name="Espalda" seamAllowance="true" united="false" version="2" width="1">
                <data annotation="" foldPosition="Indefinido" fontSize="0" height="2" letter="E" mx="3500.79" my="897.638" onFold="false" orientation="Indefinido" quantity="1" rotation="0" rotationWay="Ninguno" tilt="Ninguno" visible="true" width="3"/>
                <patternInfo fontSize="0" height="2" mx="3056.69" my="897.638" rotation="0" visible="true" width="3"/>
                <grainline arrowLength="1.27" arrows="0" length="2.667" mx="3335.43" my="985.833" rotation="90" visible="true"/>
                <nodes>
                    <node idObject="417" type="NodePoint"/>
                    <node idObject="418" type="NodePoint"/>
                    <node idObject="419" type="NodePoint"/>
                    <node idObject="420" type="NodePoint"/>
                    <node idObject="421" type="NodePoint"/>
                    <node idObject="422" reverse="1" type="NodeSpline"/>
                    <node idObject="423" reverse="1" type="NodeSpline"/>
                </nodes>
                <iPaths>
                    <record path="427"/>
                    <record path="430"/>
                    <record path="433"/>
                    <record path="439"/>
                </iPaths>
            </piece>
        </pieces>
        <groups/>
    </draftBlock>
</pattern>
"""

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(original_content)

print("Recovered successfully!")
