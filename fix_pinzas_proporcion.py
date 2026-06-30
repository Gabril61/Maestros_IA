import re

files = ['Basico_Superior_Dama_Maestro.val', 'Blusa_Cuello_Mao_Dama_Maestro.val']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Reemplazar F_Pinza_Cadera_Centro (181)
    # Original: <point angle="0" basePoint="117" id="181" length="(@S_CONT_BUSTO / 10)" ... name="F_Pinza_Cadera_Centro" type="endLine"/>
    # Nuevo: <point angle="270" basePoint="161" id="181" length="@G_ALTO_CADERA * 0.6" name="F_Pinza_Cadera_Centro" type="endLine"/>
    
    content = re.sub(
        r'<point angle="0" basePoint="117" id="181" length="\(@S_CONT_BUSTO / 10\)"[^>]*name="F_Pinza_Cadera_Centro" type="endLine"/>',
        r'<point angle="270" basePoint="161" id="181" length="@G_ALTO_CADERA * 0.6" name="F_Pinza_Cadera_Centro" type="endLine"/>',
        content
    )

    # Reemplazar T_Pinza_Cadera_Centro (281)
    # Original: <point angle="180" basePoint="217" id="281" length="(@S_ANCHO_ESPALDA/4) \+ 1.5" ... name="T_Pinza_Cadera_Centro" type="endLine"/>
    # Nuevo: <point angle="270" basePoint="261" id="281" length="@G_ALTO_CADERA * 0.75" name="T_Pinza_Cadera_Centro" type="endLine"/>
    
    content = re.sub(
        r'<point angle="180" basePoint="217" id="281" length="\(@S_ANCHO_ESPALDA/4\) \+ 1\.5"[^>]*name="T_Pinza_Cadera_Centro" type="endLine"/>',
        r'<point angle="270" basePoint="261" id="281" length="@G_ALTO_CADERA * 0.75" name="T_Pinza_Cadera_Centro" type="endLine"/>',
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f'Proporción de pinzas ajustada en {filename}')
