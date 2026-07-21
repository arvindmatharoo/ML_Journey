def min(a,b):#using function 
    if a <= b :
        return b
    else : 
        return a 
a = 2 
b = 3 
print(min(a,b))
# using ternary 
a = 2 
b = 4 
print(b if a<=b else a)