import numpy as np

import Analysistools as an
import math
import numpy
from scipy.stats import linregress

T = 273
n = [0.0025663, 0.00269, 0.0025552]
print("--------------Load Data----------------")
data_temperatur = an.read_csv_file("Experiment4_Temperatur_Druck.csv")

data_temperatur = data_temperatur[1:]
print(data_temperatur)

data_plot = []
for i in range(len(data_temperatur)):
    data_plot.append((1/(data_temperatur[i][0] +T), data_temperatur[i][1]))

print(data_plot)
print("------------Plot Data----------")

data_plot_log = []
for i in range(len(data_plot)):
    data_plot_log.append((data_plot[i][0], math.log(data_plot[i][1])))

x = np.array(data_plot_log)[:, 0]
y = np.array(data_plot_log)[:, 1]

slope_c, intercept_c, r_value_c, p_value_c, std_err_c = linregress(x, y)

data_plot_fit = []
for i in range(len(data_plot)):
    data_plot_fit.append((data_plot[i][0], math.exp(slope_c*data_plot[i][0]+ intercept_c)))

an.plot_data(data_plot, "Experiment4_Aufgabe7",data2=data_plot_fit, plot_fit=False, get_pdf=True, scale_x="linear", scale_y="log", lable_x="1/Temperatur in 1/K", lable_y="Druck in bar")

print(f"Steigung:{slope_c}")
print(f"Unsicherheit:{std_err_c}")
A = (-1)*slope_c
print(f"A: {A}")
print(f"Unsicherheit A: {std_err_c}")

print("------------Calculation of L----------------")
data_L = []
error_bars_data = []
for i in range(len(data_temperatur)):
    L = data_temperatur[i][1]*10**5*(A/(data_temperatur[i][0]+T))*(data_temperatur[i][2]/n[i%3] - data_temperatur[i][2]*n[i%3])
    error_bars_data.append((data_temperatur[i][1]*10**5*(std_err_c/(data_temperatur[i][0]+T))*(data_temperatur[i][2]/n[i%3] - data_temperatur[i][2]*n[i%3])))
    print(f"L_{i+1} : {L}, dazu Temperatur in K: {data_temperatur[i][0]+T}")
    data_L.append((data_temperatur[i][0]+T, L))

print("-------is it a circle?--------")
r_average = 0
for i in range(len(data_L)):
    r_average += math.sqrt(data_L[i][0]**2+data_L[i][1]**2)
    print(f"r_{i+1}: {math.sqrt(data_L[i][0]**2+data_L[i][1]**2)}")
r_average = r_average/len(data_L)
print(f"r_average: {r_average}")

'''
circle_data = []
for i in range(100):
    circle_data.append([math.cos((1-i/100)*1/2*math.pi)*(r_average), math.sin((1-i/100)*1/2*math.pi)*(r_average)])
'''
print("it is not a circle")
an.plot_data(data_L, "Experiment4_Aufgabe7_L", get_pdf=True, plot_fit=False, lable_x="Temperatur in K", lable_y="L in J/mol", error_bars=True, error_bars_data=error_bars_data)
