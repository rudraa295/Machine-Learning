#it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0,1.0,1000)
y = np.random.normal(50.0,10.0,1000)
plt.scatter(x,y)
plt.show()
