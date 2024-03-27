import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math

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
print(f"Steigung: {coefficients[0]}")
print(f"Achsenabschnitt: {coefficients[1]} Dieser sollte eigentlich nicht da sein!")

# Create the fit data
data_fit = []
data_fit.append([0, coefficients[1]])
for i in range(len(data_exp2_t1)):
    data_fit.append([data_exp2_t1[i][0], coefficients[0] * data_exp2_t1[i][0] + coefficients[1]])


# Plot the data
an.plot_data(data_exp2_t1, "Experiment2-Aufgabe1", data2=data_fit, plot_fit=False, get_pdf=False, scale_x="linear", scale_y="linear", lable_x="Winkel in rad", lable_y="Force in N")

r = 0.084
federkonstante = coefficients[0] * r
print(f"Federkonstante: {federkonstante}")