import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

def read_csv_file(file_name):
    data = []
    with open(f"./Experiment_Data(CVS-files)/{file_name}", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            print(", ".join(row))
            row_data = []
            for cell in row:
                row_data.append(float(cell))
            data.append(row_data)
    return data

def plot_data(data, file_name, scale_x="linear", scale_y="linear"):
    data = np.array(data)
    if scale_y == "log":
        coefficients = np.polyfit(data[:, 0], np.log(data[:, 1]), 5, rcond=None, full=False, w=None, cov=False)
    else:
        coefficients = np.polyfit(data[:, 0], data[:, 1], 5, rcond=None, full=False, w=None, cov=False)
    fit_line = np.poly1d(coefficients)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xscale(scale_x)
    ax.set_yscale(scale_y)
    ax.plot(data[:, 0], data[:, 1], 'o', color='b', label='Data Points')  # Data points
    ax.plot(data[:, 0], fit_line(data[:, 0]), color='r', label='Fit Line')  # Fit line
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.legend()
    ax.grid()
    fig.show()
    if not os.path.isdir(f"./Graphics/{file_name}.pdf"):
        fig.savefig(f"./Graphics/{file_name}.pdf")
    else:
        fig.savefig(f"./Graphics/{file_name}_1.pdf")



