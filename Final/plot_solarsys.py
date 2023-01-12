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

# xin1 - xin2
def coord_change(xin1, xin2, N):
    xout = np.zeros(N)
    for i in range(N):
        xout[i] = xin1[i] - xin2[i]
    return xout

filename_mer = 'MERCURY.aei'
titlename_mer = 'MERCURY'
filename_ven = 'VENUS.aei'
titlename_ven = 'VENUS'
filename_ear = 'EARTHMOO.aei'
titlename_ear = 'EARTHMOO'
filename_mars = 'MARS.aei'
titlename_mars = 'MARS'
filename_jup = 'JUPITER.aei'
titlename_jup = 'JUPITER'
filename_sat = 'SATURN.aei'
titlename_sat = 'SATURN'
filename_ura = 'URANUS.aei'
titlename_ura = 'URANUS'
filename_nep = 'NEPTUNE.aei'
titlename_nep = 'NEPTUNE'

methodused = 'BS'
ts = 25 # time step


t_mer  = np.loadtxt(filename_mer, usecols=(0), skiprows=4)
x_mer  = np.loadtxt(filename_mer, usecols=(3), skiprows=4)
y_mer  = np.loadtxt(filename_mer, usecols=(4), skiprows=4)
z_mer  = np.loadtxt(filename_mer, usecols=(5), skiprows=4)

t_ven  = np.loadtxt(filename_ven, usecols=(0), skiprows=4)
x_ven  = np.loadtxt(filename_ven, usecols=(3), skiprows=4)
y_ven  = np.loadtxt(filename_ven, usecols=(4), skiprows=4)
z_ven  = np.loadtxt(filename_ven, usecols=(5), skiprows=4)

t_ear  = np.loadtxt(filename_ear, usecols=(0), skiprows=4)
x_ear  = np.loadtxt(filename_ear, usecols=(3), skiprows=4)
y_ear  = np.loadtxt(filename_ear, usecols=(4), skiprows=4)
z_ear  = np.loadtxt(filename_ear, usecols=(5), skiprows=4)

t_mars  = np.loadtxt(filename_mars, usecols=(0), skiprows=4)
x_mars  = np.loadtxt(filename_mars, usecols=(3), skiprows=4)
y_mars  = np.loadtxt(filename_mars, usecols=(4), skiprows=4)
z_mars  = np.loadtxt(filename_mars, usecols=(5), skiprows=4)

t_jup  = np.loadtxt(filename_jup, usecols=(0), skiprows=4)
x_jup  = np.loadtxt(filename_jup, usecols=(3), skiprows=4)
y_jup  = np.loadtxt(filename_jup, usecols=(4), skiprows=4)
z_jup  = np.loadtxt(filename_jup, usecols=(5), skiprows=4)

t_sat  = np.loadtxt(filename_sat, usecols=(0), skiprows=4)
x_sat  = np.loadtxt(filename_sat, usecols=(3), skiprows=4)
y_sat  = np.loadtxt(filename_sat, usecols=(4), skiprows=4)
z_sat  = np.loadtxt(filename_sat, usecols=(5), skiprows=4)

t_ura  = np.loadtxt(filename_ura, usecols=(0), skiprows=4)
x_ura  = np.loadtxt(filename_ura, usecols=(3), skiprows=4)
y_ura  = np.loadtxt(filename_ura, usecols=(4), skiprows=4)
z_ura  = np.loadtxt(filename_ura, usecols=(5), skiprows=4)

t_nep  = np.loadtxt(filename_nep, usecols=(0), skiprows=4)
x_nep  = np.loadtxt(filename_nep, usecols=(3), skiprows=4)
y_nep  = np.loadtxt(filename_nep, usecols=(4), skiprows=4)
z_nep  = np.loadtxt(filename_nep, usecols=(5), skiprows=4)

N = len(t_ear)
print(N)

