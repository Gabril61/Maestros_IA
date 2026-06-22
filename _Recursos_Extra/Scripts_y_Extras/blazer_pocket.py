import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

# 1. Remove bad lower pocket
ids_to_remove = ['95005', '95006', '95007', '95008', '95009', '95018', '95019', '95020', '95021']
for eid in ids_to_remove:
    el = calc.find(f'*[@id="{eid}"]')
    if el is not None:
        calc.remove(el)

# 2. Blazer-style lower pocket xml
new_pocket_xml = """
<elements>
<point firstPoint="161" id="89100" length="8" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_Centro_Bajo" secondPoint="164" showPointName="false" type="alongLine" />
<point angle="180" basePoint="89100" id="89101" length="10" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_Temp1" showPointName="false" type="endLine" />
<point angle="0" basePoint="89100" id="89102" length="10" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_Temp2" showPointName="false" type="endLine" />
<point id="89103" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_P1" p1Line1="162" p1Line2="165" p2Line1="89101" p2Line2="89102" showPointName="true" type="lineIntersect" />
<point id="89104" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_P2" p1Line1="163" p1Line2="166" p2Line1="89101" p2Line2="89102" showPointName="true" type="lineIntersect" />
<point angle="180" basePoint="89103" id="89105" length="((@S_CONT_BUSTO / 10) + 8) / 2" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_Izq" showPointName="true" type="endLine" />
<point angle="0" basePoint="89104" id="89106" length="((@S_CONT_BUSTO / 10) + 8) / 2" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_Der" showPointName="true" type="endLine" />
<point angle="270" basePoint="89105" id="89107" length="(@S_CONT_BUSTO / 10) + 10" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_BotIzq" showPointName="true" type="endLine" />
<point angle="270" basePoint="89106" id="89108" length="(@S_CONT_BUSTO / 10) + 10" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Bolsillo_BotDer" showPointName="true" type="endLine" />
<line firstPoint="89105" id="89110" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="89103" />
<line firstPoint="89104" id="89111" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="89106" />
<line firstPoint="89106" id="89112" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="89108" />
<line firstPoint="89108" id="89113" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="89107" />
<line firstPoint="89107" id="89114" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="89105" />
</elements>
"""

pockets_root = ET.fromstring(new_pocket_xml)

idx_target = 0
for i, el in enumerate(calc):
    if el.get('id') == '50207':
        idx_target = i
        break
if idx_target == 0: idx_target = len(calc)

# Remove duplicates
for el in pockets_root:
    eid = el.get('id')
    existing = calc.find(f'*[@id="{eid}"]')
    if existing is not None:
        calc.remove(existing)
        idx_target -= 1

for el in pockets_root:
    calc.insert(idx_target, el)
    idx_target += 1

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Bolsillo bajo reemplazado con lógica Blazer!")
