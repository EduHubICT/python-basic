#List_Operations

#Simple List
list1=[1, 2, 3,'Rijvi', 4, 5]
print(list1)

#Appends a new element to the end of the list
list1.append(6)
print(list1)

# Appending a list to another list
list2=[7,8]
list1.append(list2)
print(list1)
print(list1[6])

# Extend list by appending all elements from list2
list1.extend(list2)
print(list1)

#List Concatanations
print(list2+[9,10]+['Zaman'])

# insert 5 at position 5
list1.insert(5, 5)
print(list1)