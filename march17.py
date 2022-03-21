database = {
    "jabir21":
        {"name":"Jabir", "password":"12345"},
    "usman91":
        {"name":"Usman", "password":"98756"}, 
    "mahmud21":
    {"name":"Mahmud", "password":"54321"},
         }

username = "jabir22"
password = "monkey94"

if username in database:
    if password == database[username]["password"]:
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("User not found")

print('\n\n')

students = ['Kassandrah', 'Jabir', 'Usman', 'Kabir']

if 'Kassandrah' in students:
    if 'Muhammad' in students:
        print('Muhammad and Kassandrah are in the same class')
    else:
        print('Kassandrah is in the class but Muhammad is not')
else:
    print('Kassandrah is not in the class')

print('\n\n')

if 'Kassandrah' in students:
    if 'Muhammad' in students:
        print('Muhammad and Kassandrah are in the same class')
    elif 'Jabir' in students:
        print('Kassandrah is in the class but Muhammad is not. Jabir is in the class though')
    else:
        print('Kassandrah is in the class but Muhammad is not and Jabir is not in the class')
elif 'Jabir' in students:
    print('Jabir is in the class but Kassandrah is not')
elif 'Usman' in students:
    print('Usman is in the class but Kassandrah and Jabir are not')
else:
    print('Kassandrah and Jabir are not in the class')


print('\n\n')
print('\n\n')
print('\n\n')
print('\n\n')

print('Welcome to the Awesome Game Game')
print('\n')
word = 'elephant'
possible_words = ['ant', 'leap', 'pant', 'hat', 'heat', 'pale', 'lap', 'peel', 'plant']
guess = input(f'Guess a word from "{word}": ')
if guess.lower().strip() in possible_words:
    print(f'You guessed "{guess.lower().strip()}" correctly')
else:
    print(f'Try again')


print('\n\n')

"""
Assignment

Q1: Write a program and allows users to login to a system with a phone number and password.
    The program should display an appropriate error message when the phone number or password or both is incorrect.
    If the phone number and password are correct, the program should display a welcome message.
    The program should allow users to enter their phone numbers with or without their country code.
    It should also be able to recognize numbers that are in this format +234 813 123 123.
"""



print('Kassandrah')
details =['08167095671','passs']
phone=input('enter phone number')
password=input('enter phone number')
if phone in details  :
    if password in details:
        print('sucessfull login')
    else:
        print('incorrect password, try gain')
else:
    print('incorrect phone number')
    
    
print('kbee')
    
user={'phone_number':'+2348063599265','password':'1111'}
phone_number=input('Please Enter phone number')
password=input('Please Enter password')
if password in user:
    if phone_number in user:
        print('login successful')
else:
    print('Check You Password Or Phone Number')
