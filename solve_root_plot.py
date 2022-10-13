import matplotlib.pyplot as plt
import numpy as np

bi_n = np.loadtxt('bisection.txt', skiprows = 0, usecols = 0)
bi_sol = np.loadtxt('bisection.txt', skiprows = 0, usecols = 1)
bi_err = np.loadtxt('bisection.txt', skiprows = 0, usecols = 2)

new_n = np.loadtxt('newton.txt', skiprows = 0, usecols = 0)
new_sol = np.loadtxt('newton.txt', skiprows = 0, usecols = 1)
new_err = np.loadtxt('newton.txt', skiprows = 0, usecols = 2)

sec_n = np.loadtxt('secant.txt', skiprows = 0, usecols = 0)
sec_sol = np.loadtxt('secant.txt', skiprows = 0, usecols = 1)
sec_err = np.loadtxt('secant.txt', skiprows = 0, usecols = 2)

fig = plt.figure(figsize = (7, 5), dpi = 100)
ax = fig.add_subplot(1, 1, 1)
line1, = ax.plot(np.log10(bi_n), np.log10(bi_err), 'bo',
                  markersize = 3, linestyle = 'dashed', label = 'bisection')
line2, = ax.plot(np.log10(new_n), np.log10(new_err), 'ro',
                  markersize = 3, linestyle = 'dashed', label = 'newton')
line3, = ax.plot(np.log10(sec_n), np.log10(sec_err), 'ko',
                  markersize = 3, linestyle = 'dashed', label = 'secant')
ax.legend(handles=[line1, line2, line3])
ax.set_xlabel('$log_{10}N$', fontsize = 13)
ax.set_ylabel('$log_{10}$(error)', fontsize = 13)
fig.tight_layout()
plt.grid()
plt.show()
fig.savefig('solve_root.png')