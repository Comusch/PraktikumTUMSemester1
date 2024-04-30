import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math


print("----------------Load Data----------------")
data_1 = an.read_csv_file("Experiment6_Aufgabe1.1.csv")
data_2 = an.read_csv_file("Experiment6_Aufgabe1.2.csv")
data_3 = an.read_csv_file("Experiment6_Aufgabe1.3.csv")

data_1 = data_1[1:]
data_2 = data_2[1:]
data_3 = data_3[1:]

#Guesses
l_1 = 1.5 # m Messing
l_2 = 1.2 # m Holz
l_3 = 1.5 # m Kupfer

#density of the materials
p_1 = 8.6*10**3
u_1 = 0.2*10**3

p_2 = 1.4*10**3
u_2 = 0.2*10**3

p_3 = 8.95*10**3
u_3 = 0.05*10**3

def calculate_velosity_of_matirial(data_1, length, material):
    t = 1.3
    average_1_time = 0
    for i in range(len(data_1)):
        average_1_time += (data_1[i][0])/data_1[i][1]
    average_1_time = average_1_time/len(data_1)
    print(f"Average Schingtime({material}): {average_1_time}")
    standard_deviation_time = math.sqrt(sum([(data_1[i][0]/data_1[i][1] - average_1_time)**2 for i in range(len(data_1))])/(len(data_1)-1))
    print(f"Standard deviation of Schingtime({material}): {standard_deviation_time}")
    standard_deviation_time_of_average = standard_deviation_time*t/math.sqrt(len(data_1))
    print(f"Standard deviation of average Schingtime({material}): {standard_deviation_time_of_average}")


    average_lamda = 0
    for i in range(len(data_1)):
        average_lamda += data_1[i][1]
    average_lamda = average_lamda/len(data_1)

    print(f"Average distance({material}): {average_lamda}")
    standard_deviation_length = 0.01


    average_1_time = average_1_time*10**(-3)
    standard_deviation_time_of_average = standard_deviation_time_of_average*10**(-3)

    v = length * 1/average_1_time
    print(f"Sond velosity of {material}: {v}")
    u_v = math.sqrt((average_lamda*(1/average_1_time**2)*standard_deviation_time_of_average)**2 + (standard_deviation_length * 1/average_1_time)**2)
    print(f"Uncertainty of the sond velosity of {material}: {u_v}")
    return v, u_v

def Calculate_modulus_of_elasticity(v, density, material, u_v):
    mod_el = v**2 *density
    print(f"Modulus of elasticity (kg/(m*s²): {mod_el}")
    u_mod_el = math.sqrt((2*v*density*u_v)**2 + (v**2*u_1)**2)
    print(f"Uncertainty of the modulus of elasticity: {u_mod_el}")
    return mod_el


print("--------------Results of the calculation------------")
v_1, uv1 = calculate_velosity_of_matirial(data_1, l_1, "Messing")
Calculate_modulus_of_elasticity(v_1, p_1, "Messing", uv1)
print("-------")
v_2, uv2 = calculate_velosity_of_matirial(data_2, l_2, "Wood")
Calculate_modulus_of_elasticity(v_2, p_2, "Wood", uv2)
print("-------")
v_3, uv3= calculate_velosity_of_matirial(data_3, l_3, "Kupfer")
Calculate_modulus_of_elasticity(v_3, p_3, "Kupfer", uv3)
print("-------")
