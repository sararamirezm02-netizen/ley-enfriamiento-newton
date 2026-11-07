import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ==============================
# 1. Cargar los datos
# ==============================
datos = pd.read_csv("datos_enfriamiento.csv")

t = datos["tiempo_min"].values          # tiempo en minutos
T = datos["temperatura_C"].values       # temperatura del objeto

# Temperatura ambiente (ajusta este valor según tu experimento)
T_amb = 22.0   # °C

# ==============================
# 2. Transformación para linearizar
# ==============================
delta_T = T - T_amb
y = np.log(np.abs(delta_T))             # ln|T - T_amb|

# ==============================
# 3. Ajuste lineal
# ==============================
regresion = linregress(t, y)

pendiente = regresion.slope
intercepto = regresion.intercept
r_value = regresion.rvalue
std_err = regresion.stderr              # error estándar de la pendiente

k = -pendiente                          # k = -pendiente
incertidumbre_k = std_err

print("======= RESULTADOS =======")
print(f"Coeficiente k = ({k:.5f} ± {incertidumbre_k:.5f}) min⁻¹")
print(f"Coeficiente de determinación R² = {r_value**2:.5f}")
print("==========================")

# ==============================
# 4. Gráfica 1: Temperatura vs Tiempo
# ==============================
plt.figure(figsize=(8, 5))
plt.plot(t, T, "o-", color="royalblue", label="Datos experimentales")
plt.xlabel("Tiempo (min)", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.title("Evolución de la temperatura vs tiempo", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("figura1_temperatura_vs_tiempo.png", dpi=300)
plt.show()

# ==============================
# 5. Gráfica 2: Ajuste lineal (ln|ΔT| vs t)
# ==============================
t_fit = np.linspace(min(t), max(t), 200)
y_fit = intercepto + pendiente * t_fit

plt.figure(figsize=(8, 5))
plt.plot(t, y, "o", color="darkorange", label="Datos linearizados")
plt.plot(t_fit, y_fit, "-", color="black", linewidth=2, label=f"Ajuste lineal (k = {k:.4f})")
plt.xlabel("Tiempo (min)", fontsize=12)
plt.ylabel(r"$\ln|T - T_{amb}|$", fontsize=12)
plt.title("Ajuste lineal para determinar k", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("figura2_ajuste_lineal.png", dpi=300)
plt.show()