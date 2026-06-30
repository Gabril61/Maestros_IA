import re

files = ['Basico_Superior_Dama_Maestro.val', 'Blusa_Cuello_Mao_Dama_Maestro.val']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where 40403 is defined
    # It currently looks like:
    # <point angle="0" basePoint="40401" id="40403" mx="4.94336" my="1.42695" name="F_Costado_Cliente" p1Line="119" p2Line="121" showPointName="true" type="lineIntersectAxis"/>
    
    # We want to replace it with:
    # <point angle="270" basePoint="121" id="404020" length="Line_F_Nivel_Largo_F_Largo_Cliente_Ref" lineColor="black" lineType="none" name="F_Nivel_Costado_Cliente" type="endLine"/>
    # <point angle="0" basePoint="404020" id="40403" mx="4.94336" my="1.42695" name="F_Costado_Cliente" p1Line="119" p2Line="121" showPointName="true" type="lineIntersectAxis"/>

    pattern = r'<point angle="0" basePoint="40401" id="40403"([^>]+)/>'
    
    def repl(m):
        return f'<point angle="270" basePoint="121" id="404020" length="Line_F_Nivel_Largo_F_Largo_Cliente_Ref" lineColor="black" lineType="none" name="F_Nivel_Costado_Cliente" type="endLine"/>\n            <point angle="0" basePoint="404020" id="40403"{m.group(1)}/>'

    new_content = re.sub(pattern, repl, content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Restored inclination logic in {filename}')
    else:
        print(f'Pattern not found in {filename}')
