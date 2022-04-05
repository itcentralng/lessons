""" 
Dictionary Methods 

"""

from os import PRIO_USER


people = {"name":"Kabir"}
people.pop("name")
print(people)

name = {"person":"Kassandrah"}
print(name.get("person"))

names = {"person1":"Kabir", "person2":"Jabir"}
peron = names.copy()
print(peron)

print(names.values())
print(names.keys())
print(names.items())

names.update({"person4":"Habu"})
print(names)

names.setdefault("person5", "Qasim")
print(names)

print("\n\n\n\n\n")
# TUPLES

""" Tuples are immutable """

myfirsttuple = ("Jamil", "Jabir", "Junaid")
print(myfirsttuple[0])
print(myfirsttuple[1])
print(myfirsttuple[2][3:].title())
print(myfirsttuple[0][2:])
print(myfirsttuple[0][2:]+myfirsttuple[2][3:])

print(myfirsttuple.index("Jamil"))