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

