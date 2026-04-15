# AI Log - Equipo DERRE

## Herramientas 
- Claude (claude.ai)
- Gemini

## Filosfía de uso
Nuestro uso de IA fue enfocado a debuggear el código. Si el código tenía algún error, más que nada porque usamos varias herramientas nuevas, nos apoyamos de las herramientas de inteligencia artificial para encontrar los errores más rápido y ser más eficientes. El modelado matemático y todas las decisiones técnicas respecto a éste fueron tomadas por nosotros basándonos en bibliografía de ecología matemática y nuestro propio conocimiento del área. La narrativa también fue hecha por nosotros, buscando desde un principio ir un poco más allá de lo cualitativo y exploratorio a través de predicciones hechas por un modelo. Todo lo que tenía que ver selección de datos lo realizamos nosotros pues era muy importante comprender todo el contexto geográfico y ecológico y a partir de ello seleccionar correctamente los indicadores. Además de debuggear el código, utilizamos IA para explorar distintas opciones de métodos MCMC que están disponibles en la librería PyMC de inferencia bayesiana en Python, sin embargo, investigamos los métodos MCMC y nos asegurábamos de entenderlos tanto matemáticamente como a sus ventajas y desventajas para ser nosotros quiénes tomaramos la decisión final respecto a los detalles técnicos del método MCMC (utilizado para recuperar los parámetros del modelo propuesto). En resumen, los detalles matemáticos del modelo, la selección de los datos, la estructura de las simulaciones del modelo, las decisiones narrativas fueron hechas por nosotros. 

## Registro de uso 
Se explica cuál fue la prompt y en caso de que haya sido lo suficientemente significante se añade una descripción de la decisión tomada respecto a la respuesta de la IA. 

### 03-21
**Tarea**: Se utilizó Claude para generar gráficas rápidas para visualizar los datos que ibas recopilando más rápidamente y nosotros poder juzgar su comportamiento y su coherencia conforme al contexto y la narrativa que íbamos construyendo 

**Prompt**: Genera un código rápido para visualizar este csv en pandas python. (adjuntando el csv) (realizamos este proceso múltiples veces con el objetivo de acelerar el proceso de selección de datos y de planteamiento del storytelling)

### 03-25 
**Tarea**: Revisar nuestro código del PCA que le hicimos a los datos para asegurar que no hayamos cometido ningún error en este proceso. 

**Prompt**: A continuación te envío mi código del PCA que le hice a mis datos, es correcto mi código o hay algún detalle que esté omitiendo?"

**Decisión**: El código ya funcionaba y no hicimos mayor modificación. 

## 03-25
**Tarea**: 
Preguntamos a Gemini con su función de buscar por libros de ecología/biología matemática para obtener referencias y comenzar a formular el modelo. 

**Decisión y Resultado**: Al final, complementando con una búsqueda web revisamos el libro A Primer of Ecology (Nicholas J. Gotelli). También revisamos varios papers, que no citamos pues no se terminaron usando las propuestas de éstos al final. 

### 03-27
**Tarea**: Se utilizó Claude para sugerir otros métodos numéricos para ajustar el modelo (al principio no intentamos usar métodos de MCMC) 

**Prompt**: Estos son los datos de la simulación
ParámetroValorDescripciónr0.2556Tasa crecimiento presaK1.0000Cap. de carga presa [fijo]a4.8606Tasa de ataqueh5.0000Handling timee0.2032Eficiencia conversiónm0.0100Mortalidad depredadorf0.0100Crecimiento autónomo flotaC1.0000Cap. de carga flota [fijo]
Métricas de Bondad de Ajuste
MétricaValorDescripción$R^2$ H0.1828Bondad ajuste presa$R^2$ P0.3636Bondad ajuste depredadorRMSE H0.2390Error cuadrático medio presaRMSE P0.1844Error cuadrático medio depredador

Los errores cuadráticos aún son muy bajos, que otros métodos hay diponsibles en SciPy que podríamos utilizar para conseguir un mejor ajuste 

**Decisión**: Nos propuso utilizar el método de differential evolution para obtener una mejor convergencia pues el método del descenso del gradiente Adam no nos convenció. Lo probamos y no fue muy eficiente por el ruido de los datos, así que mejor optamos por un método probabilístico para obtener intervalos de confianza y tener más certeza del ajuste del modelo 

### 03-30
**Tarea**: Se utilizó Claude para debuggear nuestro código de PyMC, había errores de sintaxis 

**Prompt**: "Este código no está compilando y no entiendo por qué, por favor corrígelo y explícame cuál es mi error y qué puedo cambiar".

**Decisión**: Había un error con los parámetros de un método de la librería.

### 04-05
**Tarea**: Se utilizó Claude para generar una primera plantilla de nuestro dashboard quarto.

**Prompt**: "Hazme un dashboard con marcadores de posición que tenga 5 pestañas y que la primera sea un menú con vínculos hacia las demás"

**Decisión**: Se utilizó la respuesta meramente como una plantilla, después realizamos todo el trabajo nosotros, como insertar las gráficas, decisiones de diseño, insertar las simulaciones. 

###  04-10 
**Tarea**: Se intentó corregir un error con las leyendas de las gráficas de plotly presentadas en el Quarto.

**Prompt**: "(Adjuntando una imagen de la gráfica) Mi gráfica de plotly no es correctamente visualizada en mi tablero de Quarto, al correr mi código en un Jupyter Notebook la leyenda no se corta, sin embargo, al correrlo en el tablero la leyenda se corta.

**Resultado**:
La IA no logró resolver el problema, intentamos usar Gemini y Claude y no logramos arreglarlo por el momento. 

