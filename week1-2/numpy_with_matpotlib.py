import numpy as np
from matplotlib import pyplot as plt
def linear_funtion():
    x = np.arange(3, 10)
    y = 4 * x + 3
    plt.title("linear funtion")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.plot(x, y)
    plt.show()

def sphere():
    x=np.arange(-10,10,0.01)
    y=x**2
    plt.title("sphere")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.plot(x,y)
    plt.show()
sphere()
def cosin():
    x=np.arange(-10,10,0.01)
    y=np.cos(x)
    plt.title("sphere")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.plot(x, y)
    plt.show()
cosin()

