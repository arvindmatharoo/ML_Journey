import matplotlib.pyplot as plt
import numpy as np 
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x,y,color = "Black" , marker= "s")
plt.xlabel(" x axis")
plt.ylabel("y axis")
plt.title("scatter chart")
plt.show()