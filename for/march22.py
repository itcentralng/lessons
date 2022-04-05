# LOOPS

"""
"""

# FOR LOOPS

""" Iterates through an iterable """

students = ['Moha', 'KB', 'Ishaq', 'Kassandrah', 'Jabir','hb']
students = ['Moha', 'KB', 'Ishaq', 'Kassandrah', 'Jabir']

for i in students:
	if 'b' in i.lower():
		print(i)

orders = [
	{
		"id": 1, 
		"cost": 100, 
		"customer": "John", 
		"items": ["apple", "orange"], 
		"status": "", 
		"status": "pending", 
		"payment": ""
	},
	{
		"id": 2, 
		"cost": 200, 
		"customer": "Jane", 
		"items": ["banana", "apple"], 
		"status": "paid", 
		"payment": "cash"
		},
	{
		"id": 3, 
		"cost": 300, 
		"customer": "John", 
		"items": ["banana", "lemon"], 
		"status": "paid", 
		"payment": "credit"
		},
	]

table = "|ID|Customer|Cost|Status|Payment|\n"
for order in orders:
	if order.get("status") == "paid":
		id = order.get("id")
		if id < 10:
			id = f"0{id}"
		customer = order.get("customer")
		if len(customer) < len('customer'):
			customer = customer.center(len('customer'), ' ')
		cost = str(order.get("cost"))
		if len(cost) < len('cost'):
			cost = cost.center(len('cost'), ' ')
		status = order.get("status")
		if len(status) < len('status'):
			status = status.center(len('status'), ' ')
		payment = order.get("payment")
		if len(payment) < len('Payment'):
			payment = payment.center(len('payment'), ' ')
		table += "|{}|{}|{}|{}|{}|\n".format(id, customer, cost, status, payment)
print(table)

print("\n\n")

students = [
	{"name": "Moha", "age": 20, "class":"Primary 1"},
	{"name": "KB", "age": 21, "class":"Primary 2"},
	{"name": "Ishaq", "age": 22, "class":"Primary 3"},
	{"name": "Kassandrah", "age": 23, "class":"Primary 4"},
	{"name": "Jabir", "age": 24, "class":"Primary 5"},
]

table = "|Name|Age|Class|\n"
lenofname = len(students[3].get('name'))
lenofclass = len(students[3].get('class'))
x = table.split('|')
table = table.replace('Name', x[1].center(lenofname, ' ')).replace('Class', x[3].center(lenofclass, ' '))
table += ''.join(['_' for i in range(len(table)-1)])
table+='\n'
for student in students:
	age = f" {student.get('age')}"
	name = student.get('name').center(lenofname, ' ')
	_class = student.get('class').center(lenofclass, ' ')
	field = f"|{name}|{age}|{_class}|\n"
	table+=field
	table += ''.join(['_' for i in range(len(field)-1)])
	table+='\n'

print(table)

# CLASS WORK

"""
Create a list of 5 different fruits each fruit should have a name, color and taste.
Loop through the fruits and create a table that displays something like this:
------------------------
| Name | Color | Taste |
| Mango| Red   | Sour  |
| Mango| Red   | Sour  |
| Mango| Red   | Sour  |
| Mango| Red   | Sour  |
| Mango| Red   | Sour  |
------------------------
"""


print('kassandrah')


fruits = [
	{"name": "mango", "color": 'yellow', "taste":"sweet"},
	{"name": "grape", "color": 'purple', "taste":"sour"},
	{"name": "avocado", "color": 'green', "taste":"sweet"},
	{"name": "durian", "color": 'yellow', "taste":"sweet"},
	{"name": "pear", "color": 'green', "taste":"sweet"},
]

table = "|Name|color|taste|\n"

namelength = len(fruits[2].get('name'))
tastelength = len(fruits[2].get('taste'))
x = table.split('|')
table = table.replace('Name', x[1].center(namelength, ' ')).replace('taste', x[3].center(tastelength, ' '))
table += ''.join(['_' for i in range(len(table)-1)])
table+='\n'

for fruit in fruits:
	colour = f" {fruit.get('color')}"
	name = fruit.get('name').center(namelength, ' ')
	taste = fruit.get('taste').center(tastelength, ' ')
	content = f"|{name}|{colour}|{taste}|\n"
	table+=content
table+= ''.join(['_' for i in range(len(content)-1)])

print(table)
