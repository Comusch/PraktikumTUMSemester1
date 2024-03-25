import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math

#Load the data from the csv file
data_experiment1_aufgabe1 = an.read_csv_file('Experiment1_Aufgabe1.csv')
#Print the data
print(data_experiment1_aufgabe1)

#Calculate the value of the degree
for i in range (1, 16):
    #this is possible, because the hypotenuse is 1
    data_experiment1_aufgabe1[i][0] = math.asin(data_experiment1_aufgabe1[i][3])

print("-------now the data with the degree-------")
print(data_experiment1_aufgabe1)

# cut the first row
data_experiment1_aufgabe1 = data_experiment1_aufgabe1[1:]

desired_columns = 5
current_columns = len(data_experiment1_aufgabe1[0]) if data_experiment1_aufgabe1 else 0
if current_columns < desired_columns:
    for row in data_experiment1_aufgabe1:
        row += [0.0] * (desired_columns - current_columns)

# It now adds the weight force to the 5th column
for i in range(0, len(data_experiment1_aufgabe1)):
    data_experiment1_aufgabe1[i][4] = math.sqrt(math.pow(data_experiment1_aufgabe1[i][1], 2) + math.pow(data_experiment1_aufgabe1[i][2], 2))
    print(data_experiment1_aufgabe1[i][4])

print("-------now the data with the degree and the weight force-------")
print(data_experiment1_aufgabe1)

#Plot the data of the task1
print("-------create the plot for the task1-------")
#Erstellen der Daten von Verhältnis von Gewichtskraft zu Tagentinalkraft in Abhängigkeit von dem Winkel
data_Fg_Fs = []
for i in range(0, len(data_experiment1_aufgabe1)):
    data_Fg_Fs.append([data_experiment1_aufgabe1[i][0], data_experiment1_aufgabe1[i][2]/data_experiment1_aufgabe1[i][4]])

print(data_Fg_Fs)
#Plot the data of sinus
data_sin = []
for i in range(0, 60):
    data_sin.append([(1/2)*math.pi*i/60, math.sin((1/2)*math.pi*i/60)])

data_cos = []
for i in range(0, 60):
    data_cos.append([(1/2)*math.pi*i/60, math.cos((1/2)*math.pi*i/60)])

data_Fg_Fn = []
for i in range(0, len(data_experiment1_aufgabe1)):
    data_Fg_Fn.append([data_experiment1_aufgabe1[i][0], data_experiment1_aufgabe1[i][1]/data_experiment1_aufgabe1[i][2]])

data_tan = []
for i in range(0, 60):
    data_tan.append([(1/4)*math.pi*i/60, math.tan((1/4)*math.pi*i/60)])

an.plot_data(data_Fg_Fs, 'Experiment1_Aufgabe4_2', data_cos, False, True,'linear', 'linear')


