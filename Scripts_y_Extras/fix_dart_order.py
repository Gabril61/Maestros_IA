import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """            <!-- COMPOSICIÓN DE SISA EN 2 SPLINES (Calibración Visual Definitiva del Taller) -->
            <spline angle1="265" angle2="115" id="28" length1="Line_D_Cuello_Ext_D_Princesa_Sisa_Real * 0.3" length2="Line_D_Cuello_Ext_D_Princesa_Sisa_Real * 0.5" point1="12" point4="38" type="simpleInteractive"/>
            <spline angle1="260" angle2="180" id="29" length1="Line_D_Princesa_Sisa_Inf_D_Costado_Sisa * 0.1" length2="(@S_ANCHO_ESPALDA / 10) + 1" point1="3800" point4="19" type="simpleInteractive"/>
            <!-- Curva del Corte Princesa hacia el Busto -->
            <spline angle1="AngleLine_D_Princesa_Sisa_Real_D_Punto_Pezon - 15" angle2="AngleLine_D_Punto_Pezon_D_Pinza_Izq - 180" id="42" length1="Line_D_Princesa_Sisa_Real_D_Punto_Pezon * 0.35" length2="Line_D_Princesa_Sisa_Real_D_Punto_Pezon * 0.35" point1="38" point4="17" type="simpleInteractive"/>
            <spline angle1="AngleLine_D_Princesa_Sisa_Inf_D_Punto_Pezon + 15" angle2="AngleLine_D_Punto_Pezon_D_Pinza_Der - 180" id="500" length1="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35" length2="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35" point1="3800" point4="17" type="simpleInteractive"/>
            <!-- Pinza y PICO PRINCESA -->
            <point angle="270" basePoint="17" id="43" length="@S_TALLE_DELANTERO - @S_ALTO_BUSTO" name="D_Centro_Pinza" type="endLine"/>
            <point angle="180" basePoint="43" id="44" length="@D_PINZA_CINT_SUP / 2" name="D_Pinza_Izq" type="endLine"/>
            <point angle="0" basePoint="43" id="45" length="@D_PINZA_CINT_SUP / 2" name="D_Pinza_Der" type="endLine"/>
            <point angle="270" basePoint="43" id="46" length="@S_TALLE_DELANTERO * 0.3" name="D_Pico_Princesa" type="endLine"/>
            <line firstPoint="17" id="47" secondPoint="44"/>
            <line firstPoint="17" id="48" secondPoint="45"/>
            <line firstPoint="44" id="49" secondPoint="46"/>
            <line firstPoint="45" id="50" secondPoint="46"/>"""

replace = """            <!-- Pinza y PICO PRINCESA -->
            <point angle="270" basePoint="17" id="43" length="@S_TALLE_DELANTERO - @S_ALTO_BUSTO" name="D_Centro_Pinza" type="endLine"/>
            <point angle="180" basePoint="43" id="44" length="@D_PINZA_CINT_SUP / 2" name="D_Pinza_Izq" type="endLine"/>
            <point angle="0" basePoint="43" id="45" length="@D_PINZA_CINT_SUP / 2" name="D_Pinza_Der" type="endLine"/>
            <point angle="270" basePoint="43" id="46" length="@S_TALLE_DELANTERO * 0.3" name="D_Pico_Princesa" type="endLine"/>
            <line firstPoint="17" id="47" secondPoint="44"/>
            <line firstPoint="17" id="48" secondPoint="45"/>
            <line firstPoint="44" id="49" secondPoint="46"/>
            <line firstPoint="45" id="50" secondPoint="46"/>
            <!-- COMPOSICIÓN DE SISA EN 2 SPLINES (Calibración Visual Definitiva del Taller) -->
            <spline angle1="265" angle2="115" id="28" length1="Line_D_Cuello_Ext_D_Princesa_Sisa_Real * 0.3" length2="Line_D_Cuello_Ext_D_Princesa_Sisa_Real * 0.5" point1="12" point4="38" type="simpleInteractive"/>
            <spline angle1="260" angle2="180" id="29" length1="Line_D_Princesa_Sisa_Inf_D_Costado_Sisa * 0.1" length2="(@S_ANCHO_ESPALDA / 10) + 1" point1="3800" point4="19" type="simpleInteractive"/>
            <!-- Curva del Corte Princesa hacia el Busto -->
            <spline angle1="AngleLine_D_Princesa_Sisa_Real_D_Punto_Pezon - 15" angle2="AngleLine_D_Punto_Pezon_D_Pinza_Izq - 180" id="42" length1="Line_D_Princesa_Sisa_Real_D_Punto_Pezon * 0.35" length2="Line_D_Princesa_Sisa_Real_D_Punto_Pezon * 0.35" point1="38" point4="17" type="simpleInteractive"/>
            <spline angle1="AngleLine_D_Princesa_Sisa_Inf_D_Punto_Pezon + 15" angle2="AngleLine_D_Punto_Pezon_D_Pinza_Der - 180" id="500" length1="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35" length2="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35" point1="3800" point4="17" type="simpleInteractive"/>"""

if target in content:
    content = content.replace(target, replace)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed order successfully.")
else:
    print("Could not find the target block to swap.")
