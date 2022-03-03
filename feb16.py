"""
1) So far, we've treated the following methods:
    (a) capitalize
    (b) casefold
    (c) center
    (d) count
    (e) format
    (f) strip
    (g) replace
    (h) index
    (i) swapcase
    (j) join
   Write an executable python code for each of the methods above
   
2) Pick 5 string methods and explain how they work with proper executable examples
"""
'''''
# KASSANDRAH
# (1) capitalize
name = "Aisha Sani"
name.capitalize()
# (2) casefold

# kassandrah

# number 1
# capitalize

name = 'kassandrah'
print(name.capitalize())

# casefold(makes the string lower case)

name = 'Kassandrah'
print(name.casefold())

# # center
name = "kassandrah"
print(name.center(5,'x'))

# count
name = 'book'
name.count('o',0 ,-1)
print(name)

# # format
wage = 10
print('your wage is:{}'.format(wage))

# strip
name = 'book worm'
print(name.strip("book"))

# replace
name = 'book worm'
print(name.replace('book' ,'earth',1))

# index
name = 'booooook'
print(name.index('k'))

# # swapcase
name ='PEOPLE,SHOE,shoe,people'
print(name.swapcase())

# # join 
name ='PEOPLE,SHOE,shoe,people'
s ='sea'
print(name.join(s))


# number 2


# split()
# split(): the split method helps us seperate the string into a list like form
name = 'kassandrah'
print(name.split('sand')) 

# startswitch(): the start switch helps us check how a string begins. we can use this to check for passwords
line = 'Have a nice day'
print(line.startswith('Have'))
print(line.startswith('h'))

# find(): the find method helps us to determine if a segment of a string exists
word = 'banana'
print (word.find('n'))


# isdigit():this helps us comfirm if the string is a digit 
name ='kassandrah'
print(name.isdigit())


# isAlpha():this helps us confirm whether or not the string is an alphabet(charaters only)
name = 'kassandrah'
print(name.isalpha())

# len()
# length of a string(the length of a string can be determined using the len() function )
name = 'kassandrah'
print(len(name))

# slice()
# slice(): the slice method helps you print a particular segment of the string as strings are divided into segments
name = 'kassandrah'
print(name[2:5])

print ("   ")
print ("   ")

print("USMAN ASSIGNMENT")

#Capitalize
Name = 'usman Abba usman'
Name.upper
print(Name.upper())

#Casefold
Name = 'USMAN ABBA USMAN'
Name.lower
print(Name.lower())

#Center
fruth = 'banana,coconut,apple'
fruth.center
print(fruth.center(1))

#Count
items = 'banana_coconut_apple'
items.count
print(items.count('a'))

#Format
Age = 20
print('My Age is: {}'. format(Age))

#Strip
product = 'coke fanta freshyo bobo'
print(product.strip("coke"))

#Replace
school = 'fud ITcentral kadpoly'
print(school.replace('fud' ,'ABU'))

#Index
Assignment = "introduction to python"
print(Assignment.index("to"))

#Swapcase
Student = "KABIRU kassandra USMAN amrah JABIR"
print(Student.swapcase())

# join
name = "R TEEY USMAN"
K ='MU'
print(name.join(K))

print("thank you")
'''
name = ["A","B","C","D"]
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
name.append(1)
name.append(2)
print(name)

name.insert(-1,"usman",)
name.insert(0,"Abba")
print(name)

name.index("A")
name.index("D")
print(name)

name.pop(0)
name.pop(-1)
print(name)

