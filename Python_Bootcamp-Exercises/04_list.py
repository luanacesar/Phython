myList = [1,2,3]
myList = ['STRING',100,23.2]
print(len(myList))
myList = ['one','two','three']
print(myList[0])
print(myList[1:])
another_list =['four','five']

joinList = myList + another_list
print(joinList)

joinList[0] = 'ONE'
print(joinList)

# add element in the end of your list
joinList.append('SIX')
print(joinList)

# remove elements in the end of your list
joinList.pop()
print(joinList)