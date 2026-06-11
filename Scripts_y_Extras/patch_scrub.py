with open(r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '<line firstPoint="5" id="14" secondPoint="13"/>\n            \n            <spline angle1="AngleLine_E_Cuello_Ancho_E_Hombro_Punta - 90"',
    '<line firstPoint="5" id="14" secondPoint="13"/>\n            <line firstPoint="13" id="999" secondPoint="11"/>\n            \n            <spline angle1="AngleLine_E_Cuello_Ancho_E_Hombro_Punta - 90"'
)

content = content.replace(
    '<line firstPoint="104" id="113" secondPoint="112"/>\n            \n            <spline angle1="AngleLine_D_Cuello_Ancho_D_Hombro_Punta + 90"',
    '<line firstPoint="104" id="113" secondPoint="112"/>\n            <line firstPoint="112" id="998" secondPoint="110"/>\n            \n            <spline angle1="AngleLine_D_Cuello_Ancho_D_Hombro_Punta + 90"'
)

with open(r"c:\Users\Ricx18\Desktop\Maestros_IA\Scrub_Top_Medico_Maestro_Clo.val", "w", encoding="utf-8") as f:
    f.write(content)
print("File patched.")
