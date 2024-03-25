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
            if row[1] == "":
                continue
            for cell in row:
                # Check if the cell is a string
                try:
                    # Try converting the cell to a float
                    value = float(cell)
                except ValueError:
                    # If it's not a float, keep it as a string
                    value = cell
                row_data.append(value)
            data.append(row_data)
    return data

def plot_data(data, file_name, data2=None, plot_fit=True, get_pdf=True, scale_x="linear", scale_y="linear"):
    data = np.array(data)
    if data2 is not None:
        data2 = np.array(data2)
    if scale_y == "log":
        coefficients = np.polyfit(data[:, 0], np.log(data[:, 1]), 5, rcond=None, full=False, w=None, cov=False)
    else:
        coefficients = np.polyfit(data[:, 0], data[:, 1], 5, rcond=None, full=False, w=None, cov=False)

    if plot_fit:
        fit_line = np.poly1d(coefficients)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xscale(scale_x)
    ax.set_yscale(scale_y)

    ax.plot(data[:, 0], data[:, 1], 'o', color='b', label='Datenwerte')  # Data points
    if data2 is not None:
        plt.plot(data2[:, 0], data2[:, 1], color='r', label='Fit Line')

    if plot_fit:
        ax.plot(data[:, 0], fit_line(data[:, 0]), color='r', label='Fit Line')  # Fit line
    ax.set_xlabel(r'Masse in kg')
    ax.set_ylabel(r'Kraft in N')
    ax.legend()
    ax.grid()
    fig.show()
    if get_pdf:
        if not os.path.isdir(f"./Graphics/{file_name}.pdf"):
            fig.savefig(f"./Graphics/{file_name}.pdf")
        else:
            fig.savefig(f"./Graphics/{file_name}_1.pdf")



