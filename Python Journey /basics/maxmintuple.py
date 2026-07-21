tuples =[(1,5),(2,10),(3,3)]
max_tuple = max(tuples,key = lambda  x: x[0])
min_tuple = min(tuples,key = lambda x:x[0])
print(max_tuple)
print(min_tuple)