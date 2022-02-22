"""

Q1: shoppinglist = ['cake', 'cashew', 'gum']
    Using the above list, execute the following:
    (a) Convert individual items in the list to capital letters such that when I call the 
        list I get all the items like this ['CAKE', 'CASHEW', 'GUM']
    (b) Switch the positions of 'gum' and 'cashew' such that when the list is called it returns ['cake', 'gum', 'cashew']

Q2: ages = [10, 15, 16, 17. 95]
    people = ['Hassan', 'Adama', 'Bishir', 'Saleh', 'Clement']
    
    using the ages and people list write a code that prints out each person with their appropraite age for example: 
    'Hassan is 10 years old' should be printed in the case of Hassan and 10
"""
print('Kassandrah')

from ssl import PEM_FOOTER


shoppinglist = ['cake', 'cashew', 'gum']

sl = shoppinglist[0]

y= sl.swapcase()

sl1 =shoppinglist[1]

x = sl1.swapcase()

sl2 = shoppinglist[2]

z= sl2.swapcase()

finallist = [y,x,z]

print(finallist)

finallist2 = [y,z,x]

print(finallist2)


# q2

ages = [10, 15, 16, 17, 95]
people = ['Hassan', 'Adama', 'Bishir', 'Saleh', 'Clement']
# for age in ages
print('{} is {} years old'.format(people[0],ages[0]))

print('{} is {} years old'.format(people[1],ages[1]))

print('{} is {} years old'.format(people[2],ages[2]))

print('{} is {} years old'.format(people[3],ages[3]))

print('{} is {} years old'.format(people[4],ages[4]))
