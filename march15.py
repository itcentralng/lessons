"""
1   a. Create 5 variables that hold string
    b. Get the last two characters from each string
    c. Use 5 string methods to perform some string operations
"""
a = "Hello"
b = "World"
c = "Python"
d = "Programming"
e = "Language"

a_last2 = a[-2:]
b_last2 = b[-2:]
c_last2 = c[-2:]
d_last2 = d[-2:]
e_last2 = e[-2:]

a.upper()
b.lower()
c.capitalize()
d.title()
e.swapcase()


"""
2 Create 5 variables that hold integer
    Use the following arithmetic operators to 
    perform some operations with the integers above:
    +=, -=, /=, *=
"""

a = 10
b = 20
c = 30
d = 40
e = 50

a += 10
b -= 10
c /= 10
d *= 10
e += 10

"""
3   a. Create 5 variables that hold list
    b. Get the last two items from each list
    c. Use 5 list methods to perform some list operations
"""

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [11, 12, 13, 14, 15]
d = [16, 17, 18, 19, 20]
e = [21, 22, 23, 24, 25]

a_last2 = a[-2:]
b_last2 = b[-2:]
c_last2 = c[-2:]
d_last2 = d[-2:]
e_last2 = e[-2:]

a.append(26)
b.extend([27, 28, 29])
c.insert(0, 0)
d.remove(18)
e.pop()

"""
4   a. Create 5 variables that hold dictionary
    b. Get the last two values from each dict
    c. Use 5 dict methods to perform some dict operations
"""
a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
b = {'a': 6, 'b': 7, 'c': 8, 'd': 9, 'e': 10}
c = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
d = {'a': 16, 'b': 17, 'c': 18, 'd': 19, 'e': 20}
e = {'a': 21, 'b': 22, 'c': 23, 'd': 24, 'e': 25}

a_last2 = list(a.values())[-2:]
b_last2 = list(b.values())[-2:]
c_last2 = list(c.values())[-2:]
d_last2 = list(d.values())[-2:]
e_last2 = list(e.values())[-2:]

a.get('a')
b.update({'a': 26})
c.pop('a')
d.popitem()
e.clear()

"""
5   a. Create a tuple
    b. What is the difference between a tuple and a list?
    c. What methods do they have in common?
"""
a = (1, 2, 3, 4, 5)
b = "The difference between a tuple and a list is that a tuple is immutable and a list is mutable."
c = "They have the following methods in common: index, count"

"""
6.  Repeat question 1 to 4 using conditional statements

"""

a1 = "Hello"
b1 = "World"
c1 = "Python"
d1 = "Programming"
e1 = "Language"

if len(a1) > 3 and len(b1) > 3 and len(c1) > 3 and len(d1) > 3 and len(e1) > 3:
    a1_last2 = a1[-2:]
    b1_last2 = b1[-2:]
    c1_last2 = c1[-2:]
    d1_last2 = d1[-2:]
    e1_last2 = e1[-2:]

if type(a1) == str and type(b1) == str and type(c1) == str and type(d1) == str and type(e1) == str:
    a1.upper()
    b1.lower()
    c1.capitalize()
    d1.title()
    e1.swapcase()

a2 = 10
b2 = 20
c2 = 30
d2 = 40
e2 = 50

if type(a2) == int and type(b2) == int and type(c2) == int and type(d2) == int and type(e2) == int:
    a2 += 10
    b2 -= 10
    c2 /= 10
    d2 *= 10
    e2 += 10

a3 = [1, 2, 3, 4, 5]
b3 = [6, 7, 8, 9, 10]
c3 = [11, 12, 13, 14, 15]
d3 = [16, 17, 18, 19, 20]
e3 = [21, 22, 23, 24, 25]

if len(a3) > 3 and len(b3) > 3 and len(c3) > 3 and len(d3) > 3 and len(e3) > 3:
    a3_last2 = a3[-2:]
    b3_last2 = b3[-2:]
    c3_last2 = c3[-2:]
    d3_last2 = d3[-2:]
    e3_last2 = e3[-2:]

if type(a3) == list and type(b3) == list and type(c3) == list and type(d3) == list and type(e3) == list:
    a3.append(26)
    b3.extend([27, 28, 29])
    c3.insert(0, 0)
    d3.remove(18)
    e3.pop()

a4 = {"name": "John", "age": 36, "country": "Norway"}
b4 = {"name": "Snow", "age": 22, "country": "USA"}
c4 = {"name": "Peter", "age": 23, "country": "UK"}
d4 = {"name": "Jack", "age": 24, "country": "UK"}
e4 = {"name": "Jill", "age": 25, "country": "USA"}

if len(a4.values()) > 2 and len(b4.values()) > 2 and len(c4.values()) > 2 and len(d4.values()) > 2 and len(e4.values()) > 2:
    a4_last2 = list(a4.values())[-2:]
    b4_last2 = list(b4.values())[-2:]
    c4_last2 = list(c4.values())[-2:]
    d4_last2 = list(d4.values())[-2:]
    e4_last2 = list(e4.values())[-2:]

if type(a4) == dict and type(b4) == dict and type(c4) == dict and type(d4) == dict and type(e4) == dict:
    a4.get('name')
    b4.update({'name': 'John'})
    c4.pop('name')
    d4.popitem()
    e4.clear()