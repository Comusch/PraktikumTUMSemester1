import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

def generate_latex_table(data):
    num_rows = len(data)
    num_cols = len(data[0]) if num_rows > 0 else 0

    if num_cols == 0:
        print("Das Array ist leer. Kann keine Tabelle generieren.")
        return

    latex_code = "\\begin{tabular}{|" + "c|" * num_cols + "}\n"
    latex_code += "\\hline\n"

    for row in data:
        for item in row:
            latex_code += str(item) + " & "
        latex_code = latex_code[:-2]  # Remove the last "& "
        latex_code += " \\\\\n"  # End the row
        latex_code += "\\hline\n"

    latex_code += "\\end{tabular}"

    print(latex_code)

def read_csv_file(file_name):
    data = []
    with open(f"./Experiment_Data(CVS-files)/{file_name}", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            print(", ".join(row))
            row_data = []
            if row == []:
                continue
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

def plot_data(data, file_name, data2=None, plot_fit=True, get_pdf=True, scale_x="linear", scale_y="linear", error_bars=False, error_bars_data=None, lable_x="Zeit in s", lable_y="Abstand in m"):
    data = np.array(data)
    if data2 is not None:
        data2 = np.array(data2)
    if scale_y == "log":
        coefficients = np.polyfit(data[:, 0], np.log(data[:, 1]), 5, rcond=None, full=False, w=None, cov=False)
    else:
        coefficients = np.polyfit(data[:, 0], data[:, 1], 5, rcond=None, full=False, w=None, cov=False)

    if plot_fit:
        fit_line = np.poly1d(coefficients)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xscale(scale_x)
    ax.set_yscale(scale_y)
    if error_bars:
        ax.errorbar(data[:, 0], data[:, 1], yerr=error_bars_data, fmt='o', color='b', label='Datenwerte')
    else:
        ax.plot(data[:, 0], data[:, 1], 'o', color='b', label='Datenwerte')  # Data points
    if data2 is not None:
        plt.plot(data2[:, 0], data2[:, 1], color='r', label='Fit Line', linestyle='--')

    if plot_fit:
        ax.plot(data[:, 0], fit_line(data[:, 0]), color='r', label='Fit Line')  # Fit line
    ax.set_xlabel(lable_x)
    ax.set_ylabel(lable_y)
    ax.legend()
    ax.grid()
    #plt.title(file_name)
    fig.show()
    if get_pdf:
        if not os.path.isdir(f"./Graphics/{file_name}.pdf"):
            fig.savefig(f"./Graphics/{file_name}.pdf")
        else:
            fig.savefig(f"./Graphics/{file_name}_1.pdf")



