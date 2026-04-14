# Metadatos de los datos de embarcaciones

## Fuentes
-Secretaría de Agricultura y Desarrollo Rural, Comisión Nacional de Acuacultura y Pesca, Anuario Estadístico de Acuacultura y Pesca Ediciones 2018 - 2023 CONAPESCA, México.
-Secretaría de Agricultura y Desarrollo Rural, Comisión Nacional de Acuacultura y Pesca, Dirección General de Planeación, Programación y Evaluación, Abril, 2025.
-Secretaría de Agricultura, Ganadería, Desarrollo Rural, Pesca y Alimentación, Comisión Nacional de Acuacultura y Pesca, Anuario Estadístico de Acuacultura y Pesca, Ediciones 2003 - 2017, CONAPESCA, México

- **URL**: http://dgeiawf.semarnat.gob.mx:8080/ibi_apps/WFServlet?IBIF_ex=D2_PESCA01_06_mar&IBIC_user=c25&IBIC_pass=c25
- **Fecha de descarga**: [02/04/2026]

## Archivos procesados 

### `total_embarcaciones.csv`
- **Descripción**: Registro del número total de embarcaciones pesqueras en la región de Baja California. Para la construcción de este dataset, se filtraron únicamente las entidades correspondientes a las Baja Californias, eliminando el resto de los estados. Posteriormente, se agregaron los datos para obtener un valor consolidado de embarcaciones, sin distinguir entre categorías específicas como pesca de altura o pesca ribereña.

Las variaciones a lo largo del tiempo pueden reflejar cambios en la capacidad pesquera, políticas de regulación del esfuerzo pesquero, condiciones económicas del sector y la disponibilidad de recursos marinos. Este indicador es relevante para analizar la presión ejercida sobre los ecosistemas marinos en relación con la actividad pesquera.
- **Variables**:
  - `año`: entero, rango 1989–2024.
  - `total_embarcaciones`: entero
- **Transformaciones aplicadas**:
  - Se juntaron los dato de Baja California y Baja California Sur.
  - Se eliminaron el resto de estados que no se usaron.
  - Se elimino las distincion entre los tipos de pesca y solo se tomo la total.

## Archivos original

### `embarcaciones.xlsx`
- **Formato**: Excel, hoja de indicadores, hoja de metadatos originales, hoja de fuentes.
- **Observaciones**: Incluye datos de otras entidades federativas asi como distincion entre tipos de pesca y distintos litorales.
- 
## Notas adicionales
- Sin notas adicionales.
