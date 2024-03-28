import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import linregress

print("-------Load the data form Experiment2-Aufgabe2.1-------")
# Read the data from the CSV file
data_exp2_t21 = an.read_csv_file("Experiment2-Aufgabe2.1.csv")

data_exp2_t21 = data_exp2_t21[1:]

#change degree to radian
for i in range(len(data_exp2_t21)):
    data_exp2_t21[i][0] = math.radians(int(data_exp2_t21[i][0].replace("°", "")))

print(data_exp2_t21)

print("-------Load the data form Experiment2-Aufgabe2.2-------")
# Read the data from the CSV file
data_exp2_t22 = an.read_csv_file("Experiment2-Aufgabe2.2.csv")

data_exp2_t22 = data_exp2_t22[1:]

#change degree to radian
for i in range(len(data_exp2_t21)):
    data_exp2_t22[i][1] = math.radians(int(data_exp2_t22[i][1].replace("°", "")))

print(data_exp2_t22)

print("-------Calculate I_0/D from the data of Experiment2-Aufgabe2.1-------")
t = 1.06
I_0_D = []
for i in range(len(data_exp2_t21)):
    I_0_D.append([data_exp2_t21[i][0], data_exp2_t21[i][1] **2 / (4*math.pi**2)])

print(I_0_D)
average_I_0_D = 0
for i in range(len(I_0_D)):
    average_I_0_D = average_I_0_D + I_0_D[i][1]
average_I_0_D = average_I_0_D/len(I_0_D)
print(f'Average I_0/D: {average_I_0_D}')
standard_deviation_I_0_D = math.sqrt(sum([(x[1] - average_I_0_D) ** 2 for x in I_0_D]) / len(I_0_D))
standard_deviation_I_0_D_of_average = 1.06/(math.sqrt(len(I_0_D)))*standard_deviation_I_0_D
print(f'standard deviation: {standard_deviation_I_0_D}')
print(f'standard deviation of the average: {standard_deviation_I_0_D_of_average}')

print("-------Calculate Iz from the data of Experiment2-Aufgabe2.2 and plot T² to mr²-------")
m = 0.0576 #Masse in kg

data_for_plot_T2_mr2 = []
for i in range(len(data_exp2_t22)):
    data_for_plot_T2_mr2.append([data_exp2_t22[i][2]**2, data_exp2_t22[i][0]**2 * m])

print(data_for_plot_T2_mr2)

# Generate fit gerade
x = np.array(data_for_plot_T2_mr2)[:, 0]
y = np.array(data_for_plot_T2_mr2)[:, 1]
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print(f"Steigung: {slope}")
print(f"Achsenabschnitt: {intercept}")
print(f"R-Wert: {r_value}")
print(f"P-Wert: {p_value}")
print(f"Standardfehler: {std_err}")

# Create the fit data
data_fit = []
data_fit.append([0, intercept])
for i in range(len(data_for_plot_T2_mr2)):
    data_fit.append([data_for_plot_T2_mr2[i][0], slope * data_for_plot_T2_mr2[i][0] + intercept])

# Plot the data
an.plot_data(data_for_plot_T2_mr2, "Experiment2-Aufgabe2.2", data2=data_fit, plot_fit=False, get_pdf=False, scale_x="linear", scale_y="linear", lable_x="T² in s²", lable_y="mr² in kgm²", slope=slope, intercept=intercept, std_err=std_err)

print("-------Calculation of D, I_0 and Iz-------")
D = (4*math.pi**2)/slope
print(f'D: {D}')
Iz = (intercept - (4*math.pi**2 * average_I_0_D))*D/(4*math.pi**2)
print(f'Iz: {Iz}')
I_0 = average_I_0_D * D
print(f'I_0: {I_0}')
