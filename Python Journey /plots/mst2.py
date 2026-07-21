import matplotlib.pyplot as plt
classes = ['class1','class2','class3','class4','class5']
boys_weights = [50,90,80,75,70]
girls_weight = [40,50,75,60,45]
plt.bar(classes,boys_weights, width = 0.234 , color = 'blue',align = 'center',label = 'boys')
plt.bar(classes,girls_weight,width = 0.234 , color = 'red',align = 'edge',label = 'girls')
plt.title("class wise weight of girls and boys")
plt.ylabel("average weight")
plt.xlabel("class")
plt.legend()
plt.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          