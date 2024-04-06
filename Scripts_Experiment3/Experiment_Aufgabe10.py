import Analysistools as an
import math
import numpy as np

#constants
u_d_I = 0.0336434908630853
t_periode = 1.9
u_d_e = math.pi/25

print("--------------Load Data----------------")
data_resonanz = an.read_csv_file("Experiment3_Aufgabe4.csv")
data_resonanz = data_resonanz[1:]
for i in range(len(data_resonanz)):
    data_resonanz[i][1] = data_resonanz[i][1]*u_d_e
    data_resonanz[i][0] = data_resonanz[i][0]/3200
print(data_resonanz)

w_D = 0.5
M_d_om = 0.02
lambda_coef = 0.018
w_0 = math.sqrt(w_D**2 + lambda_coef**2)
print(f"w_0: {w_0}")

fit_function_data = []
for i in range(500, 3000):
    print((math.sqrt((w_0**2-(i/3200)**2)**2 + (2*lambda_coef*(i/3200))**2)))
    print((M_d_om/(math.sqrt((w_0**2-(i/3200)**2)**2 + (2*lambda_coef*(i/3200))**2))))
    fit_function_data.append(((i/3200), (M_d_om/(math.sqrt((w_0**2-(i/3200)**2)**2 + 4*lambda_coef**2*(i/3200)**2)))))
print(fit_function_data)


an.plot_data(data_resonanz, "Experiment3_Aufgabe10", data2=fit_function_data, plot_fit=False, get_pdf=True , lable_x="Frequenz in Hz", lable_y="Amplitude in rad")

print("--------------Get the information of the fit function parameters----------------")
print(f"lambda(Daempfungskonstante): {lambda_coef}")
print(f"w_0: {w_0}")
print(f"M_d_om: {M_d_om}")
print("--------------Berechne die Resonanzfrequenz und die Halbwertsbreite----------------")
maximum = [0, 0]
for i in range(len(fit_function_data)):
    if fit_function_data[i][1] > maximum[1]:
        maximum = fit_function_data[i]
print(f"Maximum: {maximum}")
print(f"Resonanzfrequenz in Hz: {maximum[0]}")
print(f"Ungenauigkeit der Resonanzfrequenz in Hz: {1/3200 + 0.001}")

half_maxima = []
for i in range(len(fit_function_data)):
    if fit_function_data[i][1] > maximum[1]/math.sqrt(2):
        half_maxima.append(fit_function_data[i])
print(half_maxima)

real_half_maxima_vorne = half_maxima[0]
real_half_maxima_hinten = half_maxima[len(half_maxima)-1]
print(f"Halbwertsbreite in Hz: {real_half_maxima_hinten[0] - real_half_maxima_vorne[0]}")
if round(real_half_maxima_hinten[0] - real_half_maxima_vorne[0], 3) == round(2*lambda_coef, 3):
    print("Die Halbwertsbreite ist genau 2*lambda")