import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import linregress

print("-------Set all information about the figure and the person from the last experiments-------")
# Set all information about the figure and the person from the last experiments
#all variables with an m at the end are form the person
h_m = 1.705 #m
m_m = 65 #kg
r_m = 0.885/(2*math.pi) #m
ds_m = 0.082 #m (Abstand der Schwerpunkte zur Drehachse)
I_1_m = 1.91 #kgm²
I_2_m = 2.7 #kgm²
I_0_1_m = 0 #muss noch berechnet werden
I_0_2_m = 0 #muss noch berechnet werden

#all variables with an f at the end are form the figure
h_f = 0.325 #m
m_f = 0.1797 #kg
r_f = 0.121 #m
ds_f = 0.001 #m (Abstand der Schwerpunkte zur Drehachse)
I_1_f = 0.000 #kgm² (muss noch von Aumi genannt werden)
I_2_f = 0.000 #kgm² (muss noch von Aumi genannt werden)

print(f"Person: h = {h_m}m, m = {m_m}kg, r = {r_m}m, ds = {ds_m}m, I_1 = {I_1_m}kgm², I_2 = {I_2_m}kgm², I_0 = {I_0_1_m}kgm², I_0 = {I_0_2_m}kgm²")
print(f"Figure: h = {h_f}m, m = {m_f}kg, r = {r_f}m, ds = {ds_f}m, I_1 = {I_1_f}kgm², I_2 = {I_2_f}kgm²")

print("-------Calculate I_0 of the person-------")
# Calculate I_0 of the person
#Kopf
r_k_m = r_m/2 #Radius in m
m_k_m = m_m * 0.073 #Masse in kg (7.3% der Masse, Tabelle im Skript)
I_0_kopf_m = 2/5 * m_k_m * (r_k_m ** 2)
print(f'I_0 Kopf Person in kgm²: {I_0_kopf_m}')

#Beine
h_b_m = r_m * 0.45 #Radius in m
r_b_m = 0.04 #m (Radius der Beine)
m_b_m = m_m * 0.334/2 #Masse in kg (33.4%/2 der Masse, Tabelle im Skript)
d_bs_m = 0.025 #m (Abstand der Schwerpunkte zur Drehachse)
I_0_beine_m = (m_b_m * (r_b_m ** 2)/2 + m_b_m * (d_bs_m ** 2)) *2 #2 Beine
print(f'I_0 Beine Person in kgm²: {I_0_beine_m}')

#Rumpf
h_Rumpf_m = h_m - 2*r_k_m - r_b_m
m_Rumpf_m = m_m *0.48 #Masse in kg (48% der Masse, Tabelle im Skript)
I_0_Rumpf_m = m_Rumpf_m * (r_m ** 2) / 2
print(f'I_0 Rumpf Person in kgm²: {I_0_Rumpf_m}')

#Arme
l_a_m = (h_m -r_m)/2 #Länge der Arme in m
r_a_m = 0.025 #m (Radius der Arme)
m_a_m = m_m * 0.05 #Masse in kg (5% der Masse, Tabelle im Skript)
d_as_1_m = 0.5 * r_m + 0.06 #m (Abstand der Schwerpunkte zur Drehachse), 2,5cm von der Mitte des Körpers abstehend
d_as_2_m = 0.5 * r_m + l_a_m/2 #m (Abstand der Schwerpunkte zur Drehachse), 2,5cm von der Mitte des Körpers abstehend

I_0_1_Arme_m = (m_a_m * (r_a_m ** 2)/2 + m_a_m * (d_as_1_m ** 2))*2 #2 Arme
print(f'I_0 1. Arm Person in kgm²: {I_0_1_Arme_m}')
I_0_2_Arme_m = (m_a_m * ((r_a_m**2)/4 + (l_a_m**2)/12) + m_a_m * (d_as_2_m** 2))*2 #2 Arme
print(f'I_0 2. Arm Person in kgm²: {I_0_2_Arme_m}')

I_0_1_m = I_0_kopf_m + I_0_beine_m + I_0_Rumpf_m + I_0_1_Arme_m
I_0_2_m = I_0_kopf_m + I_0_beine_m + I_0_Rumpf_m + I_0_2_Arme_m
print(f'I_0 1. Person in kgm²: {I_0_1_m}')
print(f'I_0 2. Person in kgm²: {I_0_2_m}')
diffrence = I_0_2_m - I_0_1_m
print(f'Diffrence in kgm^2: {diffrence}')

print("--------Expolatory of the figure--------")
I_F1 = 0.00001399 #kgm²
I_F2 = 0.0002331 #kgm²

#TODO: Berechnen des Trägheitsmoments der Figur aus dem Hüftumfang der Puppe und der Masse des Menschen und der Puppe

print("----------Compare the calculated I_0 with the given I_0----------")
# Compare the calculated I_0 with the given I_0
print(f"I_0 1. Person in kgm² im Modell: {I_0_1_m}")
print(f"I_0 1. Person in kgm² in der Realität: {I_1_m}")
print(f"I_0 2. Person in kgm² im Modell: {I_0_2_m}")
print(f"I_0 2. Person in kgm² in der Realität: {I_2_m}")
#TODO: Vergleich mit den Verhältnissen der puppe (Modell und Realität)

