import matplotlib.pyplot as plt 
import numpy as np 
data = np.random.rand(100)
plt.hist(data , color = "black" , edgecolor = "red")
plt.xlabel(" X axis")
plt.ylabel("y axis")
plt.title("histogram")
plt.show()