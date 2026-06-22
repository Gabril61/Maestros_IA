import re

file_path = "Blazer_Dama_Maestro.val"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# width formulas
content = re.sub(r'(id="12004".*?) \+ 1\.5"', r'\1 + 3"', content)
content = re.sub(r'(id="12005".*?) \+ 1\.5"', r'\1"', content)
content = re.sub(r'(id="12006".*?) - 1\.5"', r'\1 - 3"', content)
content = re.sub(r'(id="12007".*?) - 1\.5"', r'\1"', content)

# codo formulas
content = re.sub(r'(id="12010".*?) \+ 2"', r'\1 + 3"', content)
content = re.sub(r'(id="12011".*?) \+ 2"', r'\1"', content)
content = re.sub(r'(id="12012".*?) - 1\.5"', r'\1 - 3"', content)
content = re.sub(r'(id="12013".*?) - 1\.5"', r'\1"', content)

# puno formulas
content = re.sub(r'(id="12014".*?) \+ 1\.5"', r'\1 + 3"', content)
content = re.sub(r'(id="12015".*?) \+ 1\.5"', r'\1"', content)
content = re.sub(r'(id="12016".*?) - 1\.5"', r'\1 - 3"', content)
content = re.sub(r'(id="12017".*?) - 1\.5"', r'\1"', content)

# add aletilla points right after 12017
target = 'name="MS_Puno_Bajera_Der" showPointName="true" type="endLine"/>'

aletillas = """name="MS_Puno_Bajera_Der" showPointName="true" type="endLine"/>
            <point firstPoint="12015" id="23001" length="12" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Top_Cimera" secondPoint="12011" showPointName="false" type="alongLine"/>
            <point angle="AngleLine_MS_Puno_Cimera_Der_MS_Codo_Cimera_Der - 90" basePoint="23001" id="23002" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Cimera_Top_Ext" showPointName="true" type="endLine"/>
            <point angle="AngleLine_MS_Puno_Cimera_Der_MS_Codo_Cimera_Der - 90" basePoint="12015" id="23003" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Cimera_Bot_Ext" showPointName="true" type="endLine"/>
            <point firstPoint="12017" id="23004" length="12" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Top_Bajera" secondPoint="12013" showPointName="false" type="alongLine"/>
            <point angle="AngleLine_MS_Puno_Bajera_Der_MS_Codo_Bajera_Der - 90" basePoint="23004" id="23005" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Bajera_Top_Ext" showPointName="true" type="endLine"/>
            <point angle="AngleLine_MS_Puno_Bajera_Der_MS_Codo_Bajera_Der - 90" basePoint="12017" id="23006" length="3.5" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="MS_Aletilla_Bajera_Bot_Ext" showPointName="true" type="endLine"/>"""

if target in content:
    content = content.replace(target, aletillas)
    print("Aletillas added!")
else:
    print("Could not find target for Aletillas")

# add aletilla hem extensions
target_ext = 'name="Ext_MS_Puno_Bajera_Der" showPointName="true" type="endLine"/>'

aletillas_ext = """name="Ext_MS_Puno_Bajera_Der" showPointName="true" type="endLine"/>
            <point angle="180 - AngleLine_MS_Aletilla_Top_Cimera_MS_Aletilla_Cimera_Bot_Ext" basePoint="23003" id="23007" length="@D_RUEDO_MANGA" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="Ext_MS_Aletilla_Cimera" showPointName="true" type="endLine"/>
            <point angle="180 - AngleLine_MS_Aletilla_Top_Bajera_MS_Aletilla_Bajera_Bot_Ext" basePoint="23006" id="23008" length="@D_RUEDO_MANGA" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="Ext_MS_Aletilla_Bajera" showPointName="true" type="endLine"/>
            <line firstPoint="23002" id="23009" lineColor="black" lineType="solidLine" lineWeight="0.35" secondPoint="23003"/>
            <line firstPoint="23005" id="23010" lineColor="black" lineType="solidLine" lineWeight="0.35" secondPoint="23006"/>"""

if target_ext in content:
    content = content.replace(target_ext, aletillas_ext)
    print("Aletilla Hem Extensions added!")
else:
    print("Could not find target for Aletilla Hem Extensions")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Formulas updated successfully!")
