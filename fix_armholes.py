import os

def fix_camisa():
    path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Camisa_Dama_Maestro.val'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update formulas
    content = content.replace('length="(@S_ANCHO_ESPALDA / 2) + 6" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Linea_Sisa"',
                              'length="(@S_CONT_SISA / 2) + #holgura_sisa" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="F_Linea_Sisa"')
    content = content.replace('length="(@S_ANCHO_ESPALDA / 2) + 6" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Linea_Sisa"',
                              'length="(@S_CONT_SISA / 2) + #holgura_sisa" lineColor="black" lineType="none" lineWeight="0.35" mx="0.1" my="0.1" name="T_Linea_Sisa"')
                              
    # 2. Hide alert text
    content = content.replace('name="ALERTA_SISA_ESTRECHA" showPointName="true"', 'name="ALERTA_SISA_ESTRECHA" showPointName="false"')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Camisa fixed.')

def fix_blazer():
    path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change holgura_sisa to 15% for Blazer
    content = content.replace('formula="@S_CONT_SISA * 0.1" name="#holgura_sisa"',
                              'formula="@S_CONT_SISA * 0.15" name="#holgura_sisa"')
    content = content.replace('description="Holgura dinámica y escalable de sisa (10%)"',
                              'description="Holgura dinámica y escalable de sisa (15% blazer)"')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Blazer fixed.')

fix_camisa()
fix_blazer()
