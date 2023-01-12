import numpy as np
import math
import matplotlib.pyplot as plt
import gravitational_constant

G = gravitational_constant.G_au_ms_year

def kep_2_cart(a,e,I,w,Om,t,N,ma):
    #len(t)=N
    MA = []
    EA = []
    nu = []
    r = []
    X = []
    Y = []
    Z = []
    Nu=[]
    #per=np.sqrt(4*(np.pi**2)*(a**3)/mu)
    #print("a=",a*AU/rs,"rs")
    #print("a=",a,"mu=",mu)
    #print("per=",per) #year
    #t0=0.5*per
    for i in range(N):
        if i==0:
            #n = np.sqrt(mu/(a**3)) #1/year
            #print(a**3,(mu/a**3),"n=",n)
            #MA.append(n*(t[i]))
            MA.append(ma[i])
            EA.append(MA[i])
            #print("EA=",EA[i],"\n")
            nu.append(2*np.arctan(np.sqrt((1-e[i])/(1+e[i])) * np.tan(EA[i]/2)))
            #print("nu=",2*np.arctan(np.tan(EA[i]/2)),nu[i],"\n")
            #Nu.append(math.radians(nu[i]))
            r.append(a[i] * (1 - e[i]*np.cos(EA[i])))

            X.append(r[i]*(np.cos(Om[i])*np.cos(w[i]+nu[i])
                           - np.sin(Om[i])*np.sin(w[i]+nu[i])*np.cos(I[i])))
            #In circular case (all parameters=0 expect radius), X=r*cos(nu)
            Y.append(r[i]*(np.sin(Om[i])*np.cos(w[i]+nu[i])
                           + np.cos(Om[i])*np.sin(w[i]+nu[i])*np.cos(I[i])))
            #In circular case, Y=r*sin(nu)
            Z.append(r[i]*(np.sin((I[i]))*np.sin((w[i]+nu[i]))))
            #In circular case, Z=0
            #print(i,":",X,Y,"\n")

        else:
            #print(i)
            #n = np.sqrt(mu / (a ** 3))
            #MA.append(n * (t[i]))
            MA.append(ma[i])
            #print(MA[i])
            EA.append(EA[i-1]-((EA[i-1]-e[i]*np.sin(EA[i-1])-MA[i])/(1-e[i]*np.cos(EA[i-1]))))
            #print("EA=", EA[i], "\n")
            nu.append(2 * np.arctan(np.sqrt((1 - e[i]) / (1 + e[i])) * np.tan(EA[i] / 2)))
            #print("nu=", 2*(EA[i]/2), nu[i], "\n")
            #print(np.cos(nu[i]))
            #Nu.append(math.radians(nu[i]))
            r.append(a[i] * (1 - e[i] * np.cos(EA[i])))


            X.append(r[i] * (np.cos(Om[i]) * np.cos(w[i] + nu[i])
                             - np.sin(Om[i]) * np.sin(w[i] + nu[i]) * np.cos(I[i])))
            # In circular case (all parameters=0 expect radius), X=r*cos(nu)
            Y.append(r[i] * (np.sin(Om[i]) * np.cos(w[i] + nu[i])
                             + np.cos(Om[i]) * np.sin(w[i] + nu[i]) * np.cos(I[i])))
            # In circular case, Y=r*sin(nu)
            Z.append(r[i] * (np.sin((I[i])) * np.sin((w[i] + nu[i]))))
            # In circular case, Z=0

            #print(i,": ", Y[i], "\n")

    return [X, Y, Z]

# change into rotating frame
def coord_change_x(xin, yin, xin2, yin2, N):
    xout = np.zeros(N)
    #theta = np.zeros(N)
    for i in range(N):
        theta = np.arctan2(yin2[i], xin2[i])
        xout[i] = xin[i]*np.cos(-theta) - yin[i]*np.sin(-theta) #to rotating frame
        #xout[i] = xin[i]*np.cos(theta) - yin[i]*np.sin(theta) #test
    return xout

def coord_change_y(xin, yin, xin2, yin2, N):
    yout = np.zeros(N)
    for i in range(N):
        theta = np.arctan2(yin2[i], xin2[i])
        yout[i] = xin[i]*np.sin(-theta) + yin[i]*np.cos(-theta)
        #yout[i] = xin[i]*np.sin(theta) + yin[i]*np.cos(theta) # test
    return yout

def coord_change(xin1, xin2, N):
    xout = np.zeros(N)
    for i in range(N):
        xout[i] = xin1[i] - xin2[i]
    return xout

