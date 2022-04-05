fruits = [
    {"name": "apple", "price": 100},
    {"name": "banana", "price": 200},
    {"name": "orange", "price": 300},
    {"name": "grape", "price": 400},
    {"name": "mango", "price": 500},
    ]

# get all the fruits that cost more than 300
# and display them in a table


print("Kassandrah")

table = "|Name|Price|\n"

for fruit in fruits:
    if fruit.get("price") > 300:
        name = f"{fruit.get('name')}"
        price = f"{fruit.get('price')}"
        table_content = f"|{name}|{price}|\n"
        table += table_content

print(table)



print("Kabir")

table = f"|{'NAME':<8}|{'PRICE':<8}|\n"

for fruit in fruits:
    name = fruit['name']
    price = fruit['price']
    if price > 300:
        table += f"|{name:<8}|{price:<8}|\n"
print(table)

print("Usman")

table = f"|NAME|PRICE|\n"
for fruit in fruits:
    name = fruit['name']
    price = fruit['price']
    if price > 300:
        u = f"|{name}|{price}|\n"
        table += u
print(table)

