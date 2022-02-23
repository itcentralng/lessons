"""
Q1: Fruits = ['Apples', 'Oranges', 'Bananas', 'Cashews']
    Using the fruits list perform the following operations:
      (a) Use the append method to add the following to the end of the list:
            Mangoes, Berries, Watermelons
      (b) Use the insert method to add Guavas, Pineapples at index 5 and 3 respectively
      
      (c) Use the insert method to repeat all the fruits at random
          indexes and find the index of all the last repeated items in the list

Q2: List all the methods available in the list class with explanation and an example.
"""

print('Kassandrah')
# # Q1:(a) Use the append method to add the following to the end of the list:
#             Mangoes, Berries, Watermelons

Fruits = ['Apples', 'Oranges', 'Bananas', 'Cashews']
Fruits.append('Mangoes')
Fruits.append('Berries')
Fruits.append('Watermelons')
print(Fruits)

# (b) Use the insert method to add Guavas, Pineapples at index 5 and 3 respectively

Fruits.insert(4,'Guavas')
Fruits.insert(3,'Pineapples ')
print(Fruits)


 #   (c) Use the insert method to repeat all the fruits at random
 #       indexes and find the index of all the last repeated items in the list

Fruits.insert(10,'apples')
Fruits.insert(11,'Oranges')
Fruits.insert(12,'Bananas')
Fruits.insert(13,'Pineapples')
Fruits.insert(14,'Cashews')
Fruits.insert(15,'Mangoes')
Fruits.insert(16,'Guavas')
Fruits.insert(17,'Berries')
Fruits.insert(18,'watermelons')
print(Fruits)

print(Fruits.index('apples',9))
print(Fruits.index('Oranges',9))
print(Fruits.index('Bananas',9))
print(Fruits.index('Pineapples',9))
print(Fruits.index('Cashews',9))
print(Fruits.index('Mangoes',9))
print(Fruits.index('Guavas',9))
print(Fruits.index('Berries',9))
print(Fruits.index('watermelons',10))


# Q2: List all the methods available in the list class with explanation and an example.
# list methods

# i. extend() 
print('the extend method works by taking a list or any other iterable and adds it to an already existing list an example is seen below')
grapes = ['red','purple']
wine= [1, 2, 3, 4, 5]
grapes.extend(wine)
print(grapes)

# ii reverse()
print('the reverse method, gives back the list from the end to the beginning. an example is')
grades = ['A', 'B','C', 'D', 'E' ]
grades.reverse()
print(grades)
print(grades.index('A'))

# sort()
print('the sort method returns the list in an alphabetical order an example is'
)
item = ['water', 'fruits', 'foods', 'fries']
item.sort()
print(item)

# append()
print('the append method helps us add to the end of a list an example is')
item.append('salads')
print(item)

# clear()
print('the clear method helps you remove all the items in your list and returns an empty list')
item.clear()
print(item)

# copy()
print('copy returns a copy of an already existing list an example is')
p = item.copy()
print(p)

# count()
print('count helps us return the number of times a value appears in a list an example')
print(grades.count('A'))

# index()
print('idex helps us confirm if a item exist in a list and returns its position an example')
print(grades.index('D'))

# insert()
print('insert helps us add a new item to a list ,specifying where we want it')
newgrade = grades.insert(-1,'F')
print(grades)

# pop()
print('pop helps us remove a value from the list using the index of the item and can return the value removed an example is')
d= grades.pop(-2)
print(d)

# remove()
print('remove helps us remove an item from a list using the value of the item')
grades.remove('E')
print(grades)