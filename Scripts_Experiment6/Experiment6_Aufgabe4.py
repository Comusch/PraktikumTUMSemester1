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
l_1 = 1.3 # m Messing
l_2 = 0.6 # m Holz
l_3 = 1.5 # m Kupfer

#density of the materials
p_1 = 8.6*10**3
u_1 = 0.2*10**3

p_2 = 1.4*10**3
u_2 = 0.2*10**3

p_3 = 8.95*10**3
u_3 = 0.05*10**3

def calculate_velosity_of_matirial(data_1, length, material):
    average_1_time = 0
    for i in range(len(data_1)):
        average_1_time += (data_1[i][0])/data_1[i][1]
    average_1_time = average_1_time/len(data_1)
    print(f"Average Schingtime({material}): {average_1_time}")
    # TODO: Calculate standard diveration

    average_lamda = 0
    for i in range(len(data_1)):
        average_lamda += data_1[i][1]
    average_lamda = average_lamda/len(data_1)
    average_lamda = length/average_lamda
    # TODO: Calculate standard diveration

    average_1_time = average_1_time*10**(-3)

    v = average_lamda * 1/average_1_time
    print(f"Sond velosity of {material}: {v}")
    return v

def Calculate_modulus_of_elasticity(v, density, material):
    mod_el = v**2 *density
    print(f"Modulus of elasticity (kg/(m²*s): {mod_el}")
    return mod_el


print("--------------Results of the calculation------------")
v_1 = calculate_velosity_of_matirial(data_1, l_1, "Messing")
Calculate_modulus_of_elasticity(v_1, p_1, "Messing")
print("-------")
v_2 = calculate_velosity_of_matirial(data_2, l_2, "Wood")
Calculate_modulus_of_elasticity(v_2, p_2, "Wood")
print("-------")
v_3 = calculate_velosity_of_matirial(data_3, l_3, "Kupfer")
Calculate_modulus_of_elasticity(v_3, p_3, "Kupfer")
print("-------")
