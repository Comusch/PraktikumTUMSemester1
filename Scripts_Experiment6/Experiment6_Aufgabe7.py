import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import linregress

print("----------------Load Data----------------")
data_1 = an.read_csv_file("Experiment6_Aufgabe3.1.csv")
data_2 = an.read_csv_file("Experiment6_Aufgabe3.2.csv")
data_3 = an.read_csv_file("Experiment6_Aufgabe3.3.csv")

data_1 = data_1[1:]
data_2 = data_2[1:]
data_3 = data_3[1:]

f_1 = data_1[0][0]
f_2 = data_2[0][0]
f_3 = data_3[0][0]

def plot_data_and_Calculate_velosity(data, f):
    print(f"------------Plot Data of {f} -----------------")
    error_bar_data = []
    for i in range(len(data)):
        data[i][0] = i+1
        error_bar_data.append(1)

    x = np.array(data)[:,0]
    y = np.array(data)[:, 1]

    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")

    data_fit = []
    data_fit.append((0, intercept))
    for i in range(len(data)):
        data_fit.append((data[i][0], slope*data[i][0]+intercept))

    an.plot_data(data, f, data2=data_fit, plot_fit=False, get_pdf=True, scale_x="linear", scale_y="linear", lable_x="number of maximum n", lable_y="length l in cm", error_bars=True, error_bars_data=error_bar_data)

    print("------------Calculate the speed of sound------------")
    u_f = 1 #Hz for the releaser of the product
    v_s = slope * 10**(-2) *2*f
    print("-------")
    u_v = math.sqrt((2*f * std_err*10**(-2))**2 + (u_f *2*slope*10**(-2))**2)
    print(f"Speed of sound: {v_s} m/s")
    print(f"Uncertainty: {u_v} m/s")
    return v_s, u_v

data_v_u = []
print("--------------Results of the calculation------------")
data_v_u.append(plot_data_and_Calculate_velosity(data_1, f_1))
print("---------------------------------------------------")
data_v_u.append(plot_data_and_Calculate_velosity(data_2, f_2))
print("---------------------------------------------------")
data_v_u.append(plot_data_and_Calculate_velosity(data_3, f_3))

print("------------Analysis of the data------------")
print(data_v_u)
u_sum = sum([data_v_u[i][1] for i in range(len(data_v_u))])

weighted_average_v = 0
weight = 0
for i in range(len(data_v_u)):
    print(f"weight: {u_sum/data_v_u[i][1]}")
    weight += u_sum/data_v_u[i][1]
    weighted_average_v += data_v_u[i][0] * (u_sum/data_v_u[i][1])
weighted_average_v = weighted_average_v/weight
print(f"Weighted average speed of sound: {weighted_average_v}")



