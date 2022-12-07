import numpy as np
import matplotlib.pyplot as plt
import math

lw_x5000_8 = np.loadtxt('advectionlw5000_08000.d', skiprows = 0, usecols = 1)
lw_u5000_8 = np.loadtxt('advectionlw5000_08000.d', skiprows = 0, usecols = 2)
lw_ua5000_8 = np.loadtxt('advectionlw5000_08000.d', skiprows = 0, usecols = 3)

lw_x500_8 = np.loadtxt('advectionlw500_00800.d', skiprows = 0, usecols = 1)
lw_u500_8 = np.loadtxt('advectionlw500_00800.d', skiprows = 0, usecols = 2)
lw_ua500_8 = np.loadtxt('advectionlw500_00800.d', skiprows = 0, usecols = 3)

lw_x50_8 = np.loadtxt('advectionlw50_00080.d', skiprows = 0, usecols = 1)
lw_u50_8 = np.loadtxt('advectionlw50_00080.d', skiprows = 0, usecols = 2)
lw_ua50_8 = np.loadtxt('advectionlw50_00080.d', skiprows = 0, usecols = 3)

lf_x5000_8 = np.loadtxt('advection5000_08000.d', skiprows = 0, usecols = 1)
lf_u5000_8 = np.loadtxt('advection5000_08000.d', skiprows = 0, usecols = 2)
lf_ua5000_8 = np.loadtxt('advection5000_08000.d', skiprows = 0, usecols = 3)

lf_x500_8 = np.loadtxt('advection500_00800.d', skiprows = 0, usecols = 1)
lf_u500_8 = np.loadtxt('advection500_00800.d', skiprows = 0, usecols = 2)
lf_ua500_8 = np.loadtxt('advection500_00800.d', skiprows = 0, usecols = 3)

lf_x50_8 = np.loadtxt('advection50_00080.d', skiprows = 0, usecols = 1)
lf_u50_8 = np.loadtxt('advection50_00080.d', skiprows = 0, usecols = 2)
lf_ua50_8 = np.loadtxt('advection50_00080.d', skiprows = 0, usecols = 3)

lw_u8  = [lw_u50_8, lw_u500_8, lw_u5000_8]
lf_u8  = [lf_u50_8, lf_u500_8, lf_u5000_8]
lw_ua8 = [lw_ua50_8, lw_ua500_8, lw_ua5000_8]
lf_ua8 = [lf_ua50_8, lf_ua500_8, lf_ua5000_8]
lw_x8  = [lw_x50_8, lw_x500_8, lw_x5000_8]
lf_x8  = [lf_x50_8, lf_x500_8, lf_x5000_8]

delx_lw2 = [(lw_x50_8[1]-lw_x50_8[0])**2, (lw_x500_8[1]-lw_x500_8[0])**2, (lw_x5000_8[1]-lw_x5000_8[0])**2]
delx_lf2 = [(lf_x50_8[1]-lf_x50_8[0])**2, (lf_x500_8[1]-lf_x500_8[0])**2, (lf_x5000_8[1]-lf_x5000_8[0])**2]
dx2 = [(1/50)**2, (1/500)**2, (1/5000)**2]
print("dx2=", dx2)
#dx = (xmax - xmin)/imax

lw_error8 = []
lf_error8 = []

lw_error8tem = 0
for j in range(len(lw_u8)):
    for i in range(len(lw_u8[j])):
        lw_error8tem += abs(lw_u8[j][i]-lw_ua8[j][i])
    k = 50 * math.pow(10,j)
    lw_error8.append(lw_error8tem/k)
    lw_error8tem = 0
print("lw_error8: ", lw_error8)

lf_error8tem = 0
for j in range(len(lf_u8)):
    for i in range(len(lf_u8[j])):
        lf_error8tem += abs(lf_u8[j][i]-lf_ua8[j][i])
    k = 50 * math.pow(10,j)
    #print(k)
    lf_error8.append(lf_error8tem/k)
    lf_error8tem = 0
print("lf_error8: ", lf_error8)

n = [50, 500, 5000]

logn = []
lw_logerr8 = []
lf_logerr8 = []
lw_logx = []
lf_logx = []
dx2_log = []
x_log = []

for i in range(len(n)):
    logn.append(math.log10(n[i]))
    lw_logerr8.append(math.log10(lw_error8[i]))
    lf_logerr8.append(math.log10(lf_error8[i]))
    lw_logx.append(math.log10(delx_lw2[i]))
    lf_logx.append(math.log10(delx_lf2[i]))
    dx2_log.append(math.log10(dx2[i]))
    x_log.append(math.log10(1/n[i]))

#print("lwerrlog=", lw_logerr8, "\nlferrlog=", lf_logerr8)
#print("dx2log=", dx2_log, "\mdxlog=", x_log)

mvlw = dx2_log[0]-lw_logerr8[0] # to parallely move the 1/x^2 line
mvlf = x_log[0]-lf_logerr8[0]
print(mvlw, mvlf)

for i in range(len(n)):
    dx2_log[i] = dx2_log[i] - mvlw
    x_log[i] = x_log[i] - mvlf

fig = plt.figure(figsize = (7, 5), dpi = 100)
ax = fig.add_subplot(1, 1, 1)
ax.plot(logn, lw_logerr8, 'bo-', label = 'LW')
ax.plot(logn, lf_logerr8, 'ro-', label = 'LF')
ax.plot(logn, dx2_log, 'ko--', label = '$1/dx^2$')
ax.plot(logn, x_log, 'go--', label = '$1/dx$')
ax.set_title('error', fontsize = 13)
ax.set_xlabel('log n', fontsize = 13)
ax.set_ylabel('log error', fontsize = 13)
plt.legend()
fig.tight_layout()
plt.grid()
#plt.show()
#plt.savefig('error.png')
plt.savefig('error_with_ana1.png')
