import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import linregress

# Read the data from the CSV file
data_exp2_t1 = an.read_csv_file("Experiment2-Aufgabe1.csv")

data_exp2_t1 = data_exp2_t1[1:]

print(data_exp2_t1)

# change degree to radian
for i in range(len(data_exp2_t1)):
    data_exp2_t1[i][0] = math.radians(data_exp2_t1[i][0])

print(data_exp2_t1)


# Generate fit gerade
x = np.array(data_exp2_t1)[:, 0]
y = np.array(data_exp2_t1)[:, 1]
coefficients = np.polyfit(x, y, 1)
'''
print(f"Steigung: {coefficients[0]}")
print(f"Achsenabschnitt: {coefficients[1]} Dieser sollte eigentlich nicht da sein!")'''

print("-------Lineare Regression-------")
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print(f"Steigung: {slope}")
print(f"Achsenabschnitt: {intercept}")
print(f"R-Wert: {r_value}")
print(f"P-Wert: {p_value}")
print(f"Standardfehler: {std_err}")
if round(intercept,2) == round(std_err,2):
    print("Der Achsenabschnitt ist gleich dem Standardfehler. Daraus folgt, dass die beidne großen Proportional sind.")
else:
    print("Der Achsenabschnitt ist nicht gleich dem Standardfehler")

# Create the fit data
data_fit = []
data_fit.append([0, intercept])
for i in range(len(data_exp2_t1)):
    data_fit.append([data_exp2_t1[i][0], slope * data_exp2_t1[i][0] + intercept])


# Plot the data
an.plot_data(data_exp2_t1, "Experiment2-Aufgabe10", data2=data_fit, plot_fit=False, get_pdf=True, scale_x="linear", scale_y="linear", lable_x="Winkel in rad", lable_y="Force in N", slope=slope, intercept=intercept, std_err=std_err)
print("-------Federkonstante-------")
r = 0.084
federkonstante = slope * r
print(f"Federkonstante: {federkonstante}")
print("-------Berechnung der Fehlerfortpflanzung-------")
uncertainty_r = 0.001
uncertainty_federkonstante = math.sqrt((r * std_err)**2 + (slope*uncertainty_r)**2)
print(f"uncertainty federkonstante: {uncertainty_federkonstante}")