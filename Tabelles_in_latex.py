import Analysistools as an
import math

'''
print("-------Experiment1_Aufgabe1-------")
data_experiment1_aufgabe1 = an.read_csv_file('Experiment1_Aufgabe1.csv')
for i in range (1, 16):
    #this is possible, because the hypotenuse is 1
    data_experiment1_aufgabe1[i][0] = round(math.asin(data_experiment1_aufgabe1[i][3]), 3)
an.generate_latex_table(data_experiment1_aufgabe1)'''

print("-------Experiment1_Aufgabe2-------")
data_experiment1_aufgabe2 = an.read_csv_file('Experiment1_Aufgabe2_Test1.csv')
an.generate_latex_table(data_experiment1_aufgabe2)

