'''
students = {"Kassandrah":"speaks hausa", "Kabir":"speaks english", "Ishaq":"speaks hausa"}

if students.get('Kassandrah')=='speaks hausa':
    print('Kassandrah speaks hausa')
elif students.get('Kabir')=='speaks english':
    print('Kabir speaks english')
elif students.get('Ishaq')=='speaks hausa':
    print('Ishaq speaks hausa')

print("\n\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number > 10:
        print(number)
    else:
        print(number)
        break

print("\n\n")
for e, number in enumerate(numbers):
    if number > 10:
        print(number)
    else:
        print(number)
    if e > 3:
        break

print("\n\n")
'''
# ASSIGNMENT

# Q1:

languages = [
    {"name":"Hausa", "speakers":1000},
    {"name":"English", "speakers":1500},
    {"name":"Yoruba", "speakers":900},
    {"name":"Igbo", "speakers":1200}
    ]

# determine the language that has the highest number of speakers
# assuming you can't see the data in the languages list above.



# Q2:

students = [
    {"name":"Ahmad", "score":100},
    {"name":"James", "score":1500},
    {"name":"Haruna", "score":200},
    {"name":"Karim", "score":750},
    {"name":"Qasim", "score":878},
    {"name":"Hadiza", "score":997},
    ]

# determine the position of every student in the student
# list above using their scores.s