import xml.etree.ElementTree as ET
import re
import sys
import os

class AntigravityAuditor:
    def __init__(self, val_path):
        self.val_path = val_path
        self.tree = ET.parse(val_path)
        self.root = self.tree.getroot()
        self.content = ET.tostring(self.root, encoding='unicode')
        self.errors = []
        self.warnings = []
        
    def check_rule_no_d_vars(self):
        """Check for deprecated @D_ variables"""
        d_vars = set(re.findall(r'@D_\w+', self.content))
        if d_vars:
            self.errors.append(f"[Regla 1] Se encontraron variables @D_ obsoletas: {d_vars}")
            
    def check_rule_chronological_ids(self):
        """Check for chronological references (Rule 7)"""
        defined_ids = set()
        for elem in self.root.iter():
            if 'id' in elem.attrib:
                defined_ids.add(elem.attrib['id'])
                
            refs = [elem.attrib.get('basePoint'), elem.attrib.get('firstPoint'), 
                    elem.attrib.get('secondPoint'), elem.attrib.get('point1'), 
                    elem.attrib.get('point4'), elem.attrib.get('idObject')]
                    
            for ref in refs:
                if ref and ref not in defined_ids:
                    self.errors.append(f"[Regla 7] Referencia futura u huérfana detectada: ID {ref} es referenciado antes de ser creado o no existe.")

    def check_rule_sisa_estrecha(self):
        """Check for ALERTA_SISA_ESTRECHA logic (Rule 13)"""
        has_alerta = False
        for p in self.root.iter('point'):
            name = p.get('name', '')
            if 'ALERTA_SISA_ESTRECHA' in name:
                has_alerta = True
                formula = p.get('length', '')
                if '@S_CONT_SISA' not in formula:
                    self.errors.append("[Regla 13] ALERTA_SISA_ESTRECHA no está utilizando @S_CONT_SISA en su fórmula.")
                if '?' not in formula:
                     self.errors.append("[Regla 13] ALERTA_SISA_ESTRECHA no utiliza el operador ternario '?' para dispararse.")
        if not has_alerta:
            self.warnings.append("[Regla 13] No se detectó el punto ALERTA_SISA_ESTRECHA. Si es una prenda superior, esto es una violación grave.")

    def check_rule_copa_manga(self):
        """Check for standard sleeve cap ratios (Rule 16)"""
        has_sleeve = False
        has_ratios = False
        for s in self.root.iter('spline'):
            l1 = s.get('length1', '')
            l2 = s.get('length2', '')
            if '0.55' in l1 or '0.55' in l2:
                has_ratios = True
            if 'MS_' in s.get('angle1', '') or 'MS_' in s.get('angle2', ''):
                has_sleeve = True
                
        if has_sleeve and not has_ratios:
            self.errors.append("[Regla 16] La prenda tiene manga pero no utiliza los ratios paramétricos obligatorios (* 0.55, * 0.15) en los tiradores de la copa.")

    def check_rule_corte_princesa(self):
        """Auditoría Topológica del Corte Princesa (Reglas 12 y 17-E)"""
        for s in self.root.iter('spline'):
            a1, a2 = s.get('angle1', ''), s.get('angle2', '')
            l1, l2 = s.get('length1', ''), s.get('length2', '')
            is_apex = 'APEX' in a1 or 'APEX' in a2 or 'APEX' in l1 or 'APEX' in l2
            
            if is_apex:
                if '0.25' not in l1 and '0.25' not in l2:
                    self.errors.append(f"[Regla 12] Corte Princesa: Spline {s.get('id')} hacia APEX no usa tensión * 0.25.")
                
                # Revisar que no se usen ángulos obsoletos como 165
                if '165' in a1 or '165' in a2:
                    self.errors.append(f"[Regla 12] Corte Princesa: Spline {s.get('id')} usa ángulo +165 obsoleto. DEBE usar 180 para planitud.")
                
                # El ángulo conectado al APEX debería usar 180
                if 'APEX' in a1 and '180' not in a1:
                    self.warnings.append(f"[Regla 12] Corte Princesa: El ángulo1 del Spline {s.get('id')} no indica desfase a 180 grados.")
                if 'APEX' in a2 and '180' not in a2:
                    self.warnings.append(f"[Regla 12] Corte Princesa: El ángulo2 del Spline {s.get('id')} no indica desfase a 180 grados.")

    def check_rule_alineacion_escapular(self):
        """Auditoría de Alineación Escapular de Pinza Trasera (Regla 12)"""
        for p in self.root.iter('point'):
            name = p.get('name', '')
            formula = p.get('length', '')
            if name == 'T_Pinza_Centro':
                if '@S_ANCHO_ESPALDA' in formula:
                    self.errors.append(f"[Regla 12] Alineación Escapular: El eje de {name} usa @S_ANCHO_ESPALDA en su fórmula ({formula}). DEBE usar @S_SEP_BUSTO / 2.")
                elif '@S_SEP_BUSTO' not in formula:
                    self.warnings.append(f"[Regla 12] Alineación Escapular: El eje de {name} no parece usar @S_SEP_BUSTO / 2 (Fórmula actual: {formula}).")

    def _parse_smis(self, smis_path):
        import xml.etree.ElementTree as ET
        vars_dict = {}
        try:
            tree = ET.parse(smis_path)
            for m in tree.getroot().iter('m'):
                name = m.get('name')
                val = m.get('value')
                if name and val:
                    try:
                        vars_dict[name] = float(val)
                    except ValueError:
                        pass
        except:
            pass
        return vars_dict

    def check_rule_matematica_contornos(self):
        """Motor Algebraico de Contornos"""
        measurements = self.root.find('.//measurements')
        if measurements is None or not measurements.text:
            self.warnings.append("[Motor Algebraico] No se definió archivo .smis en <measurements>.")
            return
            
        smis_path = os.path.join(os.path.dirname(self.val_path), measurements.text)
        if not os.path.exists(smis_path):
            self.warnings.append(f"[Motor Algebraico] No se pudo localizar el archivo {measurements.text}.")
            return
            
        smis_vars = self._parse_smis(smis_path)
        if not smis_vars:
            self.warnings.append("[Motor Algebraico] Archivo SMIS vacío o ilegible.")
            return
            
        # Parsear incrementos del .val
        local_vars = {}
        variables_node = self.root.find('.//variables')
        if variables_node is not None:
            for m in variables_node.iter('m'):
                local_vars[m.get('name')] = m.get('value')
                
        # Simulación de Fórmulas Matemáticas para Busto, Cintura y Cadera
        contornos_claves = ['Busto', 'Cintura', 'Cadera', 'BUSTO', 'CINTURA', 'CADERA']
        
        # Unimos las variables del SMIS y locales para el diccionario de reemplazo
        all_vars = {**smis_vars, **local_vars}
        
        def simulate_formula(formula):
            if not formula: return None
            # Eliminar operadores ternarios simples si los hay, o ignorarlos por seguridad
            if '?' in formula: return None
            
            # Reemplazar variables conocidas en la fórmula
            eq = formula
            # Ordenar variables por longitud descendente para evitar reemplazos parciales
            for var_name in sorted(all_vars.keys(), key=len, reverse=True):
                if var_name in eq:
                    eq = eq.replace(var_name, str(all_vars[var_name]))
            
            # Reemplazar cm o mm si existen
            eq = eq.replace('cm', '').replace('mm', '')
            try:
                # Evaluar la ecuación matemática resultante
                return eval(eq)
            except Exception:
                return None

        puntos_evaluados = 0
        for p in self.root.iter('point'):
            name = p.get('name', '')
            formula = p.get('length', '')
            
            if any(c in name for c in contornos_claves) and formula:
                resultado = simulate_formula(formula)
                if resultado is not None:
                    puntos_evaluados += 1
                    # Comprobación de que la fórmula incorpora la variable base nominal
                    base_nominal = False
                    for c in ['@G_CONT_', '@S_CONT_', '@S_CINTURA', '@S_CADERA', '@S_BUSTO']:
                        if c in formula: base_nominal = True
                    
                    if not base_nominal:
                        self.warnings.append(f"[Motor Algebraico] Contorno '{name}': La fórmula ({formula}) no parece basarse en la medida nominal maestra del SMIS.")
                    
                    # Verificamos si resta pinzas
                    if 'pinza' in formula.lower() and '-' not in formula:
                        self.errors.append(f"[Motor Algebraico] Fuga Detectada en '{name}': La fórmula nombra una pinza pero no realiza la sustracción algebraica.")

        self.warnings.append(f"[Motor Algebraico] Enlazado a {measurements.text}. SMIS ({len(smis_vars)} vars). {puntos_evaluados} puntos de contorno auditados exitosamente.")

    def run_audit(self):
        print(f"=== AUDITORÍA ANTIGRAVITY: {os.path.basename(self.val_path)} ===")
        self.check_rule_no_d_vars()
        self.check_rule_chronological_ids()
        self.check_rule_sisa_estrecha()
        self.check_rule_copa_manga()
        self.check_rule_corte_princesa()
        self.check_rule_alineacion_escapular()
        self.check_rule_matematica_contornos()
        
        if not self.errors and not self.warnings:
            print("[PASS] El patrón cumple con todas las reglas auditables estructurálmente.")
            return True
            
        for w in self.warnings:
            print(f"[WARNING] {w}")
            
        for e in self.errors:
            print(f"[FAIL] {e}")
            
        if self.errors:
            return False
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python audit_rules.py <ruta_al_archivo.val>")
        sys.exit(1)
    auditor = AntigravityAuditor(sys.argv[1])
    success = auditor.run_audit()
    if not success:
        sys.exit(1)
