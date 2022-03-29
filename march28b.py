'''
students = {"Kassandrah":"speaks hausa", "Kabir":"speaks english", "Ishaq":"speaks hausa"}
# students = {"Kassandrah":"speaks hausa", "Kabir":"speaks english", "Ishaq":"speaks hausa"}

# if students.get('Kassandrah')=='speaks hausa':
#     print('Kassandrah speaks hausa')
# elif students.get('Kabir')=='speaks english':
#     print('Kabir speaks english')
# elif students.get('Ishaq')=='speaks hausa':
#     print('Ishaq speaks hausa')

# print("\n\n")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     if number > 10:
#         print(number)
#     else:
#         print(number)
#         break

# print("\n\n")
# for e, number in enumerate(numbers):
#     if number > 10:
#         print(number)
#     else:
#         print(number)
#     if e > 3:
#         break

print("\n\n")
'''
# ASSIGNMENT
# print("\n\n")

# # ASSIGNMENT

# # Q1:


languages = [
    {"name":"Hausa", "speakers":1000},
    {"name":"English", "speakers":1500},
    {"name":"Yoruba", "speakers":900},
    {"name":"Igbo", "speakers":1200}
    ]

# # determine the language that has the highest number of speakers
# # assuming you can't see the data in the languages list above.

print("CORRECTION")

highest = {}
for language in languages:
    if language["speakers"] > highest.get("speakers", 0):
        highest = language
print(f"The language with the highest number of speakers is {highest['name']} with {highest['speakers']} speakers")

print('Kassandrah')
def _filter(key):
    return key.get('speakers')
newlist = sorted(languages, key=_filter, reverse=True)       
highest = newlist[0]
name=newlist[0].get('name')
speakers=newlist[0].get('speakers')
print(f'the {name} has the highest number of speakers with a total of {speakers}')

print("Kabir")
speakers=languages[0]['speakers'],+languages[1]['speakers'],+languages[2]['speakers'],+languages[3]['speakers']
for language in languages:
    if language == speakers:
        print(language)
    else:
        print(max(speakers))
        break
print("Kabir v2")
speakers = []
for language in languages:
    speakers.append(language['speakers'])
print(max(speakers))


# Q2:
# # Q2:

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
# # determine the position of every student in the student
# # list above using their scores.


print('\n\n')
def _filter(key):
    return key.get('score')

table="|Name|scors|position|"
newlist2=sorted(students,key=_filter,reverse=True)
for n in newlist2:
    namee=f"{n.get('name')}"
    score=f"{n.get('score')}"
    content = f"|{namee:<6}|{score:<5}|"
    table+=content
    print(content)


print("CORRECTION")
scores = [student['score'] for student in students]
scores = sorted(scores, reverse=True)
table = "|Name|Score|Position|\n"
for student in students:
    position = scores.index(student['score']) + 1
    name = student['name']
    score = student['score']
    content = f"|{name:<6}|{score:<5}|{position:<5}|\n"
    table += content
print(table)
