import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import linregress

# Read the data from the CSV file
print("-------Load Data for Experiment2-Aufgabe15-------")
data_exp2_t5 = an.read_csv_file("Experiment2-Aufgabe5.csv")

data_exp2_t5 = data_exp2_t5[1:]
for i in range(len(data_exp2_t5)):
    data_exp2_t5[i][0] = math.radians(int(data_exp2_t5[i][0].replace("°", "")))
    if data_exp2_t5[i][0] < 0:
        data_exp2_t5[i][0] *=-1

print(data_exp2_t5)

print("-------Calculate I_0 of the teller-------")
dichte = 2.7*(10**6)/1000 #kg/m³
r = 0.608/2 #m
h = 0.02 #m
m = dichte *(r**2)*math.pi*h
print(f'Masse in kg: {m}')
I_0 = m*(r**2)/2
print(f'I_0 in kgm²: {I_0}')

print("-------Calculate D of the teller and plot the data-------")
print("-------Calculate I_0/D from the data of Experiment2-Aufgabe5-------")
I_0_D = []
for i in range(len(data_exp2_t5)):
    I_0_D.append([data_exp2_t5[i][0], (data_exp2_t5[i][1] **2) / (4*math.pi**2)])
print(I_0_D)

t = 1.03 #weil wir über 20 Messwerte haben

average_I_0_D = 0
for i in range(len(I_0_D)):
    average_I_0_D = average_I_0_D + I_0_D[i][1]
average_I_0_D = average_I_0_D/len(I_0_D)
print(f'Average I_0/D: {average_I_0_D}')
standard_deviation_I_0_D = math.sqrt(sum([(x[1] - average_I_0_D) ** 2 for x in I_0_D]) / len(I_0_D))
standard_deviation_I_0_D_of_average = t/(math.sqrt(len(I_0_D)))*standard_deviation_I_0_D
print(f'standard deviation: {standard_deviation_I_0_D}')
print(f'standard deviation of the average: {standard_deviation_I_0_D_of_average}')

print("-------Calculate D of the teller-------")
D = I_0/average_I_0_D
print(f'D*: {D}')
uncertanty_D = D - I_0/(average_I_0_D + standard_deviation_I_0_D_of_average)
print(f'uncertanty D*: {uncertanty_D}')

print("-------Plot the data-------")
x = np.array(data_exp2_t5)[:, 0]
y = np.array(data_exp2_t5)[:, 1]

plot_data = np.column_stack((x, y))
an.plot_data(plot_data, "Experiment2-Aufgabe15", plot_fit=False, get_pdf=True, scale_x="linear", scale_y="linear", lable_x="Winkel in rad", lable_y="T in s", error_bars=False, error_bars_data=None, slope=None, intercept=None, std_err=None)


