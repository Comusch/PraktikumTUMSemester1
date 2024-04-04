import Analysistools as an
import numpy as np
import math
from scipy.stats import linregress

#Konstanten
u_d_I = 0.0336434908630853
t_periode = 1.9
u_d_e = math.pi/25

print("------------Load Data-------------")
data_human = an.read_csv_file("Experiment3_Aufgabe2.csv")
data_human = data_human[1:]
for i in range(len(data_human)):
    data_human[i][1] *= u_d_e
    data_human[i][0] = (data_human[i][0]-1)*t_periode
print(data_human)

an.plot_data(data_human, "Experiment3_Aufgabe9a", get_pdf=True, plot_fit=False, lable_x="Nummer der Periode", lable_y="Amplitude in rad")

print("------------Skale data------------------------")
data_human_log = data_human
for i in range(len(data_human_log)):
    data_human_log[i][1] = math.log(data_human_log[i][1])
print(data_human_log)

x_human = np.array(data_human_log)[:, 0]
y_human = np.array(data_human_log)[:, 1]
print(x_human)
print(y_human)

slope, intercept, r_value, p_value, std_err = linregress(x_human, y_human)
data_human_linear = []
for i in range(len(data_human_log)):
    data_human_linear.append((data_human_log[i][0], slope*data_human_log[i][0] + intercept))
print(data_human_linear)


an.plot_data(data_human, "Experiment3_Aufgabe9b", data2=data_human_linear, get_pdf=True, plot_fit=False, lable_x="Nummer der Periode", lable_y="Amplitude in log(rad)")

print("-------------Load Computer Data------------------------")
data_computer = an.read_csv_file("POR_A3.1.csv")
data_computer = data_computer[1:]
#delet the offset
offset = -1.9
for i in range(len(data_computer)):
    data_computer[i][1] = (float(data_computer[i][1]) -offset)
    data_computer[i][1] = data_computer[i][1]*u_d_I

print(data_computer)

an.plot_data(data_computer, "Experiment3_Aufgabe9c", get_pdf=True, plot_fit=True, lable_x="Zeit in s", lable_y="Amplitude in rad", scale_x="linear", scale_y="linear")
print("------------Calculate the maxima's of the data from the computer")
maxima = []
for i in range(len(data_computer)-2):
    if data_computer[i][1] < data_computer[i+1][1] and data_computer[i+1][1] > data_computer[i+2][1] and data_computer[i+1][1] > 5*u_d_I:
        maxima.append(data_computer[i+1])
print(maxima)
print(f'lenght of maxima: {len(maxima)}')

maxima_log = maxima
for i in range(len(maxima_log)):
    maxima_log[i][1] = math.log(maxima_log[i][1])
print(maxima_log)

x_c = np.array(maxima_log)[:,0]
y_c = np.array(maxima_log)[:,1]

slope_c, intercept_c, r_value_c, p_value_c, std_err_c = linregress(x_c, y_c)
data_computer_linear = []
data_computer_linear.append((0, intercept_c))
for i in range(len(maxima_log)):
    data_computer_linear.append((maxima_log[i][0], slope_c*maxima_log[i][0]+intercept_c))
print(data_computer_linear)

an.plot_data(maxima_log, "Experiment_Aufgabe9d", data2=data_computer_linear, get_pdf=True, plot_fit=False, lable_x="Nummer der Periode", lable_y="Amplitude in log(rad)")

print("------------Data form the human calculation-------------")
print(f"slope: {slope}, intercept: {intercept}")
print(f"Dämpfungskoeffizent: {round(-slope, 5)}, ursprüngliche Auslenkung: {round(math.exp(intercept), 5)}")
print(f"Abklingzeit: {round(-1/slope, 5)}")
print(f"Unsicherheit: {round(std_err, 5)}")

print("-----------Data form the Computer calculation------------")
print(f"slope{slope_c}, intercept: {intercept_c}")
print(f"Dämpfungskoeffizent: {round(-slope_c, 5)}, ursprüngliche Auslenkung: {round(math.exp(intercept_c), 5)}")
print(f"Abklingzeit: {round(-1/slope_c, 5)}")
print(f"Unsicherheit: {round(std_err_c, 5)}")
