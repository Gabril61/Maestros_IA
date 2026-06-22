# 🔬 Protocolo CLO
**Ingeniería Inversa: De Simulación 3D a Parametrización Escalable 2D**

> **Propósito:** Este protocolo establece el flujo de trabajo estándar para extraer la topología de prendas previamente validadas y probadas en maniquíes virtuales dentro de **CLO 3D**, y traducirlas a patrones dinámicos, paramétricos y de grado industrial en **Seamly2D (TextilFit)**.

---

## 🛠️ Fase 1: Extracción de Datos (El Escáner Geométrico)
El objetivo de esta fase es leer la "huella genética" del patrón 3D. No nos interesan las tallas fijas, sino las **proporciones relativas**.

1. **Exportación:** Desde CLO 3D, exportar el patrón 2D en formato estandarizado **DXF-AAMA**.
2. **Análisis Vectorial:** Utilizar scripts de Python (`ezdxf`) para parsear las polilíneas del archivo `.dxf`.
3. **Lectura de Landmarks:** 
   - Calcular los *Bounding Boxes* (Cajas Delimitadoras) de cada pieza (ancho y alto máximo).
   - Extraer las coordenadas (X, Y) de los puntos críticos: Punta de Hombro, Axila (Sisa inferior), y Profundidad de Escote.
4. **Diagnóstico Topológico:** Identificar visualmente y matemáticamente el tipo de prenda. ¿Es una sisa anatómica profunda? ¿Es un bloque "Drop-Shoulder" (hombro caído)? ¿Es un rectángulo holgado?

---

## 🧬 Fase 2: Traducción Paramétrica (El ADN TextilFit)
Nunca se deben trasladar valores en centímetros quemados (fijos). Cada medida de CLO debe convertirse a un múltiplo o constante dinámica ligada a la tabla `.smis`.

1. **Cálculo de Holguras (`#`):** 
   - Restar la medida corporal estándar de la medida de CLO 3D para hallar el "Ease" real.
   - *Ejemplo:* Si el CLO 3D Frontal mide 29 cm de ancho, y el cuarto de busto estándar (`@S_CONT_BUSTO / 4`) es 24 cm, la holgura se declara como: `#holgura_pecho = 5.0`.
2. **Proporciones Corporales (`@`):** 
   - Atar las medidas base a las variables M.A.S. (ej. Profundidad de escote V ligada a `@S_TALLE_DELANTERO * 0.45`).
3. **Aislamiento de Detalles:** Separar extensiones de diseño (ej. `#caida_hombro_extra = 2.0`) para permitir el escalado independiente de la estructura anatómica.

---

## 🏗️ Fase 3: Arquitectura en Seamly2D
La reconstrucción se realiza construyendo el patrón desde cero a través de XML o de la interfaz, respetando las leyes geométricas del software.

1. **DraftBlock Único:** Para garantizar la coherencia visual y paramétrica, dibujar todas las piezas principales (Delantero, Espalda, Manga) dentro del mismo bloque de dibujo (ej. `Scrub_Top_Clo`).
2. **Nomenclatura Estricta:** Usar el prefijo del bloque (`E_` para Espalda, `D_` para Delantero, `M_` para Manga).
3. **Declaración de Enlaces Invisibles:** 
   - **Regla de Oro:** Siempre declarar la herramienta `<line>` entre dos puntos clave (ej. de Punta de Hombro a Axila) antes de usar su longitud en una curva. El prefijo correcto para extraer la longitud de esa curva posteriormente es `Spl_...` (y no `Spline_...`).

---

## 📐 Fase 4: Calibración de Curvas (Reglas de Bezier)
La topología plana de CLO no garantiza un corte impecable si las curvas se trazan a ojo. Se deben aplicar las matemáticas estrictas de TextilFit para evitar bultos o "bolsas" al coser.

### A. Sisas del Tronco (Armholes)
- **Ángulo de Llegada (Axila):** La curva de sisa debe aterrizar de forma **completamente vertical (90° o 270°)** en el punto de axila. Esto garantiza que la costura lateral sea una línea fluida e invisible sin picos.
- **Ángulo de Salida (Hombro):** Debe arrancar en posición perpendicular a la pendiente de hombro (o lo más anatómico posible al diseño).

### B. El Trabajo de Copa (Manga)
- **Multiplicadores Asimétricos:** Nunca usar el mismo multiplicador para los dos extremos de la copa. Utilizar el estándar M.A.S.:
  - Tensor de Cima (Origen): `* 0.55` al `0.60` (Para mantener una caída de hombro redondeada).
  - Tensor de Axila (Sisa inferior): `* 0.15` al `0.25` (Para aplanar la curva al unirse al costado).
- **El Ángulo de la Onda (S-Curve):** Para lograr la típica curva cóncava ("onda") debajo de la axila, el ángulo de salida de la curva en el punto de la axila debe ser **completamente horizontal** (ej. `0°` o `180°`). Si se utiliza un ángulo vertical (`90°`), la copa se inflará formando una campana o domo convexo inutilizable.

---
*Protocolo instaurado oficialmente para la estandarización de moldería avanzada entre CLO 3D y Seamly2D.*
