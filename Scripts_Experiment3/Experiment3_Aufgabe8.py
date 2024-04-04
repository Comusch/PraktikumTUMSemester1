import Analysistools as an
import numpy as np


#konstanten
u_d_I = 0.0336434908630853
print("----------Load data-----------")

data_human = an.read_csv_file("Experiment3_Aufgabe1.csv")
data_human = data_human[1:]
print(data_human)

print("----------Calculate the average period and the standard deviation of the human reading-----------")
t = 1.15
avarage_periode = 0
for i in range(len(data_human)):
    avarage_periode = avarage_periode + float(data_human[i][1])
avarage_periode = avarage_periode/len(data_human)
print(f'avarage_periode: {avarage_periode}')
standard_deviation_periode = (sum([(float(x[1]) - avarage_periode) ** 2 for x in data_human]) / len(data_human)) ** 0.5
print(f'standard_deviation_periode: {standard_deviation_periode}')
standard_deviation_periode_of_average = t/(len(data_human)**0.5)*standard_deviation_periode
print(f'standard_deviation_periode_of_average: {standard_deviation_periode_of_average}')
print(f'Eigenfrequency: {1/avarage_periode}')

print("----------Calculate the average period and the standard deviation of the computer-----------")
data_computer = an.read_csv_file("POR_A3.1.csv")
data_computer = data_computer[1:]
#delet the offset
offset = -1.9
for i in range(len(data_computer)):
    data_computer[i][1] = (float(data_computer[i][1]) -offset)
    data_computer[i][1] = data_computer[i][1]*u_d_I

print(data_computer)

an.plot_data(data_computer, "Experiment3_Aufgabe8a", get_pdf=True, plot_fit=True, lable_x="Zeit in s", lable_y="Amplitude in rad", scale_x="linear", scale_y="linear")

print("----------Calculate the average period and the standard deviation of the computer reading-----------")
maxima = []
for i in range(len(data_computer)-2):
    if data_computer[i][1] < data_computer[i+1][1] and data_computer[i+1][1] > data_computer[i+2][1] and data_computer[i+1][1] > 5*u_d_I:
        maxima.append(data_computer[i+1])
print(maxima)
print(f'lenght of maxima: {len(maxima)}')

periodes = []
for i in range(len(maxima)-1):
    periodes.append(float(maxima[i+1][0]) - float(maxima[i][0]))

t = 1.08
print(periodes)
print("----------show the periodes of the computer's reading-----------")
avarage_periode_computer = sum(periodes)/len(periodes)
print(f'avarage_periode: {avarage_periode_computer}')
standard_deviation_periode_computer = (sum([(x - avarage_periode_computer) ** 2 for x in periodes]) / len(periodes)) ** 0.5
print(f'standard_deviation_periode_computer: {standard_deviation_periode_computer}')
standard_deviation_periode_of_average_computer = t/(len(periodes)**0.5)*standard_deviation_periode_computer
print(f'standard_deviation_periode_of_average: {standard_deviation_periode_of_average_computer}')

print("----------Compare the human and the computer reading-----------")
print(f'Eigenfrequency human: {1/avarage_periode}')
print(f'Eigenfrequency computer: {1/avarage_periode_computer}')
print(f'Difference: {abs(1/avarage_periode - 1/avarage_periode_computer)}')
print(f'standard_deviation_periode_of_average human: {standard_deviation_periode_of_average}')
print(f'standard_deviation_periode_of_average computer: {standard_deviation_periode_of_average_computer}')

an.plot_data(maxima, "Experiment3_Aufgabe8b",data2=data_computer, get_pdf=True, plot_fit=False, lable_x="Zeit in s", lable_y="Amplitude in rad", scale_x="linear", scale_y="linear", lable_daten="genutzte Maxima", lable_fit="alle Daten des Computers")



