import re

files = {
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Dama_Maestro.val': '30007', # T_Nivel_Doblez
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Estandar_Maestro.val': '30035',
    r'C:\Users\Ricx18\Desktop\Maestros_IA\Bata_Medica_Unisex_Maestro.val': '31002'
}

for path, dob_id in files.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Line 249 connects 232 (T_Aletilla_Bot) to 218 (T_Nivel_Largo). Change 218 to T_Nivel_Doblez.
    content = re.sub(r'(<line[^>]*id="249"[^>]*secondPoint=")218(")', rf'\g<1>{dob_id}\g<2>', content)
    
    # In Estandar, line 243 connects 221 to 232. It should probably connect to T_Costado_Doblez (30036 in Estandar)
    # Actually, the hem extension script already drew the hem lines (30043, etc.).
    # So we don't necessarily need line 243 if it's the old hem line. But let's leave it or fix it.
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed lines.")
