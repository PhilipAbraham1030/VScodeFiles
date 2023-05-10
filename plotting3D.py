import numpy as np
import matplotlib.pyplot as plt

# Single Point
ax = plt.axes(projection='3d')
ax.scatter(3,5,7)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Single Point')
plt.show()

# Scatter Plot
ax = plt.axes(projection='3d')

x_data = np.random.randn(1,5000)
y_data = np.random.randn(1,5000)
z_data = np.random.randn(1,5000)

ax.scatter(x_data,y_data,z_data,alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Scatter Plot - random normal distribution numbers, mean=0.0, std dev =1.0, one row of 5000 points')
plt.show()

#############################################
ax = plt.axes(projection='3d')

x_data = np.random.normal(loc=2.0,scale=0.5,size=(1,5000))
y_data = np.random.normal(loc=2.0,scale=0.5,size=(1,5000))
z_data = np.random.normal(loc=2.0,scale=0.5,size=(1,5000))

ax.scatter(x_data,y_data,z_data,alpha=0.3,marker='v', color='green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Scatter Plot - random normal distribution numbers, mean=2, std dev =0.5, one row of 5000 points')
plt.show()

# plot  3d functions
x_list = np.arange(-50,51,0.1)
y_list = np.arange(-50,51,0.1)
z = np.sin(x_list) + np.cos(y_list)

ax=plt.axes(projection='3d')
plt.plot(x_list,y_list,z)
ax.set_title('3d trig Function')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

# Surface Plots
ax = plt.axes(projection='3d')

xn = np.arange(-5,5,0.1)
yn = np.arange(-5,5,0.1)
X,Y = np.meshgrid(xn,yn)

Zn = np.sin(X) + np.cos(Y)

ax.plot_surface(X,Y,Zn, cmap='plasma')
ax.set_title('3d Function Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# ax.view_init(azim=86, elev=90) # fix viewing perspective
plt.show()


# Parametric Plots
zp = np.linspace(-100,100,500)
xp = zp*np.cos(zp)
yp = zp*np.sin(zp)

xc = np.linspace(-100,100,500)
yc = np.linspace(-100,100,500)
X,Y = np.meshgrid(xc,yc)
Zp = np.sqrt(X**2 + Y**2) #Surface plot
Zn = -1*np.sqrt(X**2 + Y**2) #Surface plot

ax = plt.axes(projection='3d')
ax.plot(xp,yp,zp)
ax.plot_surface(X,Y,Zp, cmap='binary',alpha=0.4)
ax.plot_surface(X,Y,Zn, cmap='binary',alpha=0.4)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Parametric Curve')
plt.show()


