# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 08:48:45 2023

@author: Daniel Skrabacz

1-D Heat diffusion problem in semi-infinite bar
Electrical Resistance and cross sectional area analysis

"""

#%% Import Libraries

import math
import numpy as np
import matplotlib.pyplot as plt

#%% Define Functions

def tempDiff(x,t,zeta, T0= 1673-273.15):
    num = x
    den = 2*np.sqrt(zeta*t)
    term = num/den
    return T0*(1 - math.erf(term))+273.15

def diffusivity(lam, rho, Cp):
    return lam/(rho*Cp)

def deltaHeat(c,m, deltaT):
    return c*m*deltaT

def csaHC(OD, ID):
    """
    

    Parameters
    ----------
    OD : outer diameter
    ID : inner diameter

    Returns
    -------
    Cross sectional Area of a Hollow Cylinder

    """
    radius_inner = ID/2
    radius_outer = OD/2
    return np.pi*(radius_outer**2 - radius_inner**2)

def findRes(length, csa, rho = 1.77e-8):
    """
    

    Parameters
    ----------
    rho : electrical resistivity, default is copper - ohm*meter
    length : Put in the length of the metal in meters
    csa : cross sectional area. put in meters^2

    Returns
    -------
    Resistance

    """
    return rho*length/csa


#%% Calculate and plot temperature profiles along semi-infinite bar


x = np.linspace(0, 10e-6, num = 1000)
t_1 = 1e-6
t_10 = 10e-6
t_20 = 20e-6
t_50 = 50e-6
t_80 = 80e-6
t_100 = 100e-6
zeta = 4e-7
my_temp1 = [tempDiff(i,t_1,zeta) for i in x]
my_temp10 = [tempDiff(i,t_10,zeta) for i in x]
my_temp100 = [tempDiff(i,t_20,zeta) for i in x]
my_temp500 = [tempDiff(i,t_50,zeta) for i in x]
my_temp1000 = [tempDiff(i,t_80,zeta) for i in x]
my_temp5000 = [tempDiff(i,t_100,zeta) for i in x]

plt.plot(x,my_temp1)
plt.plot(x,my_temp10)
plt.plot(x,my_temp100)
plt.plot(x,my_temp500)
plt.plot(x,my_temp1000)
plt.plot(x,my_temp5000)
plt.xlabel("Distance (meters)")
plt.ylabel("Temperature (K)")
plt.title('1-D Diffusion')
# plt.legend([my_temp1, my_temp10, my_temp100, my_temp500, my_temp1000, my_temp5000],['1us', '10us', '100us', '500us', '1ms', '5ms'],loc='upper right')


#%% Resistance and CSA analysis
# lengths in meters. Areas in square meters

length = 0.0508

csa3 = csaHC(0.014,0.007) # need to convert this answer to meters
csa3 = 2.979439977093287099e-7 # answer was converted in google
print(findRes(length, csa3))
