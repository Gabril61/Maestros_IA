import re

filename = 'Blusa_Cuello_Mao_Dama_Maestro.val'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# We will inject these right before the closing </calculation> tag.
injection = """
        <point angle="270" basePoint="166" id="60001" name="F_Pinza_Cliente_Der" p1Line="40401" p2Line="40403" type="lineIntersectAxis"/>
        <point angle="270" basePoint="166" id="60002" name="Ext_F_Pinza_Cliente_Der" p1Line="40406" p2Line="40407" type="lineIntersectAxis"/>
        <line firstPoint="166" id="60003" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60001"/>
        <line firstPoint="60001" id="60004" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60002"/>

        <point angle="270" basePoint="165" id="60005" name="F_Pinza_Cliente_Izq" p1Line="40401" p2Line="40403" type="lineIntersectAxis"/>
        <point angle="270" basePoint="165" id="60006" name="Ext_F_Pinza_Cliente_Izq" p1Line="40406" p2Line="40407" type="lineIntersectAxis"/>
        <line firstPoint="165" id="60007" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60005"/>
        <line firstPoint="60005" id="60008" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60006"/>

        <point angle="270" basePoint="265" id="60009" name="T_Pinza_Cliente_Der" p1Line="40503" p2Line="40504" type="lineIntersectAxis"/>
        <point angle="270" basePoint="265" id="60010" name="Ext_T_Pinza_Cliente_Der" p1Line="40508" p2Line="40509" type="lineIntersectAxis"/>
        <line firstPoint="265" id="60011" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60009"/>
        <line firstPoint="60009" id="60012" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60010"/>

        <point angle="270" basePoint="266" id="60013" name="T_Pinza_Cliente_Izq" p1Line="40503" p2Line="40504" type="lineIntersectAxis"/>
        <point angle="270" basePoint="266" id="60014" name="Ext_T_Pinza_Cliente_Izq" p1Line="40508" p2Line="40509" type="lineIntersectAxis"/>
        <line firstPoint="266" id="60015" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60013"/>
        <line firstPoint="60013" id="60016" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60014"/>

        <point angle="270" basePoint="264" id="60017" name="T_Pinza_Cliente_Centro" p1Line="40503" p2Line="40504" type="lineIntersectAxis"/>
        <point angle="270" basePoint="264" id="60018" name="Ext_T_Pinza_Cliente_Centro" p1Line="40508" p2Line="40509" type="lineIntersectAxis"/>
        <line firstPoint="264" id="60019" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60017"/>
        <line firstPoint="60017" id="60020" lineColor="black" lineType="solidLine" lineWeight="0.7" secondPoint="60018"/>
"""

if 'name="F_Pinza_Cliente_Izq"' not in content:
    content = content.replace('</calculation>', injection + '\n    </calculation>')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected successfully.")
else:
    print("Already exists.")
