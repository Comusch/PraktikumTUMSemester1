import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import linregress

print("-------Load the data form Experiment2-Aufgabe7-------")
# Read the data from the CSV file
data_exp2_t7 = an.read_csv_file("Experiment2-Aufgabe7.csv")

data_exp2_t7 = data_exp2_t7[1:]
#change degree to radian
for i in range(len(data_exp2_t7)):
    data_exp2_t7[i][1] = math.radians(int(data_exp2_t7[i][1].replace("°", "")))

print(data_exp2_t7)
#Grunddaten
I_0 = 0.72 #kgm²
D = 12.1 #Nm/rad
#D  = 40 #Nm/rad test data
m_a = 65 #kg
ds = 0.082 #m (Abstand der Schwerpunkte zur Drehachse)
I_S = m_a*(ds**2) #kgm²

print("-------Calculate I_z form the figure subject to the position of the person-------")
I_z_1 = []
I_z_2 = []

for i in range(len(data_exp2_t7)):
    if data_exp2_t7[i][0] == "P1":
        I_z_1.append([data_exp2_t7[i][1], D * ((data_exp2_t7[i][2] **2) / (4*math.pi**2)) - I_0 - I_S])
    else:
        I_z_2.append([data_exp2_t7[i][1], D * ((data_exp2_t7[i][2] **2) / (4*math.pi**2)) - I_0 - I_S])

print(I_z_1)
print(I_z_2)

print("-------Calculate the average of I_z and the standard deviation-------")
t = 1.08 #weil wir genau 8 Messwerte pro Person haben
average_I_z_1 = 0
for i in range(len(I_z_1)):
    average_I_z_1 = average_I_z_1 + I_z_1[i][1]
average_I_z_1 = average_I_z_1/len(I_z_1)
print(f'Average I_z_1: {average_I_z_1}')
standard_deviation_I_z_1 = math.sqrt(sum([(x[1] - average_I_z_1) ** 2 for x in I_z_1]) / len(I_z_1))
standard_deviation_I_z_1_of_average = t/(math.sqrt(len(I_z_1)))*standard_deviation_I_z_1
print(f'standard deviation: {standard_deviation_I_z_1}')
print(f'standard deviation of the average: {standard_deviation_I_z_1_of_average}')

average_I_z_2 = 0
for i in range(len(I_z_2)):
    average_I_z_2 = average_I_z_2 + I_z_2[i][1]
average_I_z_2 = average_I_z_2/len(I_z_2)
print(f'Average I_z_2: {average_I_z_2}')
standard_deviation_I_z_2 = math.sqrt(sum([(x[1] - average_I_z_2) ** 2 for x in I_z_2]) / len(I_z_2))
standard_deviation_I_z_2_of_average = t/(math.sqrt(len(I_z_2)))*standard_deviation_I_z_2
print(f'standard deviation: {standard_deviation_I_z_2}')
print(f'standard deviation of the average: {standard_deviation_I_z_2_of_average}')

print("-------Analysis of the data-------")
print(round(average_I_z_1, 1))
print(round(standard_deviation_I_z_1_of_average, 1))
if round(average_I_z_1, 1) + round(standard_deviation_I_z_1_of_average, 1) >=0:
    print("I_z_1 is equal to the standard deviation of the average")
    print("I_z_1 is near by zero, so the person is standing in the middle of the plate")
print(f"Differenz I_z_2 - I_z_1: {average_I_z_2 - average_I_z_1}")
