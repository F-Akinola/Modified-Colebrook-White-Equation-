"""
Explicit reformulation of the Colebrook-White equation for Turbulent flow friction
factor calculation.

Equations developed by Sonnad & Goudar.
"""
#Python code: Folaranmi A. D.

import numpy as np

# pipe roughness

eD = eval(input("E / D :"))

# Reynold's number

Re = eval (input(" Re :"))

#===============================
a = 2 / np.log(10)

d =((np.log(10)) / 5.02) * Re

b = eD / 3.7

s = (b * d) + np.log(d)

q = s ** (s / (s + 1))

g = (b * d) + np.log(d / q)

z = np.log(q / g)

#solutions for ∆

#Linear approximation

DLA = (g / (g + 1)) * z

# Continued fractions approximation

NUM = z / 2

DEN = ((g + 1) ** 2)+((z / 3) * ((2 * g) - 1))

DCFA = DLA * (1 + (NUM / DEN))

#solutions for f

#Case 1: ∆ = 0

f1 = 1 / ((a * ((np.log(d/q)) + 0)) ** 2)

print ("f (∆ = 0) :", f1)

#Case 2: ∆ = ∆LA

f2 = 1 / ((a * ((np.log(d/q)) + DLA)) ** 2)

print ("f (∆ = ∆LA) :", f2)

#Case 3: ∆ = ∆CFA

f3 = 1 / ((a*((np.log(d/q))+DCFA))**2)

print ("f (∆ = ∆CFA) :", f3)

