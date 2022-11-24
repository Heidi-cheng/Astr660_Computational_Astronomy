import matplotlib.pyplot as plt
import numpy as np
g = 9.81 # m/s**2

'''Exercise 1'''

x_euler = np.loadtxt('trajectory_euler_01.txt', skiprows = 1, usecols = 1)
t_euler_1 = np.loadtxt('trajectory_euler_1.txt', skiprows = 1, usecols = 0)
t_euler_01 = np.loadtxt('trajectory_euler_01.txt', skiprows = 1, usecols = 0)
t_euler_001 = np.loadtxt('trajectory_euler_001.txt', skiprows = 1, usecols = 0)
t_euler_0001 = np.loadtxt('trajectory_euler_0001.txt', skiprows = 1, usecols = 0)
y_euler_1 = np.loadtxt('trajectory_euler_1.txt', skiprows = 1, usecols = 2)
y_euler_01 = np.loadtxt('trajectory_euler_01.txt', skiprows = 1, usecols = 2)
y_euler_001 = np.loadtxt('trajectory_euler_001.txt', skiprows = 1, usecols = 2)
y_euler_0001 = np.loadtxt('trajectory_euler_0001.txt', skiprows = 1, usecols = 2)
y_ana_euler_1 = np.loadtxt('trajectory_euler_1.txt', skiprows = 1, usecols = 3)
y_ana_euler_01 = np.loadtxt('trajectory_euler_01.txt', skiprows = 1, usecols = 3)
y_ana_euler_001 = np.loadtxt('trajectory_euler_001.txt', skiprows = 1, usecols = 3)
y_ana_euler_0001 = np.loadtxt('trajectory_euler_0001.txt', skiprows = 1, usecols = 3)

x_rk2 = np.loadtxt('trajectory_rk2_01.txt', skiprows = 1, usecols = 1)
t_rk2_1 = np.loadtxt('trajectory_rk2_1.txt', skiprows = 1, usecols = 0)
t_rk2_01 = np.loadtxt('trajectory_rk2_01.txt', skiprows = 1, usecols = 0)
t_rk2_001 = np.loadtxt('trajectory_rk2_001.txt', skiprows = 1, usecols = 0)
t_rk2_0001 = np.loadtxt('trajectory_rk2_0001.txt', skiprows = 1, usecols = 0)
y_rk2_1 = np.loadtxt('trajectory_rk2_1.txt', skiprows = 1, usecols = 2)
y_rk2_01 = np.loadtxt('trajectory_rk2_01.txt', skiprows = 1, usecols = 2)
y_rk2_001 = np.loadtxt('trajectory_rk2_001.txt', skiprows = 1, usecols = 2)
y_rk2_0001 = np.loadtxt('trajectory_rk2_0001.txt', skiprows = 1, usecols = 2)
y_ana_rk2_1 = np.loadtxt('trajectory_rk2_1.txt', skiprows = 1, usecols = 3)
y_ana_rk2_01 = np.loadtxt('trajectory_rk2_01.txt', skiprows = 1, usecols = 3)
y_ana_rk2_001 = np.loadtxt('trajectory_rk2_001.txt', skiprows = 1, usecols = 3)
y_ana_rk2_0001 = np.loadtxt('trajectory_rk2_0001.txt', skiprows = 1, usecols = 3)

x_rk4 = np.loadtxt('trajectory_rk4_01.txt', skiprows = 1, usecols = 1)
t_rk4_1 = np.loadtxt('trajectory_rk4_1.txt', skiprows = 1, usecols = 0)
t_rk4_01 = np.loadtxt('trajectory_rk4_01.txt', skiprows = 1, usecols = 0)
t_rk4_001 = np.loadtxt('trajectory_rk4_001.txt', skiprows = 1, usecols = 0)
t_rk4_0001 = np.loadtxt('trajectory_rk4_0001.txt', skiprows = 1, usecols = 0)
y_rk4_1 = np.loadtxt('trajectory_rk4_1.txt', skiprows = 1, usecols = 2)
y_rk4_01 = np.loadtxt('trajectory_rk4_01.txt', skiprows = 1, usecols = 2)
y_rk4_001 = np.loadtxt('trajectory_rk4_001.txt', skiprows = 1, usecols = 2)
y_rk4_0001 = np.loadtxt('trajectory_rk4_0001.txt', skiprows = 1, usecols = 2)
y_ana_rk4_1 = np.loadtxt('trajectory_rk4_1.txt', skiprows = 1, usecols = 3)
y_ana_rk4_01 = np.loadtxt('trajectory_rk4_01.txt', skiprows = 1, usecols = 3)
y_ana_rk4_001 = np.loadtxt('trajectory_rk4_001.txt', skiprows = 1, usecols = 3)
y_ana_rk4_0001 = np.loadtxt('trajectory_rk4_0001.txt', skiprows = 1, usecols = 3)


