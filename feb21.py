"""
Question 1:
Create 10 list with the following criteria:
(1) A list of whole numbers
(2) A list containing names of students
(3) A list of decimal numbers
(4) A list of whole numbers and decimal numbers
(5) A list containing names of students, whole numbers and decimal numbers
(6) A list containing numbers and other lists
(7) A list containing decimal numbers and other lists
(8) A list containing names of fruits and other lists
(9) A list containing numbers and other lists
(10) A list containing numbers, names and other lists

Question 2:
Create 2 list and join them together on a third list

Question 3:
Create 2 list containing at least three items and get each item individually

NOTE: Answers should be submitted within the same file and pushed to github. Indicate your name above your answer and ensure you don't submit the same answer as your collegues.
"""
 

# Kassandrah

# (1) A list of whole numbers

whole_numbers = [1,3,5,6,8,9,40,56.78]
print(whole_numbers)

# (2) A list containing names of students
student_names = ['amrah', 'alee', 'amrah alee', 'amrah lee']
print(student_names)

# (3) A list of decimal numbers
decimal_numbers = [1.2, 3.2, 4.5,6.5, 8.0]
print(decimal_numbers)

# (4) A list of whole numbers and decimal numbers
wn_dn = [2, 4, 7, 8, 90, 3.0, 4.5, 9.0]
print(wn_dn)

# (5) A list containing names of students, whole numbers and decimal numbers
names_numbers = ['amrah', 3, 5, 60, 9.0, 50, 69.9,'kabir']
print(names_numbers)

# (6) A list containing numbers and other lists
numbers_lists = [3, 6, 8, 90, ['amrah', 'amrahlee', 6, 'onion'], ['s' 'kabir', 78, 'gift']]
print(numbers_lists)

# (7) A list containing decimal numbers and other list
decimal_list = [5.6, 6.0, 8.0, ['decimals', 'a decimal and list list', 45], ['apples', 'avocado', 'oranges']]
print(decimal_list)

# (8) A list containing names of fruits and other lists
fruits = ['apples', 'mango', 'orange', 'pears']
print(fruits)

# (9) A list containing numbers and other lists
numbers_lists = [3, 6, 8, 90, ['amrah', 'amrahlee', 6, 'onion'], ['s' 'kabir', 78, 'gifts']]
print(numbers_lists)

# (10) A list containing numbers, names and other lists
last_list = [{'numbers': [1,5,7,9]}, {'name':['amrah','kabir'],}, [],['shoes', 'knickers']]
print(last_list)

# Question 2:
# Create 2 list and join them together on a third list
fisrt_list = ['amrah', 'surename', 'police']
second_list =['apples', 'mango', 'gauve']
total_list = fisrt_list + second_list
print(total_list)

# Question 3:
# Create 2 list containing at least three items and get each item individually

shop = ['kiosk', 'shop shop', 'a shop']
print(shop[0])
print(shop[1])
print(shop[2])

names = ['kabir', 'mr teey', 'milk', 'images']
print(names[0])
print(names[1])
print(names[2])
print(names[3])


