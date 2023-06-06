import numpy as np
import matplotlib.pyplot as plt


## Taylor Series for an exponential function

def expTaylor(x,x0,nmax):
    'Taylor Series of an exponential function'
    # x: argument
    # x0: argument at which the derivatives will be calculated
    # nmax: n at which the series will terminate

    t=0
    for n in range(nmax+1):
        t = t + (np.exp(x0) * (x-x0)**n)/np.math.factorial(n)
    return t

expTaylor(1,0,10)

# plots of expTaylor at different arguments
x_list = np.linspace(-5,10,100)
nmax = 10

plt.xlabel('x')
plt.ylabel('y')
plt.title("Exponential Function - Taylor Series with " +str(nmax) +" Terms")
plt.scatter(x_list, np.exp(x_list), color='black')
plt.plot(x_list, expTaylor(x_list,0,nmax), color='blue')
plt.plot(x_list, expTaylor(x_list,1,nmax), color='pink')
plt.plot(x_list, expTaylor(x_list,-3,nmax), color='green')
plt.plot(x_list, expTaylor(x_list,3,nmax), color='orange')
plt.ylim([0,60])
plt.legend(['exponential function','x0=0','x0=1','x0=-3','x0=3'])
plt.show()
