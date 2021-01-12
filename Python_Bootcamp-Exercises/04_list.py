myList = [1,2,3]
myList = ['STRING',100,23.2]
print(len(myList))
myList = ['one','two','three']
print(myList[0])
print(myList[1:])

# combine list
another_list =['four','five']
joinList = myList + another_list
print(joinList)

# changing the first element
joinList[0] = 'ONE'
print(joinList)

# + element in the end of your list
joinList.append('SIX')
print(joinList)

# - elements in the end of your list
joinList.pop()
print(joinList)

# to save as removed
popped_item = joinList.pop()
print(joinList)

# to remove a element in the begining of the list
joinList.pop(0)
print(joinList)

# to sort the list (organizing alphabetical order)
new_list =['a','e', 'x','b','c']
num_list =[4,1,8,3]
new_list.sort()
print(new_list)
print(new_list)

# to reserve the list (opposite way)
new_list.reverse()
print(new_list)

