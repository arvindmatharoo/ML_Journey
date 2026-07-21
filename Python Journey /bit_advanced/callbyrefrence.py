def swap_lists(lst1,lst2):
    lst1[:],lst2[:]=lst2[:],lst1[:]
    print("after swapping",lst1,lst2)
list1 = [1,2,3,4]
list2 = [5,6,7,8]
print("before swapping",list1,list2)
swap_lists(list1 , list2 )