err_euler_1 = 0
err_euler_01 = 0
err_euler_001 = 0
err_euler_0001 = 0

for i in range(len(y_euler_1)):
    err_euler_1 += abs(y_euler_1[i]-y_ana_euler_1[i])/len(y_euler_1)
for i in range(len(y_euler_01)):
    err_euler_01 += abs(y_euler_01[i]-y_ana_euler_01[i])/len(y_euler_01)
for i in range(len(y_euler_001)):
    err_euler_001 += abs(y_euler_001[i]-y_ana_euler_001[i])/len(y_euler_001)
for i in range(len(y_euler_0001)):
    err_euler_0001 += abs(y_euler_0001[i]-y_ana_euler_0001[i])/len(y_euler_0001)

err_rk2_1 = 0
err_rk2_01 = 0
err_rk2_001 = 0
err_rk2_0001 = 0

for i in range(len(y_rk2_1)):
    err_rk2_1 += abs(y_rk2_1[i]-y_ana_rk2_1[i])/len(y_rk2_1)
for i in range(len(y_rk2_01)):
    err_rk2_01 += abs(y_rk2_01[i]-y_ana_rk2_01[i])/len(y_rk2_01)
for i in range(len(y_rk2_001)):
    err_rk2_001 += abs(y_rk2_001[i]-y_ana_rk2_001[i])/len(y_rk2_001)
for i in range(len(y_rk2_0001)):
    err_rk2_0001 += abs(y_rk2_0001[i]-y_ana_rk2_0001[i])/len(y_rk2_0001)

err_rk4_1 = 0
err_rk4_01 = 0
err_rk4_001 = 0
err_rk4_0001 = 0

for i in range(len(y_rk4_1)):
    err_rk4_1 += abs(y_rk4_1[i]-y_ana_rk4_1[i])/len(y_rk4_1)
for i in range(len(y_rk4_01)):
    err_rk4_01 += abs(y_rk4_01[i]-y_ana_rk4_01[i])/len(y_rk4_01)
for i in range(len(y_rk4_001)):
    err_rk4_001 += abs(y_rk4_001[i]-y_ana_rk4_001[i])/len(y_rk4_001)
for i in range(len(y_rk4_0001)):
    err_rk4_0001 += abs(y_rk4_0001[i]-y_ana_rk4_0001[i])/len(y_rk4_0001)

print(err_euler_1, err_euler_01, err_euler_001, err_euler_0001)

log_dt = [-3, -2, -1, 0]
err_euler = [err_euler_0001, err_euler_001, err_euler_01, err_euler_1]
err_rk2 = [err_rk2_0001, err_rk2_001, err_rk2_01, err_rk2_1]
err_rk4 = [err_rk4_0001, err_rk4_001, err_rk4_01, err_rk4_1]


'''plot'''
fig = plt.figure(figsize = (7, 5), dpi = 100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(x_euler, y_euler_01, 'bo', markersize = 1, linestyle = 'dashed', label='Euler')
ax.plot(x_rk2, y_rk2_01, 'go', markersize = 1, linestyle = 'dashed', label='Rk2')
ax.plot(x_rk4, y_rk4_01, 'ko', markersize = 1, linestyle = 'dashed', label='Rk4')
#ax.plot(x_an, y_ana_rk4_1, 'ro', markersize = 1, linestyle = 'dashed', label='analytical')
ax.set_xlabel('x_position', fontsize = 13)
ax.set_ylabel('y_position', fontsize = 13)
plt.legend()
#ax.set_ylim(0, 50)
ax.set_title('Trajectory (dt=0.1s)')
fig.tight_layout()
plt.grid()
plt.show()
#fig.savefig('trajectory_0001.png')


fig = plt.figure(figsize = (7, 5), dpi = 100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(log_dt, np.log10(err_euler), 'bo', markersize = 3, linestyle = 'dashed', label='Euler')
ax.plot(log_dt, np.log10(err_rk2), 'go', markersize = 3, linestyle = 'dashed', label='Rk2')
ax.plot(log_dt, np.log10(err_rk4), 'ko', markersize = 3, linestyle = 'dashed', label='Rk4')
ax.set_xlabel('log_dt', fontsize = 13)
ax.set_ylabel('log_err', fontsize = 13)
plt.legend()
ax.invert_xaxis()
ax.set_title('error vs dt')
fig.tight_layout()
plt.grid()
plt.show()
fig.savefig('err.png')
