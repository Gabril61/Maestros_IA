# Proyecto: Revisión y Corrección de Prendas Superiores (Corte Princesa)
*Fecha de inicio: 05 de Junio 2026*

## Objetivo
Revisar progresivamente todos los patrones maestros de prendas superiores en la carpeta `Maestros_IA` que incorporan el modelo "corte princesa". Estos archivos fueron clonados de un patrón original con defectos de calibración geométrica y deben ser actualizados a los nuevos estándares logrados en la `Camisa_Dama_Maestro.val`.

## Archivos a Revisar (Pendientes)
- [x] `Blazer_Dama_Maestro.val` (COMPLETADO)
- [ ] `Bata_Medica_Dama_Maestro.val`
- [ ] `Blusa_Dama_CortePrincesa_Maestro.val`
- [ ] `Blusa_Medica_Dama_Maestro.val`
- [ ] `Chaqueta_Universitaria_Dama_Maestro.val`
- [ ] `Chaleco_Femenino_Maestro.val`
- [ ] `Scrub_Top_Medico_Dama_Maestro.val`

## Estándares de Calibración a Inyectar:
1. **Corte Princesa Espalda:** La pinza debe originarse elegantemente desde la mitad del hombro (`T_Mitad_Hombro`) hasta la cintura, eliminando la curva bizarra hacia la sisa.
2. **Eliminación de Pinza Sisa Trasera:** La distancia entre `T_Sisa_Pinza_Sup` y `T_Sisa_Pinza_Inf` debe ser `0` (cerrando la sisa sin romper el trazado).
3. **Corte Princesa Delantero:** Las curvas de sisa (`splines 207, 209`) deben conectar directamente al ápice del busto (`F_APEX`) y estar suavizadas matemáticamente con las líneas de la pinza de cintura para evitar esquinas afiladas.
4. **Holguras Paramétricas Exactas:** La fórmula del entalle de cintura (`F_Costado_Real`, `T_Costado_Real`) debe usar la ecuación: `((@S_CONT_BUSTO + @D_HOLGURA_SUPERIOR) - (@G_CONT_CINTURA + @D_HOLGURA_CINTURA)) / 4 - @D_PINZA_CINT_SUP`.
5. **Manga Corta Proporcional (si aplica):** Regla condicional en el ruedo de la manga para evitar que el ancho en manga corta quede igual de ancho que el bíceps.

## Registro de Cambios
*Aquí se registrarán las prendas a medida que se completen.*
