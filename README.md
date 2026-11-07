# Ley de Enfriamiento y Convección Térmica de Newton

Proyecto final de Cálculo Diferencial  
Universidad de La Salle

## Descripción
Este repositorio contiene los datos experimentales y el código utilizado para determinar el coeficiente de enfriamiento \( k \) según la **Ley de Enfriamiento de Newton** (también conocida como Ley de Convección Térmica de Newton).

## Archivos incluidos
- `datos_enfriamiento.csv` → Datos experimentales de temperatura vs tiempo
- `analisis_k.py` → Script de Python para el procesamiento de datos y cálculo de \( k \)
- `figura1_temperatura_vs_tiempo.png` → Gráfica de la evolución de la temperatura
- `figura2_ajuste_lineal.png` → Gráfica del ajuste lineal para obtener \( k \)

## Resultados principales
- Coeficiente de enfriamiento obtenido:  
  \( k = (0.04905 \pm 0.00045) \) min⁻¹  
- Coeficiente de determinación: \( R^{2} = 0.99923 \)

## Cómo reproducir los resultados
1. Clona o descarga este repositorio.
2. Instala las librerías necesarias:
   ```bash
   pip install numpy pandas matplotlib scipy
