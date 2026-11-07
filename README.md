# Ley de Enfriamiento y Convección Térmica de Newton

Proyecto final de Cálculo Diferencial, Universidad de La Salle.

Integrantes: [nombres]

## Descripción

Este repositorio contiene los datos experimentales y el código utilizado para determinar el coeficiente de enfriamiento $k$ según la **Ley de Enfriamiento de Newton** (también conocida como Ley de Convección Térmica de Newton), cuya ecuación es

$$\frac{dT}{dt} = -k\,(T - T_{amb}) \quad\Rightarrow\quad T(t) = T_{amb} + (T_0 - T_{amb})\,e^{-kt}$$

## Montaje experimental

- Vaso de aluminio de paredes delgadas con 200 mL de agua caliente, sobre una superficie aislante.
- Temperatura inicial del agua: aproximadamente 75 °C.
- Temperatura ambiente: $T_{amb} = 22.0$ °C, medida con un segundo termómetro.
- Termómetro digital con resolución de 0.1 °C.
- 11 lecturas, una cada 30 s, durante 5 minutos.

## Archivos incluidos

- `datos_enfriamiento.csv` → Datos experimentales de temperatura vs tiempo.
- `analisis_k.py` → Script de Python que linealiza los datos, hace el ajuste por mínimos cuadrados, calcula $k$ con su incertidumbre y genera las figuras.
- `figura1_temperatura_vs_tiempo.png` → Gráfica de la evolución de la temperatura con el modelo ajustado.
- `figura2_ajuste_lineal.png` → Gráfica del ajuste lineal de $\ln|T - T_{amb}|$ contra $t$, de donde se obtiene $k$.

## Método

1. Se calcula $\Delta T = T - T_{amb}$ y se linealiza con $\ln \Delta T = \ln \Delta T_0 - kt$.
2. Se ajusta una recta por mínimos cuadrados (`scipy.stats.linregress`) y se toma $k = -\text{pendiente}$.
3. La incertidumbre de $k$ es el error estándar de la pendiente.
4. Se calculan la constante de tiempo $\tau = 1/k$, la vida media $\ln 2 / k$ y la tasa instantánea $dT/dt = -k(T - T_{amb})$.

## Resultados principales

- Coeficiente de enfriamiento: $k = (0.04905 \pm 0.00045)\ \text{min}^{-1}$
- Coeficiente de determinación: $R^2 = 0.99923$
- Constante de tiempo: $\tau = 20.4 \pm 0.2$ min
- Vida media de la diferencia de temperatura: $14.1 \pm 0.1$ min
- Tasa instantánea: $-2.60$ °C/min al inicio y $-2.04$ °C/min al final

## Cómo reproducir los resultados

1. Clona o descarga este repositorio y abre una terminal en la carpeta.
2. Instala las librerías necesarias (Python 3.14):

```
   pip install numpy pandas matplotlib scipy
```

3. Ejecuta el análisis, con `datos_enfriamiento.csv` en la misma carpeta que el script:

```
   python analisis_k.py
```

El script imprime el valor de $k$, $R^2$, $\tau$, la vida media y las tasas, y guarda `figura1_temperatura_vs_tiempo.png` y `figura2_ajuste_lineal.png` en la carpeta actual.
