import matplotlib.pyplot as plt 
#basic plotting
# x = [1,2,5,18]
# plt.plot(x)
# plt.show()


#plotting x and y against each other 
# y = [7,12,11,22]
# plt.plot(x,y)
# plt.show()

#better graph 

x = [3,9,14]
y = [2,7,38]

# plotting x and y
plt.plot(x,y, c="red",linewidth=2,label="Line1")
x2 = [1,15,18]
y2 = [0,3,12]
plt.plot(x2,y2,c="green",linewidth = 2 , label ="Line 2", linestyle = "dashed",
marker = 'o',markerfacecolor="orange",markersize = 10)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("two lines!")

#limits of the axis
plt.ylim(1,10)
plt.xlim(0,30)

#show the legends
plt.legend()
plt.show()
