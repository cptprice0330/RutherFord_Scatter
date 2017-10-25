import numpy as np
import plotly

def sinc (x):
    a = (x(2-x)**11)
    fx = sins

x = np.linspace(0,2,1000)
y = (np.sin(1/(x*(2-x))))**2

trace = plotly.graph_objs.Scatter(x = x,y = y,mode = 'lines')
data = [trace]
plotly.offline.plot(trace,filename = 'MCI.html')