import matplotlib.pyplot as plt
import numpy as np 
data = [np.random.rand(50) for x in range(4)]
plt.boxplot(data, tick_labels=['A', 'B', 'C', 'D'])
plt.title("box plot grah")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()