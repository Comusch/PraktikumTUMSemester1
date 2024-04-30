import Analysistools as an
import math
import numpy as np
from scipy.stats import linregress

print("-------------Load Data--------------------")
data_r = an.read_csv_file("Experiment6_Aufgabe2.csv")

data_r = data_r[1:]

print(data_r)

print("------------Plot Data-----------------")
x = np.array(data_r)[:,0]
y = np.array(data_r)[:, 1]

slope, intercept, r_value, p_value, std_err = linregress(x, y)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")

data_fit = []
data_fit.append((0, intercept))
for i in range(len(data_r)):
    data_fit.append((data_r[i][0], slope*data_r[i][0]+intercept))

an.plot_data(data_r, "Experiment6_Aufgabe5", data2=data_fit, plot_fit=False, get_pdf=True, scale_x="linear", scale_y="linear", lable_x="time in ms", lable_y="Way in cm")

print("------------Calculate the speed of sound------------")
v_gas = slope * 10
print(f"Speed of sound: {v_gas} m/s")
print(f"Uncertainty: {std_err*10} m/s")

print("------------Calculate of the adiabatenkoeffizion------------")
p_0 = 10**5 #Pa
rho_0 = 1.2 #kg/m^3

k = v_gas**2 * rho_0/p_0
print(f"Adiabatenkoeffizion: {k}")
u_k = math.sqrt((2*v_gas*std_err*rho_0/p_0)**2 + (v_gas**2*0.1*10**5/p_0**2)**2)
print(f"Uncertainty: {u_k}")




