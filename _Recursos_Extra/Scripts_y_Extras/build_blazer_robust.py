import xml.etree.ElementTree as ET
import re

file_path = "Blazer_Dama_Maestro.val"
tree = ET.parse(file_path)
root = tree.getroot()

calculation_node = None
for draft in root.findall('.//draftBlock'):
    if draft.get('name') == 'Corpino_y_Manga':
        calculation_node = draft.find('calculation')
        break

new_sleeve_xml = """<root>
    <point id="12000" mx="0.1" my="0.1" name="MS_Origen" showPointName="true" type="single" x="150" y="0"/>
    <point angle="270" basePoint="12000" id="12001" length="@S_LARGO_MANGA" mx="0.1" my="0.1" name="MS_Largo" showPointName="true" type="endLine"/>
    <point angle="270" basePoint="12000" id="12002" length="(@S_LARGO_MANGA/2)+2" mx="0.1" my="0.1" name="MS_Codo" showPointName="true" type="endLine"/>
    <point firstPoint="12000" id="12003" length="(@S_CONT_BUSTO / 10) + 4" mx="0.1" my="0.1" name="MS_Copa_Alto" secondPoint="12001" showPointName="true" type="alongLine"/>
    
    <point angle="180" basePoint="12003" id="12004" length="(@S_CONT_BICEP + #holgura_biceps) / 2" mx="0.1" my="0.1" name="MS_Ancho_Izq" showPointName="true" type="endLine"/>
    <point angle="0" basePoint="12003" id="12005" length="(@S_CONT_BICEP + #holgura_biceps) / 2" mx="0.1" my="0.1" name="MS_Ancho_Der" showPointName="true" type="endLine"/>
    
    <point firstPoint="12000" id="12006" length="Line_MS_Origen_MS_Ancho_Izq / 2" mx="0.1" my="0.1" name="MS_Guia_Izq" secondPoint="12004" type="alongLine" />
    <point firstPoint="12000" id="12007" length="Line_MS_Origen_MS_Ancho_Der / 2" mx="0.1" my="0.1" name="MS_Guia_Der" secondPoint="12005" type="alongLine" />
    
    <point angle="180" basePoint="12002" id="12010" length="(((@S_CONT_BICEP + #holgura_biceps) / 2) + ((@S_CONT_PUNO + #holgura_puno) / 2)) / 2" mx="0.1" my="0.1" name="MS_Codo_Izq" showPointName="true" type="endLine"/>
    <point angle="0" basePoint="12002" id="12011" length="(((@S_CONT_BICEP + #holgura_biceps) / 2) + ((@S_CONT_PUNO + #holgura_puno) / 2)) / 2" mx="0.1" my="0.1" name="MS_Codo_Der" showPointName="true" type="endLine"/>
    <point angle="180" basePoint="12001" id="12014" length="(@S_CONT_PUNO + #holgura_puno) / 2" mx="0.721382" my="-5.59601" name="MS_Puno_Izq" showPointName="true" type="endLine"/>
    <point angle="0" basePoint="12001" id="12015" length="(@S_CONT_PUNO + #holgura_puno) / 2" mx="0.1" my="0.1" name="MS_Puno_Der" showPointName="true" type="endLine"/>
    
    <line firstPoint="12004" id="12031" lineColor="black" secondPoint="12010"/>
    <line firstPoint="12010" id="12032" lineColor="black" secondPoint="12014"/>
    <line firstPoint="12005" id="12033" lineColor="black" secondPoint="12011"/>
    <line firstPoint="12011" id="12034" lineColor="black" secondPoint="12015"/>
    
    <spline angle1="180" angle2="AngleLine_MS_Origen_MS_Ancho_Izq - 180" color="black" id="12020" length1="(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.55" length2="(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.05" point1="12000" point4="12006" type="simpleInteractive"/>
    <spline angle1="AngleLine_MS_Origen_MS_Ancho_Izq + 20" angle2="0" color="black" id="12021" length1="(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.4" length2="(Line_MS_Origen_MS_Ancho_Izq / 2) * 0.2" point1="12006" point4="12004" type="simpleInteractive"/>
    <spline angle1="0" angle2="AngleLine_MS_Origen_MS_Ancho_Der - 220" color="black" id="12022" length1="(Line_MS_Origen_MS_Ancho_Der / 2) * 0.55" length2="(Line_MS_Origen_MS_Ancho_Der / 2) * 0.05" point1="12000" point4="12007" type="simpleInteractive"/>
    <spline angle1="AngleLine_MS_Origen_MS_Ancho_Der - 20" angle2="180" color="black" id="12023" length1="(Line_MS_Origen_MS_Ancho_Der / 2) * 0.3" length2="(Line_MS_Origen_MS_Ancho_Der / 2) * 0.2" point1="12007" point4="12005" type="simpleInteractive"/>

    <point angle="180" basePoint="12003" id="30001" length="((@S_CONT_BICEP + #holgura_biceps) / 2) / 2" mx="0.1" my="0.1" name="Fold_Frente_Bicep" showPointName="false" type="endLine"/>
    <point angle="0" basePoint="12003" id="30002" length="((@S_CONT_BICEP + #holgura_biceps) / 2) / 2" mx="0.1" my="0.1" name="Fold_Espalda_Bicep" showPointName="false" type="endLine"/>
    <point angle="180" basePoint="12002" id="30003" length="((((@S_CONT_BICEP + #holgura_biceps) / 2) + ((@S_CONT_PUNO + #holgura_puno) / 2)) / 2) / 2" mx="0.1" my="0.1" name="Fold_Frente_Codo" showPointName="false" type="endLine"/>
    <point angle="0" basePoint="12002" id="30004" length="((((@S_CONT_BICEP + #holgura_biceps) / 2) + ((@S_CONT_PUNO + #holgura_puno) / 2)) / 2) / 2" mx="0.1" my="0.1" name="Fold_Espalda_Codo" showPointName="false" type="endLine"/>
    <point angle="180" basePoint="12001" id="30005" length="((@S_CONT_PUNO + #holgura_puno) / 2) / 2" mx="0.1" my="0.1" name="Fold_Frente_Puno" showPointName="false" type="endLine"/>
    <point angle="0" basePoint="12001" id="30006" length="((@S_CONT_PUNO + #holgura_puno) / 2) / 2" mx="0.1" my="0.1" name="Fold_Espalda_Puno" showPointName="false" type="endLine"/>
    
    <point angle="180" basePoint="30001" id="30011" length="-3" mx="0.1" my="0.1" name="Corte_Frente_Bicep" showPointName="true" type="endLine"/>
    <point angle="180" basePoint="30003" id="30012" length="-3" mx="0.1" my="0.1" name="Corte_Frente_Codo" showPointName="true" type="endLine"/>
    <point angle="180" basePoint="30005" id="30013" length="-3" mx="0.1" my="0.1" name="Corte_Frente_Puno" showPointName="true" type="endLine"/>
    
    <point angle="0" basePoint="30002" id="30014" length="0" mx="0.1" my="0.1" name="Corte_Espalda_Bicep" showPointName="true" type="endLine"/>
    <point angle="0" basePoint="30004" id="30015" length="0" mx="0.1" my="0.1" name="Corte_Espalda_Codo" showPointName="true" type="endLine"/>
    <point angle="0" basePoint="30006" id="30016" length="0" mx="0.1" my="0.1" name="Corte_Espalda_Puno" showPointName="true" type="endLine"/>
    
    <line firstPoint="30011" id="30021" lineColor="blue" lineType="dashLine" secondPoint="30012"/>
    <line firstPoint="30012" id="30022" lineColor="blue" lineType="dashLine" secondPoint="30013"/>
    <line firstPoint="30002" id="30023" lineColor="blue" lineType="dashLine" secondPoint="30004"/>
    <line firstPoint="30004" id="30024" lineColor="blue" lineType="dashLine" secondPoint="30006"/>
    
    <point angle="90" basePoint="30011" curve="12020" id="30031" lineColor="black" lineType="none" mx="0.1" my="0.1" name="Copa_Frente_Pico" showPointName="true" type="curveIntersectAxis"/>
    <point angle="90" basePoint="30002" curve="12022" id="30032" lineColor="black" lineType="none" mx="0.1" my="0.1" name="Copa_Espalda_Pico" showPointName="true" type="curveIntersectAxis"/>
    
    <line firstPoint="30011" id="30033" lineColor="blue" lineType="dashLine" secondPoint="30031"/>
    <line firstPoint="30002" id="30034" lineColor="blue" lineType="dashLine" secondPoint="30032"/>
    
    <point firstPoint="30006" id="23001" length="12" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Top" secondPoint="30004" showPointName="false" type="alongLine"/>
    <point angle="AngleLine_Fold_Espalda_Codo_Fold_Espalda_Puno + 90" basePoint="23001" id="23002" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Top_Ext" showPointName="true" type="endLine"/>
    <point angle="AngleLine_Fold_Espalda_Codo_Fold_Espalda_Puno + 90" basePoint="30006" id="23003" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Bot_Ext" showPointName="true" type="endLine"/>
    <line firstPoint="23002" id="23004" lineColor="blue" secondPoint="23003"/>
    <line firstPoint="23001" id="23005" lineColor="blue" secondPoint="23002"/>
    <line firstPoint="30006" id="23006" lineColor="blue" secondPoint="23003"/>
    
    <point angle="270" basePoint="12001" id="89500" length="@D_RUEDO_MANGA" mx="0.1" my="0.1" name="Ext_MS_Largo" showPointName="true" type="endLine"/>
    <point angle="180 - AngleLine_MS_Codo_Izq_MS_Puno_Izq" basePoint="12014" id="89501" length="@D_RUEDO_MANGA" mx="-4.7675" my="1.34276" name="Ext_MS_Puno_Izq" showPointName="true" type="endLine"/>
    <point angle="180 - AngleLine_Corte_Frente_Codo_Corte_Frente_Puno" basePoint="30013" id="89502" length="@D_RUEDO_MANGA" mx="0.1" my="0.1" name="Ext_Corte_Frente" showPointName="true" type="endLine"/>
    <point angle="180 - AngleLine_Fold_Espalda_Codo_Fold_Espalda_Puno" basePoint="23003" id="23007" length="@D_RUEDO_MANGA" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="Ext_MS_Aletilla" showPointName="true" type="endLine"/>
    
    <line firstPoint="89501" id="30051" lineColor="black" secondPoint="89500"/>
    <line firstPoint="89500" id="30052" lineColor="black" secondPoint="23007"/>
    <line firstPoint="23003" id="30053" lineColor="black" secondPoint="23007"/>
    <line firstPoint="12014" id="30054" lineColor="black" secondPoint="89501"/>
    <line firstPoint="30013" id="30055" lineColor="blue" lineType="dashLine" secondPoint="89502"/>
</root>"""
new_nodes_tree = ET.fromstring(new_sleeve_xml)
new_ids = {node.get('id') for node in new_nodes_tree if node.get('id')}

