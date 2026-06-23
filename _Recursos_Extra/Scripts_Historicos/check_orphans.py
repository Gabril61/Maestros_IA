import xml.etree.ElementTree as ET

file_path = 'c:/Users/Ricx18/Desktop/Maestros_IA/Blazer_Dama_Maestro.val'
tree = ET.parse(file_path)
root = tree.getroot()

print("Buscando Puntos A1, A2, A7_Piquete:")
for pt in root.iter('point'):
    if pt.get('name') in ['A1', 'A2', 'A7_Piquete']:
        print(f"  Encontrado punto {pt.get('name')} (id: {pt.get('id')})")

print("Buscando Splines 12044, 12045:")
for spline in root.iter('spline'):
    if spline.get('id') in ['12044', '12045']:
        print(f"  Encontrado spline {spline.get('id')}")

print("Buscando Lineas 12044, 12045:")
for line in root.iter('line'):
    if line.get('id') in ['12044', '12045']:
        print(f"  Encontrada linea {line.get('id')}")

