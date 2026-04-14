# Metadatos de los datos de producción pesquera

## Fuentes: 
- Secretaría de Agricultura y Desarrollo Rural, Comisión Nacional de Acuacultura y Pesca, Anuario Estadístico de Acuacultura y Pesca Ediciones 2018 - 2023 CONAPESCA, México.
- Secretaría de Agricultura y Desarrollo Rural, Comisión Nacional de Acuacultura y Pesca, Dirección General de Planeación, Programación y Evaluación, Abril, 2025.
- Secretaría de Agricultura, Ganadería, Desarrollo Rural, Pesca y Alimentación, Comisión Nacional de Acuacultura y Pesca, Anuario Estadístico de Acuacultura y Pesca, Ediciones 2003 - 2017, CONAPESCA, México.

- **URL**: http://dgeiawf.semarnat.gob.mx:8080/ibi_apps/WFServlet?IBIF_ex=D2_PESCA01_01&IBIC_user=c25&IBIC_pass=c25
- **Fecha de descarga**: [02-04-2026]

## Archivo procesado

### `produccion_pesquera.csv`
- **Descripción**: Volúmenes de captura y de producción de acuacultura. Las diferencias observadas entre años consecutivos en los datos se deben a la variabilidad natural de las poblaciones de especies pesqueras (productividad natural), así como a la ocasionada por los cambios en las condiciones oceánicas (régimen de temperatura, fenómenos meteorológicos como El Niño), y a los niveles particulares de explotación a que sea sometida una pesquería en un año o periodo en particular, por lo cual se afectan los volúmenes de captura de años posteriores. Los datos proceden de los anuarios que se indican en la fuente y de la Comisión Nacional de Acuacultura y Pesca (Conapesca) para el caso de la información más reciente que aún no se integra al anuario correspondiente; una vez que se publica éste dicha información se revisa de acuerdo con él.
Debe señalarse que en materia del destino de la producción, a partir del Anuario 2021 se presentan en consumo humano directo datos de pesquerías que normalmente se presentaban en anuarios previos solo en consumo humano indirecto o en uso industrial; es el caso de las pesquerías algas, fauna de acompañamiento y peces de ornato. En el Anuario 2022, por ejemplo, se presenta producción de fauna de acompañamiento destinada al consumo humano directo y al indirecto.
- **Variables**:
  - `año`: entero, rango 1986–2024.
  - `Producción pesquera en Baja California (Sur y norte) (toneladas)`: entero
- **Transformaciones aplicadas**:
  - Se eliminó la información de todos los estados distintos a Baja California y Baja California Sur
  - Se sumó la cantidad de toneladas en Baja California y Baja California Sur.

## Archivo original

### `produccion_pesquera_original.xlsx`
- **Formato**: Excel, hoja de indicadores, hoja de metadatos originales, hoja de fuentes.
- **Observaciones**: Incluye datos de otras entidades federativas, 

## Notas adicionales
- Sin notas adicionales

