---
title: "DERRE - HackODS"
subtitle: "ODS 14 · Vida Submarina "
author: "DERRE"
date: today
execute:
  echo: false
  warning: false
format:
  dashboard:
    scrolling: true
    orientation: columns
    self-contained: true 
---

```{python}
#| label: setup
#| include: false

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


# ── Paleta Dashboard ──────────
C_DEEP  = "#03045E"
C_MID   = "#0077B6"
C_LIGHT = "#00B4D8"
C_FOAM  = "#90E0EF"
C_MIST  = "#CAF0F8"
C_CORAL = "#F4A261"
C_TEAL  = "#2A9D8F"

# ═══════════════════════════════════════════════
#  CARGA DE DATOS
# ═══════════════════════════════════════════════

# BALLENAS
np.random.seed(42)
ballenas = pd.read_csv('../datos/ballenas/ballenas.csv').iloc[:28]
ballenas.columns = ['año', 'poblacion registrada']
ballenas['poblacion registrada']=ballenas['poblacion registrada'].str.replace(',', '').astype(float)
ballenas['año']=pd.to_numeric(ballenas['año'])

# PELICANOS
pelicanos=pd.read_csv('../datos/pelicanos/pelicanos.csv').iloc[:22,:2]  
pelicanos.columns = ['año', 'cantidad_nidos_pelicanos']
pelicanos['año']=pelicanos['año'].astype(str)

# PRODUCCION PESQUERA
produccion_pesquera=pd.read_csv('../datos/produccion_pesquera/produccion_pesquera.csv',header=None,names=['año','toneladas_pescadas'])
produccion_pesquera['toneladas_pescadas']=produccion_pesquera['toneladas_pescadas'].str.replace(',', '').astype(float)
produccion_pesquera['año']=produccion_pesquera['año'].astype(float)

# EMBARCACIONES
embarcaciones=pd.read_csv('../datos/embarcaciones/total_embarcaciones.csv').iloc[:36]
embarcaciones['total_embarcaciones']=embarcaciones['total_embarcaciones'].str.replace(',', '').astype(float)
embarcaciones['año']=pd.to_numeric(embarcaciones['año'])   


# ── Layout base para todas las figuras ────────
_layout = dict(
    template="plotly_white",
    plot_bgcolor=C_MIST,
    paper_bgcolor="white",
    font_color=C_DEEP,
    title_font_size=16,
    margin=dict(l=40, r=20, t=55, b=40),
)

```

# 🌊 Introducción {.seccion}

## Column {width="100%"}

