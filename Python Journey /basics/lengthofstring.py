string = "alphabetical" #with function
str1 = len(string)
print(str1)
def finlen(str): #without function
    counter = 0 
    for i in str:
        counter += 1
    return counter
str = "geeks"
print(finlen(str))