import matplotlib.pyplot as plt 
import numpy as np 
labels = ['Apples','bananas','cherries','date']
sizes = [30,20,25,22]
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title(" pie chart")
plt.xlabel("x axis")
plt.ylabel("y axis ")
plt.show()