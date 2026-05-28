import xml.etree.ElementTree as ET

xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
<pattern>
    <version>0.9.1</version>
    <unit>cm</unit>
    <description />
    <notes />
    <measurements>Maestro_Variables_IA.smis</measurements>
    <increments>
        <increment description="Holgura General Pantalon" formula="4" name="@M_HOLGURA_PANTALON"/>
    </increments>
    <draw name="Pantalon_Jogger_Clinico">
        <calculation>
            <point id="1" mx="0.132292" my="0.264583" name="A" type="single" x="10" y="10"/>
        </calculation>
        <modeling />
        <details />
    </draw>
</pattern>
'''
with open(r'C:\Users\Ricx18\Desktop\Maestros_IA\Pantalon_Jogger_Clinico_Maestro.val', 'w', encoding='utf-8') as f:
    f.write(xml_string)