'''
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

errorx = np.zeros(N)
plotn = np.zeros(N)
#logn = np.zeros(N)
for i in range(1, N):
    errorx[i] = math.log10(abs(my_x[i] - x[i]/x[i]))
    plotn[i] = math.log10(i)
    #logn[i] = math.log10(i)

print(errorx)

fig = plt.figure(figsize = (7, 5), dpi = 500, facecolor='white')
ax2 = fig.add_subplot(1, 1, 1)
ax2.plot(plotn[1:], errorx[1:], 'b-', label='x error')
ax2.set_xlabel("log (N)", fontsize = 13)
ax2.set_ylabel("log (x error)", fontsize = 13)
ax2.set_title(f"Relative error, {methodused} method")
ax2.legend()
plt.savefig(f"Relative error, {methodused} method")
plt.close()


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
plt.savefig(f'{titlename}_{methodused}.png')
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
plt.savefig(f'{titlename_cen}_{methodused}.png')
plt.close()
'''

# The x-y plot
'''
x = coord_change(x, x_cen, N)
y = coord_change(y, y_cen, N)
z = coord_change(z, z_cen, N)
x_cen = coord_change(x_cen, x_cen, N)
y_cen = coord_change(y_cen, y_cen, N)
z_cen = coord_change(z_cen, z_cen, N)

x_plot = np.zeros(N)
y_plot = np.zeros(N)
z_plot = np.zeros(N)
x_cen_plot = np.zeros(N)
y_cen_plot = np.zeros(N)
z_cen_plot = np.zeros(N)

for i in range(N):
    x_plot[i] = float(x[i])
    y_plot[i] = float(y[i])
    z_plot[i] = float(z[i])
    x_cen_plot[i] = float(x_cen[i])
    y_cen_plot[i] = float(y_cen[i])
    z_cen_plot[i] = float(z_cen[i])
'''
startpoint = 0
endpoint = N
#print(x_plot, y_plot)
fig = plt.figure(figsize = (5, 5), dpi = 500, facecolor='white')
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(x_mer[startpoint:endpoint], y_mer[startpoint:endpoint], 'b-', label=titlename_mer, linewidth=0.5)
ax1.plot(x_ven[startpoint:endpoint], y_ven[startpoint:endpoint], 'g-', label=titlename_ven, linewidth=0.5)
ax1.plot(x_ear[startpoint:endpoint], y_ear[startpoint:endpoint], 'k-', label=titlename_ear, linewidth=0.5)
ax1.plot(x_mars[startpoint:endpoint], y_mars[startpoint:endpoint], 'r-', label=titlename_mars, linewidth=0.5)
#ax1.plot(x_jup[startpoint:endpoint], y_jup[startpoint:endpoint], 'c-', label=titlename_jup)
#ax1.plot(x_sat[startpoint:endpoint], y_sat[startpoint:endpoint], 'b-', label=titlename_sat)
#ax1.plot(x_ura[startpoint:endpoint], y_ura[startpoint:endpoint], 'k-', label=titlename_ura)
#ax1.plot(x_nep[startpoint:endpoint], y_nep[startpoint:endpoint], 'g-', label=titlename_nep)
ax1.set_xlabel("x", fontsize = 13)
ax1.set_ylabel("y", fontsize = 13)
#ax1.set_xlim([-50, 50])
#ax1.set_ylim([-50, 50])
ax1.set_title(f"Position, {methodused} method")
#ax1.grid()
ax1.legend()
plt.tight_layout()
#plt.savefig(f"{titlename}_{methodused}_ts{ts}_full.png")
#plt.savefig(f"{titlename}_{methodused}_ts{ts}.png")
plt.savefig(f"solar_system_inner_{methodused}_xy.png")
#plt.savefig(f"{titlename}_{methodused}_xy_full.png")
plt.close()

'''
# use the transformation
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
    x_plot[i] = float(x[i])
    y_plot[i] = float(y[i])
    z_plot[i] = float(z[i])
    x_cen_plot[i] = float(x_cen[i])
    y_cen_plot[i] = float(y_cen[i])
    z_cen_plot[i] = float(z_cen[i])
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
#plt.savefig(f"{titlename}_{methodused}_ts{ts}_full.png")
#plt.savefig(f"{titlename}_{methodused}_ts{ts}.png")
plt.savefig(f"{titlename}_{methodused}_xy.png")
#plt.savefig(f"{titlename}_{methodused}_xy_full.png")
plt.close()
'''