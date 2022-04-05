'''
"""Assignment"""

languages = [
  {"name":"Hausa", "population":1000, "continent":"Africa", "country":"Nigeria"},
  {"name":"English", "population":7000, "continent":"Europe", "country":"England"},
  {"name":"Arabic", "population":1200, "continent":"Asia", "country":"Saudi Arabia"},
  {"name":"French", "population":2300, "continent":"Europe", "country":"France"},
  {"name":"Spanish", "population":1500, "continent":"Europe", "country":"Spain"}
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

print("CORRECTION")

# Q1:
print("TABLE SHOWING ALL LANGUAGES")
table = f"|{'Name':<10}|{'Population':<10}|{'Continent':<10}|{'Country':<15}|\n"
for language in languages:
    name = language['name']
    population = language['population']
    continent = language['continent']
    country = language['country']
    table += f"|{name:<10}|{population:<10}|{continent:<10}|{country:<15}|\n"

print(table)

# Q2:
print("TABLE SHOWING LANGUAGES WITH AT LEAST 2000 SPEAKERS")
table2 = f"|{'Name':<10}|{'Population':<10}|{'Continent':<10}|{'Country':<15}|\n"
for language in languages:
    name = language['name']
    population = language['population']
    continent = language['continent']
    country = language['country']
    if population >= 2000:
        table2 += f"|{name:<10}|{population:<10}|{continent:<10}|{country:<15}|\n"
print(table2)

#Q3:
print("TABLE SHOWING EUROPEAN LANGUAGES")
table3 = f"|{'Name':<10}|{'Population':<10}|{'Continent':<10}|{'Country':<15}|\n"
for language in languages:
    name = language['name']
    population = language['population']
    continent = language['continent']
    country = language['country']
    if continent == 'Europe':
        table3 += f"|{name:<10}|{population:<10}|{continent:<10}|{country:<15}|\n"
print(table3)
'''
import numbers


fruits =[
    {"name":"apple","price":100},
    {"name":"banana","price":200},
    {"name":"orange","price":300},
    {"name":"grape","price":400},
    {"name":"mango","price":500}
    ]
table = f"|{'Name':}|{'price':}|\n"
for fruit in fruits:
    name = fruit["name"]
    price = fruit["price"]
    if fruit.get('price') >300:
        lt=f'|{name}|{price}|\n'
        table +=lt
        print(table)
number = 5
while number > 1:
    number-=1
    print(number)
print(number)
