import os
import json
from datetime import datetime

def create_ki():
    ki_dir = r"C:\Users\Ricx18\.gemini\antigravity\knowledge\Antigravity_Rules"
    artifacts_dir = os.path.join(ki_dir, "artifacts")
    
    os.makedirs(artifacts_dir, exist_ok=True)
    
    metadata = {
        "summary": "CRÍTICO: REGLAS FUNDAMENTALES DEL WORKSPACE. Antes de iniciar cualquier análisis, codificación o refactorización, el agente DEBE leer el archivo .antigravityrules ubicado en la raíz del workspace (c:\\Users\\Ricx18\\Desktop\\Maestros_IA\\.antigravityrules). Este archivo contiene las leyes de geometría, topología y MTM que gobiernan los patrones de TextilFit. IGNORAR ESTE ARCHIVO ES INACEPTABLE.",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "last_accessed": datetime.utcnow().isoformat() + "Z",
        "references": ["Workspace root: .antigravityrules"]
    }
    
    with open(os.path.join(ki_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
        
    instructions = "# Instrucciones de Cumplimiento\n\n1. Utiliza tu herramienta `view_file` para leer el archivo `c:\\Users\\Ricx18\\Desktop\\Maestros_IA\\.antigravityrules` en su totalidad.\n2. No inicies ningún plan de implementación sin antes haber validado tus decisiones arquitectónicas contra las reglas de este archivo.\n3. Si una regla (ej. Regla 14 de empalme o Regla 15 de contornos) aplica a tu tarea, menciónalo explícitamente en el plan."
    
    with open(os.path.join(artifacts_dir, "instrucciones_obligatorias.md"), "w", encoding="utf-8") as f:
        f.write(instructions)
        
    print("KI Antigravity_Rules creado exitosamente.")

if __name__ == "__main__":
    create_ki()
