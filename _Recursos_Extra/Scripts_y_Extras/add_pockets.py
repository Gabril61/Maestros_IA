import xml.etree.ElementTree as ET
import re

filepath = r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Dama_Maestro.val"
ET.register_namespace('', '')

tree = ET.parse(filepath)
root = tree.getroot()
calc = root.find('.//calculation')

pocket_xml = """
<elements>
<point angle="90" basePoint="160" id="95000" length="2" lineColor="black" lineType="none" name="F_Bolsillo_Alto_C" showPointName="false" type="endLine" />
<point angle="180" basePoint="95000" id="95001" length="((@S_CONT_BUSTO / 10) + 2) / 2" lineColor="black" lineType="none" name="F_Bolsillo_Alto_TopIzq" showPointName="false" type="endLine" />
<point angle="0" basePoint="95000" id="95002" length="((@S_CONT_BUSTO / 10) + 2) / 2" lineColor="black" lineType="none" name="F_Bolsillo_Alto_TopDer" showPointName="false" type="endLine" />
<point angle="270" basePoint="95001" id="95003" length="(@S_CONT_BUSTO / 10) + 4" lineColor="black" lineType="none" name="F_Bolsillo_Alto_BotIzq" showPointName="false" type="endLine" />
<point angle="270" basePoint="95002" id="95004" length="(@S_CONT_BUSTO / 10) + 4" lineColor="black" lineType="none" name="F_Bolsillo_Alto_BotDer" showPointName="false" type="endLine" />
<point angle="90" basePoint="181" id="95005" length="3" lineColor="black" lineType="none" name="F_Bolsillo_Bajo_C" showPointName="false" type="endLine" />
<point angle="180" basePoint="95005" id="95006" length="((@S_CONT_BUSTO / 10) + 8) / 2" lineColor="black" lineType="none" name="F_Bolsillo_Bajo_TopIzq" showPointName="false" type="endLine" />
<point angle="0" basePoint="95005" id="95007" length="((@S_CONT_BUSTO / 10) + 8) / 2" lineColor="black" lineType="none" name="F_Bolsillo_Bajo_TopDer" showPointName="false" type="endLine" />
<point angle="270" basePoint="95006" id="95008" length="(@S_CONT_BUSTO / 10) + 10" lineColor="black" lineType="none" name="F_Bolsillo_Bajo_BotIzq" showPointName="false" type="endLine" />
<point angle="270" basePoint="95007" id="95009" length="(@S_CONT_BUSTO / 10) + 10" lineColor="black" lineType="none" name="F_Bolsillo_Bajo_BotDer" showPointName="false" type="endLine" />
<line firstPoint="95001" id="95014" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="95002" />
<line firstPoint="95002" id="95015" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="95004" />
<line firstPoint="95004" id="95016" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="95003" />
<line firstPoint="95003" id="95017" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="95001" />
<line firstPoint="95006" id="95018" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="95007" />
<line firstPoint="95007" id="95019" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="95009" />
<line firstPoint="95009" id="95020" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="95008" />
<line firstPoint="95008" id="95021" lineColor="black" lineType="dashLine" lineWeight="0.35" secondPoint="95006" />
</elements>
"""

pocket_root = ET.fromstring(pocket_xml)

idx_target = 0
for i, el in enumerate(calc):
    if el.get('id') == '50207':
        idx_target = i
        break
if idx_target == 0: idx_target = len(calc)

# Remove existing if any (prevent duplicate IDs)
for el_to_add in pocket_root:
    eid = el_to_add.get('id')
    existing = calc.find(f'*[@id="{eid}"]')
    if existing is not None:
        calc.remove(existing)
        idx_target -= 1 # Adjust index

for el in pocket_root:
    calc.insert(idx_target, el)
    idx_target += 1

xmlstr = ET.tostring(root, encoding='utf-8', method='xml').decode('utf-8')
xmlstr = re.sub(r'\n\s*\n', '\n', xmlstr)
xmlstr = xmlstr.replace(' />', '/>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + xmlstr)

print("Bolsillos inyectados!")
