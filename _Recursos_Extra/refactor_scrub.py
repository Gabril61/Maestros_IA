import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Basico_Maestro.val'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Change 1: Variables
target1 = '''        <variable name="#largo_abertura" formula="12.0" description="Largo de la abertura lateral (tajo)" />
    </variables>'''
rep1 = '''        <variable name="#largo_abertura" formula="12.0" description="Largo de la abertura lateral (tajo)" />
        <variable name="#ruedo_prenda" formula="3.0" description="Dobladillo de ruedo estandar" />
    </variables>'''
content = content.replace(target1, rep1)

# Change 2: Hem Extension Espalda
target2 = '''            <line firstPoint="8" id="11" secondPoint="10" />
            <line firstPoint="2" id="12" secondPoint="10" />
            <point angle="0" basePoint="1" id="13" length="(@S_ANCHO_ESPALDA / 2) + #hombro_extendido" name="E_Hombro_Guia" type="endLine" />'''
rep2 = '''            <line firstPoint="8" id="11" secondPoint="10" />
            <line firstPoint="2" id="12" secondPoint="10" />
            <point angle="270" basePoint="2" id="20" length="#ruedo_prenda" name="E_Ruedo_Centro_Ext" type="endLine" />
            <point angle="540 - AngleLine_E_Axila_E_Ruedo_Costado" basePoint="10" id="21" length="#ruedo_prenda" name="E_Ruedo_Costado_Ext" type="endLine" />
            <line firstPoint="20" id="22" secondPoint="21" />
            <line firstPoint="10" id="23" secondPoint="21" />
            <line firstPoint="2" id="24" secondPoint="20" />
            <point angle="0" basePoint="1" id="13" length="(@S_ANCHO_ESPALDA / 2) + #hombro_extendido" name="E_Hombro_Guia" type="endLine" />'''
content = content.replace(target2, rep2)

# Change 3: Hem Extension Delantero
target3 = '''            <line firstPoint="107" id="110" secondPoint="109" />
            <line firstPoint="101" id="111" secondPoint="109" />
            <point angle="180" basePoint="100" id="112" length="Line_E_Origen_E_Hombro_Guia" name="D_Hombro_Guia" type="endLine" />'''
rep3 = '''            <line firstPoint="107" id="110" secondPoint="109" />
            <line firstPoint="101" id="111" secondPoint="109" />
            <point angle="270" basePoint="101" id="120" length="#ruedo_prenda" name="D_Ruedo_Centro_Ext" type="endLine" />
            <point angle="540 - AngleLine_D_Axila_D_Ruedo_Costado" basePoint="109" id="121" length="#ruedo_prenda" name="D_Ruedo_Costado_Ext" type="endLine" />
            <line firstPoint="120" id="122" secondPoint="121" />
            <line firstPoint="109" id="123" secondPoint="121" />
            <line firstPoint="101" id="124" secondPoint="120" />
            <point angle="180" basePoint="100" id="112" length="Line_E_Origen_E_Hombro_Guia" name="D_Hombro_Guia" type="endLine" />'''
content = content.replace(target3, rep3)

# Change 4: Rule 14 Front Shoulder
target4 = '''            <point angle="270" basePoint="112" id="113" length="#caida_hombro_delantero" name="D_Hombro_Punta" type="endLine" />
            <line firstPoint="104" id="114" secondPoint="113" />'''
rep4 = '''            <point angle="270" basePoint="112" id="1120" length="#caida_hombro_delantero" name="D_Hombro_Temp" type="endLine" />
            <point angle="AngleLine_D_Cuello_Ancho_D_Hombro_Temp" basePoint="104" id="113" length="Line_E_Cuello_Ancho_E_Hombro_Punta" name="D_Hombro_Punta" type="endLine" />
            <line firstPoint="104" id="114" secondPoint="113" />'''
content = content.replace(target4, rep4)

# Change 5: Sleeve MAS
target5 = '''            <point angle="180" basePoint="203" id="204" length="Spl_E_Hombro_Punta_E_Axila" name="M_Sisa_Izq" type="endLine" />
            <point angle="0" basePoint="203" id="205" length="Spl_D_Hombro_Punta_D_Axila" name="M_Sisa_Der" type="endLine" />
            <line firstPoint="204" id="206" secondPoint="205" />
            <spline angle1="0" angle2="180" color="black" id="207" length1="Line_M_Nivel_Copa_M_Sisa_Izq * 0.4" length2="Line_M_Nivel_Copa_M_Sisa_Izq * 0.6" lineWeight="0.35" penStyle="solidLine" point1="204" point4="200" type="simpleInteractive" />
            <spline angle1="0" angle2="180" color="black" id="208" length1="Line_M_Nivel_Copa_M_Sisa_Der * 0.6" length2="Line_M_Nivel_Copa_M_Sisa_Der * 0.4" lineWeight="0.35" penStyle="solidLine" point1="200" point4="205" type="simpleInteractive" />'''
