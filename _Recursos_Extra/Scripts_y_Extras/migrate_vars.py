import xml.etree.ElementTree as ET

filepath = r'C:\Users\Ricx18\Desktop\Maestros_IA\Falda_Ejecutiva_Dama_Maestro.val'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

variables_xml = """<variables>
        <m description="Holgura inferior total" name="#holgura_inferior" value="4"/>
        <m description="Pinza de cintura" name="#pinza_cintura" value="3"/>
        <m description="Ancho de pretina" name="#ancho_pretina" value="4"/>
        <m description="Ruedo prenda" name="#ruedo_prenda" value="3"/>
        <m description="Largo cierre" name="#largo_cierre" value="15"/>
    </variables>"""

content = content.replace('<variables/>', variables_xml)

replacements = {
    '@D_HOLGURA_INFERIOR': '#holgura_inferior',
    '@D_PINZA_CINT_INF': '#pinza_cintura',
    '@D_ANCHO_PRETINA': '#ancho_pretina',
    '@D_RUEDO_PRENDA': '#ruedo_prenda',
    '@D_LARGO_CIERRE': '#largo_cierre'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Variables migrated successfully.")
