import ulula.setups.sedov_taylor as setup_sedov
import ulula.setups.shocktube as setup_shock
import ulula.run as ulula_run
import ulula.simulation as ulula_sim
import ulula.plots as ulula_plt
import matplotlib.pyplot as plt
import numpy as np


def func():
    return setup_shock.SetupSodX().direction()
    
   

def truesol(sim, x, qplot):
    dir = setup_shock.SetupSodX().trueSolution(sim, x, q1_plot)
    return dir

# setup the Sod shocktube problem in x-direction
#setup = setup_sedov.SetupSedov()
setup = setup_shock.SetupSodX()

# specify the hydro schemes
hs = ulula_sim.HydroScheme(reconstruction = 'const', limiter = 'minmod', riemann='hll', time_integration='euler', cfl = 0.8)
hs1 = ulula_sim.HydroScheme(reconstruction = 'linear', limiter = 'minmod', riemann='hll', time_integration='euler', cfl = 0.8)
hs2 = ulula_sim.HydroScheme(reconstruction = 'linear', limiter = 'vanleer', riemann='hll', time_integration='euler', cfl = 0.8)
hs3 = ulula_sim.HydroScheme(reconstruction = '', limiter = 'minmod', riemann='hll', time_integration='hancock', cfl = 0.8)

# run the simulation
sim = ulula_run.run(setup, hydro_scheme=hs, tmax=0.2, nx=200)
sim1 = ulula_run.run(setup, hydro_scheme=hs1, tmax=0.2, nx=200)
sim2 = ulula_run.run(setup, hydro_scheme=hs2, tmax=0.2, nx=200)
sim3 = ulula_run.run(setup, hydro_scheme=hs3, tmax=0.2, nx=200)

# plot the 2D images

q_plot = ['DN','PR']
ulula_plt.plot2d(sim, q_plot=q_plot, panel_size=5.0)
plt.savefig("Sod_img.png")


#func = setup_shock.SetupSodX().direction()

x = np.linspace(0, 1, 100)

q1_plot = ['DN', 'VX', 'PR']
print(type(q1_plot))
ulula_plt.plot1d(sim, q_plot=q1_plot, plot_type='line', 
                idir_func=func, true_solution_func=truesol)
plt.savefig("Sod_img_1d.png")

ulula_plt.plot1d(sim1, q_plot=q1_plot, plot_type='line', 
                idir_func=func, true_solution_func=truesol)
plt.savefig("Sod_img_1d_1.png")

ulula_plt.plot1d(sim2, q_plot=q1_plot, plot_type='line', 
                idir_func=func, true_solution_func=truesol)
plt.savefig("Sod_img_1d_2.png")

ulula_plt.plot1d(sim3, q_plot=q1_plot, plot_type='line', 
                idir_func=func, true_solution_func=truesol)
plt.savefig("Sod_img_1d_3.png")