rep5 = '''            <point angle="180" basePoint="203" id="204" length="sqrt((Spl_E_Hombro_Punta_E_Axila * Spl_E_Hombro_Punta_E_Axila) - (Line_M_Origen_M_Nivel_Copa * Line_M_Origen_M_Nivel_Copa))" name="M_Sisa_Izq" type="endLine" />
            <point angle="0" basePoint="203" id="205" length="sqrt((Spl_D_Hombro_Punta_D_Axila * Spl_D_Hombro_Punta_D_Axila) - (Line_M_Origen_M_Nivel_Copa * Line_M_Origen_M_Nivel_Copa))" name="M_Sisa_Der" type="endLine" />
            <line firstPoint="204" id="206" secondPoint="205" />
            <spline angle1="0" angle2="180" color="black" id="207" length1="Line_M_Nivel_Copa_M_Sisa_Izq * 0.15" length2="Line_M_Nivel_Copa_M_Sisa_Izq * 0.55" lineWeight="0.35" penStyle="solidLine" point1="204" point4="200" type="simpleInteractive" />
            <spline angle1="0" angle2="180" color="black" id="208" length1="Line_M_Nivel_Copa_M_Sisa_Der * 0.55" length2="Line_M_Nivel_Copa_M_Sisa_Der * 0.15" lineWeight="0.35" penStyle="solidLine" point1="200" point4="205" type="simpleInteractive" />
            <point angle="90" basePoint="200" id="2000" length="((Spl_E_Hombro_Punta_E_Axila + Spl_D_Hombro_Punta_D_Axila) &gt; (Spl_M_Sisa_Izq_M_Origen + Spl_M_Origen_M_Sisa_Der)) ? 20 : 0" name="ALERTA_MANGA_DESPROPORCIONADA" type="endLine" />
            <line firstPoint="200" id="2001" lineColor="black" lineType="dottedLine" lineWeight="0.8" secondPoint="2000" />'''
content = content.replace(target5, rep5)

# Change 6: Modeling
target6 = '''            <point id="802" idObject="800" inUse="true" type="modeling" />
            <point id="803" idObject="801" inUse="true" type="modeling" />
        </modeling>'''
rep6 = '''            <point id="802" idObject="800" inUse="true" type="modeling" />
            <point id="803" idObject="801" inUse="true" type="modeling" />
            <point id="411" idObject="20" inUse="true" type="modeling" />
            <point id="412" idObject="21" inUse="true" type="modeling" />
            <point id="511" idObject="120" inUse="true" type="modeling" />
            <point id="512" idObject="121" inUse="true" type="modeling" />
        </modeling>'''
content = content.replace(target6, rep6)

# Change 7: Pieces Espalda
target7 = '''            <piece id="410" inLayout="true" name="Espalda" seamAllowance="true" version="2">
                <nodes>
                    <node idObject="400" type="NodePoint" />
                    <node idObject="401" type="NodePoint" />
                    <node idObject="402" type="NodePoint" />
                    <node idObject="802" type="NodePoint" />'''
rep7 = '''            <piece id="410" inLayout="true" name="Espalda" seamAllowance="true" version="2">
                <nodes>
                    <node idObject="400" type="NodePoint" />
                    <node idObject="401" type="NodePoint" />
                    <node idObject="411" type="NodePoint" />
                    <node idObject="412" type="NodePoint" />
                    <node idObject="402" type="NodePoint" />
                    <node idObject="802" type="NodePoint" />'''
content = content.replace(target7, rep7)

# Change 8: Pieces Delantero
target8 = '''            <piece id="510" inLayout="true" name="Delantero" seamAllowance="true" version="2">
                <nodes>
                    <node idObject="500" type="NodePoint" />
                    <node idObject="501" type="NodePoint" />
                    <node idObject="503" type="NodePoint" />
                    <node idObject="504" type="NodePoint" />
                    <node idObject="505" reverse="0" type="NodeSpline" />
                    <node idObject="506" type="NodePoint" />
                    <node idObject="803" type="NodePoint" />
                    <node idObject="507" type="NodePoint" />
                </nodes>
            </piece>'''
rep8 = '''            <piece id="510" inLayout="true" name="Delantero" seamAllowance="true" version="2">
                <nodes>
                    <node idObject="500" type="NodePoint" />
                    <node idObject="501" type="NodePoint" />
                    <node idObject="503" type="NodePoint" />
                    <node idObject="504" type="NodePoint" />
                    <node idObject="505" reverse="0" type="NodeSpline" />
                    <node idObject="506" type="NodePoint" />
                    <node idObject="803" type="NodePoint" />
                    <node idObject="507" type="NodePoint" />
                    <node idObject="512" type="NodePoint" />
                    <node idObject="511" type="NodePoint" />
                </nodes>
            </piece>'''
content = content.replace(target8, rep8)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
