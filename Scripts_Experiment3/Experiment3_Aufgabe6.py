import Analysistools as an
import numpy as np
import math
from scipy.stats import linregress

#constants
u_d_I = 0.0336434908630853
t_periode = 1.9
u_d_e = math.pi/25
offset = -1.9

print("------------Load Data-------------")
data_amper = an.read_csv_file("Experiment3_Aufgabe5.csv")
data_amper = data_amper[1:]

data_graphs = []
for amper_set in data_amper:
    data_graphs.append(an.read_csv_file(f"{amper_set[2]}.csv"))

for i in range(len(data_graphs)):
    data_graphs[i] = data_graphs[i][1:]
    for j in range(len(data_graphs[i])):
        data_graphs[i][j][1] -= offset
        data_graphs[i][j][1] = data_graphs[i][j][1] * u_d_I

print(data_graphs)
'''
for i in range(len(data_graphs)):
    an.plot_data(data_graphs[i], f"Experiment3_Aufgabe6_{i}", get_pdf=True, plot_fit=True, lable_x="Zeit in s", lable_y="Amplitude in rad", scale_x="linear", scale_y="linear", lable_daten="Daten-Graph")
'''

print("------------Calculate the maxima's of the data from the computer")
maxima_data = []
for i in range(len(data_graphs)):
    maxima = []
    for j in range(len(data_graphs[i])-2):
        if data_graphs[i][j][1] < data_graphs[i][j+1][1] and data_graphs[i][j+1][1] > data_graphs[i][j+2][1] and data_graphs[i][j+1][1] > 2*u_d_I:
            maxima.append(data_graphs[i][j+1])
    maxima_data.append(maxima)

'''
for i in range(len(data_graphs)):
    an.plot_data(maxima_data[i], f"Experiment3_Aufgabe6_{i}b", data2=data_graphs[i], get_pdf=True, plot_fit=False, lable_x="Zeit in s", lable_y="Amplitude in rad", scale_x="linear", scale_y="linear", lable_daten="Maxima-Graph")
'''

print(maxima_data)
print(f'lenght of maxima: {len(maxima_data)}')
print("------------Calculate the average period and the standard deviation of the computer reading-----------")
periode_data = []
for i in range(len(maxima_data)):
    periodes = []
    if len(maxima_data[i]) > 4:
        for j in range(4):
            periodes.append(float(maxima_data[i][j+1][0]) - float(maxima_data[i][j][0]))
    elif len(maxima_data[i]) >= 2:
        for j in range(len(maxima_data[i])-1):
            periodes.append(float(maxima_data[i][j+1][0]) - float(maxima_data[i][j][0]))
    periode_data.append(periodes)

average_periode_data = []
standard_deviation_periode_data = []
standard_deviation_periode_of_average_data = []
average_w_data = []
standard_deviation_w_data = []
standard_deviation_w_of_average_data = []
t = 1.2
for i in range(len(periode_data)):
    if len(periode_data[i]) == 0:
        continue
    average_periode = sum(periode_data[i])/len(periode_data[i])
    average_periode_data.append(average_periode)
    print(f'avarage_periode {i}: {average_periode}')
    average_w_data.append(2*math.pi/average_periode)
    standard_deviation_periode = (sum([(x - average_periode) ** 2 for x in periode_data[i]]) / len(periode_data[i])) ** 0.5
    standard_deviation_periode_data.append(standard_deviation_periode)
    print(f'standard_deviation_periode {i}: {standard_deviation_periode}')
    standard_deviation_w_data.append(2*math.pi/average_periode**2*standard_deviation_periode)
    standard_deviation_periode_of_average = t/(len(periode_data[i])**0.5)*standard_deviation_periode
    standard_deviation_periode_of_average_data.append(standard_deviation_periode_of_average)
    print(f'standard_deviation_periode_of_average {i}: {standard_deviation_periode_of_average}')
    standard_deviation_w_of_average_data.append(2*math.pi/average_periode**2*standard_deviation_periode_of_average)
    print('----')

print("------------Calculation of Dämpfungskonstante-----------")
lambda_data = []
error_lambda_data = []
maxima_data_log = []
for i in range(len(maxima_data)):
    maxima_log = maxima_data[i]
    for j in range(len(maxima_log)):
        maxima_log[j][1] = math.log(maxima_log[j][1])
    maxima_data_log.append(maxima_log)

    if len(maxima_log) < 2:
        continue

    x = np.array(maxima_log)[:,0]
    y = np.array(maxima_log)[:,1]

    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    print(f'lambda {i}: {(-1)*slope}')
    print(f"error lambda {i}: {std_err}")
    print('----')
    lambda_data.append((-1)*slope)
    error_lambda_data.append(std_err)

print("------------Plot the data lambda to I²-----------")


plot_data_lambda_I = []
for i in range(len(lambda_data)):
    plot_data_lambda_I.append([data_amper[i][1]**2, lambda_data[i]])

print("cut the data data with index 1, 2, 3")

x_lambda = np.array(plot_data_lambda_I)[:,0]
y_lambda = np.array(plot_data_lambda_I)[:,1]
slope_lambda, intercept_lambda, r_value_lambda, p_value_lambda, std_err_lambda = linregress(x_lambda, y_lambda)
data_lambda_linear = []
data_lambda_linear.append([0, intercept_lambda])
for i in range(len(plot_data_lambda_I)):
    data_lambda_linear.append([plot_data_lambda_I[i][0], slope_lambda*plot_data_lambda_I[i][0]+intercept_lambda])

an.plot_data(plot_data_lambda_I, "Experiment3_Aufgabe6_lambda_normal",data2=data_lambda_linear,  get_pdf=True, plot_fit=False, lable_x="I^2 in A^2", lable_y="lambda in 1/s", scale_x="linear", scale_y="linear", lable_daten="Datenwerte",lable_fit="Fit Gerade", error_bars=True, error_bars_data=error_lambda_data)
print("Da die Fit Funktion eine ursprungsgerade ist, ist lambda proportional zu I²")

print("-----------------Plot the data w to lambda-----------------")
plot_data_w_lambda = []
for i in range(len(lambda_data)):
    plot_data_w_lambda.append([lambda_data[i], average_w_data[i]])

'''
x_w = np.array(plot_data_w_lambda)[:,0]
y_w = np.array(plot_data_w_lambda)[:,1]

slope_w, intercept_w, r_value_w, p_value_w, std_err_w = linregress(x_w, y_w)
data_w_linear = []
data_w_linear.append([0, intercept_w])
for i in range(len(plot_data_w_lambda)):
    data_w_linear.append([plot_data_w_lambda[i][0], slope_w*plot_data_w_lambda[i][0]+intercept_w])
'''
an.plot_data(plot_data_w_lambda, "Experiment3_Aufgabe6_w_lambda",  get_pdf=True, plot_fit=False, lable_x="lambda in 1/s", lable_y="w in 1/s", scale_x="linear", scale_y="linear", lable_daten="Datenwerte", error_bars=True, error_bars_data=error_lambda_data)



