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
for i in range(len(data_exp2_t22)):
    data_exp2_t22[i][1] = math.radians(int(data_exp2_t22[i][1].replace("°", "")))
    #change cm to m
    data_exp2_t22[i][0] = data_exp2_t22[i][0]/100

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


print("-------Calculation of Iz form the mess data----------")
m = 0.0576 #Masse in kg
r_k = 0.03/2 #Radius in m
h = 0.095 #Höhe in m

I_O_Massekörper = m*r_k**2*1/2
print(f'I_O_Massekörper: {I_O_Massekörper}')

data_for_plot_T2_mr2 = []
for i in range(len(data_exp2_t22)):
    data_for_plot_T2_mr2.append([2*data_exp2_t22[i][0]**2 * m, data_exp2_t22[i][2]**2])
    print(f"mr²: {data_exp2_t22[i][0]**2 * m}")
    print(f"Unterscheid zu I_O_Massekörper: {(data_exp2_t22[i][0]**2 * m - I_O_Massekörper)/I_O_Massekörper}")

print(data_for_plot_T2_mr2)
print("-------Calculate Iz from the data of Experiment2-Aufgabe2.2 and plot T² to mr²-------")

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
an.plot_data(data_for_plot_T2_mr2, "Experiment2-Aufgabe11", data2=data_fit, plot_fit=False, get_pdf=True, scale_x="linear", scale_y="linear", lable_y="T² in s²", lable_x="2mr² in kgm²", slope=slope, intercept=intercept)

print("-------Calculation of D, I_0 and Iz-------")
D = (2*math.pi**2)/slope
print(f'D: {D}')
I_0 = average_I_0_D * D
print(f'I_0 durch erste Messreihe: {I_0}')
I_02 = intercept/(4*math.pi**2)*D
print(f'I_O form the second data:{I_02}')
if round(I_02, 4) == round(I_0):
    print(f'the rounded value of I_0: {round(I_02, 4)}')
else:
    print(round(I_02, 4))
    print(round(I_0, 4))
