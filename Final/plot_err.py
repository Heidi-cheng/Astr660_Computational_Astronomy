import numpy as np
import matplotlib.pyplot as plt


x = np.loadtxt("energy.dat", usecols=(0), skiprows=1)
y = np.loadtxt("energy.dat", usecols=(1), skiprows=1)

fig = plt.figure(figsize = (7, 5), dpi = 500, facecolor='white')
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, 'bo', markersize=1.5)
ax.set_xlabel("time(days)", fontsize = 13)
ax.set_ylabel("Relative error", fontsize = 13)
ax.set_title("Relative error")
ax.grid()
plt.savefig("outer_scaled_error.png")
