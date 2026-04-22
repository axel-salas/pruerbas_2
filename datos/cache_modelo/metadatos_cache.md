# Metadatos de los datos

## Fuentes:
- Generación propia a partir de simulaciones de modelo ecológico implementado en Python.
- Basado en los datos procesados y en la estructura del modelo dinámico descrito en el tablero.

- **URL**: No aplica (datos generados localmente)

- **Fecha de generación**: [16-04-2026]

## Archivos procesados 

### `cache_escenarios.json`
- **Descripción**: Archivo de almacenamiento (cache) de los resultados de simulaciones del modelo ecológico utilizado en el tablero. Contiene predicciones generadas previamente para evitar la ejecución repetida del modelo durante el renderizado.

Originalmente, las simulaciones se ejecutaban cada vez que se renderizaba el tablero, lo que implicaba un alto costo computacional y tiempos de espera elevados. Para optimizar el desempeño, los resultados fueron precomputados y almacenados en este archivo, permitiendo una carga eficiente y consistente de las predicciones.

El cache incluye las trayectorias simuladas del sistema bajo distintas condiciones iniciales y/o parámetros, dependiendo de la configuración del modelo.


- **Código de generación**:
  En /scripts se pueden encontrar todos,los codigos utilizados para la creacion y almacenaje de los datos

## Archivos originales

### No aplica
- **Formato**: No aplica
- **Observaciones**: Los datos fueron generados directamente a partir de simulaciones del modelo, no provienen de una fuente externa.

## Notas adicionales
- Este archivo forma parte de una estrategia de optimización del tablero.
- Su uso permite reducir significativamente el tiempo de renderizado y el consumo de recursos.
- En caso de modificar el modelo o sus parámetros, es necesario regenerar este archivo para mantener la consistencia de los resultados.
