list1 = [1,2,3]
list2 = list1.copy() #Return a shallow copy of the list.

list2[0] = 100
print(list1, list2)

