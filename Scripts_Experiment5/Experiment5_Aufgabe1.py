import Analysistools as an
import numpy as np
import math
from scipy.stats import linregress


print("------------Load Data-------------")
data_kugel_fall = an.read_csv_file("Experiment5_Aufgabe2.csv")

data_kugel_fall = data_kugel_fall[1:]

print(data_kugel_fall)

print("------------Calculate the average of the velocity-------------")
t = 1.06
v = 0
for i in range(len(data_kugel_fall)):
    v += (data_kugel_fall[i][0]/data_kugel_fall[i][1])
v = v/len(data_kugel_fall)
print("Average velocity: ", v)
standard_deviation = math.sqrt(sum([(data_kugel_fall[i][0]/data_kugel_fall[i][1] - v)**2 for i in range(len(data_kugel_fall))]))
print("Standard deviation: ", standard_deviation)
standard_deviation_of_average = standard_deviation*t/math.sqrt(len(data_kugel_fall))
print("Standard deviation of the average: ", standard_deviation_of_average)

print("------------Calculation of the viscosity-------------")
dk = 0.0065
rk = dk/2
g = 9.81
Rroh = 0.049

V_k = 4/3*math.pi*rk**3
print("Volume of the small ball in m^3: ", V_k)
m_k = 2.924/10 *10**(-3) #kg
print("Mass of the small ball in kg: ", m_k)
dichte_k = m_k/V_k
print("Dichte kleine Kugel in kg\m^3: ", dichte_k)
dichte_f = 1.22

print("-----")
n_t = (2*rk**2*g*(dichte_k-dichte_f))/(9*v)
print("theory Viscosity: ", n_t)

n_r = (2*rk**2*g*(dichte_k-dichte_f))/(9*v*(1+2.4*rk/Rroh))
print("real Viscosity: ", n_r)

print("------------Calculation of the Reynolds number-------------")

Re = 2*Rroh*v*dichte_f/n_r
print("Reynolds number: ", Re)
if Re < 1000:
    print("The flow is laminar")
else:
    print("The flow is turbulent")
