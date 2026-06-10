import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Chaleco_Halter_Dama_Maestro.val'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

# Using indexing to modify lines precisely
for i, line in enumerate(lines):
    if 'id="21"' in line and 'name="D_Costado_Cintura_Guia"' in line:
        lines[i] = '            <point angle="0" basePoint="5" id="22" length="((@G_CONT_CINTURA + #holgura_chaleco) / 4) + @D_PINZA_CINT_SUP" name="D_Costado_Cintura" type="endLine"/>'
    elif 'id="22"' in line and 'name="D_Costado_Cintura"' in line:
        lines[i] = ''
    elif 'id="107"' in line and 'name="E_Costado_Cintura_Guia"' in line:
        lines[i] = '            <point angle="180" basePoint="101" id="108" length="((@G_CONT_CINTURA + #holgura_chaleco) / 4) + @D_PINZA_CINT_SUP" name="E_Costado_Cintura" type="endLine"/>'
    elif 'id="108"' in line and 'name="E_Costado_Cintura"' in line:
        lines[i] = ''
    elif 'id="41"' in line and 'firstPoint="38"' in line and 'secondPoint="17"' in line:
        # Add the new point and its lines right AFTER line 41
        lines[i] = line + '\n' + \
                   '            <!-- Pinza de sisa (Apertura de volumen tridimensional) -->\n' + \
                   '            <point angle="AngleLine_D_Princesa_Sisa_Real_D_Costado_Sisa" basePoint="38" id="3800" length="2.5" name="D_Princesa_Sisa_Inf" type="endLine"/>\n' + \
                   '            <line firstPoint="3800" id="3801" secondPoint="19"/>\n' + \
                   '            <line firstPoint="3800" id="3802" secondPoint="17"/>'
    elif 'id="29"' in line and 'type="simpleInteractive"' in line:
        lines[i] = '            <spline angle1="260" angle2="180" id="29" length1="Line_D_Princesa_Sisa_Inf_D_Costado_Sisa * 0.1" length2="(@S_ANCHO_ESPALDA / 10) + 1" point1="3800" point4="19" type="simpleInteractive"/>'
    elif 'id="42"' in line and 'type="simpleInteractive"' in line:
        lines[i] = '            <!-- Curva del Corte Princesa hacia el Busto (Con apertura de pinza para volumen 3D) -->\n' + \
                   '            <spline angle1="AngleLine_D_Princesa_Sisa_Real_D_Punto_Pezon - 15" angle2="AngleLine_D_Punto_Pezon_D_Pinza_Izq - 180" id="42" length1="Line_D_Princesa_Sisa_Real_D_Punto_Pezon * 0.35" length2="Line_D_Princesa_Sisa_Real_D_Punto_Pezon * 0.35" point1="38" point4="17" type="simpleInteractive"/>\n' + \
                   '            <spline angle1="AngleLine_D_Princesa_Sisa_Inf_D_Punto_Pezon + 15" angle2="AngleLine_D_Punto_Pezon_D_Pinza_Der - 180" id="420" length1="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35" length2="Line_D_Princesa_Sisa_Inf_D_Punto_Pezon * 0.35" point1="3800" point4="17" type="simpleInteractive"/>'
    elif 'id="395"' in line and 'idObject="42"' in line and 'type="modelingSpline"' in line:
        lines[i] = '            <spline id="395" idObject="420" inUse="true" type="modelingSpline"/>'

# remove empty lines left by deleted nodes
lines = [l for l in lines if l != '']

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print("Safe line-by-line patch applied.")
