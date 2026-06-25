import xml.etree.ElementTree as ET
import os

def insert_points(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    calc = root.find('.//calculation')

    if calc is None:
        print("calculation not found")
        return

    # XML snippets to insert
    snippets = """
        <point angle="270" basePoint="166" id="50614" name="F_Pinza_Cliente_Der" p1Line="40401" p2Line="40403" type="lineIntersectAxis" />
        <point angle="270" basePoint="166" id="50615" name="Ext_F_Pinza_Cliente_Der" p1Line="40406" p2Line="40407" type="lineIntersectAxis" />
        <line firstPoint="166" id="50616" secondPoint="50614" lineColor="black" lineType="solidLine" lineWeight="0.7" />
        <line firstPoint="50614" id="50617" secondPoint="50615" lineColor="black" lineType="solidLine" lineWeight="0.7" />

        <point angle="270" basePoint="165" id="50618" name="F_Pinza_Cliente_Izq" p1Line="40401" p2Line="40403" type="lineIntersectAxis" />
        <point angle="270" basePoint="165" id="50619" name="Ext_F_Pinza_Cliente_Izq" p1Line="40406" p2Line="40407" type="lineIntersectAxis" />
        <line firstPoint="165" id="50620" secondPoint="50618" lineColor="black" lineType="solidLine" lineWeight="0.7" />
        <line firstPoint="50618" id="50621" secondPoint="50619" lineColor="black" lineType="solidLine" lineWeight="0.7" />

        <point angle="270" basePoint="265" id="50622" name="T_Pinza_Cliente_Der" p1Line="40503" p2Line="40504" type="lineIntersectAxis" />
        <point angle="270" basePoint="265" id="50623" name="Ext_T_Pinza_Cliente_Der" p1Line="40508" p2Line="40509" type="lineIntersectAxis" />
        <line firstPoint="265" id="50624" secondPoint="50622" lineColor="black" lineType="solidLine" lineWeight="0.7" />
        <line firstPoint="50622" id="50625" secondPoint="50623" lineColor="black" lineType="solidLine" lineWeight="0.7" />

        <point angle="270" basePoint="266" id="50626" name="T_Pinza_Cliente_Izq" p1Line="40503" p2Line="40504" type="lineIntersectAxis" />
        <point angle="270" basePoint="266" id="50627" name="Ext_T_Pinza_Cliente_Izq" p1Line="40508" p2Line="40509" type="lineIntersectAxis" />
        <line firstPoint="266" id="50628" secondPoint="50626" lineColor="black" lineType="solidLine" lineWeight="0.7" />
        <line firstPoint="50626" id="50629" secondPoint="50627" lineColor="black" lineType="solidLine" lineWeight="0.7" />

        <point angle="270" basePoint="264" id="50630" name="T_Pinza_Cliente_Centro" p1Line="40503" p2Line="40504" type="lineIntersectAxis" />
        <point angle="270" basePoint="264" id="50631" name="Ext_T_Pinza_Cliente_Centro" p1Line="40508" p2Line="40509" type="lineIntersectAxis" />
        <line firstPoint="264" id="50632" secondPoint="50630" lineColor="black" lineType="solidLine" lineWeight="0.7" />
        <line firstPoint="50630" id="50633" secondPoint="50631" lineColor="black" lineType="solidLine" lineWeight="0.7" />
    """

    from xml.dom import minidom
    
    # We will use string manipulation to avoid stripping Seamly2D formatting
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    insert_pos = content.rfind('</calculation>')
    if insert_pos == -1:
        print('Error: </calculation> not found')
        return

    new_content = content[:insert_pos] + snippets + "\n" + content[insert_pos:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("Points injected successfully.")

insert_points('c:/Users/Ricx18/Desktop/Maestros_IA/Basico_Superior_Dama_Maestro.val')
