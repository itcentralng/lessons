""" Submit 2nd March 2022 """

q1 = """
        My name is Jabir Bashir Kabir, 
        I am a shopkeeper at Usman Kasandrah stores.
        Please kindly help me create an empty shopping cart so that
        my customers can make purchases.
    """
# Write your answer below this line
print("Usman")
Cart = []
print("My cart is Empty", Cart)
print("Thank you for the Empty shopping cart")

print("  ")
print("  ")
q2 = """
        Thank you for the empty shopping cart,
        my customer james just came in and purchased
        cake, cashew, brownies and zobo. 
        Please kindly help him add them to the cart.
    """
# Write your answer below this line
Cart.insert(0,"cake")
Cart.insert(1,"cashew")
Cart.insert(2,"brownies")
Cart.insert(3,"zobo")
print("Thank you for purchase", Cart)
q3 = """
    James is happy with his purchase and wants to checkout.
    Please modify his cart so that it shows the price and quantity
    of each item purchased.
    """
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
q4 = """
    Thank you for all the help dear programmer,
    Please print the total to be paid by our dear customer
    and empty the cart one by one
    """

# Write your answer below this line