filename_cen = 'JUPITER.aei'
titlename_cen = 'JUPITER'
filename = 'POterma.aei'
titlename = 'POterma'
filename15 = 'S03.aei'
titlename15 = 'S03'
methodused = 'BS'
note = 'rotate5'
ts = 25 # time step


t_cen  = np.loadtxt(filename_cen, usecols=(0), skiprows=4)
x_cen  = np.loadtxt(filename_cen, usecols=(3), skiprows=4)
y_cen  = np.loadtxt(filename_cen, usecols=(4), skiprows=4)
z_cen  = np.loadtxt(filename_cen, usecols=(5), skiprows=4)
m_cen  = np.loadtxt(filename_cen, usecols=(2), skiprows=4)

t  = np.loadtxt(filename, usecols=(0), skiprows=4)
x  = np.loadtxt(filename, usecols=(3), skiprows=4)
y  = np.loadtxt(filename, usecols=(4), skiprows=4)
z  = np.loadtxt(filename, usecols=(5), skiprows=4)
m  = np.loadtxt(filename, usecols=(2), skiprows=4)

t15  = np.loadtxt(filename15, usecols=(0), skiprows=4)
x15  = np.loadtxt(filename15, usecols=(3), skiprows=4)
y15  = np.loadtxt(filename15, usecols=(4), skiprows=4)
z15  = np.loadtxt(filename15, usecols=(5), skiprows=4)
m15  = np.loadtxt(filename15, usecols=(2), skiprows=4)



# The parameters of the center body (of the plot) 
my_t_cen  = np.loadtxt(filename_cen, usecols=(0), skiprows=4)
my_ma_cen = np.loadtxt(filename_cen, usecols=(2), skiprows=4)
my_a_cen  = np.loadtxt(filename_cen, usecols=(6), skiprows=4)
my_e_cen  = np.loadtxt(filename_cen, usecols=(7), skiprows=4)
my_i_cen  = np.loadtxt(filename_cen, usecols=(8), skiprows=4)
my_w_cen  = np.loadtxt(filename_cen, usecols=(9), skiprows=4)
my_Om_cen = np.loadtxt(filename_cen, usecols=(10), skiprows=4)

# The parameters of the small body
my_t  = np.loadtxt(filename, usecols=(0), skiprows=4)
my_ma = np.loadtxt(filename, usecols=(2), skiprows=4)
my_a  = np.loadtxt(filename, usecols=(6), skiprows=4)
my_e  = np.loadtxt(filename, usecols=(7), skiprows=4)
my_i  = np.loadtxt(filename, usecols=(8), skiprows=4)
my_w  = np.loadtxt(filename, usecols=(9), skiprows=4)
my_Om = np.loadtxt(filename, usecols=(10), skiprows=4)

my_N_cen = len(my_t_cen)
my_N = len(my_t)
[my_x_cen, my_y_cen, my_z_cen] = kep_2_cart(my_a_cen, my_e_cen, my_i_cen, my_w_cen, my_Om_cen, my_t_cen, my_N_cen, my_ma_cen)
[my_x, my_y, my_z] = kep_2_cart(my_a, my_e, my_i, my_w, my_Om, my_t, my_N, my_ma)
#print(np.shape(x), np.shape(y), np.shape(z))
#print(type(x), type(y), type(z))

N = len(t)
print(N)
'''
errorx = np.zeros(N)
plotn = np.zeros(N)
#logn = np.zeros(N)
for i in range(1, N):
    errorx[i] = math.log10(abs(my_x[i] - x[i]/x[i]))
    plotn[i] = math.log10(i)
    #logn[i] = math.log10(i)
#print(errorx)
fig = plt.figure(figsize = (7, 5), dpi = 500, facecolor='white')
ax2 = fig.add_subplot(1, 1, 1)
ax2.plot(plotn[1:], errorx[1:], 'b-', label='x error')
ax2.set_xlabel("log (N)", fontsize = 13)
ax2.set_ylabel("log (x error)", fontsize = 13)
ax2.set_title(f"Relative error, {methodused} method")
ax2.legend()
plt.savefig(f"Relative error, {methodused} method")
plt.close()
'''

fig, axs = plt.subplots(3)
axs[0].plot(t, x, 'b-', markersize = 1.5)
axs[1].plot(t, y, 'g-', markersize = 1.5)
axs[2].plot(t, z, 'k-', markersize = 1.5)

axs[2].set_xlabel('time(year)', fontsize = 12)
axs[0].set_ylabel('AU', fontsize = 12)
axs[1].set_ylabel('AU', fontsize = 12)
axs[2].set_ylabel('AU', fontsize = 12)

