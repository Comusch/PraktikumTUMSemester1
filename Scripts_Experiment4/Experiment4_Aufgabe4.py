import Analysistools as an
import numpy as np
import math
from scipy.stats import linregress
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1: Gruppe 1, 2: Gruppe 2, 3: Gruppe 3
n_1 = 0.00269  # 1: 25.1, 2: 32.2, 3: 40.2
n_2 = 0.00269  # 1: 27, 2: 34.9,3: 41.8
n_3 = 0.0025552  # 1: 30.4, 2: 37.2, 3: 45.1


def filter_boundary_points(data):
    # Sortiere die Datenpunkte nach x-Koordinaten
    sorted_data = sorted(data, key=lambda point: point[0])

    # Bestimme die kleinste und größte x-Koordinate
    min_x = sorted_data[0][0]
    max_x = sorted_data[-1][0]

    # Filtere die Randpunkte anhand der x-Koordinaten
    boundary_points_x = [point for point in data if point[0] == min_x or point[0] == max_x]

    # Sortiere die Datenpunkte nach y-Koordinaten
    sorted_data = sorted(data, key=lambda point: point[1])

    # Bestimme die kleinste und größte y-Koordinate
    min_y = sorted_data[0][1]
    max_y = sorted_data[-1][1]

    # Filtere die Randpunkte anhand der y-Koordinaten
    boundary_points_y = [point for point in data if point[1] == min_y or point[1] == max_y]

    # Kombiniere die Randpunkte für x- und y-Koordinaten und entferne Duplikate
    boundary_points = list(set(boundary_points_x + boundary_points_y))

    return boundary_points


def get_fit_dampfkurve(a, b, Vm_g, T):
    T = T + 273.15
    R = 8.314
    data = []
    for i in range(100):
        data.append((Vm_g * ((i + 1) / 100) + 0.0001, ((R * T) / ((Vm_g * ((i + 1) / 100) + 0.0001) - b) - a / (
                    (Vm_g * ((i + 1) / 100) + 0.0001) ** 2)) * 10 ** (-5)))
    return data


print("------------Load Data-------------")
data_3_1_r = an.read_csv_file("Experiment4_Aufgabe1.1.csv")
data_3_2_r = an.read_csv_file("Experiment4_Aufgabe1.2.csv")
data_3_3_r = an.read_csv_file("Experiment4_Aufgabe1.3.csv")

data_2_1_r = an.read_csv_file("Experiment4_Aufgabe1.4.csv")
data_2_2_r = an.read_csv_file("Experiment4_Aufgabe1.5.csv")
data_2_3_r = an.read_csv_file("Experiment4_Aufgabe1.6.csv")

data_1_1_r = an.read_csv_file("Experiment4_Aufgabe1.7.csv")
data_1_2_r = an.read_csv_file("Experiment4_Aufgabe1.8.csv")
data_1_3_r = an.read_csv_file("Experiment4_Aufgabe1.9.csv")

data_3_1_r = data_3_1_r[1:]
data_3_2_r = data_3_2_r[1:]
data_3_3_r = data_3_3_r[1:]

data_2_1_r = data_2_1_r[2:]
data_2_2_r = data_2_2_r[3:]
data_2_3_r = data_2_3_r[2:]

data_1_1_r = data_1_1_r[3:]
data_1_2_r = data_1_2_r[3:]
data_1_3_r = data_1_3_r[3:]

print(data_1_1_r)
print(data_1_2_r)
print(data_1_3_r)
print("------------Change the data that it can be used for the plot-------------")
data_2_1 = []
error_baar_data_2_1 = []
data_2_2 = []
error_baar_data_2_2 = []
data_2_3 = []
error_baar_data_2_3 = []

data_1_1 = []
error_baar_data_1_1 = []
data_1_2 = []
error_baar_data_1_2 = []
data_1_3 = []
error_baar_data_1_3 = []

for i in range(len(data_1_1_r)):
    average_p_1_1 = (data_1_1_r[i][1] + data_1_1_r[i][2]) / 2
    standradabweichung_1_1 = math.sqrt(
        (data_1_1_r[i][1] - average_p_1_1) ** 2 + (data_1_1_r[i][2] - average_p_1_1) ** 2)
    standradabweichung_of_average_p_1_1 = 1.3 * standradabweichung_1_1
    molar_volume_1_1 = data_1_1_r[i][0] / n_1
    data_1_1.append((molar_volume_1_1, average_p_1_1))
    error_baar_data_1_1.append(standradabweichung_of_average_p_1_1)

