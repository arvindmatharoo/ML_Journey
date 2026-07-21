import matplotlib.pyplot as plt
plt.figure(figsize = (10,8))
x =[1,2,3,4,5]
y = [18,33,24,22,33]
plt.subplot(2,2,1)
plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Line chart")


x1 = [1,2,3,4,5]
y1 = [33,11,43,55,66]
plt.subplot(2,2,2)
plt.bar(x1,y1)
plt.xlabel("X axis")
plt.ylabel("Y label")
plt.title("Bar graph")


x2 = [1,2,3,4,5]
y2 = [22,33,44,55,66]
plt.subplot(2,2,3)
plt.scatter(x2,y2)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Scatter chart ")
plt.show()