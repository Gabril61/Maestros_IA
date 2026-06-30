import re

files = ['Basico_Superior_Dama_Maestro.val', 'Blusa_Cuello_Mao_Dama_Maestro.val']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix 40401
    # <point angle="270" basePoint="100" id="40401" length="@G_LARGO_PRENDA" mx="-10.6483" my="-5.34049" name="F_Largo_Cliente_Ref" showPointName="true" type="endLine"/>
    # Change basePoint to 118, length to #ajuste_largo_prenda
    content = re.sub(
        r'<point angle="270" basePoint="100" id="40401" length="@G_LARGO_PRENDA"([^>]*)/>',
        r'<point angle="270" basePoint="118" id="40401" length="#ajuste_largo_prenda"\1/>',
        content
    )

    # 2. Fix 40501
    # <point angle="270" basePoint="200" id="40501" length="@G_LARGO_PRENDA" mx="3.41737" my="0.697127" name="T_Largo_Cliente_Ref" showPointName="true" type="endLine"/>
    # Change basePoint to 218, length to #ajuste_largo_prenda
    content = re.sub(
        r'<point angle="270" basePoint="200" id="40501" length="@G_LARGO_PRENDA"([^>]*)/>',
        r'<point angle="270" basePoint="218" id="40501" length="#ajuste_largo_prenda"\1/>',
        content
    )

    # 3. Fix 404020
    # <point angle="270" basePoint="121" id="404020" length="(@G_LARGO_PRENDA - (@S_TALLE_DELANTERO + @G_ALTO_CADERA))" lineColor="black" lineType="none" name="F_Nivel_Costado_Cliente" type="endLine"/>
    # Change length to #ajuste_largo_prenda
    content = re.sub(
        r'<point angle="270" basePoint="121" id="404020" length="\(\@G_LARGO_PRENDA - \(\@S_TALLE_DELANTERO \+ \@G_ALTO_CADERA\)\)"([^>]*)/>',
        r'<point angle="270" basePoint="121" id="404020" length="#ajuste_largo_prenda"\1/>',
        content
    )

    # 4. Fix 261 (T_Pinza_Centro)
    # <point angle="180" basePoint="216" id="261" length="(@S_CONT_BUSTO / 10)" mx="-3.80493" my="2.84777" name="T_Pinza_Centro" type="endLine"/>
    # Change length to (@S_ANCHO_ESPALDA/4) + 1.5
    content = re.sub(
        r'<point angle="180" basePoint="216" id="261" length="\(\@S_CONT_BUSTO / 10\)"([^>]*)/>',
        r'<point angle="180" basePoint="216" id="261" length="(@S_ANCHO_ESPALDA/4) + 1.5"\1/>',
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {filename}')
