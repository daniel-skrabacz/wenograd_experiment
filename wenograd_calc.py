# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:21:15 2021
Performing Mesh Analysis on Wheatstone Bridge with resistor at the bridge
@author: Daniel Skrabacz
"""

#%% Import Library

from sympy import *

#%% Define symbols
# This is per my definition of the circuit

R1, R2, R3, R4, Rg, I1, I2, I3, Vs = symbols('R1, R2, R3, R4, Rg, I1, I2, I3, Vs')


#%% Define Matrices

my_matrix = Matrix(3,3, [(R1+R3), -R1, -R3, -R1, (R2+R1+Rg), -Rg, -R3, -Rg, (R3+R4+Rg)])

x = Matrix(3,1,[I1, I2, I3])

b = Matrix(3,1,[Vs, 0, 0])

#%% Take the inverse of my_matrix

inv_matrix = my_matrix.inv()

x = inv_matrix*b
print(output)
#%%
"""
Performing Mesh Analysis on Wheatstone Bridge with Voltage at bridge
"""

#%% Define symbols
# This is from Wenograd's paper
R1, R2, R3, R4, Ra, I1, I2, I3, E, Eb = symbols('R1, R2, R3, R4, Ra, I1, I2, I3, E, Eb')


#%% Define Matrices

wen_matrix = Matrix(3,3, [(Ra+R3+R4), -R3, -R4, -R3, (R1+R3), 0, -R4, 0, (R2+R4)])

wen_x = Matrix(3,1,[I1, I2, I3])

wen_b = Matrix(3,1,[Eb, E, -E])
#%% Solve for inverse and dot product
# x = b*A^-1

wen_inv = wen_matrix.inv()

wen_x = wen_inv*wen_b

print(pretty(wen_x))
#%% Solve for R1

num2 = wen_x[1]
num3 = wen_x[2]

print(solve(num2-num3, R1))

#%% Wen's formula
def wenR(Eb, R2, E, Ra):
    num = 25*Eb*R2 + 50*E*R2 + E*R2+Ra + 50*E*Ra
    den = 25*Eb - 50*E -E*Ra
    return num/den

def findR(Rref, T, Tref, alpha):
    return 

def findTemp(R,Rref,Tref,alpha):
    frac = R/(Rref*alpha)
    flip = 1/alpha
    return frac-flip+Tref

def findAlpha(T,Tref, R, Rref):
    myT = 1/(T-Tref)
    myR = (R/Rref) - 1
    alpha = myT*myR

    return alpha
