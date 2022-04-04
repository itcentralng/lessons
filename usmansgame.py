import random
print("usman Changes\n".upper())

print("----- Welcome To The Wold Guess Game----\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
state = ['kaduna', 'kano', 'yobe', 'borno', 'sokoto', 'kasina', 'zanfara', 'lagos', 'ido','adamawa','bauchi']
play = True
q1 = {"q":"Guess a prime number between 1 and 20 that is a factor of 20:  ", "a":5}
q2 = {"q":"I have a number between 1 and 10, guess the number: ", "a":random.choice(numbers)}
q3 = {"q":"I am a prime number between 1 and 10\n, if you remove the first letter I become divisble by 2,\n what am I?: ", "a":7}
q4 = {"q":"which state that has a (2 a's and 1 d) guess :","a":'kaduna'}
q5 = {"q":"in the state that we have which one his speling start with (y) :","a":'yobe'}
q6 = {"q":"in Nigeria which State tha his slogan is  home of peace :","a":'borno'}
q7 = {"q":"which state was lan of beauty:","a":'adamawa'}
q8 = {"q":"in the state that we have, which State that have 3 alphabet spelling and have (d):","a":'ido'}
q9 = {"q":"which state that have 4 alphabet but start with (k) :","a":'kano'}
q10= {"q":"which state in Nigeria that has (s)on the End of his Spelling :","a":'lagos'}

questions = [q1, q2, q3,q4,q5,q6,q7,q8,q9,q10]

name = input("|Welcome| Enter your name: ")
name = name.strip()
print(' ')
print(f'Hello! ---{name}--- : Would you like to play a game?')
print(' ')
print("options")
print('If Yes press 1) ')
print('If No press  2) ')
option = input('Select your Option: ')
option=int(option)
if option == 1:
    print("Welcome to The Guessing game")
    print(' ')
elif option == 2:
    print("Thank you!....")
    play = False
else:
    print("Invalid Option")
    play = False
tries = 0 
while play:
    if option == 1:
            question = random.choice(questions)
            submitted_answer = input(question.get('q'))
            if submitted_answer == str(question.get('a')):
                tries = tries+1
                print(f"Will don!!!!...{name}... your get the correct Anwser:\n correct is: {submitted_answer}")
            
            if submitted_answer == question:
                play = False
            if submitted_answer != str(question.get('a')):
                print(f"Oops! try again the correct answer is {question.get('a')}")
                tries = tries-1
            print(f'you have  {tries} point\n')
print(" ")
