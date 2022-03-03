# """
# Q1: Fruits = ['Apples', 'Oranges', 'Bananas', 'Cashews']
#     Using the fruits list perform the following operations:
#       (a) Use the append method to add the following to the end of the list:
#             Mangoes, Berries, Watermelons
#       (b) Use the insert method to add Guavas, Pineapples at index 5 and 3 respectively
      
#       (c) Use the insert method to repeat all the fruits at random
#           indexes and find the index of all the last repeated items in the list

# Q2: List all the methods available in the list class with explanation and an example.
# """

# print('Kassandrah')
# # # Q1:(a) Use the append method to add the following to the end of the list:
# #             Mangoes, Berries, Watermelons

# Fruits = ['Apples', 'Oranges', 'Bananas', 'Cashews']
# Fruits.append('Mangoes')
# Fruits.append('Berries')
# Fruits.append('Watermelons')
# print(Fruits)

# # (b) Use the insert method to add Guavas, Pineapples at index 5 and 3 respectively

# Fruits.insert(4,'Guavas')
# Fruits.insert(3,'Pineapples ')
# print(Fruits)


#  #   (c) Use the insert method to repeat all the fruits at random
#  #       indexes and find the index of all the last repeated items in the list

# Fruits.insert(10,'apples')
# Fruits.insert(11,'Oranges')
# Fruits.insert(12,'Bananas')
# Fruits.insert(13,'Pineapples')
# Fruits.insert(14,'Cashews')
# Fruits.insert(15,'Mangoes')
# Fruits.insert(16,'Guavas')
# Fruits.insert(17,'Berries')
# Fruits.insert(18,'watermelons')
# print(Fruits)

# print(Fruits.index('apples',9))
# print(Fruits.index('Oranges',9))
# print(Fruits.index('Bananas',9))
# print(Fruits.index('Pineapples',9))
# print(Fruits.index('Cashews',9))
# print(Fruits.index('Mangoes',9))
# print(Fruits.index('Guavas',9))
# print(Fruits.index('Berries',9))
# print(Fruits.index('watermelons',10))


# # Q2: List all the methods available in the list class with explanation and an example.
# # list methods

<<<<<<< HEAD
# # i. extend() 
# print('the extend method works by taking a list or any other iterable and adds it to an already existing list an example is seen below')
# grapes = ['red','purple']
# wine= [1, 2, 3, 4, 5]
# grapes.extend(wine)
# print(grapes)

# # ii reverse()
# print('the reverse method, gives back the list from the end to the beginning. an example is')
# grades = ['A', 'B','C', 'D', 'E' ]
# grades.reverse()
# print(grades)
# print(grades.index('A'))

# # sort()
# print('the sort method returns the list in an alphabetical order an example is'
# )
# item = ['water', 'fruits', 'foods', 'fries']
# item.sort()
# print(item)

# # append()
# print('the append method helps us add to the end of a list an example is')
# item.append('salads')
# print(item)

# # clear()
# print('the clear method helps you remove all the items in your list and returns an empty list')
# item.clear()
# print(item)

# # copy()
# print('copy returns a copy of an already existing list an example is')
# p = item.copy()
# print(p)

# # count()
# print('count helps us return the number of times a value appears in a list an example')
# print(grades.count('A'))

# # index()
# print('idex helps us confirm if a item exist in a list and returns its position an example')
# print(grades.index('D'))

# # insert()
# print('insert helps us add a new item to a list ,specifying where we want it')
# newgrade = grades.insert(-1,'F')
# print(grades)

# # pop()
# print('pop helps us remove a value from the list using the index of the item and can return the value removed an example is')
# d= grades.pop(-2)
# print(d)

# # remove()
# print('remove helps us remove an item from a list using the value of the item')
# grades.remove('E')
# print(grades)

fruits = ['oranges','berries','mango']
fruits[::2]+[fruits[1]]
fruits=[fruits[0] , fruits[2] , fruits[1]]
print(fruits)
=======
# remove()
print('remove helps us remove an item from a list using the value of the item')
grades.remove('E')
print(grades)




print("   ")
print("   ")
print("Usman")
print("(1a) Use the append method to add the following to the end of the list Mangoes, Berries, Watermelons")
print(" ")
Fruitlist = ['Apples', 'Oranges', 'Bananas', 'Cashews']
print("fruitlist Befor append",Fruitlist)
Fruitlist.append("Mangos")
Fruitlist.append("Berries")
Fruitlist.append("Watermelons")
print("fruitlist after append",Fruitlist)
print(" ")
print("(1b)Use the insert method to add Guavas, Pineapples at index 5 and 3 respectively")
print("   ")
Fruitlist = ['Apples', 'Oranges', 'Bananas', 'Cashews']
print("fruitlist B4 insert",Fruitlist)
Fruitlist.insert(3,"Pineapples")
Fruitlist.insert(5,"Guavas")
print("fruitlist after insert",Fruitlist)

print("   ")

print("(1c) Use the insert method to repeat all the fruits at random indexes and find the index of all the last repeated items in the list")
print("   ")
Fruitlist = ['Apples', 'Oranges', 'Bananas', 'Cashews','Berries','Pineapples','Mangoes','watermelons','Guavas']
Fruitlist.insert(4,"Apples")
Fruitlist.insert(1,"Pineapples")
Fruitlist.insert(7,"Bananas")
Fruitlist.insert(8,"Oranges")
Fruitlist.insert(9,"watermelons")
Fruitlist.insert(3,"Guavas")
Fruitlist.insert(12,"Berries")
Fruitlist.insert(2,"Mangoes")
Fruitlist.insert(6,"Cashews")
print(Fruitlist)
print("   ")

print(Fruitlist.index("Apples",4))
print(Fruitlist.index("Pineapples",2))
print(Fruitlist.index("Bananas",10))
print(Fruitlist.index("Oranges",6))
print(Fruitlist.index("watermelons",14))
print(Fruitlist.index("Guavas",13))
print(Fruitlist.indext("Berries",11))
print(Fruitlist.index("Mangoes",13))
print(Fruitlist.index("Cashews",3))
print("Q2: List all the methods available in the list class with explanation and an example")

print("   ")

# remove()
print('remove helps us remove an item from a list using the value of the item')
name = ("usman", "product")
name.remove('a')
print(name)

# index()
print('idex helps us confirm if a item exist in a list and returns its position an example')
print(name.index('u'))

# insert()
print('insert helps us add a new item to a list ,specifying where we want it')
product = name.insert('o','F')
print(name)

# append()
print('the append method help to add a word to the end of a list an example it will add tiko to the end of the sentance')
name.append('tiko')
print(name)

# clear()
print('the clear method helps you remove all the items in your list and returns an empty list')
name.clear()
print(name)

# pop()
print('pop helps to remove a value from the list using the index of the item and can return the value removed an example is')
tiko= name.pop(4)
print(tiko)

# count()
print('count it helps to return the number of times a value appears in a list an example')
print(name.count('usman abba usman'))

# copy()
print('copy returns a copy of items that is corently in the list an example is')
tiko = name.copy()
print(tiko)


people=['Hassan', 'Adama', 'Bishir', 'saleh', 'Clement']
ages=[10, 15, 16, 17, 95]
iT='Hello',people[0],'is',ages[0],'years old'
('Hello', 'Hassan', 'is', 10, 'years old')
>>>>>>> 979e0c6cc1c71c80e77af3ae58db71401e0c573f
