import math
import numpy as np
import matplotlib.pyplot as plt
import Analysistools as an
import scipy.optimize as opt

#Algortihmus to cut the ebene over the data
def cut_ebene(data):
    return [data[i] for i in range(len(data)-1) if data[i][1] != data[i+1][1]]

def cut_rest(data):
    max = 0
    max_i = 0
    min = 99
    min_i = 99
    for i in range(len(data)):
        if data[i][1] > max:
            max = data[i][1]
            max_i = i
        if data[i][1] < min:
            min = data[i][1]
            min_i = i
    print(f'min: {min} at {min_i}')
    print(f'max: {max} at {max_i}')
    return data[min_i:max_i]

# Calculate the coefficient of the quadratic function
def fit_quadratic(data):
    data = np.array(data)
    x = data[:,0]
    y = data[:,1]
    a, b, c = np.polyfit(x, y, 2)
    return a, b, c

data_set = []
for i in range(2, 13):
    print(f'-------Experiment1_Aufgabe6------- Test{i}-------')
    new_data = an.read_csv_file(f'Experiment1_Aufgabe3_test{i}.csv')
    new_data = new_data[1:]
    print(new_data)
    new_data = cut_ebene(new_data)
    new_data = cut_rest(new_data)
    data_set.append(new_data)

print("-------fit the quadratic function-------")
cofficients = []
for i in range(len(data_set)):
    a, b, c = fit_quadratic(data_set[i])
    print(f'{i+1}: a: {a}, b: {b}, c: {c}')
    cofficients.append([a, b, c])

print("-------plot the quadratic function-------")

data_quadratic = []
for i in range(len(data_set)):
    data_quadratic_i = []
    for e in range(len(data_set[i])):
        data_quadratic_i.append([data_set[i][e][0], cofficients[i][0] * data_set[i][e][0] ** 2 + cofficients[i][1] * data_set[i][e][0] + cofficients[i][2]])
    data_quadratic.append(data_quadratic_i)

for i in range(len(data_set)):
    an.plot_data(data_set[i], f'Experiment1_Aufgabe3_test{i+2}', data2=data_quadratic[i], plot_fit=False, get_pdf=True, scale_x='linear', scale_y='linear')

print("-------Calculate the average acceleration-------")
average_acceleration_first_degree = 0
average_acceleration_first_degree = sum([cofficients[i][0] for i in range(3)])/3
print(f'average acceleration first degree: {average_acceleration_first_degree}')
standard_deviation_first_degree = math.sqrt(sum([(cofficients[i][0] - average_acceleration_first_degree) ** 2 for i in range(3)]) / 3)
print(f'standard deviation first degree: {standard_deviation_first_degree}')

average_acceleration_second_degree = 0
average_acceleration_second_degree = sum([cofficients[i+3][0] for i in range(3)])/3
print(f'average acceleration second degree: {average_acceleration_second_degree}')
standard_deviation_second_degree = math.sqrt(sum([(cofficients[i+3][0] - average_acceleration_second_degree) ** 2 for i in range(3)]) / 3)
print(f'standard deviation second degree: {standard_deviation_second_degree}')

average_acceleration_third_degree = 0
average_acceleration_third_degree = sum([cofficients[i+6][0] for i in range(3)])/3
print(f'average acceleration third degree: {average_acceleration_third_degree}')
standard_deviation_third_degree = math.sqrt(sum([(cofficients[i+6][0] - average_acceleration_third_degree) ** 2 for i in range(3)]) / 3)
print(f'standard deviation third degree: {standard_deviation_third_degree}')

#the 13 data set is not complete
average_acceleration_fourth_degree = 0
average_acceleration_fourth_degree = sum([cofficients[i+9][0] for i in range(2)])/2
print(f'average acceleration fourth degree: {average_acceleration_fourth_degree}')
standard_deviation_fourth_degree = math.sqrt(sum([(cofficients[i+9][0] - average_acceleration_fourth_degree) ** 2 for i in range(2)]) / 2)
print(f'standard deviation fourth degree: {standard_deviation_fourth_degree}')

print("-------calculation of the degree-------")
degress_set = []
degress_set.append(math.asin(0.289))
degress_set.append(math.asin(0.350))
degress_set.append(math.asin(0.379))
degress_set.append(math.asin(0.401))
print(degress_set)

data_points = []
data_points.append([degress_set[0], average_acceleration_first_degree])
data_points.append([degress_set[1], average_acceleration_second_degree])
data_points.append([degress_set[2], average_acceleration_third_degree])
data_points.append([degress_set[3], average_acceleration_fourth_degree])

error_bars = [standard_deviation_first_degree, standard_deviation_second_degree, standard_deviation_third_degree, standard_deviation_fourth_degree]

an.plot_data(data_points, 'Experiment1_Aufgabe3_winkel_beschleunigung', None, False, True, 'linear', 'linear', True, error_bars, lable_x='Winkel in rad', lable_y='Beschleunigung in m/s^2')

print("-------calculate the acceleration divided by the gravity acceleration-------")
g = 9.807
acceleration_divided_by_gravity = []
acceleration_divided_by_gravity.append([degress_set[0], average_acceleration_first_degree/g])
acceleration_divided_by_gravity.append([degress_set[1], average_acceleration_second_degree/g])
acceleration_divided_by_gravity.append([degress_set[2], average_acceleration_third_degree/g])
acceleration_divided_by_gravity.append([degress_set[3], average_acceleration_fourth_degree/g])

error_bars_divided_by_gravity = [standard_deviation_first_degree/g, standard_deviation_second_degree/g, standard_deviation_third_degree/g, standard_deviation_fourth_degree/g]

def sin_cos_fit(degree, reibungs_koeffizient):
    return np.sin(degree)-reibungs_koeffizient*np.cos(degree)

reibungs_koeffizient_fit, _ = opt.curve_fit(sin_cos_fit, degress_set, [average_acceleration_first_degree, average_acceleration_second_degree, average_acceleration_third_degree, average_acceleration_fourth_degree])
print(f'reibungs_koeffizient_fit: {reibungs_koeffizient_fit[0]}')

reibungs_koeffizient_fit[0] =

fit_function = []
for i in range(60):
    fit_function.append([(1/4)*math.pi*i/60, math.sin((1/4)*math.pi*i/60)-reibungs_koeffizient_fit[0]*math.cos((1/4)*math.pi*i/60)])

an.plot_data(acceleration_divided_by_gravity, 'Experiment1_Aufgabe3_winkel_beschleunigung_g_fit', fit_function, False, True, 'linear', 'linear', True, error_bars_divided_by_gravity, lable_x='Winkel in rad', lable_y='Beschleunigung in g')







