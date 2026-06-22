import os

rules_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/.antigravityrules'
with open(rules_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'PROTOCOLO DE GÉNESIS' not in content:
    genesis_block = """
18. PROTOCOLO DE GÉNESIS (Creación de Nuevos Maestros):
Al recibir la orden de crear un archivo `.val` desde cero, el agente tiene PROHIBIDO improvisar la estructura. Debe iniciar obligatoriamente con este esqueleto "boilerplate":
- Paso 1 (Cabecera): Iniciar XML en v0.7.3 estricto y enlazar inmediatamente a <measurements>Maestro_Variables_IA.smis</measurements>.
- Paso 2 (Bloque de Incrementos): Declarar inmediatamente la etiqueta <variables> e inyectar el kit básico de parámetros de diseño (mínimo #holgura_superior, #holgura_inferior, #holgura_cintura, #ruedo_prenda, #holgura_sisa).
- Paso 3 (DraftBlock Base): Abrir un único <draftBlock name="Cuerpo_Principal"> con un punto <point id="1" name="F_Origen" type="single" x="0" y="0"/> (u otros orígenes distanciados).
- Paso 4 (Pre-Inyección M.A.S.): Si la prenda pertenece al tren superior (camisa, chaqueta, bata), se debe declarar la variable ALERTA_SISA_ESTRECHA anclada a F_Origen incluso antes de empezar a dibujar las curvas, para asegurar que el blindaje nazca con el archivo.
"""
    with open(rules_path, 'a', encoding='utf-8') as f:
        f.write(genesis_block)
    print("Protocolo de Génesis añadido.")
else:
    print("El protocolo ya estaba presente.")
