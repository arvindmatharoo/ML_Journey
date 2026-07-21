import numpy as np 
arr1 = np.array([[1,2,4],[4,59,6],[74,8,9]])
inv = np.linalg.inv(arr1)
#for inverse = inv = np.linalg.inv(name of array)
#for determinant = det = np.linalg.det(name of array)
#for trace (sum of diagnols) = arr1.trace()
#for diagnol elements use arr1.diagonal()
#for eigen values eig = np.linalg.eig(name of the array)
#for norm of matrix norm = np.linalf.norm(name of the array)
#for singular value decompostion svd = np.linalg.svd(name of the array)
# for transpose of matrix use arr1.T
# for matrix multiplication use arr1 @ arr2 or dot(arr1,arr2)
# for matrix addition use arr1 + arr2
# for matrix subtraction use arr1 - arr2
# for matrix size arr1.size()
# for shape of matrix arr1.shape().

print(arr1.trace())
print(arr1.diagonal())
print(inv)