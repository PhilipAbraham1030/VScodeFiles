import numpy as np
import matplotlib.pyplot as plt


## Taylor Series for an sine function

def sinTaylor(x,nmax):
    'Taylor Series of an sine function'
    # x: argument
    # nmax: n at which the series will terminate

    t=0
    for n in range(nmax+1):
        t = t + (((-1)**n)/(np.math.factorial(2*n+1)))*x**(2*n+1)
    return t

sinTaylor(np.pi/2,10)

# plots of sinTaylor at different arguments
x_list = np.linspace(-7,7,100)


plt.xlabel('x')
plt.ylabel('y')
plt.title("Taylor Series of Sine Function at x0 = 0")
plt.scatter(x_list, np.sin(x_list), color='black',label='sine function')
plt.plot(x_list, sinTaylor(x_list,nmax=3), color='blue',label='n=3')
plt.plot(x_list, sinTaylor(x_list,nmax=5), color='pink',label='n=5')
plt.plot(x_list, sinTaylor(x_list,nmax=7), color='green',label='n=7')
plt.plot(x_list, sinTaylor(x_list,nmax=10), color='orange',label='n=10')
plt.ylim([-2,2])
plt.grid()
plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
plt.show()
