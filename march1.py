""" Submit 2nd March 2022 """

q1 = """
        My name is Jabir Bashir Kabir, 
        I am a shopkeeper at Usman Kasandrah stores.
        Please kindly help me create an empty shopping cart so that
        my customers can make purchases.
    """
# Write your answer below this line
<<<<<<< HEAD
print("Usman")
Cart = []
print("My cart is Empty", Cart)
print("Thank you for the Empty shopping cart")
=======
print ('Kassandrah\n')

js_shoppingcart =[] 
print(f'Jabir, here is your cart:{js_shoppingcart}\n ')
>>>>>>> 25c51807cfd5d1116e2cf737c6c794cebe1fbb56

print("  ")
print("  ")
q2 = """
        Thank you for the empty shopping cart,
        my customer james just came in and purchased
        cake, cashew, brownies and zobo. 
        Please kindly help him add them to the cart.
    """
# Write your answer below this line
<<<<<<< HEAD
Cart.insert(0,"cake")
Cart.insert(1,"cashew")
Cart.insert(2,"brownies")
Cart.insert(3,"zobo")
print("Thank you for purchase", Cart)
=======

js_shoppingcart.append('cake')
js_shoppingcart.append('cashew')
js_shoppingcart.append('brownies')
js_shoppingcart.append('zobo')
print(f'your cart conatins {js_shoppingcart}\n' )

>>>>>>> 25c51807cfd5d1116e2cf737c6c794cebe1fbb56
q3 = """
    James is happy with his purchase and wants to checkout.
    Please modify his cart so that it shows the price and quantity
    of each item purchased.
    """
<<<<<<< HEAD
print("  ")
print("  ")
# Write your answer below  this line
price1 = [Cart [0],"price is",1000," and quantity is",5]
price2 = [Cart [1],"price is ",400, " and quantity is",10]
price3 = [Cart [2],"price is ",2000, " and quantity is",2]
price4 = [Cart [3],"price is",100, " and quantity is",1]
result = price1+price2+price3+price4
print(result)
print("  ")
print("  ")
=======



# Write your answer below  this line

prices = [100, 200, 300, 400]
js_shoppingcart =['cake', 'cashew', 'brownies', 'zobo']
quantity = [2,3,4,5]

print(f'item 1 : {js_shoppingcart[0]}, the price is {prices[0]} and you got {quantity[0]} in total')
print(f'item 2 : {js_shoppingcart[1]}, the price is {prices[1]} and you got {quantity[1]} in total')
print(f'item 3 : {js_shoppingcart[2]}, the price is {prices[2]} and you got {quantity[2]} in total')
print(f'item 4 : {js_shoppingcart[3]}, the price is {prices[3]} and you got {quantity[3]} in total\n')


>>>>>>> 25c51807cfd5d1116e2cf737c6c794cebe1fbb56
q4 = """
    Thank you for all the help dear programmer,
    Please print the total to be paid by our dear customer
    and empty the cart one by one
    """

# Write your answer below this line

total_price =sum(prices)

total_quantity = sum(quantity)

print(f'the total items purchased is {total_quantity} and the price is {total_price} naira\n')

prices.clear()
quantity.clear()
js_shoppingcart.clear()

print(f'now your cart is empty and ready for the next operation Jabir: {js_shoppingcart},prices:{prices} and quantity: {quantity}\n')

