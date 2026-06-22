import os

xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<pattern>
    <version>0.7.3</version>
    <unit>cm</unit>
    <description>Bata Medica Estandar - Motor M.A.S.</description>
    <notes>Cuerpos bases estabilizados con sisas parametricas y costados calibrados.</notes>
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
    <draftBlock name="Bata_Maestra">
        <calculation>
            <!-- ========================================================= -->
            <!-- DELANTERO (Origen X=0)                                    -->
            <!-- ========================================================= -->
            <point id="100" mx="0.1" my="0.1" name="F_Origen" type="single" x="0" y="0"/>
            
            <!-- Ejes Centrales -->
            <point angle="270" basePoint="100" id="102" length="(@S_CONTCUELLO/6) + 2" name="F_Escote_Alto" type="endLine"/>
            <point angle="270" basePoint="100" id="107" length="(@S_ANCHOESP/2) + 4" name="F_Nivel_Sisa" type="endLine"/>
            <point angle="270" basePoint="100" id="109" length="((@S_ANCHOESP/2)+4)/2" name="F_Nivel_Pecho" type="endLine"/>
            <point angle="270" basePoint="100" id="116" length="@S_TALLEDEL" name="F_Nivel_Cintura" type="endLine"/>
            <point angle="270" basePoint="100" id="118" length="@G_LARGOPRENDA" name="F_Nivel_Largo" type="endLine"/>
            
            <!-- Escote y Hombro -->
            <point angle="0" basePoint="100" id="101" length="(@S_CONTCUELLO/6) + 1" name="F_Escote_Ancho" type="endLine"/>
            <spline angle1="270" angle2="0" color="black" id="103" length1="1" length2="1" point1="101" point4="102" type="simpleInteractive"/>
            <point angle="0" basePoint="100" id="104" length="(@S_ANCHOESP/2)" name="F_Guia_Espalda" type="endLine"/>
            <point angle="270" basePoint="104" id="105" length="4" name="F_Caida_Hombro" type="endLine"/>
            <line firstPoint="101" id="106" secondPoint="105"/>
            
            <!-- Anchos Transversales -->
            <point angle="0" basePoint="109" id="110" length="(@S_ANCHOESP/2) - 1.5" name="F_Ancho_Pecho" type="endLine"/>
            <point angle="0" basePoint="107" id="111" length="((@S_CONTBUSTO + @M_HOLGURA_BATA)/4)" name="F_Costado_Sisa" type="endLine"/>
            <point angle="0" basePoint="118" id="121" length="((@I_CONTCADBA + @M_HOLGURA_BATA)/4) + 3" name="F_Costado_Ruedo" type="endLine"/>
            
            <!-- Costado y Cintura -->
            <line firstPoint="111" id="122" secondPoint="121"/>
            <point angle="0" basePoint="116" id="119" name="F_Costado_Cintura" p1Line="111" p2Line="121" type="lineIntersectAxis"/>
            
            <!-- Sisa Parametrica (Motor M.A.S.) -->
            <line firstPoint="105" id="112" secondPoint="110"/>
            <line firstPoint="110" id="113" secondPoint="111"/>
            <spline angle1="AngleLine_F_Escote_Ancho_F_Caida_Hombro - 90" angle2="AngleLine_F_Caida_Hombro_F_Ancho_Pecho + 180" color="black" id="114" length1="Line_F_Caida_Hombro_F_Ancho_Pecho * 0.4" length2="Line_F_Caida_Hombro_F_Ancho_Pecho * 0.4" point1="105" point4="110" type="simpleInteractive"/>
            <spline angle1="AngleLine_F_Caida_Hombro_F_Ancho_Pecho" angle2="180" color="black" id="115" length1="Line_F_Ancho_Pecho_F_Costado_Sisa * 0.4" length2="Line_F_Ancho_Pecho_F_Costado_Sisa * 0.3" point1="110" point4="111" type="simpleInteractive"/>
            
            <!-- Elementos Utilitarios (Pasamanos y Bolsillo) -->
            <point angle="AngleLine_F_Costado_Sisa_F_Costado_Ruedo" basePoint="119" id="122_b" length="5" name="F_Pasamanos_Top" type="endLine"/>
            <point angle="AngleLine_F_Costado_Sisa_F_Costado_Ruedo" basePoint="122_b" id="123" length="20" name="F_Pasamanos_Bot" type="endLine"/>
            <point angle="180" basePoint="122_b" id="125" length="18" name="F_Bolsillo_Top" type="endLine"/>
            <point angle="180" basePoint="123" id="126" length="18" name="F_Bolsillo_Bot" type="endLine"/>
            <line firstPoint="125" id="127" secondPoint="126"/>

            <!-- ========================================================= -->
            <!-- TRASERO (Origen X=80)                                     -->
            <!-- ========================================================= -->
            <point id="200" mx="0.1" my="0.1" name="T_Origen" type="single" x="80" y="0"/>
            
            <!-- Ejes Centrales -->
            <point angle="270" basePoint="200" id="202" length="2.5" name="T_Escote_Alto" type="endLine"/>
            <point angle="270" basePoint="200" id="207" length="(@S_ANCHOESP/2) + 4" name="T_Nivel_Sisa" type="endLine"/>
            <point angle="270" basePoint="200" id="209" length="((@S_ANCHOESP/2)+4)/2" name="T_Nivel_Pecho" type="endLine"/>
            <point angle="270" basePoint="200" id="216" length="@S_TALLETRA" name="T_Nivel_Cintura" type="endLine"/>
            <point angle="270" basePoint="200" id="218" length="@G_LARGOPRENDA" name="T_Nivel_Largo" type="endLine"/>
            
            <!-- Escote y Hombro -->
            <point angle="180" basePoint="200" id="201" length="(@S_CONTCUELLO/6) + 1.5" name="T_Escote_Ancho" type="endLine"/>
            <spline angle1="270" angle2="0" color="black" id="203" length1="1" length2="1" point1="201" point4="202" type="simpleInteractive"/>
            <point angle="180" basePoint="200" id="204" length="(@S_ANCHOESP/2)" name="T_Guia_Espalda" type="endLine"/>
            <point angle="270" basePoint="204" id="205" length="3" name="T_Caida_Hombro" type="endLine"/>
            <line firstPoint="201" id="206" secondPoint="205"/>
            
            <!-- Anchos Transversales -->
            <point angle="180" basePoint="209" id="210" length="(@S_ANCHOESP/2) - 0.5" name="T_Ancho_Espalda" type="endLine"/>
            <point angle="180" basePoint="207" id="211" length="((@S_CONTBUSTO + @M_HOLGURA_BATA)/4)" name="T_Costado_Sisa" type="endLine"/>
            <point angle="180" basePoint="218" id="221" length="((@I_CONTCADBA + @M_HOLGURA_BATA)/4) + 3" name="T_Costado_Ruedo" type="endLine"/>
            
            <!-- Costado y Cintura -->
            <line firstPoint="211" id="222" secondPoint="221"/>
            <point angle="180" basePoint="216" id="219" name="T_Costado_Cintura" p1Line="211" p2Line="221" type="lineIntersectAxis"/>
            
            <!-- Sisa Parametrica (Motor M.A.S.) -->
            <line firstPoint="205" id="212" secondPoint="210"/>
            <line firstPoint="210" id="213" secondPoint="211"/>
            <spline angle1="AngleLine_T_Escote_Ancho_T_Caida_Hombro + 90" angle2="AngleLine_T_Caida_Hombro_T_Ancho_Espalda + 180" color="black" id="214" length1="Line_T_Caida_Hombro_T_Ancho_Espalda * 0.4" length2="Line_T_Caida_Hombro_T_Ancho_Espalda * 0.4" point1="205" point4="210" type="simpleInteractive"/>
            <spline angle1="AngleLine_T_Caida_Hombro_T_Ancho_Espalda" angle2="0" color="black" id="215" length1="Line_T_Ancho_Espalda_T_Costado_Sisa * 0.4" length2="Line_T_Ancho_Espalda_T_Costado_Sisa * 0.3" point1="210" point4="211" type="simpleInteractive"/>
            
            <!-- Elementos Utilitarios (Pasamanos y Abertura Trasera) -->
            <point angle="AngleLine_T_Costado_Sisa_T_Costado_Ruedo" basePoint="219" id="222_b" length="5" name="T_Pasamanos_Top" type="endLine"/>
            <point angle="AngleLine_T_Costado_Sisa_T_Costado_Ruedo" basePoint="222_b" id="223" length="20" name="T_Pasamanos_Bot" type="endLine"/>
            <point angle="0" basePoint="222_b" id="224" length="4" name="T_Aletilla_Pasamanos_Top" type="endLine"/>
            <point angle="0" basePoint="223" id="225" length="4" name="T_Aletilla_Pasamanos_Bot" type="endLine"/>
            <line firstPoint="224" id="226" secondPoint="225"/>
            
            <point angle="90" basePoint="218" id="230" length="20" name="T_Abertura_Central_Top" type="endLine"/>
            <point angle="180" basePoint="230" id="231" length="5" name="T_Aletilla_Centro_Top" type="endLine"/>
            <point angle="180" basePoint="218" id="232" length="5" name="T_Aletilla_Centro_Bot" type="endLine"/>
            <line firstPoint="231" id="233" secondPoint="232"/>

            <!-- ========================================================= -->
            <!-- VISTA / SOLAPA (Origen X=-40)                             -->
            <!-- ========================================================= -->
            <point id="300" mx="0.1" my="0.1" name="V_Origen" type="single" x="-40" y="0"/>
            <point angle="270" basePoint="300" id="302" length="(@S_CONTCUELLO/6) + 2" name="V_Escote_Alto" type="endLine"/>
            <point angle="0" basePoint="300" id="301" length="(@S_CONTCUELLO/6) + 1" name="V_Escote_Ancho" type="endLine"/>
            <spline angle1="270" angle2="0" color="black" id="303" length1="1" length2="1" point1="301" point4="302" type="simpleInteractive"/>
            <point angle="0" basePoint="301" id="304" length="5" name="V_Hombro_Ext" type="endLine"/>
            <point angle="270" basePoint="300" id="305" length="@G_LARGOPRENDA" name="V_Nivel_Largo" type="endLine"/>
            <point angle="0" basePoint="305" id="306" length="7" name="V_Ruedo_Ext" type="endLine"/>
            <line firstPoint="304" id="307" secondPoint="306"/>
            <line firstPoint="302" id="308" secondPoint="305"/>
        </calculation>
        <modeling/>
        <pieces/>
        <groups/>
    </draftBlock>
</pattern>
"""

with open(r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val', 'w', encoding='utf-8') as f:
    f.write(xml_content)

print("Master file generated successfully.")
