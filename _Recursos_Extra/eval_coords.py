import xml.etree.ElementTree as ET
import os
import re

def eval_coords():
    val_path = r"C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Patrones_Generados\Darlis_Sifontes_2026-06-28T233841\Blusa_Cuello_Mao_Dama_Maestro.val"
    smis_path = r"C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Patrones_Generados\Darlis_Sifontes_2026-06-28T233841\Maestro_Variables_IA.smis"
    
    # 1. Parse SMIS variables
    smis_tree = ET.parse(smis_path)
    variables = {}
    for m in smis_tree.findall('.//m'):
        name = m.attrib.get('name')
        value = m.attrib.get('value')
        if name and value:
            value = value.replace(',', '.')
            try:
                variables[name] = float(value)
            except:
                pass
                
    # 2. Parse VAL variables
    val_tree = ET.parse(val_path)
    for v in val_tree.findall('.//variable'):
        name = v.attrib.get('name')
        formula = v.attrib.get('formula')
        if name and formula:
            try:
                variables[name] = float(formula)
            except:
                pass
                
    def evaluate(formula):
        for k, v in variables.items():
            formula = formula.replace(k, str(v))
        formula = re.sub(r'@[A-Za-z_]+', '0', formula)
        try:
            return eval(formula)
        except Exception as e:
            return 0
            
    print("Variables:")
    print("Busto:", variables.get('@S_CONT_BUSTO'))
    print("Espalda:", variables.get('@S_ANCHO_ESPALDA'))

    for pt in ['100', '109', '110', '107', '111', '159', '160']:
        p = val_tree.find(f'.//point[@id="{pt}"]')
        if p is not None:
            name = p.attrib.get('name', pt)
            length = evaluate(p.attrib.get('length', '0'))
            angle = evaluate(p.attrib.get('angle', '0'))
            base = p.attrib.get('basePoint', 'None')
            print(f"Point {name} (id={pt}): base={base}, angle={angle}, length={length}")

if __name__ == "__main__":
    eval_coords()
