import Analysistools as an
import numpy as np
import math
from scipy.stats import linregress
import matplotlib.pyplot as plt
import scipy


# 1: Gruppe 1, 2: Gruppe 2, 3: Gruppe 3
n_1 = 0.00269 # 1: 25.1, 2: 32.2, 3: 40.2
n_2 = 0.00269 # 1: 27, 2: 34.9,3: 41.8
n_3 = 0.0025552 # 1: 30.4, 2: 37.2, 3: 45.1

print("------------Load Data-------------")
data_liquid = [(1.75 * 10 ** (-6) / n_2, 23), (0.35 * 10 ** (-6) / n_2, 42), (1.5 * 10 ** (-6) / n_2, 27.5),
               (0.4 * 10 ** (-6) / n_2, 29), (1.1 * 10 ** (-6) / n_2, 33), (0.4 * 10 ** (-6) / n_2, 44.8),
               (1.75 * 10 ** (-6) / n_1, 22), (0.25 * 10 ** (-6) / n_1, 32), (1.4 * 10 ** (-6) / n_1, 27),
               (0.5 * 10 ** (-6) / n_1, 29), (1.25 * 10 ** (-6) / n_1, 32), (0.5 * 10 ** (-6) / n_1, 38),
               (1.75 * 10 ** (-6) / n_3, 25.25), (0.175 * 10 ** (-6) / n_3, 30.75), (1.5 * 10 ** (-6) / n_3, 28.75),
               (0.25 * 10 ** (-6) / n_3, 36.25), (1 * 10 ** (-6) / n_3, 35.5), (0.45 * 10 ** (-6) / n_3, 40)]

print("data_liquid: ", data_liquid)

print("------------Bestimmung der Koexistenzkurve-------------")

P_c = 49.7 # Kritischer Druck
T_c = 304.2 # Kritische Temperatur
R = 8.314 # Universelle Gaskonstante
n = 0.0025552  # Anzahl der Mole
T_min = 250 # Minimale Temperatur
T_max = 350 # Maximale Temperatur
dT = 1 # Temperaturintervall

def van_der_waals(p, V, n, R, T):
  a = 2.479 * R**2 * T**2 / (64 * P_c)
  b = 0.0427 * R * T / P_c
  return p + n**2 * a / V**2 - n * R * T / (V - b)

p_coex = []
V_coex = []
for T in np.arange(T_min, T_max, dT):
  p_guess = P_c  # Initial guess for pressure
  V_guess = 3 * n * R * T / P_c  # Initial guess for volume
  root = scipy.optimize.fsolve(van_der_waals, (p_guess,), args=(V_guess, n, R, T))
  p_coex.append(root[0])
  V_coex.append(V_guess)  # V_guess was already calculated

plt.plot(p_coex, V_coex, label="Koexistenzkurve")
plt.ylabel("Druck (bar)")
plt.xlabel("Volumen (L)")
plt.legend()
plt.show()
