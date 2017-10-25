from math import sqrt


def Sigma (x):
    a = 0
    meanx = float(sum(x)/len(x))
    for i in range (1,len(x)+1):
        a += (x(i)-meanx)**2
    a = a/(len(x)-1)
    sigma = sqrt(a)
    return sigma