for i in range(len(data_1_2_r)):
    average_p_1_2 = (data_1_2_r[i][1] + data_1_2_r[i][2]) / 2
    standradabweichung_1_2 = math.sqrt(
        (data_1_2_r[i][1] - average_p_1_2) ** 2 + (data_1_2_r[i][2] - average_p_1_2) ** 2)
    standradabweichung_of_average_p_1_2 = 1.3 * standradabweichung_1_2
    molar_volume_1_2 = data_1_2_r[i][0] / n_1
    data_1_2.append((molar_volume_1_2, average_p_1_2))
    error_baar_data_1_2.append(standradabweichung_of_average_p_1_2)
print("Error_bar_data_1_2: ", error_baar_data_1_2)
print("Data_1_2_r: ", data_1_2_r)
for i in range(len(data_1_3_r)):
    average_p_1_3 = (data_1_3_r[i][1] + data_1_3_r[i][2]) / 2
    standradabweichung_1_3 = math.sqrt(
        (data_1_3_r[i][1] - average_p_1_3) ** 2 + (data_1_3_r[i][2] - average_p_1_3) ** 2)
    standradabweichung_of_average_p_1_3 = 1.3 * standradabweichung_1_3
    molar_volume_1_3 = data_1_3_r[i][0] / n_1
    data_1_3.append((molar_volume_1_3, average_p_1_3))
    error_baar_data_1_3.append(standradabweichung_of_average_p_1_3)

for i in range(len(data_2_1_r)):
    average_p = (data_2_1_r[i][1] + data_2_1_r[i][2]) / 2
    standradabweichung_2_1 = math.sqrt((data_2_1_r[i][1] - average_p) ** 2 + (data_2_1_r[i][2] - average_p) ** 2)
    standradabweichung_of_average_p_2_1 = 1.3 * standradabweichung_2_1
    molar_volume = data_2_1_r[i][0] / n_2
    data_2_1.append((molar_volume, average_p))
    error_baar_data_2_1.append(standradabweichung_of_average_p_2_1)

for i in range(len(data_2_2_r)):
    average_p2 = (data_2_2_r[i][1] + data_2_2_r[i][2]) / 2
    molar_volume2 = data_2_2_r[i][0] / n_2
    standradabweichung_2_2 = math.sqrt((data_2_1_r[i][1] - average_p2) ** 2 + (data_2_1_r[i][2] - average_p2) ** 2)
    standradabweichung_of_average_p_2_2 = 1.3 * standradabweichung_2_2
    data_2_2.append((molar_volume2, average_p2))
    error_baar_data_2_2.append(standradabweichung_of_average_p_2_2)

for i in range(len(data_2_3_r)):
    average_p3 = (data_2_3_r[i][1] + data_2_3_r[i][2]) / 2
    molar_volume3 = data_2_3_r[i][0] / n_2
    standradabweichung_2_3 = math.sqrt((data_2_3_r[i][1] - average_p3) ** 2 + (data_2_3_r[i][2] - average_p3) ** 2)
    standradabweichung_of_average_p_2_3 = 1.3 * standradabweichung_2_3
    data_2_3.append((molar_volume3, average_p3))
    error_baar_data_2_3.append(standradabweichung_of_average_p_2_3)

print("------------Calculation of molares Volumen-------------")
for i in range(len(data_3_1_r)):
    data_3_1_r[i][1] = data_3_1_r[i][1] / n_1

for i in range(len(data_3_2_r)):
    data_3_2_r[i][1] = data_3_2_r[i][1] / n_1

for i in range(len(data_3_3_r)):
    data_3_3_r[i][1] = data_3_3_r[i][1] / n_1



print("------------Koexistenzkurve-------------")
data_liquid = [(1.75 / n_2, 23), (1.5 / n_2, 27.5),
               (0.4 / n_2, 29), (1.1 / n_2, 33),
               (1.75 / n_1, 22), (0.25 / n_1, 32), (1.4/ n_1, 27),
               (0.5 / n_1, 29), (1.25 / n_1, 32), (0.5 / n_1, 38),
               (1.75 / n_3, 25.25), (0.175 / n_3, 30.75), (1.5 / n_3, 28.75),
               (0.25 / n_3, 36.25), (1 / n_3, 35.5), (0.45 / n_3, 40)]

