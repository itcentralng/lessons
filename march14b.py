"CONDITIONALS"

# What are conditional statements?
# A conditional statement is a statement that is used to determine whether a block of code should be executed or not.

# Example:
# if statement
# if <condition>:
#   <block of code>

mohdsage = 15

if mohdsage > 18:
    print("you can vote")

if mohdsage < 18:
    print("you can't vote")

fruits = ['apple', 'banana', 'orange', 'pineapple', 'mango']

if 'apple' in fruits:
    print("you have an apple")

if fruits[0] == 'apple':
    print("the first index has an apple")

if len(fruits) >= 5:
    print("you have 5 fruits or more")

if 'cashew' not in fruits:
    fruits.insert(2, 'cashew')
    print(fruits)

if 'cashew' in fruits:
    fruits.pop(2)
    print(fruits)

if 'apple' in fruits:
    fruits.remove('apple')
    print(fruits)

name = ''
age = 15

if name and age:
    print(name, age)

if 1 and 1 and 1 and 1:
    print(name, age)


"""
Assignment

Q1: 
    (a) Create a list of 10 decimals ensure the last decimal is less than 10.
        Use a conditional statement to determine whether the last decimal is less than 10.
        If it is, add a new decimal to the last that is exactly 0.9 points greater than the last one.
    (b) Use a conditional statement and indexing to print out all the decimal numbers that are greater than 5.8
    (c) Finally, remove the newly added decimal using a conditional statement and a list method

Q2: students = [{'name':'Hassan Usman', 'age':15, 'voterStatus':''}]
    using the students list above answer the following questions.
    (a) Populate the list with 4 more students using the appropraite list method(s)
    (b) Use a conditional statement to update the voterStatus of each student taking the voting age as 18 years.

"""

print('kassandrah')

deck = [1.1, 20.1, 3.4,7.5 , 5.6, 8.9, 1.2, 6.9, 2.5, 5.1]
if deck[-1]<10: 
    print('the last decimal is indeed less than 10/n')
    deck.append(6.0)
    print(deck)

a=deck[1]
b=deck[3]
c=deck[5]
d=deck[7]
if a >5.8 and b >5.8 and c>5.8 and d>5.8:
    print(a,b,c,d)


if deck[-1]==5.1:print(deck.remove(deck[-1]))
print(deck)

print ('number 2')

students = [{'name':'Hassan Usman', 'age':15, 'voterStatus':''}]
students. append({'name':'jam jam','age':17,'votestatus':''})
students. append({'name':'jamila','age':16,'votestatus':''})
students. append({'name':'james A','age':13,'votestatus':''})
students. append({'name':'jami jami','age':14,'votestatus':''})
# print(students)


age1=students[0].get('age') 
age2=students[1].get('age')
age3=students[2].get('age')
age4=students[3].get('age')
# print(age1,age2,age3,age4)
if age1 <18:
    print(f"you are underaged {students[0].get('name')}")
if age2 <18:
    print(f"you are underaged {students[1].get('name')}")
if age3 <18:
    print(f"you are underaged {students[2].get('name')}")
if age4 <18:
    print(f"you are underaged {students[3].get('name')}")

"""
print ("usman")
#Q1a
list = [0.1,0.2,6.8,0.4,7.5,0.6,8.7,0.8,7.9,-11.9]
if list[-1] < 10:
    print( ' the Decimal is less than 10')
    list.append(0.9)
    print(list)
number = 5.8
#Q1b
for index in list:
    if (index>=number):
        print(index)
        
#Q1c 
list = [0.1,0.2,6.8,0.4,7.5,0.6,8.7,0.8,7.9,-11.9,0.9]
list.remove(0.9)
print(list)

#Q2a
students = [{'name':'Hassan Usman', 'age':15,'voterStatus':''},
            {'name':'Kabiru Ali', 'age':16, 'voterStatus':''},
                {'name':'fatima Abubakar', 'age':13, 'voterStatus':''},
                    {'name':'Aisha Abdul', 'age':17, 'voterStatus':''},
                        {'name':'jamil musa', 'age':19, 'voterStatus':''}] 

print(students)
"""