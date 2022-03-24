# FOR LOOP

mutane = ['Kassandarah', 'Ishaq', 'Kabir']

for mutum in mutane:
    print(mutum)
print("\n\n\n")
for mutum in mutane:
    if "s" in mutum:
        print(mutum)
        
print("\n\n\n")
for mutum in mutane:
    if len(mutum) >= 10:
        print(mutum)
print("\n\n\n")
for mutum in mutane:
    if "K" in mutum:
        print(mutum)
        
print("\n\n\n")
fruits = ["Apple", "Orange", "Banana", "Melon", "Blueberry", "Avocado", "Cranberry"]

for i in fruits:
    if i.endswith('e'):
        print(i)

print("\n\n\n")
for i in fruits:
    if i.startswith('B'):
        print(i)
print("\n\n\n")

# Print all fruits that have an 'a' in their names
for i in fruits:
    if 'a' in i:
        print(i)

fruits = ["Apple", "Orange", "Banana", "Melon", "Blueberry", "Avocado", "Cranberry"]
print("\n\n\n")
# Print all fruits that have an 'a' in their names regardless of case
for i in fruits:
    if 'a' in i.lower():
        print(i)

print("\n\n\n")
for i in fruits:
    print(i)
    
print("\n\n\n")
# Print the last two characters of all the fruits in the fruits list
for fruit in fruits:
    print(fruit[-2:])
 

"""Assignment"""

languages = [
  {"name":"Hausa", "population":1000, "continent":"Africa", "country":"Nigeria"},
  {"name":"English", "population":7000, "continent":"Europe", "country":"England"},
  {"name":"Arabic", "population":1200, "continent":"Asia", "country":"Saudi Arabia"},
  {"name":"French", "population":2300, "continent":"Europe", "country":"France"},
  {"name":"Spanish", "population":3500, "continent":"Europe", "country":"Spain"}
]

"""
Using the language list above, answer the follwoing questions:
1 - Write a code that print out all the languages in a table with their names, population, continent and country in format as below:
|Names|Population|Continent|Country|
|Hausa|  1000    |  Africa |Nigeria|
|Hausa|  1000    |  Africa |Nigeria|
|Hausa|  1000    |  Africa |Nigeria|
|Hausa|  1000    |  Africa |Nigeria|

2. Create a table and print out all the fruits that have at least 2000 speakers
3. Create a table and print out all the Eurpean languages
NOTE all tables must have this heading: |Names|Population|Continent|Country|
"""