x_fit = np.linspace(0, 800, 300)
def cubic_fit(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

#obere Grenzfläche
popt_cub, pcov_cub = curve_fit(cubic_fit, np.array(data_liquid)[:, 0], np.array(data_liquid)[:, 1])

#letzter Datenpunkt habe ich hinzugefügt
data_gas= [(0.45/n_3, 40), (0.35/n_2, 42), (0.36/n_2, 43), (0.4/n_2, 44.8),  (0.25/n_1, 42), (185, 37), (210, 36), (230, 35.7), (245, 35.5),  (260, 35.7), (280, 36), (300, 37)]
sorted(data_gas, key=lambda x: x[0])
x_fit_q = np.linspace(10, 300, 300)
def quad_fit(x, a, b, c):
    return a * x ** 2 + b * x + c
popt_quad, pcov_quad = curve_fit(quad_fit, np.array(data_gas)[:, 0], np.array(data_gas)[:, 1])

print("------------Dampfungspunkte-------------")
print(data_3_1_r)
print(data_3_2_r)
print(data_3_3_r)
print("--------")
print(data_2_1)
print(data_2_2)
print(data_2_3)
print("------------Plot Isotherme of the gas-------------")
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xscale("linear")
ax.set_yscale("linear")
ax.set_ylabel("Druck in bar")
ax.set_xlabel("morlares Volumen in m^3/mol")

plt.plot(np.array(data_1_1)[:, 0], np.array(data_1_1)[:, 1], '--', color='k', label='25.1°C')  # Datenpunkte
plt.plot(np.array(data_1_1)[:, 0], np.array(data_1_1)[:, 1], 'x', color='k')  # Datenpunkte

plt.plot(np.array(data_2_1)[:, 0], np.array(data_2_1)[:, 1], '--', color='m', label='27°C')  # Datenpunkte
plt.errorbar(np.array(data_2_1)[:, 0], np.array(data_2_1)[:, 1], yerr=error_baar_data_2_1, fmt='x', color='m')  # Datenpunkte

plt.plot(np.array(data_3_1_r)[:, 1], np.array(data_3_1_r)[:, 2], '--', color='r', label='30.4°C')  # Datenpunkte
plt.plot(np.array(data_3_1_r)[:, 1], np.array(data_3_1_r)[:, 2], 'x', color='r')  # Datenpunkte

plt.errorbar(np.array(data_1_2)[:, 0], np.array(data_1_2)[:, 1], yerr=error_baar_data_1_2, fmt='x', color='orange')  # Datenpunkte
plt.plot(np.array(data_1_2)[:, 0], np.array(data_1_2)[:, 1], '--', color='orange',label='32.2°C')  # Datenpunkte

plt.plot(np.array(data_2_2)[:, 0], np.array(data_2_2)[:, 1], '--', color='c', label='34.9°C')  # Datenpunkte
plt.plot(np.array(data_2_2)[:, 0], np.array(data_2_2)[:, 1], 'x', color='c')  # Datenpunkte

plt.plot(np.array(data_3_2_r)[:, 1], np.array(data_3_2_r)[:, 2], '--', color='g', label='37.2°C')  # Datenpunkte
plt.plot(np.array(data_3_2_r)[:, 1], np.array(data_3_2_r)[:, 2], 'x', color='g')  # Datenpunkte

plt.plot(np.array(data_1_3)[:, 0], np.array(data_1_3)[:, 1], '--', color='purple', label='40.2°C')  # Datenpunkte
plt.plot(np.array(data_1_3)[:, 0], np.array(data_1_3)[:, 1], 'x', color='purple')  # Datenpunkte

plt.errorbar(np.array(data_2_3)[:, 0], np.array(data_2_3)[:, 1], yerr=error_baar_data_2_3, fmt='x', color='y')  # Datenpunkte
plt.plot(np.array(data_2_3)[:, 0], np.array(data_2_3)[:, 1], '--', color='y',label='41.8°C')  # Datenpunkte

plt.plot(np.array(data_3_3_r)[:, 1], np.array(data_3_3_r)[:, 2], '--', color='b', label='45.1°C')  # Datenpunkte
plt.plot(np.array(data_3_3_r)[:, 1], np.array(data_3_3_r)[:, 2], 'x', color='b')  # Datenpunkte

plt.plot(x_fit, cubic_fit(x_fit, *popt_cub), '--', color='gray', label='Fit', linewidth=2)  # Fit curve
plt.plot(x_fit_q, quad_fit(x_fit_q, *popt_quad), '--', color='gray', label='Fit', linewidth=2)  # Fit curve
plt.text(100, 20, 'Koexistenzbereich', fontsize=12, color='black')
plt.text(150, 48, "Direkter Übergang", fontsize=12, color='black')

#plt.plot(x_fit_q, quad_fit(x_fit_q, *popt_quad), '--', color='gray', label='Fit')  # Fit curve
ax.legend()
ax.grid()
plt.show()
fig.savefig("../Graphics/Experiment4_Aufgabe4.pdf")

print("------------Plot Agregatsgrenzen-------------")

print("------------Load Example Data-------------")
'''e1 = get_fit_dampfkurve(0.2653362999405756, 4.956629491945476*10**(-8), data_1_1[0][0], 25.1)
e2 = get_fit_dampfkurve(1.2156, 4.956629491945476*10**(-5), data_1_2[0][0], 32.2)
e3 = get_fit_dampfkurve(1.2156, 4.956629491945476*10**(-5), data_1_3[0][0], 40.2)
e4 = get_fit_dampfkurve(1.2156, 4.956629491945476*10**(-5), data_2_1[0][0], 27)
e5 = get_fit_dampfkurve(1.2156, 4.956629491945476*10**(-5), data_2_2[0][0], 34.9)
e6 = get_fit_dampfkurve(1.2156, 4.956629491945476*10**(-5), data_2_3[0][0], 41.8)
e7 = get_fit_dampfkurve(1.2156, 4.956629491945476*10**(-5), data_3_1_r[0][1], 30.4)
e8 = get_fit_dampfkurve(1.2156, 0.0001486988847583643, data_3_2_r[0][1], 37.2)
e9 = get_fit_dampfkurve(1.2156, 0.0001486988847583643, data_3_3_r[0][1], 45.1)


def get_fit_dampfkurve(Vm_g, T, a, b):
    T = T + 273.15
    R = 8.314
    return ((R * T) / ((Vm_g) - b) - a / ((Vm_g) ** 2)) * 10 ** (-5)


popt, pcov = curve_fit(get_fit_dampfkurve, np.array(data_1_1)[:, 0], np.array(data_1_1)[:, 1])

print("Vm_g:", popt[0])
print("T:", popt[1])
print("a:", popt[2])
#print("b:", popt[3])'''

print("------------Plot Agregatsgrenzen-------------")





# Sortieren der Datenpunkte nach x-Werten
sorted_data = sorted(data_liquid, key=lambda x: x[0])

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xscale("linear")
ax.set_yscale("linear")
ax.set_ylabel("Druck in bar")
ax.set_xlabel("morlares Volumen in cm^3/mol")
#plt.plot(np.array(e1)[:, 0], np.array(e1)[:, 1], '-', color='r', label='25.1°C')  # Data points
plt.plot(np.array(data_1_1)[:, 0], np.array(data_1_1)[:, 1], 'o', color='k', label='25.1°C')  # Data points
#plt.plot(np.array(data_liquid)[:, 0], np.array(data_liquid)[:, 1], 'o', color='gray',
 #        label="Dampfungspunkte")  # Data points
plt.plot(x_fit, cubic_fit(x_fit, *popt_cub), '--', color='r', label='Fit')  # Fit curve
plt.plot(np.array(data_gas)[:, 0], np.array(data_gas)[:, 1], 'o', color='gray', label="Gas")  # Data points
plt.plot(x_fit_q, quad_fit(x_fit_q, *popt_quad), '--', color='gray', label='Fit')  # Fit curve
ax.legend()
ax.grid()
plt.show()
fig.savefig("../Graphics/Experiment4_Aufgabe5.pdf")





print("------------Fit function-------------")
# Daten vorbereiten
x_data = [x[0] for x in data_liquid]
y_data = [x[1] for x in data_liquid]

# Bereich für den Fit definieren
x_min = 0.15 * 10**(-6)
x_max = 1.75 * 10**(-6)

# Funktion für den Fit definieren
def func(x, a, b):
  return a * x**2 + b

# Fit-Parameter durch lineare Regression ermitteln
popt, pcov = curve_fit(func, x_data, y_data, bounds=((0, -np.inf), (np.inf, np.inf)))

# Fit-Kurve plotten
x_fit = np.linspace(x_min, x_max, 100)
y_fit = func(x_fit, *popt)

# Originaldaten und Fit-Kurve plotten
plt.plot(x_data, y_data, 'o', label='Daten')
plt.plot(x_fit, y_fit, '-', label='Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Fit-Parameter ausgeben
print('Fit-Parameter:')
print('a =', popt[0])
print('b =', popt[1])


'''
print("------------show with the liquid points-------------")
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xscale("linear")
ax.set_yscale("linear")
ax.set_ylabel("Druck in bar")
ax.set_xlabel("morlares Volumen in m^3/mol")
plt.plot(np.array(data_1_1)[:, 0], np.array(data_1_1)[:, 1], 'o', color='k', label='25.1°C')  # Data points
plt.plot(np.array(data_3_3_r)[:, 1], np.array(data_3_3_r)[:, 2], 'o', color='b', label='45,1°C')  # Data points
plt.plot(np.array(data_liquid)[:, 0], np.array(data_liquid)[:, 1], 'o', color='gray', label="Dampfungspunkte")  # Data points

data_fit_boundarys = filter_boundary_points(data_liquid)

get_fit_dampfkurve(data_liquid)


plt.fill(np.array(data_fit_boundarys)[:, 0], np.array(data_fit_boundarys)[:, 1], color='blue', alpha=0.3, label= "Koexsistenz von Flüssigkeit und Gas")

ax.legend()
ax.grid()
plt.show()
fig.savefig("../Graphics/Experiment4_Aufgabe5.pdf")'''