axs[0].set_title(f'{titlename} x, y, z position', fontsize = 13)
plt.tight_layout()

#plt.savefig(f'my_{titlename}_{methodused}_ts{ts}.png')
plt.savefig(f'{titlename}_{methodused}_{note}.png')
plt.close()

#center body plot
fig, axs = plt.subplots(3)
axs[0].plot(t_cen, x_cen, 'b-', markersize = 1.5)
axs[1].plot(t_cen, y_cen, 'g-', markersize = 1.5)
axs[2].plot(t_cen, z_cen, 'k-', markersize = 1.5)
axs[2].set_xlabel('time(year)', fontsize = 12)

axs[0].set_ylabel('AU', fontsize = 12)
axs[1].set_ylabel('AU', fontsize = 12)
axs[2].set_ylabel('AU', fontsize = 12)

axs[0].set_title(f'{titlename_cen} x, y, z position', fontsize = 13)
plt.tight_layout()
#plt.savefig(f'my_{titlename_cen}_{methodused}_ts{ts}.png')
plt.savefig(f'{titlename_cen}_{methodused}_{note}.png')
plt.close()

'''
#mean anomaly
x_plot = np.zeros(N)
y_plot = np.zeros(N)
x_cen_plot = np.zeros(N)
y_cen_plot = np.zeros(N)

for i in range(N):
    x_plot[i] = float(t[i])
    y_plot[i] = float(m[i])
    x_cen_plot[i] = float(t_cen[i])
    y_cen_plot[i] = float(m_cen[i])
startpoint = 0
endpoint =N
#print(x_plot, y_plot)
fig = plt.figure(figsize = (7, 5), dpi = 500, facecolor='white')
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(x_plot[startpoint:endpoint], y_plot[startpoint:endpoint], 'b-', label='P/Oterma')
ax1.plot(x_cen_plot[startpoint:endpoint], y_cen_plot[startpoint:endpoint], 'k-', label='JUPITER')
ax1.set_xlabel("time", fontsize = 13)
ax1.set_ylabel("mean anomaly", fontsize = 13)
ax1.set_title(f"Mean Anomaly, {methodused} method")
#ax1.grid()
ax1.legend()
plt.savefig(f"mean_anomaly_{methodused}_{note}.png")
plt.close()
'''

# The x-y plot
x = coord_change_x(x, y, x_cen, y_cen, N)
y = coord_change_y(x, y, x_cen, y_cen, N)
x_cen = coord_change_x(x_cen, y_cen, x_cen, y_cen, N)
y_cen = coord_change_y(x_cen, y_cen, x_cen, y_cen, N)

x = coord_change(x, x_cen, N)
y = coord_change(y, y_cen, N)
x_cen = coord_change(x_cen, x_cen, N)
y_cen = coord_change(y_cen, y_cen, N)

x_plot = np.zeros(N)
y_plot = np.zeros(N)
x_cen_plot = np.zeros(N)
y_cen_plot = np.zeros(N)

for i in range(N):
    x_plot[i] = float(x[i])
    y_plot[i] = float(y[i])
    x_cen_plot[i] = float(x_cen[i])
    y_cen_plot[i] = float(y_cen[i])
startpoint = 0
endpoint = N
#print(x_plot, y_plot)
fig = plt.figure(figsize = (5, 5), dpi = 500, facecolor='white')
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(x_plot[startpoint:endpoint], y_plot[startpoint:endpoint], 'b-', label='P/Oterma')
ax1.plot(x_cen_plot[startpoint:endpoint], y_cen_plot[startpoint:endpoint], 'ko', markersize=3, linestyle='solid', label='JUPITER')
#ax1.plot(x_cen_plot[startpoint:endpoint], y_cen_plot[startpoint:endpoint], 'k-', label='JUPITER')
ax1.set_xlabel("x", fontsize = 13)
ax1.set_ylabel("y", fontsize = 13)
#ax1.set_xlim([-8, 8])
#ax1.set_ylim([-8, 8])
ax1.set_title(f"Position, {methodused} method")
#ax1.grid()
ax1.legend()
plt.tight_layout()
#plt.savefig(f"{titlename}_{methodused}_ts{ts}_full.png")
#plt.savefig(f"{titlename}_{methodused}_ts{ts}.png")
#plt.savefig(f"{titlename}_{methodused}_xy_{note}.png")
plt.savefig(f"{titlename}_{methodused}_xy_full_{note}.png")
#plt.savefig(f"ori_{titlename}_{methodused}_xy_full_{note}.png")
#plt.savefig(f"Jupiter_only_{titlename}_{methodused}_xy_full_{note}.png")
plt.close()


