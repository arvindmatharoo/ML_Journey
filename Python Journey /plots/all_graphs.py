import matplotlib.pyplot as plt 
import numpy as np
plt.figure(figsize=(10,128))
x = [1,2,3,4,5]
y = [4,5,6,7,8]
plt.subplot(3,2,1)
plt.plot(x,y)
plt.title("line chart")


x1 = np.random.rand(50)
y1 = np.random.rand(50)
plt.subplot(3,2,2)
plt.scatter(x1,y1,color = "red")
plt.title("scatter chart")


x2 = np.random.rand(100)
plt.subplot(3,2,3)
plt.hist(x2,color = "black",edgecolor = "red")
plt.title("histogram")


x3 = [30,24,35,16,27]
y3 = ['A','B','C','D','E']
plt.subplot(3,2,4)
plt.pie(x3,labels=y3 , autopct='%1.1f%%',startangle = 190)

plt.subplot(3,2,5)
plt.bar(x,y,color = 'red')



data = [np.random.rand(100)for x in range(4)]
plt.subplot(3,2,6)
plt.boxplot(data,labels = ['label1','label2','label3','label4'])
plt.show()

