# FUNCTION CONTINUATION

from datetime import datetime
import arrow

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
    current_date = arrow.now().timestamp()
    date = arrow.get(date).timestamp()
    seconds_to_day = 86400
    days = int((current_date - date)/seconds_to_day)
    return days

for transaction in transactions:
    # Kabir - 2hours ago - Cake, Biscuit
    name = transaction.get('customer').split()[0]
    duration = time_ago(transaction.get('date'))
    items = [item.get('name') for item in transaction.get('items')]
    items = ', '.join(items)
    content = f'{name} - {duration} days ago - {items}'
    print(content)

def get_years(date):
    """
    Function takes a date argument as string in this format 2020-10-10
    and returns how long it has been in comparison to the current date in years
    """
    current_date = arrow.now().timestamp()
    date = arrow.get(date).timestamp()
    seconds_to_year = 86400*365
    years = int((current_date - date)/seconds_to_year)
    return years