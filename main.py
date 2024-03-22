import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

x = np.linspace(0, 4*np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(4, 2.5))

ax.plot(x, y, color='r')

ax.set_xlabel(r'$x$ in rad')
ax.set_ylabel(r'$\sin(x)$')
ax.grid()

fig.show()

fig.savefig('plot.pdf')

# Daten als punkt hinzeichen
a = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 4.5), (6, 3.5), (7, 2.5), (8, 1.5), (9, 1), (10, 0.5)]
data = np.array(a)

# Fit a line to the data points
coefficients = np.polyfit(data[:, 0], data[:, 1], 5, rcond=None, full=False, w=None, cov=False)
fit_line = np.poly1d(coefficients)

# Plotting
fig, ax = plt.subplots(figsize=(4, 2.5))
ax.plot(data[:, 0], data[:, 1], 'o', color='b', label='Data Points')  # Data points
ax.plot(data[:, 0], fit_line(data[:, 0]), color='r', label='Fit Line')  # Fit line
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.legend()
ax.grid()
fig.show()
fig.savefig('data_with_fit_line.pdf')