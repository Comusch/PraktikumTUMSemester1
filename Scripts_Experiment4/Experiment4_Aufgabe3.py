import Analysistools as an
import numpy as np
import math
from scipy.stats import linregress

print("------------Load Data-------------")
data_aufgabe2 = an.read_csv_file("Experiment4_Aufgabe2.csv")

data_aufgabe2 = data_aufgabe2[1:]

print(data_aufgabe2)

print("------------change the data that it can be used for the plot-------------")

data_calc = []
for i in range(len(data_aufgabe2)):
    data_calc.append((1/data_aufgabe2[i][1], data_aufgabe2[i][1]*data_aufgabe2[i][2]))

print(data_calc)

an.plot_data(data_calc, "Experiment4_Aufgabe3", data2=data_calc, get_pdf=True, plot_fit=False, lable_x="1/V [1/cm^3]", lable_y="p*V [bar*cm^3]")


print("------------Calculation of Stoffmenge-------------")
data_calc.remove(data_calc[len(data_calc)-1])
data_calc.remove(data_calc[len(data_calc)-2])
x = np.array(data_calc)[:, 0]
y = np.array(data_calc)[:, 1]

slope, intercept, r_value, p_value, std_err = linregress(x, y)

print("slope: ", slope)
print("intercept: ", intercept)
print("r_value: ", r_value)
print("p_value: ", p_value)
print("std_err: ", std_err)
data_linear = []
data_linear.append((0, intercept))
for i in range(len(data_calc)):
    data_linear.append((data_calc[i][0], slope*data_calc[i][0]+intercept))
an.plot_data(data_calc, "Experiment4_Aufgabe3", data2=data_linear, get_pdf=True, plot_fit=False, lable_x="1/V [1/cm^3]", lable_y="p*V [bar*cm^3]")

R = 8.314
T = 273.15
p_V_0 = intercept*0.1

n = p_V_0/(R*(T + data_aufgabe2[0][0]))
print("Stoffmenge: ", n)
