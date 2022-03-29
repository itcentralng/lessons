import random

while False:
    print('This will keep running forever!')

number = 5

while number > 1:
    number -= 1
    print(number)

print(number)



print("\n\n")
alphabets = ['A', 'B', 'C']

count = 0
while len(alphabets) < 5:
    count+=1
    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    a = random.choice(x)
    if a not in alphabets:
        alphabets.append(a)

print("it took ", count, " tries to get it right")
print(alphabets)