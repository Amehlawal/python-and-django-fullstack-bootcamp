# create a list

myList = [1, 2, 3, 4, 5]
myList1 = [1, 2, 3, 'a', 'b', ['a', 'b',],]

print(myList)
print(len(myList))
print(myList1[0], myList[:3])
myList[0] = 100
print(myList)

myList1.append(100)

print(myList1)

listtwo = ['x', 'y', 'z']
myList1.extend(listtwo)

print(myList1)

item = myList1.pop(0)
print(item)

# others include the sort, reverse

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# list comprehension
first_col = [x[0] for x in matrix]

print(first_col)
