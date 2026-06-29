import xml.etree.ElementTree as ET
import os
import re

def eval_seamly():
    val_path = r"C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Patrones_Generados\Darlis_Sifontes_2026-06-28T233841\Blusa_Cuello_Mao_Dama_Maestro.val"
    smis_path = r"C:\Users\Ricx18\Desktop\App_Formulario\TextilFit_Bot\Patrones_Generados\Darlis_Sifontes_2026-06-28T233841\Maestro_Variables_IA.smis"
    
    # 1. Parse SMIS variables
    smis_tree = ET.parse(smis_path)
    variables = {}
    for m in smis_tree.findall('.//m'):
        name = m.attrib.get('name')
        value = m.attrib.get('value')
        if name and value:
            # Replace comma with dot for float
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

    # 3. Find F_Costado_Sisa formula
    point = val_tree.find('.//point[@name="F_Costado_Sisa"]')
    formula_sisa = point.attrib.get('length')
    
    point_pecho = val_tree.find('.//point[@name="F_Ancho_Pecho"]')
    formula_pecho = point_pecho.attrib.get('length')
    
    print(f"Sisa Formula: {formula_sisa}")
    print(f"Pecho Formula: {formula_pecho}")
    
    # Simple evaluation
    def evaluate(formula):
        for k, v in variables.items():
            formula = formula.replace(k, str(v))
        # Remove anything unknown
        formula = re.sub(r'@[A-Za-z_]+', '0', formula)
        try:
            return eval(formula)
        except Exception as e:
            return f"Error: {e}"

    print(f"Sisa Evaluated: {evaluate(formula_sisa)}")
    print(f"Pecho Evaluated: {evaluate(formula_pecho)}")

if __name__ == "__main__":
    eval_seamly()
