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
print("Radius of the small ball in m: ", rk)
g = 9.81
Rroh = 0.049
print("Radius of the cylinder in m: ", Rroh)

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

print("------------Error Analysis-------------")
uk = 1
u_F = 0.01

u_v = standard_deviation_of_average
u_r = 0.0005

u_eta = math.sqrt((4*rk*g/(9*v)*(dichte_k-dichte_f)*u_r)**2 + (2*rk**2*g/(9*v)*1*uk)**2 + (2*rk**2*g/(9*v)*u_F)**2 + (2*rk**2*g/(9*v**2)*u_v)**2)
print("Error of the viscosity (theory): ", u_eta)

print("------------Calculation of the Reynolds number-------------")

Re = (2*Rroh)*v*dichte_f/n_r
print("Reynolds number: ", Re)
if Re < 1000:
    print("The flow is laminar")
else:
    print("The flow is turbulent")

u_Rroh = 0.001
u_re = math.sqrt((dichte_f*v/(n_r)*2*u_Rroh)**2 + (2*Rroh*v/(n_r)*u_F)**2 + (2*Rroh*dichte_f/(n_r)*u_v)**2 + (2*Rroh*dichte_f*v/(n_r**2)*u_eta)**2)
print("Error of the Reynolds number: ", u_re)
