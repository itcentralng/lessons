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


print("USMAN ABBA") 
print("[1] A list of whole numbers.")
Whole_Numbers = [100,200,300,40,59,68,79]
print(Whole_Numbers)

print("[2] A list containing names of students.")
Name_Student = ['sani', 'mohammed', 'sulaiman', 'jamilu', 'usman']
print(Name_Student)

print("[3] A list of decimal numbers")
_Decimal_numbers = [3.999, 200.9, 7.0,0.5, 9.4]
print(_Decimal_numbers)

print("[4] A list of whole numbers and decimal numbers")
Dec_Whole = [50, 60, 90, 28, 4.6, 6.7, 8.0, 1.0]
print(Dec_Whole)

print("[5] A list containing names of students, whole numbers and decimal numbers")
list = ['Jamilu', "Habib", 'Musa', 1,3,6,8,0,8,9,7,9,7,"Usman"]
print(list)

print("[6] A list containing numbers and other lists")
Num_other = [70,40,60,9, ['name', 'school', 'student',]]
print(Num_other)

print("[7] A list containing decimal numbers and other list")
decimal_other = [1.5, 90.4, 0.5, ["school", "student", "book", 4, 8,], ['class', 'lecture', 'totur']]
print(decimal_other)

print("[8] A list containing names of fruits and other lists")
list_Frt = [{"frt": ['orange', 'apple', 'banana', 'coconut']},["name", 3, 4, 5, 6,"moimoi", "School"]]
print(list_Frt)

print("[9] A list containing numbers and other lists")
numbers_other = [3, 6, 8, 90, ["Studet", "families", "friend"], ['food', "meet", 100, 50.0, "go"]]
print(numbers_other)

print("[10] A list containing numbers, names and other lists")
name_num_others = ['Names'"parveen","zafreen","fatima","Rahama", "Num", 30, 6, 80, 90, 9, 'others', 4.5, "shop", "musa",3]
print(name_num_others)

print("Question 2:")
print("[] Create 2 list and join them together on a third list")
Whole_Numbers = [100,200,300,40,59,68,79]
Name_Student = ['sani', 'mohammed', 'sulaiman', 'jamilu', 'usman']
Value = Whole_Numbers + Name_Student
print(Value)

print("Question 3:")
print("[] Create 2 list containing at least three items and get each item individually")
items = ['A', 'B', 'C', 'D', 'E']
print(items[0])
print(items[1])
print(items[2])
print(items[3])
print(items[4])

print("thank you")

c = "project x"
print(c.swapcase)

v = "project y"
print(v[-1]+v[0:7])
print(v)
 

sentence = "my name is usman, i am 15 years old."
Age = 15
sentence.capitalize()
