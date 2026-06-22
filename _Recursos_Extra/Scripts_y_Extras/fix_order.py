import re

file_path = "Blazer_Dama_Maestro.val"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# The block to extract
aletillas_block = """
            <point firstPoint="12015" id="23001" length="12" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Top_Cimera" secondPoint="12011" showPointName="false" type="alongLine"/>
            <point angle="AngleLine_MS_Codo_Cimera_Der_MS_Puno_Cimera_Der + 90" basePoint="23001" id="23002" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Cimera_Top_Ext" showPointName="true" type="endLine"/>
            <point angle="AngleLine_MS_Codo_Cimera_Der_MS_Puno_Cimera_Der + 90" basePoint="12015" id="23003" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Cimera_Bot_Ext" showPointName="true" type="endLine"/>
            <point firstPoint="12017" id="23004" length="12" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Top_Bajera" secondPoint="12013" showPointName="false" type="alongLine"/>
            <point angle="AngleLine_MS_Codo_Bajera_Der_MS_Puno_Bajera_Der + 90" basePoint="23004" id="23005" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Bajera_Top_Ext" showPointName="true" type="endLine"/>
            <point angle="AngleLine_MS_Codo_Bajera_Der_MS_Puno_Bajera_Der + 90" basePoint="12017" id="23006" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Bajera_Bot_Ext" showPointName="true" type="endLine"/>"""

# Remove the block from its current location
if aletillas_block in content:
    content = content.replace(aletillas_block, "")
    print("Removed block from original position")
else:
    # Try regex with flexible whitespace
    import re
    pattern = re.compile(r'\s*<point firstPoint="12015" id="23001".*?id="23006".*?type="endLine"/>', re.DOTALL)
    if pattern.search(content):
        match = pattern.search(content).group(0)
        content = content.replace(match, "")
        aletillas_block = match # save it to insert later
        print("Removed block using regex")
    else:
        print("COULD NOT FIND BLOCK TO REMOVE")

# Insert it right before 23007
target_insert = '<point angle="180 - AngleLine_MS_Aletilla_Top_Cimera_MS_Aletilla_Cimera_Bot_Ext" basePoint="23003" id="23007"'

if target_insert in content:
    content = content.replace(target_insert, aletillas_block.lstrip() + "\n            " + target_insert)
    print("Inserted block successfully")
else:
    print("COULD NOT FIND TARGET TO INSERT")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
