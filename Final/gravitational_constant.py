G=6.67408e-11 #m^3/kg/s^2
Ms=1.98e30
AU=1.5e8


G_au_ms_hr=(G*Ms*3600*3600)/((1000*AU)*(1000*AU)*(1000*AU))
G_au_ms_day=G_au_ms_hr*24*24
G_au_ms_year=G_au_ms_day*365*365

G_cgs=G*1e3

'''
print("G in the unit of AU, solar mass, hr=",G_au_ms_hr,"\n",
      "G in the unit of AU, solar mass, day=",G_au_ms_day,"\n",
      "G in the unit of AU, solar mass, year=",G_au_ms_year,"\n",
      "G in the unit of cm, g, s=",G_cgs,"\n")
'''