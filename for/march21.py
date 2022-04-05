# LOOPS

# FOR LOOP
"""
 Uses iterables e.g. lists, strings, sets, dictionaries or tuples
 example will be going through a list of students to find one that
 meets a certain condtion.
"""

students = [ {"name":"Ashir Musa", "age":16}, {'name':"Kawu Dupe", 'age':18}]

for i in students:
    if i.get('age') == 16:
        print("Found "+i.get('name'))

print("\n")
for student in students:
    print(student.get("name").split()[0])

print("\n")
for student in students:
    for alphabet in student.get('name'):
        print(alphabet)