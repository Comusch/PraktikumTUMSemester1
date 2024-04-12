import Analysistools as an
import numpy as np
import math
from scipy.stats import linregress

offset_mass = 11.176 #g
dichte = 1
print("------------Load Data-------------")
data_nadel1 = an.read_csv_file("Experiment5_Aufgabe1.1.csv")
data_nadel2 = an.read_csv_file("Experiment5_Aufgabe1.2.csv")

data_nadel1 = data_nadel1[1:]
data_nadel2 = data_nadel2[1:]

print(data_nadel1)
print(data_nadel2)

print("---------Preparing Data for Plotting----------")
data_stromstarke_druck1 = []
for i in range(len(data_nadel1)):
    data_nadel1[i][2] = (data_nadel1[i][2] - offset_mass)* 0.001
    data_stromstarke_druck1.append((data_nadel1[i][2]*10**(-3)/data_nadel1[i][1], data_nadel1[i][0]*dichte*9.81))
    print(f"Druck: {data_nadel1[i][0]*dichte*9.81} Stromstarke: {data_nadel1[i][2]*10**(-3)/data_nadel1[i][1]} Masse: {data_nadel1[i][2]}")

data_stromstarke_druck2 = []
for i in range(len(data_nadel2)):
    data_nadel2[i][2] = (data_nadel2[i][2] - offset_mass)* 0.001
    data_stromstarke_druck2.append((data_nadel2[i][2]*10**(-3)/data_nadel2[i][1], data_nadel2[i][0]*dichte*9.81))
    print(f"Druck: {data_nadel2[i][0]*dichte*9.81} Stromstarke: {data_nadel2[i][2]*10**(-3)/data_nadel2[i][1]} Masse: {data_nadel2[i][2]}")

x_1 = np.array(data_stromstarke_druck1)[:, 0]
y_1 = np.array(data_stromstarke_druck1)[:, 1]

x_2 = np.array(data_stromstarke_druck2)[:, 0]
y_2 = np.array(data_stromstarke_druck2)[:, 1]

slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_1, y_1)

slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_2, y_2)

data_fit1 = []
data_fit1.append((0, intercept1))
for i in range(len(data_stromstarke_druck1)):
    data_fit1.append((data_stromstarke_druck1[i][0], slope1*data_stromstarke_druck1[i][0]+intercept1))

an.plot_data(data_stromstarke_druck1, "Experiment5_Aufgabe1.1", data2=data_fit1, get_pdf=True, plot_fit=False, lable_x="A*v [m^3/s]", lable_y="p [Pa]")

data_fit2 = []
data_fit2.append((0, intercept2))
for i in range(len(data_stromstarke_druck2)):
    data_fit2.append((data_stromstarke_druck2[i][0], slope2*data_stromstarke_druck2[i][0]+intercept2))

an.plot_data(data_stromstarke_druck2, "Experiment5_Aufgabe1.2", data2=data_fit2, get_pdf=True, plot_fit=False, lable_x="A*v [m^3/s]", lable_y="p [Pa]")

print("----------Information about the fit----------")
print("slope1: ", slope1)
print("intercept1: ", intercept1)
print("r_value1: ", r_value1)
print("p_value1: ", p_value1)
print("std_err1: ", std_err1)
print("------")
print("slope2: ", slope2)
print("intercept2: ", intercept2)
print("r_value2: ", r_value2)
print("p_value2: ", p_value2)
print("std_err2: ", std_err2)
print("------")
print("W1 in (s*Pa)/m^3: ", slope1)
print("Uncertainty in W1: ", std_err1)
print("W2 in (s*Pa)/m^3: ", slope2)
print("Uncertainty in W2: ", std_err2)
w1 = slope1
w2 = slope2

print("----------Calculation of the viscosity----------")
l1 = 0.031 #m
d1 = 0.25*31*10**(-3) #m
r1 = d1/2

l2 = 0.026 #m
d2 = 0.25*22*10**(-3) #m
r2 = d2/2
print("r1: ", r1)
print("r2: ", r2)

n1 = w1*(math.pi*r1**4)/(8*l1)
n2 = w2*(math.pi*r2**4)/(8*l2)

uncertainty_n1 = math.sqrt((std_err1*math.pi*r1**4/(8*l1))**2 + (math.pi*w1*(r1**3)*4*0.001)/(8*l1)**2)
uncertainty_n2 = math.sqrt((std_err2*math.pi*r2**4/(8*l2))**2 + (math.pi*w2*(r2**3)*4*0.001)/(8*l2)**2)

print("Viscosity 1 in (s*Pa): ", n1)
print("Uncertainty in Viscosity 1: ", uncertainty_n1)
print("Viscosity 2 in (s*Pa): ", n2)
print("Uncertainty in Viscosity 2: ", uncertainty_n2)


