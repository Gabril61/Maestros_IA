import os

file_path = r'c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Basico_Maestro.val'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''            <point angle="270" basePoint="112" id="1120" length="#caida_hombro_delantero" name="D_Hombro_Temp" type="endLine" />
            <point angle="AngleLine_D_Cuello_Ancho_D_Hombro_Temp" basePoint="104" id="113" length="Line_E_Cuello_Ancho_E_Hombro_Punta" name="D_Hombro_Punta" type="endLine" />'''

rep = '''            <point angle="270" basePoint="112" id="1120" length="#caida_hombro_delantero" name="D_Hombro_Temp" type="endLine" />
            <line firstPoint="104" id="1121" secondPoint="1120" />
            <point angle="AngleLine_D_Cuello_Ancho_D_Hombro_Temp" basePoint="104" id="113" length="Line_E_Cuello_Ancho_E_Hombro_Punta" name="D_Hombro_Punta" type="endLine" />'''

if target in content:
    content = content.replace(target, rep)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fix applied.")
else:
    print("Target not found. Check formatting.")
