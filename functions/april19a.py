# def hello():
#     name = "kabir abbakar"
#     if name == 'kabir abbakar':
#         print("hello")
#     return name

# print(hello())


# def hello():
#     name = 'Kabir Abubakar'
#     h = "Hello"
#     z = h+name
#     return z

# print(hello())


# def greetings(name):
#     return f"Hello {name}"

# print(greetings('James'))
# print(greetings('Ashir'))
# print(greetings('Kassandra'))
# print(greetings('Salis'))


# def sum():
#     x = 6
#     y = 9
#     z = x + y
#     return z

# print(sum)


# def sum():
#     return 6+9

# print(sum())


# def add(sum):
#     return sum

# print(add(1+1))
# print(add(1+2))
# print(add(1+3))

# def addition(x, y=1):
#     return x + y

# print(addition(5, 7))
# print(addition(16, 4))

# def test(**args):
#     print(args)
#     for i in args:
#         print(i)

# test(a=1, b=2, c=3)

# def add(**numbers):
#     total = 0
#     for number in numbers.values():
#         total += number
#     return total

# print(add(a=1, b=2, c=3, d=4, e=5))
# print(add(a=1, b=2, c=3))
# print(add(a=1, b=2))

def test(*args):
    total = 0
    for number in args:
        total += number
    return total

print(test(1, 1, 2, 5, 6, 6))

