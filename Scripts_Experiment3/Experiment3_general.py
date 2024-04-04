import Analysistools as an
import math
import numpy as np
from scipy.stats import linregress

#Load Data

d_E_g = math.pi/25
offset = -1.9

print("---------Load Data------------")
data_amper_winkel = an.read_csv_file("Experiment3_Aufgabe3.1.csv")

data_amper_winkel = data_amper_winkel[1:]

print(data_amper_winkel)

for i in range(len(data_amper_winkel)):
    data_amper_winkel[i][0] = float(data_amper_winkel[i][0])*d_E_g
    data_amper_winkel[i][1] = (-1)*(data_amper_winkel[i][1] -offset)
print(data_amper_winkel)

x = np.array(data_amper_winkel)[:,0]
y = np.array(data_amper_winkel)[:, 1]

slope, intercept, r_value, p_value, std_err = linregress(x, y)
data_linear = []
data_linear.append((0, intercept))
for i in range(len(data_amper_winkel)):
    data_linear.append((x[i], slope*x[i]+intercept))

error_data =[]
for i in range(len(data_amper_winkel)):
    error_data.append(0.1)


an.plot_data(data_amper_winkel, "Experiment3_Winkel_Ampere_Verhältnis", data2=data_linear, get_pdf=True, plot_fit=False, lable_x="Winkel in rad", lable_y="Amper", error_bars_data=error_data, error_bars=True)

print(f"slope: {slope}, intercept: {intercept}")
print(f"rad/Amper: {1/slope}")
