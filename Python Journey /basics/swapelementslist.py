def swap(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list
list = [99,3,4,2,131,3123]
pos1,pos2 = 4,5
print(swap(list,pos1-1,pos2-1))    