import matplotlib.pyplot as plt
import numpy as np 
fig,ax = plt.subplots(2,2,figsize = (10,8))
x = np.linspace(0,10,100)
y = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)
y4 = x**2 
ax[0,0].plot(x,y , color = "Red")
ax[0,0].set_title("Sine wave")
ax[0,1].plot(x,y2 , color = "black")
ax[0,1].set_title("cos wave")
ax[1,0].plot(x,y3 , color = "grey")
ax[1,0].set_title("exponential decay")
ax[1,1].plot(x,y4 , color = "blue")
ax[1,1].set_title("sqaures of x equal y ")
plt.show()