# import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# play = True

# q1 = {"q":"Guess a prime number between 1 and 20 that is a factor of 20", "a":5}
# q2 = {"q":"I have a number between 1 and 10, guess the number", "a":random.choice(numbers)}
# q3 = {"q":"I am a prime number between 1 and 10\n, if you remove the first letter I become divisble by 2,\n what am I?", "a":7}

# questions = [q1, q2, q3]

# while play:
#     question = random.choice(questions)
#     submitted_answer = input(question.get('q')+": ")
#     if submitted_answer == 'q':
#         play = False
#     elif submitted_answer == str(question.get('a')):
#         print("Way to go!")
#     else:
#         print("Oops! try again")

# ASSIGNMENT:
"""
Build an improved version of the guessing game,
The student with the most improved version gets 1k recharge card.
"""
print ("Kassandrah's changes")
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
play = True

q1 = {"q":"Guess a prime number between 1 and 20 that is a factor of 20", "a":5}
q2 = {"q":"I have a number between 1 and 10, guess the number", "a":random.choice(numbers)}
q3 = {"q":"I am a prime number between 1 and 10\n, if you remove the first letter I become divisble by 2,\n what am I?", "a":7}
q4 = {"q":"If 1=3\n 2=3\n 3=5\n 4=4\n 5=4\n Then 6=?", "a":3}
q5 = {"q":"Which 3 numbers have the same answer whether they're added or multiplied together?", "a":'123'}
q6 = {"q":"There is a three-digit number. The second digit is four times as big as the third digit, while the first digit is three less than the second digit. What is the number?", "a":141}
q7 = {"q":"How many feet are in a mile?", "a":5280}
q8 = {"q":"Look at this series: 36, 34, 30, 28, 24, … What number should come next?", "a":22}
q9 = {"q":" Look at this series: 22, 21, 23, 22, 24, 23, … What number should come next?", "a":25}
q10 = {"q":"Look at this series: 53, 53, 40, 40, 27, 27, … What number should come next?", "a":14}
q11= {"q":"what word describes the state of solitude?", "a":'lonely'}
q12= {"q":"what does it mean for someone or something to be closely connected or appropriate to what is being done or considered", "a":'relevant'}
q13= {"q":"what word describes the expression of earnest disapproval of ", "a":'deprecate'}
q14 = {"q":"what word describes having an angry or sullen look on one's face", "a":'glower'}
q15= {"q":"having or showing knowledge that is gained by studying is best described as being an ", "a":'erudite'}

number_questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10] 
spelling_questions=[q11,q12, q13, q14, q15]
score = 0
name = input('enter your name dear subscriber \n')
print(f'{name.title()}! welcome to our guessing game')
chooice = input('kindly enter n for the number game and s for the spelling game \n')
while play:
    if chooice=='n':
        try:
            question = random.choice(number_questions)
            submitted_answer = input(question.get('q')+": ")
            if submitted_answer== str(question.get('a')):
                score =score+1
                print(f'Way to go {name}! your answer {submitted_answer} is correct\n')
            if submitted_answer == 'done':
                play = False
            if submitted_answer!=str(question.get('a')):
                print(f"sorry you lost a point the correct answer is {question.get('a')}")
                score=score-1
            print(f'your score so far is {score} points\n')
        except:print(f'check the question{submitted_answer} again please and provide the correct answer')
    if chooice=='s':
        try:
            question = random.choice(spelling_questions)
            submitted_answer = input(question.get('q')+": ").lower()
            
            if submitted_answer== str(question.get('a')):
                score =score+1
                print(f'Way to go {name}! your answer {submitted_answer} is coamrrect\n\n')
            if submitted_answer == 'done':
                play = False
            if submitted_answer!=str(question.get('a')):
                print(f"sorry you lost a point the correct answer is{question.get('a')}")
                score=score-1
            print(f'your score so far is {score} points\n')
        except:print(f'check the question{submitted_answer} again please and provide the correct answer')

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
if option == 2:
    print("Thank you!....")
tries = 0 
while play:
    if option == 1:
            question = random.choice(questions)
            submitted_answer = input(question.get('q')).lower()
            if submitted_answer == str(question.get('a')):
                tries = tries+1
                print(f"Will don!!!!...{name}... your get the correct Anwser:\n correct is:---{submitted_answer}---")
            
            if submitted_answer == question:
                play = False
            if submitted_answer != str(question.get('a')):
                print(f"Oops! try again the correct answer is {question.get('a')}")
                tries = tries-1
            print(f'you have  --{tries}-- point\n')
print(" ")
    

