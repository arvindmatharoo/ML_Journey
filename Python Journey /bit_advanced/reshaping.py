import numpy as np 
arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr1.reshape(2,3,2)
print(newarr)

#for unknown number of times
print()
print()

arr2 = np.array([12,3,4,1,2,3,4,5])
newaar = arr2.reshape(2,2,-1)
print(newaar)


print()
print()
print()

#reshaping many dimension into 1 
arr3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12,],[13,14,15,16]])
print(arr3)
newarr3 = arr3.flatten() # or we can use newarr3 = arr.reshape()
print(newarr3)