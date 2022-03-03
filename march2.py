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