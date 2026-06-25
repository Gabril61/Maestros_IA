import xml.etree.ElementTree as ET
import glob
import os
import sys

def auditar_contornos():
    directorio_maestros = r"C:\Users\Ricx18\Desktop\Maestros_IA"
    
    if len(sys.argv) > 1:
        nombre_especifico = sys.argv[1]
        ruta_especifica = os.path.join(directorio_maestros, nombre_especifico)
        if not os.path.exists(ruta_especifica):
            print(f"Error: No se encontró el archivo {nombre_especifico}")
            return
        archivos_val = [ruta_especifica]
    else:
        archivos_val = glob.glob(os.path.join(directorio_maestros, "*.val"))
    
    reporte = []
    reporte.append("==========================================================")
    reporte.append("      REPORTE DEL VIGILANTE DE CONTORNOS Y PINZAS")
    reporte.append("==========================================================\n")
    
    for archivo in archivos_val:
        nombre_archivo = os.path.basename(archivo)
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()
            puntos_cintura_cadera = []
            
            for p in root.findall('.//point'):
                name = p.attrib.get('name', '')
                formula = p.attrib.get('length', '')
                
                if not name or not formula:
                    continue
                    
                # Solo nos interesan los puntos de expansión lateral o pinzas
                if 'Costado_Cintura' in name or 'Costado_Cadera' in name or 'Costado_Ruedo' in name:
                    puntos_cintura_cadera.append((name, formula))
            
            if puntos_cintura_cadera:
                reporte.append(f"[{nombre_archivo}]")
                for nombre, formula in puntos_cintura_cadera:
                    estado = "OK"
                    observacion = ""
                    
                    # Verificación de Método de Bloque (Plomada de Busto)
                    if "@S_CONT_BUSTO" in formula:
                        # Si cae a plomo desde el busto, OBLIGATORIAMENTE debe descontar una pinza (o ser un bloque 100% recto)
                        if "Line_" in formula or "Pinza" in formula or "-" in formula:
                            estado = "OK (Bloque con Descuento)"
                        else:
                            estado = "ADVERTENCIA"
                            observacion = "Cae a plomo desde Busto pero NO resta ninguna pinza. Verificar si el entalle se hace en otro punto."
                    elif "@S_CONT_CINTURA" in formula:
                        if "Line_" in formula or "Pinza" in formula:
                            estado = "OK (Medida Real con Descuento)"
                        else:
                            estado = "OK (Medida Real Plana)"
                    
                    reporte.append(f"  -> {nombre}")
                    reporte.append(f"     Formula: {formula}")
                    reporte.append(f"     Estado: {estado} {observacion}")
                reporte.append("-" * 50)
                
        except Exception as e:
            reporte.append(f"Error analizando {nombre_archivo}: {e}")

    reporte_final = "\n".join(reporte)
    
    # Imprimir en consola
    print(reporte_final)
    
    # Guardar reporte en archivo
    ruta_reporte = os.path.join(directorio_maestros, "_Recursos_Extra", "auditoria_contornos.txt")
    with open(ruta_reporte, "w", encoding="utf-8") as f:
        f.write(reporte_final)
        
    print(f"\nReporte guardado exitosamente en: {ruta_reporte}")

if __name__ == "__main__":
    auditar_contornos()
