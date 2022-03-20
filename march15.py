"""
1   a. Create 5 variables that hold string
    b. Get the last two characters from each string
    c. Use 5 string methods to perform some string operations

2 Create 5 variables that hold integer
    Use the following arithmetic operators to 
    perform some operations with the integers above:
    +=, -=, /=, *=

3   a. Create 5 variables that hold list
    b. Get the last two items from each list
    c. Use 5 string methods to perform some list operations

4   a. Create 5 variables that hold dictionary
    b. Get the last two values from each dict
    c. Use 5 dict methods to perform some dict operations

5   a. Create a tuple
    b. What is the difference between a tuple and a list?
    c. What methods do they have in common?

6.  Repeat question 1 to 4 using conditional statements

"""

print("Usman Assignment")
#Q1
var1 = "SCHOOL"
print(" ")
var2 = "character"
print(" ")
var3 = "performances"
print(" ")
var4 = "statement"
print(" ")
var5 = "oprationss"
seeout1 =var1,var2,var3,var4,var5
print("The out put of var1 to var5 is",seeout1)
print("The last two Character of each variable are:-",var1[-2:],var2[7:],var3[-2:],var4[-2:],var5[8:])

""" The String methot that i use 
1. Replece()
2. Upper()
3. find()
4. capitalize()
5. lowar()
6. count()
 """
L = var1.lower()
print(L)
f = var2.find("a")
print(f)
u = var3.upper()
print(u)
R = var4.replace("state","Result")
print(R)
c = var5.count("r")
print(c)
print("  ")
print(" Q2 ")

int1 = 10
int2 = 20
int3 = 30
int4 = 50
int5 = 13
seeout2 =int1,int2,int3,int4,int5 
print("The out put of int1 to int5 is",seeout2)

addition = int1+int2+int3+int4+int5   #using Concatunation +
print("The sum of All integers are:",addition)
int1 += 2
print(int1)
int2 -= 4
print(int2)
int3 /= 2
print(int3)
int4 *= 2
print(int4)
int5 %= 3
print(int5)

print("  ")
print(" Q3 ")
fruits= ['apples', 'mango', 'orange', 'pears', 'banana', 'coconut']
names = ['mohammed','kassandra','Hassan', 'jabir', 'Bishir', 'kabiru', 'usman']
schools = ["FUD","FUT","ABU","BUK","UNIMAID","KASU","Alqalam"]
drinks = ['coke','fanta','smoov','maltina','sprite','pepsi','mirinder','lacasera']
numbers = [7,10,5,8,11,1,3,0,2,4,6,9]
print(fruits[4:])
print(names[5:])
print(numbers[-2:])
print(drinks[6:])
print(schools[5:])
""" The list methot that i use 
1. reverse()
2. remove()  
3. insert()
4. len()
5. sort()
 """
print(" ")
fruits.reverse()
print(fruits)
names.remove("Hassan")
print(names)
schools.insert(0 ,"Universities")
print(schools)
print(len(drinks))
numbers.sort()
print(numbers)

print(" ")
print("Q4")
fruits ={ "name":"apple"}
cars = {"car name":"toyota"}
name = {"studen":"yusuf"}
states = {"s":"jigawa"}
unit = {"kd":"U/rimi"}

""" The Dictionary methot that i use 
1. update()
2. get()  
3. keys()
4. copy()
5. clear()
 """
fruit = {"apple","gova","cashew"}
more_fruit = ["orange","mango","coconut"]
fruit.update(more_fruit)
print(fruit)
print(" ")
car = {"Brand":"Toyota","Model":"Jepp","Year":"2021"}
print("The car Model is: ",car.get("Model"))
print(car)
print(" ")
"""Adding a keys to my cars"""
cars["car color"] = "red"
cars["car zise"] = "big"
print(cars)
print(" ")
print("My keys in Dictionary cars is:",cars.keys())
print(name.copy())
print(unit.clear())
print(" ")
print("Q5 Tuple")

Element= (1,2, 3.0, 40, "name", "property","etc")
print(Element)
print("(tuple)element of the tuple are immutable and ordered, it allows duplicate values and can have any numbes of elements")
print("(list) is mutable")
print(" count and Index")

print(" ")
print("Q6 if")

if "S" in var1 and "a" in var2:
    print(" yes thier is")
