#Imports
import random
#

#Inital Conditions Setup
from math import sqrt, sin, cos, pi

import plotly
import scipy.constants
from mpmath import ln10
from scipy.constants.constants import epsilon_0
from sympy.functions import ln

random.seed(42)
phi = []
theta = 90
Z = 79
E = 7.76e3*scipy.constants.e
sigma = scipy.constants.value('Bohr radius')
x = []
y = []
count = 0
#

#Random Number List Generation
def Gausian():
    z =random.random()
    r =sqrt(-2*sigma**2*ln(1-z))
    phi = 2*pi*random.random()
    x.append(r*cos(phi))
    y.append(r*sin(phi))


for i in range (0,10000):
    Gausian()
    b = sqrt(x[i] * x[i] + y[i] * x[i])
    if b < ((Z * scipy.constants.e ** 2) / (2 * pi * epsilon_0 * E)):
        count += 1
    print(i)
x.pop(0)
y.pop(0)
trace = plotly.graph_objs.Scatter(x = x,y = y,mode = 'markers')
data = [trace]
plotly.offline.plot(data,filename = 'Scatter.html')
print(count)