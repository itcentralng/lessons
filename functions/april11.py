# FUNCTION CONTINUATION

# from datetime import datetime

students = [
    {'name':'James Authur', 'dob':'2020-10-10'},
    {'name':'Kabir Gombe', 'dob':'2000-10-10'},
    {'name':'Kassandrah Jonah', 'dob':'2005-10-10'},
    {'name':'Shehu Usman Danfodio', 'dob':'1991-10-10'},
]

# dob = '1990-07-07'


# age = int(current.split('-')[0]) - int(dob.split('-')[0])


# def multiply(x, y=1):
#     return x*y

# print(multiply(5, 6))
# print(multiply(y=6, x=3))


def age(dob):
    current = '2022-04-11'
    return int(current.split('-')[0]) - int(dob.split('-')[0])

print(f"|{'NAME':<20}|AGE|\n")
for student in students:
    name = student.get('name')
    dob = student.get('dob')
    print(f'|{name:<20}|{age(dob):<3}|\n')


transactions = [
    {'customer':'Kabir Abubakar', 'date':'2022-03-01', 'items':[{'name':'Cup Cake', 'price':250, 'unit':10}]},
    {'customer':'Habu Ladan', 'date':'2022-04-01', 'items':[{'name':'Coke', 'price':200, 'unit':2}]},
    {'customer':'Usman Shehu', 'date':'2022-04-09', 'items':[{'name':'Fanta', 'price':50, 'unit':4}, {'name':'Zero Blade', 'price':50, 'unit':14}]},
]

# Define a function that returns how long ago a transaction is performed give the date it was performed
# Print out all the transactions in this format: Kabir - 2hours ago - Cake, Biscuit


