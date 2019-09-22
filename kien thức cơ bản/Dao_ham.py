import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
x=np.linspace(0,10,1000) # chia khoảng từ 0-> 10 thàn 1000 khoảng
dx=x[1]-x[0]
y=np.sin(x)
d=np.gradient(y,dx)
plt.xlabel('x')
plt.ylabel('dao ham')
plt.plot(x,d)
plt.show()
