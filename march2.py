'''
q1 = """ My name is Jabir Bashir Kabir, remember me? Great! Please help with the same problem but this time use dictionaries"""
print('kassandrah')
# dictionary storage

cart = {}
print (f'here is your empty cart{cart}')
cart = {'items':['cake', 'cashew','brownies', 'zobo'],'prices':[100,200,300,400],'quantity':[2,3,4,5]}

cartitems=cart['items']
ct = cartitems
c = cart['items'][0]
x =cart['items'][1]
b = cart ['items'][2]
g = cart['items'][3]
y =cart['prices'][0]
f=cart['prices'][1]
k=cart['prices'][2]
w =cart['prices'][3]
d = cart['quantity'][0]
s =cart['quantity'][1]
l =cart['quantity'][2]
q =cart['quantity'][3]

print ('you have picked:')
print(f'{c},{d} in number, for {y}')
print(f'{x},{s} in number, for {f}')
print(f'{b},{l} in number, for {k}')
print(f'{g},{q} in number,for {w}')

totalp=14
totalq=1000
total = totalp*totalq
print (f' you purchased {cartitems} for a total amount of {total} naira') 
'''
print("Usman Abba")
print(" ")
shopcart = {}
print(shopcart)

shopcart['1']={'fruith name is': 'cake'}
shopcart['2']={'fruith name is': 'cashew'}
shopcart['3']={'fruith name is': 'brownies'}
shopcart['4']={'fruith name is': 'zobo'}
print(shopcart['1'])
print(shopcart['2'])
print(shopcart['3'])
print(shopcart['4'])
print("  ")
print("  ")
shopcart['1']={'fruith is': 'cake', 'price':1000, 'queantity':2}
shopcart['2']={'fruith is': 'cashew','price':50, 'queantity':6}
shopcart['3']={'fruith is': 'brownies','price':700, 'queantity':1}
shopcart['4']={'fruith is': 'zobo','price':60, 'queantity':10}
print(shopcart['1'])
print(shopcart['2'])
print(shopcart['3'])
print(shopcart['4'])

print("  ")
print("  ")

shopcart['1']['total']= shopcart['1']['price'] * shopcart['1']['queantity']
shopcart['2']['total']= shopcart['2']['price'] * shopcart['2']['queantity']
shopcart['3']['total']= shopcart['3']['price'] * shopcart['3']['queantity']
shopcart['4']['total']= shopcart['4']['price'] * shopcart['4']['queantity']

print('The total of cake is',shopcart['1']['total'])
print('The total of cashew is',shopcart['2']['total'])
print('The total of brownies is',shopcart['3']['total'])
print('The total of zobo is',shopcart['4']['total'])
print("  ")
print("Thank you for purchissing")