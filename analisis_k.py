import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ==============================
# 1. Cargar los datos
# ==============================
datos = pd.read_csv("datos_enfriamiento.csv")

t = datos["tiempo_min"].values          # tiempo en minutos
T = datos["temperatura_C"].values       # temperatura del agua (°C)

T_amb = 22.0      # temperatura ambiente medida (°C)
sigma_T = 0.1     # resolución del termómetro digital (°C)

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

# ==============================
# 4. Magnitudes derivadas
# ==============================
tau = 1 / k                             # constante de tiempo (min)
sigma_tau = incertidumbre_k / k**2
t_half = np.log(2) / k                  # vida media de la diferencia (min)
sigma_half = np.log(2) * incertidumbre_k / k**2
dTdt_inicio = -k * (T[0] - T_amb)       # tasa instantánea al inicio (°C/min)
dTdt_final = -k * (T[-1] - T_amb)       # tasa instantánea al final (°C/min)

print("======= RESULTADOS =======")
print(f"Coeficiente k = ({k:.5f} ± {incertidumbre_k:.5f}) min⁻¹")
print(f"Coeficiente de determinación R² = {r_value**2:.5f}")
print(f"Constante de tiempo tau = {tau:.2f} ± {sigma_tau:.2f} min")
print(f"Vida media = {t_half:.2f} ± {sigma_half:.2f} min")
print(f"dT/dt inicial = {dTdt_inicio:.3f} °C/min, final = {dTdt_final:.3f} °C/min")
print("==========================")

# ==============================
# 5. Gráfica 1: Temperatura vs Tiempo (datos + curva ajustada)
# ==============================
t_fit = np.linspace(min(t), max(t), 200)
T_fit = T_amb + np.exp(intercepto + pendiente * t_fit)

plt.figure(figsize=(8, 5))
plt.errorbar(t, T, yerr=sigma_T, fmt="o", capsize=3, color="royalblue",
             label="Datos experimentales (± resolución del termómetro)")
plt.plot(t_fit, T_fit, "-", color="black", label="Modelo ajustado")
plt.xlabel("Tiempo (min)", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.title("Evolución de la temperatura vs tiempo", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("figura1_temperatura_vs_tiempo.png", dpi=300)
plt.show()

# ==============================
# 6. Gráfica 2: Ajuste lineal (ln|ΔT| vs t) con barras de error
# ==============================
y_fit = intercepto + pendiente * t_fit
sigma_y = sigma_T / np.abs(delta_T)     # propagación: σ(ln ΔT) = σ_T / ΔT

plt.figure(figsize=(8, 5))
plt.errorbar(t, y, yerr=sigma_y, fmt="o", capsize=3, color="darkorange",
             label="Datos linearizados")
plt.plot(t_fit, y_fit, "-", color="black", linewidth=2,
         label=f"Ajuste lineal (k = {k:.4f})")
plt.xlabel("Tiempo (min)", fontsize=12)
plt.ylabel(r"$\ln|T - T_{amb}|$", fontsize=12)
plt.title("Ajuste lineal para determinar k", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("figura2_ajuste_lineal.png", dpi=300)
plt.show()
