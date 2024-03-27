import math
import numpy as np
import matplotlib.pyplot as plt
import Analysistools as an

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



# Load the data from the csv file
print("-------Experiment1_Aufgabe6-------")
load_data = an.read_csv_file('Experiment1_Aufgabe3_test11.csv')

# Print the data
print(load_data)

load_data = load_data[1:]
an.plot_data(load_data, 'Experiment1_Aufgabe3_test11', None, plot_fit=False, get_pdf=False, scale_x='linear', scale_y='linear')

#Cut the ebene over the data

print("-------cuted data-------")#
load_data = cut_ebene(load_data)
load_data = cut_rest(load_data)
for i in range(len(load_data)):
    print(load_data[i])

def quadratic_function(x, a, b, c):
    return a*x**2 + b*x + c

'''
print("-------plot the quadratic function-------")
a = 0.662
b = 0.186
c = 0.0531



data_quadrat = []
for i in range(len(load_data)):
    data_quadrat.append([load_data[i][0], quadratic_function(load_data[i][0], a, b, c)])

an.plot_data(load_data, 'Experiment1_Aufgabe3_test3_cut', data_quadrat, plot_fit=False, get_pdf=False, scale_x='linear', scale_y='linear')
'''

print("-------Berechnung des perfekt fits-------")
a_s, b_s, c_s = fit_quadratic(load_data)
print(f'a: {a_s}, b: {b_s}, c: {c_s}')
data_perfekt_fit = []
for i in range(len(load_data)):
    data_perfekt_fit.append([load_data[i][0], quadratic_function(load_data[i][0], a_s, b_s, c_s)])

an.plot_data(load_data, 'Experiment1_Aufgabe3_test11_cut_perfekt_fit', data_perfekt_fit, plot_fit=False, get_pdf=False, scale_x='linear', scale_y='linear')