::: {.intro-hero}
🌊 **ODS 14 · Vida Submarina (En el Golfo de California**

:::

::: {.callout-note appearance="minimal" icon=false}
## Un mar que se está vaciando

<!--
════════════════════════════════════════════════════
STORYTELLING
-->
Hay un momento en que los números dejan de ser estadísticas y se convierten en una advertencia.
En Baja California, ese momento ya llegó.
En menos de cuatro décadas, las embarcaciones pesqueras registradas en el litoral pasaron de poco más de 4,700 a casi 7,000 unidades, un crecimiento del 48% que no se detuvo ni en años de crisis climática ni en temporadas de colapso de capturas. Al mismo tiempo, la extracción pesquera alcanzó en 2024 su pico histórico: más de 550,000 toneladas registradas en un solo año, una cifra sin precedentes en los 40 años de registros hasta el dia de hoy.
La pregunta ya no es si el ecosistema está bajo presión. La pregunta es si todavía es capaz de recuperarse.
Para responderla, no basta con mirar las redes. Tenemos que ver el ecosistema completo.


<!--
════════════════════════════════════════════════════
CONTEXTO Y RELEVANCIA

-->
El análisis que hicimos se centra en el ecosistema marino de Baja California, una región de alta relevancia ecológica caracterizada por su gran biodiversidad (900 especies de peces, el 90% endémicas, el 39% de los mamíferos marinos del mundo, 4500 especies de invertebrados marinos y mas de 181 expeacies de aves marinas) y su intensa actividad pesquera (67% del volumen total de la producción pesquera y acuícola nacional). Esta zona es particularmente sensible a la variabilidad climática, especialmente a fenómenos como El Niño, que afectan la disponibilidad de nutrientes, las cadenas tróficas y, en consecuencia, la dinámica de las especies marinas.
Para entender estos procesos, se utilizan indicadores clave que reflejan tanto la salud del ecosistema como la presión humana. Entre ellos destacan los avistamientos de ballenas y la cantidad de nidos de pelícanos como proxies de biodiversidad, así como la producción pesquera y el número de embarcaciones como medidas del esfuerzo de explotación. Estas variables permiten analizar de manera integrada la interacción entre factores ambientales y actividades humanas.

<!--
════════════════════════════════════════════════════
OBJETIVO Y ESTRUCTURA DEL DASHBOARD

-->
El objetivo de este dashboard es analizar la relación entre la biodiversidad marina y la actividad pesquera en la zona de estudio, teniendo en cuaenta tanto el comportamiento histórico como posibles escenarios futuros. Se permite identificar tendencias, detectar momentos clave asociados a fenómenos como El Niño y entender cómo la presión humana impacta el ecosistema.

Está organizado en tres partes. Primero, un análisis exploratorio muestra la evolución histórica de variables como ballenas, pelícanos, producción pesquera y flota. Después, un modelo predictivo presenta escenarios futuros bajo distintas condiciones, comparando qué pasa si todo sigue igual frente a posibles estrategias de conservación. Finalmente, se resumen los hallazgos más importantes y sus implicaciones para la sostenibilidad.
:::

#  Análisis Exploratorio {.seccion}

## Column {width="70%"}

::: {.intro-hero}
Evolucion historica de nuestros indicadores.


::: {.panel-tabset .tabset-ocean}

####  Ballenas

```{python}
#| label: grafica-1
#| fig-responsive: true

from IPython.display import display
import plotly.graph_objects as go

def crear_fig(ballenas):

    el_nino_periods = [
        (2002, 2003), (2004, 2005), (2006, 2007),
        (2009, 2010), (2014, 2016), (2018, 2019)
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='markers',
        marker=dict(symbol="square", size=15, color="rgba(173, 216, 230, 0.2)"), 
        name='Fenómeno de El Niño',
        showlegend=True
    ))

    fig.add_trace(go.Scatter(
        x=ballenas['año'], 
        y=ballenas['poblacion registrada'],
        mode='lines+markers',
        name='Avistamientos',
        line=dict(color='#005b96', width=3), 
        marker=dict(size=9, color='#00a8cc', symbol='circle'), 
        hovertemplate="<b>Año:</b> %{x}<br>" +
                      "<b>Individuos:</b> %{y}<br>" +
                      "<extra></extra>"
    ))

    shapes = [
        dict(
            type="rect",
            x0=start, x1=end,
            y0=0, y1=1,
            xref="x", yref="paper",
            fillcolor="rgba(173, 216, 230, 0.2)",
            line_width=0,
            layer="below"
        )
        for (start, end) in el_nino_periods
    ]

    fig.add_annotation(
        x=0.01, y=1.08,
        xref="paper", yref="paper",
        text="■ Periodos de El Niño",
        showarrow=False,
        font=dict(size=11, color="gray")
    )
    fig.add_annotation(
        x=2012, y=3070,
        text="<b>Máximo histórico</b>",
        showarrow=True, arrowhead=2, ax=0, ay=-40,
        font=dict(color="#00a8cc", size=12)
    )

    fig.update_layout(
        shapes=shapes,
        title={
            'text': "<b>Monitoreo de Ballenas en Baja California</b><br><span style='font-size:14px; color:gray;'>Variabilidad poblacional y salud del ecosistema</span>",
            'y':0.96, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
        },
        xaxis_title="Temporada (Año)",
        yaxis_title="Individuos Registrados",
        template="plotly_white",
        hovermode="x unified",
        font=dict(family="Arial", size=12, color="#2c3e50"),
    
        autosize=True,
    

        legend=dict(
            orientation="v",      
            y=0.95,               
            yanchor="top",
            x=0.02,              
            xanchor="left",
            bgcolor="rgba(255, 255, 255, 0.9)",  
            bordercolor="lightgray",            
            borderwidth=1
        ),
        margin=dict(l=60, r=30, t=110, b=60),
        height=550
    )

    fig.update_xaxes(
        tickformat=".0f",
        tickangle=-45,
        dtick=1.0,
        type='linear',
        range=[1996, 2024],
        showgrid=True, gridcolor='lightgray'
    )

    fig.update_yaxes(showgrid=True, gridcolor='lightgray')

    return fig

crear_fig(ballenas)
```


####  Pelicanos
```{python}
from IPython.display import display
import plotly.graph_objects as go

def crear_fig_pelicanos(pelicanos):

    el_nino_periods = [
        (2002, 2003), (2004, 2005), (2006, 2007),
        (2009, 2010), (2014, 2016), (2018, 2019)
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='markers',
        marker=dict(symbol="square", size=15, color="rgba(173, 216, 230, 0.8)"), 
        name='Fenómeno de El Niño',
        showlegend=True
    ))

    fig.add_trace(go.Scatter(
        x=pelicanos['año'], 
        y=pelicanos['cantidad_nidos_pelicanos'],
        mode='lines+markers',
        name='Nidos de Pelícano',
        line=dict(color='#005b96', width=3),
        marker=dict(size=9, color='#00a8cc', symbol='circle'),
        hovertemplate="<b>Año:</b> %{x}<br>" +
                      "<b>Nidos:</b> %{y}<br>" +
                      "<extra></extra>"
    ))

    shapes = [
        dict(
            type="rect",
            x0=start, x1=end,
            y0=0, y1=1,
            xref="x", yref="paper",
            fillcolor="rgba(173, 216, 230, 0.2)",
            line_width=0,
            layer="below"
        )
        for (start, end) in el_nino_periods
    ]

    fig.add_annotation(
        x=0.01, y=1.08,
        xref="paper", yref="paper",
        text="■ Periodos de El Niño",
        showarrow=False,
        font=dict(size=11, color="gray")
    )

    fig.add_annotation(
        x=2011, y=30400,
        text="<b>Máximo histórico</b>",
        showarrow=True, arrowhead=2, ax=0, ay=-40,
        font=dict(color="#00a8cc", size=12)
    )

    fig.update_layout(
        shapes=shapes,
        title={
            'text': "<b>Dinámica Reproductiva: Pelícano Pardo de California</b><br><span style='font-size:14px; color:gray;'>Impacto de la variabilidad oceánica en la anidación</span>",
            'y':0.96, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
        },
        xaxis_title="Temporada (Año)",
        yaxis_title="Cantidad de Nidos",
        template="plotly_white",
        hovermode="x unified",
        font=dict(family="Arial", size=12, color="#2c3e50"),

        autosize=True,

        legend=dict(
            orientation="v",
            y=0.5,
            yanchor="middle",
            x=1.02,
            xanchor="left"
        ),

        margin=dict(l=60, r=120, t=110, b=60),
        height=550
    )

    fig.update_xaxes(
        tickformat=".0f",
        tickangle=-45,
        dtick=1.0,
        type='linear',
        range=[1999, 2020],
        showgrid=True, gridcolor='lightgray'
    )

    fig.update_yaxes(showgrid=True, gridcolor='lightgray')

    return fig


display(crear_fig_pelicanos(pelicanos))
```

####  Produccion pesquera
```{python}
from IPython.display import display
import plotly.graph_objects as go

def crear_fig_pesca(produccion_pesquera):

    el_nino_periods = [
        (2002, 2003), (2004, 2005), (2006, 2007),
        (2009, 2010), (2014, 2016), (2018, 2019)
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='markers',
        marker=dict(symbol="square", size=15, color="rgba(239, 83, 80, 0.6)"), 
        name='Fenómeno de El Niño',
        showlegend=True
    ))

    fig.add_trace(go.Scatter(
        x=produccion_pesquera['año'], 
        y=produccion_pesquera['toneladas_pescadas'],
        mode='lines+markers',
        name='Producción (Toneladas)',
        line=dict(color='#C62828', width=3),
        marker=dict(size=8, color='#B71C1C', symbol='diamond'),
        fill='tozeroy', 
        fillcolor='rgba(7, 59, 76, 0.05)',
        hovertemplate="<b>Año:</b> %{x}<br><b>Captura:</b> %{y:,.0f} ton<extra></extra>"
    ))

    shapes = [
        dict(
            type="rect",
            x0=start, x1=end,
            y0=0, y1=1,
            xref="x", yref="paper",
            fillcolor="rgba(239, 83, 80, 0.2)",
            line_width=0,
            layer="below"
        )
        for (start, end) in el_nino_periods
    ]

    fig.add_annotation(
        x=0.01, y=1.08,
        xref="paper", yref="paper",
        text="■ Periodos de El Niño",
        showarrow=False,
        font=dict(size=11, color="gray")
    )

    max_ton = produccion_pesquera['toneladas_pescadas'].max()
    max_year = produccion_pesquera.loc[
        produccion_pesquera['toneladas_pescadas'].idxmax(), 'año'
    ]

    fig.add_annotation(
        x=max_year, y=max_ton,
        text="<b>Pico máximo</b>",
        showarrow=True, arrowhead=2, ax=-30, ay=-40,
        font=dict(color="#E53935", size=12)
    )

    fig.update_layout(
        shapes=shapes,
        title={
            'text': "<b>Extracción Pesquera en Baja California</b><br><span style='font-size:14px; color:gray;'>Presión antrópica sobre el ecosistema marino</span>",
            'y':0.96, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
        },
        xaxis_title="Año",
        yaxis_title="Toneladas Registradas",
        template="plotly_white",
        hovermode="x unified",
        font=dict(family="Arial", size=12, color="#2c3e50"),

        autosize=True,

        legend=dict(
            orientation="v",
            y=0.5,
            yanchor="middle",
            x=1.02,
            xanchor="left"
        ),

        margin=dict(l=80, r=120, t=110, b=60),
        height=550
    )

    fig.update_xaxes(
        tickangle=-45,
        dtick=1,
        showgrid=True, gridcolor='rgba(200, 200, 200, 0.2)'
    )

    fig.update_yaxes(
        tickformat=",",
        showgrid=True, gridcolor='rgba(200, 200, 200, 0.2)'
    )

    return fig


display(crear_fig_pesca(produccion_pesquera))
```

#### Número de Embarcaciones
```{python}
from IPython.display import display
import plotly.graph_objects as go

def crear_fig_embarcaciones(embarcaciones):

    el_nino_periods = [
        (2002, 2003), (2004, 2005), (2006, 2007),
        (2009, 2010), (2014, 2016), (2018, 2019)
    ]

    fig = go.Figure()


    fig.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='markers',
        marker=dict(symbol="square", size=15, color="rgba(239, 83, 80, 0.6)"),
        name='Fenómeno de El Niño',
        showlegend=True
    ))

    fig.add_trace(go.Scatter(
        x=embarcaciones['año'], 
        y=embarcaciones['total_embarcaciones'],
        mode='lines+markers',
        name='Total Embarcaciones',
        line=dict(color='#C62828', width=3), 
        marker=dict(size=8, color='#B71C1C', symbol='diamond'),
        fill='tozeroy',
        fillcolor='rgba(7, 59, 76, 0.05)',
        hovertemplate="<b>Año:</b> %{x}<br><b>Flota:</b> %{y:,.0f} barcos<extra></extra>"
    ))

    shapes = [
        dict(
            type="rect",
            x0=start, x1=end,
            y0=0, y1=1,
            xref="x", yref="paper",
            fillcolor="rgba(239, 83, 80, 0.15)",
            line_width=0,
            layer="below"
        )
        for (start, end) in el_nino_periods
    ]

    max_val = embarcaciones['total_embarcaciones'].max()
    max_year = embarcaciones.loc[
        embarcaciones['total_embarcaciones'].idxmax(), 'año'
    ]

    fig.add_annotation(
        x=max_year, y=max_val,
        text="<b>Pico máximo</b>",
        showarrow=True, arrowhead=2, ax=-30, ay=-40,
        font=dict(color="#E53935", size=12)
    )

    fig.update_layout(
        shapes=shapes,
        title={
            'text': "<b>Crecimiento de la Flota Pesquera</b><br><span style='font-size:14px; color:gray;'>Capacidad instalada y esfuerzo de captura en el litoral</span>",
            'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
        },
        template="plotly_white",
        hovermode="x unified",
        font=dict(family="Arial", size=12, color="#2c3e50"),

        autosize=True,

        legend=dict(
            orientation="v",
            y=0.5,
            yanchor="middle",
            x=1.02,
            xanchor="left"
        ),

        margin=dict(l=80, r=120, t=110, b=60),
        height=550
    )

    fig.update_xaxes(
        title="Año",
        tickangle=-45,
        dtick=1,
        showgrid=True, gridcolor='rgba(200, 200, 200, 0.2)'
    )

    fig.update_yaxes(
        title="Total de Embarcaciones",
        tickformat=",",
        showgrid=True, gridcolor='rgba(200, 200, 200, 0.2)'
    )

    return fig

display(crear_fig_embarcaciones(embarcaciones))
```

:::
:::
## Column {width="30%"}

::: {.intro-hero}
Informacion indicadores 

::: {.panel-tabset .tabset-ocean}

### Ballenas

::: {.callout-note appearance="minimal" icon=false}
## Indicador pelágico de largo alcance

La ballena gris recorre hasta 20,000 kilómetros por temporada entre sus zonas de alimentación en el Ártico y sus criaderos en las lagunas de Baja California. Eso la convierte en algo extraordinario para la ciencia: un integrador biológico de condiciones oceánicas a escala continental.
Cuando los avistamientos caen, no es porque las ballenas se hayan escondido. Es porque el sistema que las sostiene: zooplancton, peces pequeños, corrientes frías, está fallando.
Los datos de monitoreo muestran una trayectoria perturbadora. Desde el máximo histórico de más de 3,000 individuos registrados en 2012, la población ha caído sistemáticamente. Para 2020, los avistamientos tocaron mínimos de apenas 1,000 individuos, una caída del 67% en ocho años. La ligera recuperación de 2023-2024 aún no alcanza la mitad del pico registrado.
Los años sombreados en las gráficas corresponden a eventos El Niño; perturbaciones climáticas que calientan el Pacífico oriental y reducen la productividad marina. Algunos valles en la curva coinciden con estos eventos. Pero no todos. Y eso importa.

**Variables utilizadas:**

- **[Variable 1]:** [Descripción breve]
- **[Variable 2]:** [Descripción breve]
- **Fuente:** [Origen de los datos]
:::

::: {.callout-important appearance="minimal" icon=false}
## 💡 Hallazgo clave

[Escribe aquí el dato o tendencia más importante que
revela esta gráfica.]
:::

### Pelicanos

::: {.callout-note appearance="minimal" icon=false}
## Indicador costero y de peces pequeños

Si la ballena gris mira el océano desde lejos, el pelícano pardo lo mira desde arriba, literalmente. Se zambulle en picada para capturar sardinas, anchovetas y macarelas: exactamente las mismas especies que captura la flota pesquera industrial.
La cantidad de nidos activos es el termómetro más sensible de su éxito reproductivo. Un pelícano que no come bien, no anida. Y una colonia que no anida, es una población que no se renueva.
Los datos son contundentes. Desde un máximo de más de 30,000 nidos en 2011, la curva cae de forma casi vertical. Para 2014-2015, los registros muestran valores cercanos a cero nidos activos —un colapso reproductivo sin precedente en la serie histórica. La recuperación posterior es modesta y errática, oscilando entre 2,000 y 5,000 nidos, muy lejos de los niveles que esta especie necesita para mantener una población estable.
El pelícano pardo compite con la flota pesquera por el mismo recurso. Donde la flota abunda, el pelícano escasea. Los datos no lo podrían mostrar de manera más clara.


**Variables utilizadas:**

- **[Variable 1]:** [Descripción breve]
- **[Variable 2]:** [Descripción breve]
- **Fuente:** [Origen de los datos]
:::

::: {.callout-important appearance="minimal" icon=false}
## 💡 Hallazgo clave

[Dato o tendencia más importante de la segunda gráfica.]
:::

### Embarcaciones y Produccion Pesquera
::: {.callout-note appearance="minimal" icon=false}
## Captura y flota pesquera

Mientras las poblaciones silvestres oscilan, dos curvas no han dejado de crecer.
La flota pesquera registrada pasó de menos de 5,000 embarcaciones a mediados de los años ochenta a casi 7,000 en 2024, con un crecimiento acelerado particularmente notable desde 2018. No se trata de fluctuaciones estacionales: es una expansión estructural de la capacidad extractiva instalada en el litoral.
La producción pesquera registrada siguió una trayectoria similar, con años de alta variabilidad pero una tendencia clara al alza desde 2015. El pico de 2024 (más de 550,000 toneladas) ocurrió precisamente cuando los indicadores biológicos de ballenas y pelícanos mostraban sus valores más bajos de la última década.
Esta es la paradoja central: a mayor extracción, menor biomasa silvestre observable. Y sin embargo, la flota sigue creciendo, cayendo en el borde de la sobreexplotación del ecosistema.

**Variables utilizadas:**

- **[Variable 1]:** [Descripción breve]
- **[Variable 2]:** [Descripción breve]
- **Fuente:** [Origen de los datos]
:::

::: {.callout-important appearance="minimal" icon=false}
## 💡 Hallazgo clave

[Dato o tendencia más importante de la tercera gráfica.]
:::
:::
:::

#  Modelo Predictivo {.seccion}

## Column {width="60%"}

::: {.intro-hero}
## Cuando la ecología se vuelve matemática

::: {.callout-tip appearance="minimal" icon=false}
## Cuando la ecología se vuelve matemática


```{python}
#| cache: true
#| 
import numpy as np
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# ── 1. DATOS Y PARÁMETROS ────────────────────────────────────────────────────

H_OBS = np.array([
    0.3955, 0.2110, 0.1324, 0.2965, 0.1371, 0.7856, 0.6301, 0.7755,
    0.1915, 0.2478, 0.1508, 0.0019, 0.7141, 1.0000, 0.3317, 0.5094,
    0.5473, 0.4663, 0.2647, 0.3063, 0.0490, 0.0000, 0.1266, 0.0481,
    0.1683, 0.1683
])
P_OBS = np.array([
    0.2620, 0.3156, 0.2890, 0.3070, 0.2879, 0.2694, 0.2575, 0.2641,
    0.2496, 0.1191, 0.1842, 0.2185, 0.1624, 0.2637, 0.0000, 0.3311,
    0.1241, 0.1882, 0.3972, 0.6336, 0.5479, 0.6653, 0.5310, 0.7614,
    0.7429, 1.0000
])

# Parámetros medianas MCMC
PARAMS = dict(r=1.1564, a=2.045, f=0.0472, sH=0.2643, sP=0.197)
K, C = 1.0, 1.0

# Configuración de la simulación
T_PROJ   = 100
AÑO_INI  = 1999
AÑOS     = np.arange(AÑO_INI, AÑO_INI + T_PROJ)
N_HIST   = len(H_OBS)
N_SIMS   = 200

# Grids (incluyendo explotación > 1.0)
GRID_A  = np.array([0.20, 0.40, 0.60, 0.80, 1.00, 1.20, 1.40, 1.60, 1.80, 2.00])
GRID_F  = np.array([0.20, 0.40, 0.60, 0.80, 1.00, 1.20, 1.40, 1.60, 1.80, 2.00])
GRID_YR = np.array([2025, 2027, 2030, 2032, 2035, 2037, 2040])

COLORES = {
    'H_cons': '#1DB38A',
    'H_iner': '#E05C2A',
    'P_cons': '#F39C12',
    'P_iner': '#cc7a40',
    'hist_H': '#1DB38A',
    'hist_P': '#E05C2A',
    'bg':     '#0f1117',
    'ax':     '#1a1d27',
    'grid':   '#2a2d3a',
    'text':   '#c8ccd8',
}


# ── 2. SIMULACIÓN MONTE CARLO ─────────────────────────────────────────────────

def simular_escenario(ruido_hist_H, ruido_hist_P,
                      ruido_fut_H, ruido_fut_P,
                      año_interv, factor_a, factor_f):
    r, a, f, sH, sP = PARAMS['r'], PARAMS['a'], PARAMS['f'], PARAMS['sH'], PARAMS['sP']
    H = np.zeros(T_PROJ)
    P = np.zeros(T_PROJ)
    H[0], P[0] = H_OBS[0], P_OBS[0]

    fut_idx = 0
    for t in range(T_PROJ - 1):
        es_futuro = AÑOS[t] >= año_interv
        a_act = a * factor_a if es_futuro else a
        f_act = f * factor_f if es_futuro else f

        if es_futuro:
            rH = ruido_fut_H[fut_idx]
            rP = ruido_fut_P[fut_idx]
            fut_idx += 1
        else:
            rH = ruido_hist_H[t]
            rP = ruido_hist_P[t]

        H[t + 1] = np.clip(
            H[t] * np.exp(r * (1 - H[t] / K) - a_act * P[t]) + rH,
            0.001, 5.0
        )
        P[t + 1] = np.clip(
            P[t] * np.exp(f_act * (1 - P[t] / C)) + rP,
            0.001, 5.0
        )
    return H, P


def monte_carlo(año_interv, factor_a, factor_f, seed=42):
    rng = np.random.default_rng(seed)
    sH, sP = PARAMS['sH'], PARAMS['sP']

    H_i = np.zeros((N_SIMS, T_PROJ))
    P_i = np.zeros((N_SIMS, T_PROJ))
    H_c = np.zeros((N_SIMS, T_PROJ))
    P_c = np.zeros((N_SIMS, T_PROJ))

    for i in range(N_SIMS):
        ruidoH_hist = rng.normal(0, sH, T_PROJ)
        ruidoP_hist = rng.normal(0, sP, T_PROJ)
        ruidoH_fut_iner = rng.normal(0, sH, T_PROJ)
        ruidoP_fut_iner = rng.normal(0, sP, T_PROJ)
        ruidoH_fut_cons = rng.normal(0, sH, T_PROJ)
        ruidoP_fut_cons = rng.normal(0, sP, T_PROJ)

        H_i[i], P_i[i] = simular_escenario(
            ruidoH_hist, ruidoP_hist,
            ruidoH_fut_iner, ruidoP_fut_iner,
            año_interv, 1.0, 1.0
        )
        H_c[i], P_c[i] = simular_escenario(
            ruidoH_hist, ruidoP_hist,
            ruidoH_fut_cons, ruidoP_fut_cons,
            año_interv, factor_a, factor_f
        )

    def stats(mat):
        return {
            'med': np.median(mat, axis=0),
            'q5':  np.percentile(mat, 5,  axis=0),
            'q95': np.percentile(mat, 95, axis=0),
        }

    return {
        'Hi': stats(H_i), 'Pi': stats(P_i),
        'Hc': stats(H_c), 'Pc': stats(P_c),
    }


# ── 3. PRE-CÓMPUTO DE TODAS LAS COMBINACIONES ────────────────────────────────
CACHE = {}


for fa in GRID_A:
    for ff in GRID_F:
        for yr in GRID_YR:
            key = (round(fa, 2), round(ff, 2), int(yr))
            CACHE[key] = monte_carlo(int(yr), fa, ff)
 

# ── 4. CONSTRUCCIÓN DE FIGURAS CON SLIDERS Y BANDAS DE INCERTIDUMBRE ─────────

AÑOS_STR    = [str(a) for a in AÑOS]
AÑOS_OBS    = list(AÑOS[:N_HIST])
AÑOS_FULL   = list(AÑOS)


def _hex_rgba(hex_color, alpha):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return f'rgba({r},{g},{b},{alpha})'


def construir_figura(variable='H'):
    assert variable in ('H', 'P')
    es_H = variable == 'H'
    col_cons = COLORES['H_cons'] if es_H else COLORES['P_cons']
    col_iner = COLORES['H_iner'] if es_H else COLORES['P_iner']
    obs_data = H_OBS if es_H else P_OBS
    titulo   = ('H — Biodiversidad marina (presa)' if es_H
                 else 'P — Flota pesquera (depredador)')
    ytit     = 'H normalizado' if es_H else 'P normalizado'

    # Combinación inicial base (1.0 = Índice 4 en el nuevo Grid, Año 2030)
    IDX_BASE = 4
    fa0, ff0, yr0 = GRID_A[IDX_BASE], GRID_F[IDX_BASE], 2030
    key0 = (fa0, ff0, yr0)
    d0   = CACHE[key0]
    dk   = 'Hc' if es_H else 'Pc'
    di   = 'Hi' if es_H else 'Pi'

    def band_y(d, key):
        return list(d[key]['q95']) + list(d[key]['q5'])[::-1]

    band_x = AÑOS_FULL + AÑOS_FULL[::-1]

    fig = go.Figure()

    # Traces fijos (datos históricos)
    fig.add_trace(go.Scatter(
        x=AÑOS_OBS, y=list(obs_data),
        mode='markers',
        marker=dict(color='white', size=7, line=dict(color=col_cons, width=1.5)),
        name='Datos históricos',
        hovertemplate='Año: %{x}<br>Valor: %{y:.3f}<extra></extra>',
    ))

    # Curvas de mediana
    fig.add_trace(go.Scatter(
        x=AÑOS_FULL, y=list(d0[di]['med']),
        mode='lines', line=dict(color=col_iner, width=2, dash='dash'),
        name='Inercial (100% presión)',
        hovertemplate='Año: %{x}<br>%{y:.3f}<extra>Inercial</extra>',
    ))
    fig.add_trace(go.Scatter(
        x=AÑOS_FULL, y=list(d0[dk]['med']),
        mode='lines', line=dict(color=col_cons, width=2.8),
        name='Escenario proyectado',
        hovertemplate='Año: %{x}<br>%{y:.3f}<extra>Proyección</extra>',
    ))

    # Línea vertical de intervención
    fig.add_vline(
        x=yr0, line=dict(color='rgba(220,220,220,0.55)', width=1.5, dash='dot'),
        annotation=dict(text='Año de intervención', font=dict(color=COLORES['text'], size=10),
                        showarrow=False, yref='paper', y=1.02, xanchor='left')
    )

    def ganancia_txt(d, dk, di):
        hi_fin  = float(np.mean(d[di]['med'][-10:]))
        hc_fin  = float(np.mean(d[dk]['med'][-10:]))
        g = (hc_fin - hi_fin) / max(hi_fin, 0.001) * 100
        return (f"Proyectado: {hc_fin:.3f} | Inercial: {hi_fin:.3f} "
                f"| Diferencia: {'+' if g>=0 else ''}{g:.1f}%")

    # Frames para todos los escenarios
    frames = []
    for fa in GRID_A:
        for ff in GRID_F:
            for yr in GRID_YR:
                key = (round(fa, 2), round(ff, 2), int(yr))
                d   = CACHE[key]
                frames.append(go.Frame(
                    name=f"{fa:.2f}_{ff:.2f}_{yr}",
                    data=[
                        go.Scatter(x=AÑOS_OBS, y=list(obs_data)),
                        go.Scatter(x=band_x, y=band_y(d, di)),   # Banda inercial
                        go.Scatter(x=band_x, y=band_y(d, dk)),   # Banda proyectada
                        go.Scatter(x=AÑOS_FULL, y=list(d[di]['med'])),
                        go.Scatter(x=AÑOS_FULL, y=list(d[dk]['med'])),
                    ],
                    layout=go.Layout(
                        shapes=[dict(type='line', x0=yr, x1=yr, y0=0, y1=1,
                                     xref='x', yref='paper',
                                     line=dict(color='rgba(220,220,220,0.55)', width=1.5, dash='dot'))],
                        annotations=[dict(xref='paper', yref='paper', x=0.01, y=0.97,
                                          text=ganancia_txt(d, dk, di),
                                          font=dict(color=COLORES['text'], size=11),
                                          showarrow=False, bgcolor='rgba(26,29,39,0.8)',
                                          borderpad=6)]
                    )
                ))
    fig.frames = frames

    # ── SLIDERS (separados verticalmente) ──
    sliders = [
        dict(
            active=IDX_BASE,
            steps=[dict(method='animate',
                        args=[[f"{round(fa,2):.2f}_{round(GRID_F[IDX_BASE],2):.2f}_{GRID_YR[2]}"],
                              dict(mode='immediate', frame=dict(duration=0, redraw=True),
                                   transition=dict(duration=0))],
                        label=f'{int(fa*100)}%') for fa in GRID_A],
            currentvalue=dict(prefix='Factor presión pesquera (a): ',
                              font=dict(color=COLORES['text'], size=11), xanchor='left'),
            pad=dict(t=10), len=0.88, x=0.06, y=-0.15,
            bgcolor=COLORES['ax'], bordercolor=COLORES['grid'],
            tickcolor=COLORES['text'], font=dict(color=COLORES['text'], size=10),
        ),
        dict(
            active=IDX_BASE,
            steps=[dict(method='animate',
                        args=[[f"{round(GRID_A[IDX_BASE],2):.2f}_{round(ff,2):.2f}_{GRID_YR[2]}"],
                              dict(mode='immediate', frame=dict(duration=0, redraw=True),
                                   transition=dict(duration=0))],
                        label=f'{int(ff*100)}%') for ff in GRID_F],
            currentvalue=dict(prefix='Factor crec. flota (f): ',
                              font=dict(color=COLORES['text'], size=11), xanchor='left'),
            pad=dict(t=10), len=0.88, x=0.06, y=-0.35,
            bgcolor=COLORES['ax'], bordercolor=COLORES['grid'],
            tickcolor=COLORES['text'], font=dict(color=COLORES['text'], size=10),
        ),
        dict(
            active=2,
            steps=[dict(method='animate',
                        args=[[f"{round(GRID_A[IDX_BASE],2):.2f}_{round(GRID_F[IDX_BASE],2):.2f}_{int(yr)}"],
                              dict(mode='immediate', frame=dict(duration=0, redraw=True),
                                   transition=dict(duration=0))],
                        label=str(int(yr))) for yr in GRID_YR],
            currentvalue=dict(prefix='Año de intervención: ',
                              font=dict(color=COLORES['text'], size=11), xanchor='left'),
            pad=dict(t=10), len=0.88, x=0.06, y=-0.55,
            bgcolor=COLORES['ax'], bordercolor=COLORES['grid'],
            tickcolor=COLORES['text'], font=dict(color=COLORES['text'], size=10),
        ),
    ]

    # Layout final
    fig.update_layout(
        title=dict(text=titulo, font=dict(color=COLORES['text'], size=16),
                   x=0.5, xanchor='center'),
        plot_bgcolor=COLORES['ax'], paper_bgcolor=COLORES['bg'],
        font=dict(color=COLORES['text'], family='Arial, sans-serif'),
        xaxis=dict(title='Año', tickfont=dict(color=COLORES['text'], size=10),
                   gridcolor=COLORES['grid'], linecolor=COLORES['grid'],
                   range=[AÑO_INI - 1, AÑO_INI + T_PROJ]),
        yaxis=dict(title=ytit, tickfont=dict(color=COLORES['text'], size=10),
                   gridcolor=COLORES['grid'], linecolor=COLORES['grid'],
                   rangemode='nonnegative'),
        legend=dict(bgcolor='rgba(26,29,39,0.85)', bordercolor=COLORES['grid'],
                    font=dict(color=COLORES['text'], size=11),
                    orientation='h', y=1.08, x=0.0),
        margin=dict(t=100, b=280, l=60, r=40),
        sliders=sliders,
        height=750,
        hovermode='x unified',
    )

    return fig


# ── 5. EJECUCIÓN ──────────────────────────────────────────────────────────────
# Para visualizar H (presa) con bandas de incertidumbre:
fig_H = construir_figura('H')
fig_H.show()

# Para visualizar P (depredador):
# fig_P = construir_figura('P')
# fig_P.show()
```
:::
:::


## Column {width="40%"}

::: {.callout-note appearance="minimal" icon=false}
##  Descripción del modelo
Para entender no solo qué está pasando, sino cuánto puede resistir el ecosistema, usamos un modelo dinámico basado en Lotka-Volterra y Ricker, adaptado a este caso.

Definimos dos variables:

- **H(t): biodiversidad marina** (salud del ecosistema).
- **P(t): presión pesquera** (impacto humano).

Ambas siguen un crecimiento con límite natural. Sin embargo:

La pesca crece de forma casi independiente.
La biodiversidad disminuye conforme aumenta la presión pesquera.

El modelo describe esta interacción y añade ruido para capturar variaciones climáticas y de datos.

Aunque el ajuste histórico no es perfecto (como es común en sistemas ecológicos), el objetivo no es predecir exactamente, sino entender tendencias, riesgos y posibles escenarios futuros. Por eso, los resultados se muestran con incertidumbre incluida.
:::

::: {.callout-note appearance="minimal" icon=false}
##  Parte Interactiva  (CAMBIAR NOMBRE POR ALGO MENOS OBVIO)
El modelo nos permite hacer algo que los datos históricos solos no pueden: explorar escenarios de intervención. Los sliders a continuación te permiten ajustar dos parámetros de política pública y un horizonte temporal.
**¿Qué puedes controlar?**
- **Factor de reducción de la presión pesquera (a):** Simula regulaciones que limiten la captura total permitida: vedas, cuotas, zonas de exclusión. Un valor del 30% significa que la presión baja a una tercera parte de su nivel actual.


- **Factor de reducción del crecimiento de la flota (f):** Simula políticas que frenen la expansión de embarcaciones: moratorias de registro, retiro de permisos, incentivos de reconversión. Un valor del 30% significa que la flota deja de crecer y empieza a contraerse.


- **Año de intervención:** El momento en que comienzan a aplicarse estas políticas. Cada año de retraso tiene consecuencias que el modelo cuantifica.

:::

# Escenarios a futuro {.seccion}

## Column {width="55%"}
sfaadfda

## Column {width="45%"}

::: {.callout-note appearance="minimal" icon=false}
## 01 — [Escenario 1 **(Escenario inercial)**]

Sin intervención, el índice H continúa su declive hacia valores cercanos a cero en el horizonte 2035-2040. La flota sigue creciendo por inercia económica. Las capturas se mantienen artificialmente altas mientras quedan recursos, luego colapsan. Este es el escenario del punto de no retorno.

:::

::: {.callout-note appearance="minimal" icon=false}
## 02 — [Escenario 2 **(Escenario moderado)**]

Una reducción del 50-60% en presión pesquera y crecimiento de flota, iniciada antes de 2030, permite que H se estabilice en torno a valores bajos pero positivos. El ecosistema no se recupera a sus niveles históricos, pero deja de colapsar. Es el escenario de la gestión del daño.
:::

::: {.callout-note appearance="minimal" icon=false}
## 03 — [Escenario 3 **(Escenario de conservacion activa)**]

Escenario de conservación activa: Reducciones del 70-90% en ambos parámetros, iniciadas cuanto antes, producen una trayectoria de recuperación lenta pero sostenida. H muestra una tendencia positiva hacia 2040. Este es el único escenario en que la respuesta a la pregunta inicial es: sí, puede recuperarse.

:::

::: {.callout-warning appearance="minimal" icon=false}
## 📋 Recomendaciones

- [Recomendación 1 para tomadores de decisiones]
- [Recomendación 2 para organismos de conservación]
- [Recomendación 3 para investigación futura]
:::

::: {.ods-footer-box}
**ODS 14 · Vida Submarina** · Agenda 2030 para el Desarrollo Sostenible
:::
