import Analysistools as an
import numpy as np
import matplotlib.pyplot as plt
import math


#Load the data from the csv file
print("-------Experiment1_Aufgabe5-------")
print("-------Test1-------")
data_experiment1_versuch2_test1 = an.read_csv_file('Experiment1_Aufgabe2_Test1.csv')
#Print the data
print(data_experiment1_versuch2_test1)
print("-------Test2-------")
data_experiment1_versuch2_test2 = an.read_csv_file('Experiment1_Aufgabe2_Test2.csv')
#Print the data
print(data_experiment1_versuch2_test2)
print("-------Test3-------")
data_experiment1_versuch2_test3 = an.read_csv_file('Experiment1_Aufgabe2_Test3.csv')
#Print the data
print(data_experiment1_versuch2_test3)

#Cut the first row
data_experiment1_versuch2_test1 = data_experiment1_versuch2_test1[1:]
data_experiment1_versuch2_test2 = data_experiment1_versuch2_test2[1:]
data_experiment1_versuch2_test3 = data_experiment1_versuch2_test3[1:]

#Calculate the average value of the force
average_force_test1 = 0
for i in range(0, len(data_experiment1_versuch2_test1)):
    average_force_test1 = average_force_test1 + data_experiment1_versuch2_test1[i][1]

#for calculating the standard deviation of the average force
t = 1.06

average_force_test1 = average_force_test1/len(data_experiment1_versuch2_test1)
standard_deviation_test1 = math.sqrt(sum([(x[1] - average_force_test1) ** 2 for x in data_experiment1_versuch2_test1]) / len(data_experiment1_versuch2_test1))
standard_deviation_test1_of_average = t/(math.sqrt(len(data_experiment1_versuch2_test1)))*standard_deviation_test1

average_force_test2 = 0
for i in range(0, len(data_experiment1_versuch2_test2)):
    average_force_test2 = average_force_test2 + data_experiment1_versuch2_test2[i][1]
average_force_test2 = average_force_test2/len(data_experiment1_versuch2_test2)
standard_deviation_test2 = math.sqrt(sum([(x[1] - average_force_test2) ** 2 for x in data_experiment1_versuch2_test2]) / len(data_experiment1_versuch2_test1))
standard_deviation_test2_of_average = t/(math.sqrt(len(data_experiment1_versuch2_test2)))*standard_deviation_test2

average_force_test3 = 0
for i in range(0, len(data_experiment1_versuch2_test3)):
    average_force_test3 = average_force_test3 + data_experiment1_versuch2_test3[i][1]
average_force_test3 = average_force_test3/len(data_experiment1_versuch2_test3)
standard_deviation_test3 = math.sqrt(sum([(x[1] - average_force_test1) ** 2 for x in data_experiment1_versuch2_test1]) / len(data_experiment1_versuch2_test3))
standard_deviation_test3_of_average = t/(math.sqrt(len(data_experiment1_versuch2_test3)))*standard_deviation_test3

print("-------Average Force Test1-------")
print(average_force_test1)
print(f'standard deviation: {standard_deviation_test1}')
print(f'standard deviation of the average: {standard_deviation_test1_of_average}')
print("-------Average Force Test2-------")
print(average_force_test2)
print(f'standard deviation: {standard_deviation_test2}')
print(f'standard deviation of the average: {standard_deviation_test2_of_average}')
print("-------Average Force Test3-------")
print(average_force_test3)
print(f'standard deviation: {standard_deviation_test3}')
print(f'standard deviation of the average: {standard_deviation_test3_of_average}')

#Create the plot for the task2
print("-------create the plot for the task2-------")

data_points = []
data_points.append([data_experiment1_versuch2_test1[0][0], average_force_test1])
data_points.append([data_experiment1_versuch2_test2[0][0], average_force_test2])
data_points.append([data_experiment1_versuch2_test3[0][0], average_force_test3])

error_bars =[standard_deviation_test1_of_average, standard_deviation_test2_of_average, standard_deviation_test3_of_average]

print(data_points)

data_line = []
data_line.append([0, 0])
data_line.append([data_experiment1_versuch2_test3[0][0], average_force_test3])

an.plot_data(data_points, 'Experiment2', data2=data_line, plot_fit=False, get_pdf=True, scale_x='linear', scale_y='linear', error_bars=True, error_bars_data=error_bars, lable_x='Masse in kg', lable_y='Kraft in N')

steigung = (average_force_test3 - 0)/(data_experiment1_versuch2_test3[0][0] - 0)
print("-------Steigung-------")
print(steigung)
print("Reibungskoeffizient")
print(steigung/9.807)

print("-------Fehlerfortpflanzung-------")
u_f_max = math.sqrt(math.pow((1/(data_experiment1_versuch2_test3[0][0]*9.807))*standard_deviation_test2_of_average, 2) + math.pow((average_force_test3/(math.pow(data_experiment1_versuch2_test3[0][0], 2)*9.807))*0.01, 2))
u_f_min = math.sqrt(math.pow((1/(data_experiment1_versuch2_test3[0][0]*9.807))*standard_deviation_test1_of_average, 2) + math.pow((average_force_test3/(math.pow(data_experiment1_versuch2_test3[0][0], 2)*9.807))*0.01, 2))
print(f"Fehlerfortpflanzung von u = {u_f_max} am Daten Punkt 3")
print(f"Fehlerfortpflanzung von u = {u_f_min} am Daten Punkt 1")




