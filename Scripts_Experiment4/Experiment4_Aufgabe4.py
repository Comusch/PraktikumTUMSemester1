import Analysistools as an
import numpy as np
import math
from scipy.stats import linregress
import matplotlib.pyplot as plt

# 1: Gruppe 1, 2: Gruppe 2, 3: Gruppe 3
n_1 = 0.00269
n_2 = 0.00269
n_3 = 0.0025552

print("------------Load Data-------------")
data_3_1_r = an.read_csv_file("Experiment4_Aufgabe1.1.csv")
data_3_2_r = an.read_csv_file("Experiment4_Aufgabe1.2.csv")
data_3_3_r = an.read_csv_file("Experiment4_Aufgabe1.3.csv")

data_3_1_r = data_3_1_r[1:]
data_3_2_r = data_3_2_r[1:]
data_3_3_r = data_3_3_r[1:]

print(data_3_1_r)
print(data_3_2_r)
print(data_3_3_r)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xscale("linear")
ax.set_yscale("linear")
ax.set_ylabel("Druck in bar")
ax.set_xlabel("Volumen in cm^3")
plt.plot(np.array(data_3_1_r)[:, 1], np.array(data_3_1_r)[:, 2], 'o', color='r', label='30.4°C')  # Data points

plt.show()