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

average_force_test1 = average_force_test1/len(data_experiment1_versuch2_test1)
standard_deviation_test1 = math.sqrt(sum([(x[1] - average_force_test1) ** 2 for x in data_experiment1_versuch2_test1]) / len(data_experiment1_versuch2_test1))

average_force_test2 = 0
for i in range(0, len(data_experiment1_versuch2_test2)):
    average_force_test2 = average_force_test2 + data_experiment1_versuch2_test2[i][1]
average_force_test2 = average_force_test2/len(data_experiment1_versuch2_test2)
standard_deviation_test2 = math.sqrt(sum([(x[1] - average_force_test2) ** 2 for x in data_experiment1_versuch2_test2]) / len(data_experiment1_versuch2_test1))

average_force_test3 = 0
for i in range(0, len(data_experiment1_versuch2_test3)):
    average_force_test3 = average_force_test3 + data_experiment1_versuch2_test3[i][1]
average_force_test3 = average_force_test3/len(data_experiment1_versuch2_test3)
standard_deviation_test3 = math.sqrt(sum([(x[1] - average_force_test1) ** 2 for x in data_experiment1_versuch2_test1]) / len(data_experiment1_versuch2_test3))

print("-------Average Force Test1-------")
print(average_force_test1)
print("-------Average Force Test2-------")
print(average_force_test2)
print("-------Average Force Test3-------")
print(average_force_test3)

#Create the plot for the task2
print("-------create the plot for the task2-------")

data_points = []
data_points.append([data_experiment1_versuch2_test1[0][0], average_force_test1])
data_points.append([data_experiment1_versuch2_test2[0][0], average_force_test2])
data_points.append([data_experiment1_versuch2_test3[0][0], average_force_test3])

error_bars =[standard_deviation_test1, standard_deviation_test2, standard_deviation_test3]

print(data_points)

data_line = []
data_line.append([0, 0])
data_line.append([data_experiment1_versuch2_test3[0][0], average_force_test3])

an.plot_data(data_points, 'Experiment1_Aufgabe5', data_line, False, True, 'linear', 'linear', True, error_bars)

steigung = (average_force_test3 - 0)/(data_experiment1_versuch2_test3[0][0] - 0)
print("-------Steigung-------")
print(steigung)
print("Reibungskoeffizient")
print(steigung)