target_prefixes = ('MS_', 'Ale_', 'Fold_', 'Corte_', 'Ext_MS_', 'Ext_Corte_', 'Copa_Frente_', 'Copa_Espalda_')
prefix_ids = set()

for node in list(calculation_node):
    name = node.get('name', '')
    if name.startswith(target_prefixes):
        if node.get('id'):
            prefix_ids.add(node.get('id'))

permanently_deleted = prefix_ids - new_ids
deleted_nodes = set()

# First pass: mark prefix matches for deletion
for node in list(calculation_node):
    node_id = node.get('id')
    if node_id in prefix_ids:
        deleted_nodes.add(node_id)
    if node_id in new_ids:
        deleted_nodes.add(node_id)

# Splines/Lines check
for node in list(calculation_node):
    if node.tag in ('line', 'spline'):
        node_id = node.get('id')
        if node_id and node_id in new_ids:
            deleted_nodes.add(node_id)
            continue
            
        deps = [
            node.get('basePoint'), node.get('firstPoint'), node.get('secondPoint'),
            node.get('point1'), node.get('point4')
        ]
        deps = [d for d in deps if d is not None]
        
        if len(deps) > 0 and all(d in prefix_ids for d in deps):
            if node_id:
                deleted_nodes.add(node_id)

original_children = list(calculation_node)
first_deleted_index = next((i for i, node in enumerate(original_children) if node.get('id') in deleted_nodes), -1)

if first_deleted_index == -1:
    first_deleted_index = len(original_children)

new_children = []
removed_count = 0

for i, node in enumerate(original_children):
    if i == first_deleted_index:
        for new_node in new_nodes_tree:
            new_children.append(new_node)
            
    if node.get('id') not in deleted_nodes:
        new_children.append(node)
    else:
        removed_count += 1

calculation_node.clear()
for child in new_children:
    calculation_node.append(child)

pieces_root = root.find('.//pieces')
if pieces_root is not None:
    for piece in list(pieces_root):
        if piece.get('name') in ('Manga_Grde', 'Manga_Int', 'Cimera', 'Bajera'):
            pieces_root.remove(piece)

tree.write(file_path, encoding="utf-8", xml_declaration=True)
print(f"Removed {removed_count} old nodes safely. Injected true traditional 1-piece base with fold overlays.")
