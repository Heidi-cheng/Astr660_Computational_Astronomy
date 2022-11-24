import numpy as np
import matplotlib.pyplot as plt
'''
x = np.loadtxt('advection_00000.d', skiprows = 0, usecols = 1)
u = np.loadtxt('advection_00000.d', skiprows = 0, usecols = 2)

x250 = np.loadtxt('advection_00250.d', skiprows = 0, usecols = 1)
u250 = np.loadtxt('advection_00250.d', skiprows = 0, usecols = 2)

x500 = np.loadtxt('advection_00500.d', skiprows = 0, usecols = 1)
u500 = np.loadtxt('advection_00500.d', skiprows = 0, usecols = 2)

x870 = np.loadtxt('advection_00870.d', skiprows = 0, usecols = 1)
u870 = np.loadtxt('advection_00870.d', skiprows = 0, usecols = 2)

fig = plt.figure(figsize = (7, 5), dpi = 100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, u, 'b-', label = '000')
ax.plot(x250, u250, 'r-', label = '250')
ax.plot(x500, u500, 'g-', label = '500')
ax.plot(x870, u870, 'k-', label = '870')
plt.legend()

ax.set_xlabel('x', fontsize = 13)
ax.set_ylabel('u', fontsize = 13)
fig.tight_layout()
plt.grid()
plt.show()
fig.savefig('FTCS.png')
'''

x = np.loadtxt('advection_00000.d', skiprows = 0, usecols = 1)
u = np.loadtxt('advection_00000.d', skiprows = 0, usecols = 2)

x250 = np.loadtxt('advection_00250.d', skiprows = 0, usecols = 1)
u250 = np.loadtxt('advection_00250.d', skiprows = 0, usecols = 2)

x500 = np.loadtxt('advection_00500.d', skiprows = 0, usecols = 1)
u500 = np.loadtxt('advection_00500.d', skiprows = 0, usecols = 2)

x870 = np.loadtxt('advection_00870.d', skiprows = 0, usecols = 1)
u870 = np.loadtxt('advection_00870.d', skiprows = 0, usecols = 2)

fig = plt.figure(figsize = (7, 5), dpi = 100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, u, 'b-', label = '000')
ax.plot(x250, u250, 'r-', label = '250')
ax.plot(x500, u500, 'g-', label = '500')
ax.plot(x870, u870, 'k-', label = '870')
plt.legend()

ax.set_xlabel('x', fontsize = 13)
ax.set_ylabel('u', fontsize = 13)
fig.tight_layout()
plt.grid()
plt.show()
fig.savefig('FVM.png')