# The x-y plot of small body (-15)
#x15 = coord_change_x(x15, y15, x_cen, y_cen, N)
#y15 = coord_change_y(x15, y15, x_cen, y_cen, N)
#x_cen = coord_change_x(x_cen, y_cen, x_cen, y_cen, N)
#y_cen = coord_change_y(x_cen, y_cen, x_cen, y_cen, N)

#x15 = coord_change(x15, x_cen, N)
#y15 = coord_change(y15, y_cen, N)
#x_cen = coord_change(x_cen, x_cen, N)
#y_cen = coord_change(y_cen, y_cen, N)

x15_plot = np.zeros(N)
y15_plot = np.zeros(N)
x_cen_plot = np.zeros(N)
y_cen_plot = np.zeros(N)

for i in range(N):
    x15_plot[i] = float(x15[i])
    y15_plot[i] = float(y15[i])
    x_cen_plot[i] = float(x_cen[i])
    y_cen_plot[i] = float(y_cen[i])
startpoint = 0
endpoint =N
#print(x_plot, y_plot)
fig = plt.figure(figsize = (5, 5), dpi = 500, facecolor='white')
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(x15_plot[startpoint:endpoint], y15_plot[startpoint:endpoint], 'b-', label=titlename15)
#ax1.plot(x_cen_plot[startpoint:endpoint], y_cen_plot[startpoint:endpoint], 'ko', markersize=3, linestyle='solid', label='JUPITER')
ax1.plot(x_cen_plot[startpoint:endpoint], y_cen_plot[startpoint:endpoint], 'k-', label='JUPITER')
ax1.set_xlabel("x", fontsize = 13)
ax1.set_ylabel("y", fontsize = 13)
ax1.set_xlim([-8, 8])
ax1.set_ylim([-8, 8])
ax1.set_title(f"Position, {methodused} method")
#ax1.grid()
ax1.legend()
plt.tight_layout()
#plt.savefig(f"{titlename}_{methodused}_ts{ts}_full.png")
#plt.savefig(f"{titlename}_{methodused}_ts{ts}.png")
#plt.savefig(f"{titlename15}_{methodused}_xy_{note}.png")
#plt.savefig(f"{titlename15}_{methodused}_xy_full_{note}.png")
plt.savefig(f"ori_{titlename15}_{methodused}_xy_full_{note}.png")
plt.close()



'''use the transformation'''
'''
my_x = coord_change(my_x, my_x_cen, N)
my_y = coord_change(my_y, my_y_cen, N)
my_z = coord_change(z, z_cen, N)
my_x_cen = coord_change(x_cen, x_cen, N)
my_y_cen = coord_change(y_cen, y_cen, N)
my_z_cen = coord_change(z_cen, z_cen, N)

x_plot = np.zeros(N)
y_plot = np.zeros(N)
z_plot = np.zeros(N)
x_cen_plot = np.zeros(N)
y_cen_plot = np.zeros(N)
z_cen_plot = np.zeros(N)

for i in range(N):
    x_plot[i] = float(my_x[i])
    y_plot[i] = float(my_y[i])
    z_plot[i] = float(my_z[i])
    x_cen_plot[i] = float(my_x_cen[i])
    y_cen_plot[i] = float(my_y_cen[i])
    z_cen_plot[i] = float(my_z_cen[i])
startpoint = 0
endpoint =N
#print(x_plot, y_plot)
fig = plt.figure(figsize = (7, 5), dpi = 500, facecolor='white')
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(x_plot[startpoint:endpoint], y_plot[startpoint:endpoint], 'b-', label='P/Oterma')
ax1.plot(x_cen_plot[startpoint:endpoint], y_cen_plot[startpoint:endpoint], 'ko', markersize=3, linestyle='solid', label='JUPITER')
ax1.set_xlabel("x", fontsize = 13)
ax1.set_ylabel("y", fontsize = 13)
ax1.set_xlim([-2, 2])
ax1.set_ylim([-2, 2])
ax1.set_title(f"Position, {methodused} method")
#ax1.grid()
ax1.legend()
#plt.savefig(f"my_{titlename}_{methodused}_ts{ts}_full.png")
#plt.savefig(f"my_{titlename}_{methodused}_ts{ts}.png")
plt.savefig(f"my_{titlename}_{methodused}_xy_{note}.png")
#plt.savefig(f"my_{titlename}_{methodused}_xy_full_{note}.png")
plt.close()
'''