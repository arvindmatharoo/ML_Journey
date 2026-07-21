def swap(list):
    newlist[0],newlist[-1] = newlist[-1],newlist[0]
    return newlist
newlist = [12,34,35,56,11]
print(swap(newlist))