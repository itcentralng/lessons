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

print("\n\n\n\n")

print("Kabir")
# Q(a)
Shoppinglist =['cake cashew gum']
shoppinglist.upper()

# Q(b)
fruit=['cake','cashew','gum']
fruit[1] ='Gum'
fruit[2] = 'cashew'
print(fruit)
['cake', 'Gum', 'cashew']

# Q2
people=['Hassan', 'Adama', 'Bishir', 'saleh', 'Clement']
ages=[10, 15, 16, 17, 95]
iT='Hello',people[0],'is',ages[0],'years old'
('Hello', 'Hassan', 'is', 10, 'years old')


print("USMAN")

shoppinglist = ['cake', 'cashew', 'gum']

new_list = []
for name in shoppinglist:
        new_name = name.upper()
        new_list.append(new_name)
print("befor",shoppinglist)     
print("after",new_list)

print(" ")
print("shoppinglist Befor Swapping",shoppinglist)
shoppinglist = ['cake', 'cashew', 'gum']
shoppinglist[1],shoppinglist[-1]=shoppinglist[-1],shoppinglist[1]
print("shoppinglist after Swapping",shoppinglist)