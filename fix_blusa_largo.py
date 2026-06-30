import re

with open('Blusa_Cuello_Mao_Dama_Maestro.val', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace F_Nivel_Largo
content = re.sub(
    r'id="118" length="@S_TALLE_DELANTERO \+ 25"',
    r'id="118" length="@S_TALLE_DELANTERO + @G_ALTO_CADERA"',
    content
)

# Replace T_Nivel_Largo
content = re.sub(
    r'id="218" length="@S_TALLE_TRASERO \+ 25"',
    r'id="218" length="@S_TALLE_TRASERO + @G_ALTO_CADERA"',
    content
)

# Replace F_Largo_Cliente_Ref
content = re.sub(
    r'id="40401" length="@S_TALLE_DELANTERO \+ 25 \+ #ajuste_largo_prenda"',
    r'id="40401" length="@G_LARGO_PRENDA"',
    content
)

# Remove 404020 and update 40403 basePoint
pattern_to_replace = r'<point angle="270" basePoint="121" id="404020".*?/>\s*<point angle="0" basePoint="404020" id="40403"'
replacement = r'<point angle="0" basePoint="40401" id="40403"'
content = re.sub(pattern_to_replace, replacement, content, flags=re.DOTALL)

# Replace T_Largo_Cliente_Ref
content = re.sub(
    r'id="40501" length="@S_TALLE_TRASERO \+ 25 \+ #ajuste_largo_prenda"',
    r'id="40501" length="@G_LARGO_PRENDA"',
    content
)

with open('Blusa_Cuello_Mao_Dama_Maestro.val', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
