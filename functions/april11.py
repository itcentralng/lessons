# FUNCTION CONTINUATION

# from datetime import datetime

students = [
    {'name':'James Authur', 'dob':'2020-10-10'},
    {'name':'Kabir Gombe', 'dob':'2000-10-10'},
    {'name':'Kassandrah Jonah', 'dob':'2005-10-10'},
    {'name':'Shehu Usman Danfodio', 'dob':'1991-10-10'},
]

# dob = '1990-07-07'


# age = int(current.split('-')[0]) - int(dob.split('-')[0])


# def multiply(x, y=1):
#     return x*y

# print(multiply(5, 6))
# print(multiply(y=6, x=3))


# def age(dob):
#     current = '2022-04-11'
#     return int(current.split('-')[0]) - int(dob.split('-')[0])

# print(f"|{'NAME':<20}|AGE|\n")
# for student in students:
#     name = student.get('name')
#     dob = student.get('dob')
#     print(f'|{name:<20}|{age(dob):<3}|\n')


transactions = [
    {'customer':'Kabir Abubakar', 'date':'2020-03-01', 'items':[{'name':'Cup Cake', 'price':250, 'unit':10}]},
    {'customer':'Habu Ladan', 'date':'2022-04-01', 'items':[{'name':'Coke', 'price':200, 'unit':2}]},
    {'customer':'Usman Shehu', 'date':'2022-04-09', 'items':[{'name':'Fanta', 'price':50, 'unit':4}, {'name':'Zero Blade', 'price':50, 'unit':14}]},
]

# Define a function that returns how long ago a transaction is performed give the date it was performed
# Print out all the transactions in this format: Kabir - 2hours ago - Cake, Biscuit

def time_ago(date):
    """
    Function takes a date argument as string in this format 2020-10-10
    and returns how long it has been in comparison to the current date
    """
    current_date = "2022-04-12"
    current_date = current_date.split('-') #  ['2022', '04', '12']
    current_year = int(current_date[0])
    current_month = int(current_date[1])
    current_day = int(current_date[2])
    date = date.split('-') # ['2022', '04', '12']
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    days = ((current_year - year)*365) + ((current_month-month)*30) + (current_day - day)
    return days

for transaction in transactions:
    # Kabir - 2hours ago - Cake, Biscuit
    name = transaction.get('customer').split()[0]
    duration = time_ago(transaction.get('date'))
    items = [item.get('name') for item in transaction.get('items')]
    items = ', '.join(items)
    content = f'{name} - {duration} days ago - {items}'
    print(content)

print("\n\n")


def get_duration(transaction):
    current = '2022-04-11'
    b_month=transaction.get('date').split('-')[1]
    c_cmonth=current.split('-')[1]
    b_year=transaction.get('date').split('-')[0]
    c_cyear=current.split('-')[0]
    d_day=transaction.get('date').split('-')[2]
    c_cday=current.split('-')[2]
    year_difference=(int(c_cyear)-int(b_year))
    month_difference =int(c_cmonth)-int(b_month)
    day_diefference=int(c_cday)-int(d_day)
    duration = ''
    if year_difference > 0:
        duration+= f'{year_difference} years '
    if month_difference > 0:
        duration+= f'{month_difference} months '
    if day_diefference > 0:
        duration+= f'{day_diefference} days '
    return duration


for transaction in transactions:
    # print(get_duration(transaction))
    name = transaction.get('customer')
    items=','.join([item.get('name') for item in transaction.get('items')])
    print(f"{name} - {get_duration(transaction)} -{items}")


print('kbee')
def time_ago(date):
    """
    Function takes a date argument as string in this format 2020-10-10
    and returns how long it has been in comparison to the current date
    """
    current_date = "2022-04-12"
    current_date = current_date.split('-') #  ['2022', '04', '12']
    current_year = int(current_date[0])
    current_month = int(current_date[1])
    current_day = int(current_date[2])
    date = date.split('-') # ['2022', '04', '12']
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    duration = ''
    if current_year > 0:
        duration+= f'{current_year - year} years '
    if current_month > 1:
        duration+= f'{current_month - month} months '
    if current_day > 2:
        duration+= f'{current_day - day} days '
    return duration

for transaction in transactions:
    # Kabir - 2hours ago - Cake, Biscuit
    name = transaction.get('customer').split()[0]
    duration = time_ago(transaction.get('date'))
    items = [item.get('name') for item in transaction.get('items')]
    items = ', '.join(items)
    content = f'{name} - {duration} ago, - {items}'
    print(content)
