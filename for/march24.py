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
1 - Write a code that prints out all the languages in a table with their names, 
	population, continent and country in format as below:
|Names|Population|Continent|Country|
|Hausa|  1000    |  Africa |Nigeria|
|Hausa|  1000    |  Africa |Nigeria|
|Hausa|  1000    |  Africa |Nigeria|
|Hausa|  1000    |  Africa |Nigeria|

2. Create a table and prints out all the languages that have at least 2000 speakers
3. Create a table and prints out all the Eurpean languages
NOTE all tables must have this heading: |Names|Population|Continent|Country|
"""


print('Kassandrah')

table = "|Name|Population|Continent|Country|\n"

coutt= len(languages[3].get('country'))
contin = len(languages[2].get('continent'))
x = table.split('|')
table = table.replace('Name', x[1].center(coutt, ' ')).replace('taste', x[3].center(contin, ' '))


for lang in languages:
	pop = f" {lang.get('population')}"
	namee= f"{lang.get('name')}"
	namee.center(coutt,' ')
	continent=f"{lang.get('country')}"
	continent.center(coutt,' ')
	con=f"{lang.get('continent')}"
	con.center(coutt,' ')
	content = f"|{namee}|{pop}|{con}|{continent}|\n"
	table+=content

print(table)

table2="|Name|Population|Continent|Country|\n"

# for lang in languages:
x=3
for lang in languages:
	if lang.get('population')>=2000:
		pop = f" {lang.get('population')}"
		namee= f"{lang.get('name')}"
		namee.center(coutt,' ')
		continent=f"{lang.get('country')}"
		continent.center(coutt,' ')
		con=f"{lang.get('continent')}"
		con.center(coutt,' ')
		content = f"|{namee}|{pop}|{con}|{continent}|\n"
		table2+=content
print(table2)

table3="|Name|Population|Continent|Country|\n"
for lang in languages:
	if lang.get('continent')=='Europe':
		pop = f" {lang.get('population')}"
		namee= f"{lang.get('name')}"
		namee.center(coutt,' ')
		continent=f"{lang.get('country')}"
		continent.center(coutt,' ')
		con=f"{lang.get('continent')}"
		con.center(coutt,' ')
		content = f"|{namee}|{pop}|{con}|{continent}|\n"
		table3+=content
print(table3)


print('kbee')
# Q1
table = "|Name|Population|Continent|Country|\n"

iTcentral= len(languages[3].get('country'))
continent = len(languages[2].get('continent'))
x = table.split('|')
table = table.replace('Name', x[1].center(iTcentral, ' ')).replace(' ', x[3].center(continent, ' '))


for language in languages:
	population = f" {language.get('population')}"
    
	name= f"{language.get('name')}"
	name.center(iTcentral,' ')
    
	continent=f"{language.get('country')}"
	continent.center(iTcentral,' ')

	country=f"{language.get('continent')}"
	country.center(iTcentral,' ')

	content = f"|{name}|{population}|{country}|{continent}|\n"
	table+=content
print(table)

# Q3
table = "|Name|Population|Continent|Country|\n"
for language in languages:
	if language.get('continent')=='Europe':
		population = f"{language.get('population')}"
		name=f"{language.get('name')}"
		country=f" {language.get('country')}"
		continent=f"{language.get('continent')}"
		content = f"|{name}|{population}|{country}|{continent}|\n"
		table+=content
print(table)
