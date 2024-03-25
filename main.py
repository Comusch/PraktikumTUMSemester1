import Analysistools as an

#Test at first
data = an.read_csv_file('test.csv')
print(data)
an.plot_data(data, 'test3_linear', 'linear', 'linear')
an.plot_data(data, 'test3_log', 'linear', 'log')