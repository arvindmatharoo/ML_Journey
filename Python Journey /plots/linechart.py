import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y,color = "pink")
plt.xlabel("X axis")
plt.ylabel("y axis")
plt.title("line chart")
plt.show()