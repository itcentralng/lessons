import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
play = True

q1 = {"q":"Guess a prime number between 1 and 20 that is a factor of 20", "a":5}
q2 = {"q":"I have a number between 1 and 10, guess the number", "a":random.choice(numbers)}
q3 = {"q":"I am a prime number between 1 and 10\n, if you remove the first letter I become divisble by 2,\n what am I?", "a":7}

questions = [q1, q2, q3]

while play:
    question = random.choice(questions)
    submitted_answer = input(question.get('q')+": ")
    if submitted_answer == 'q':
        play = False
    elif submitted_answer == str(question.get('a')):
        print("Way to go!")
    else:
        print("Oops! try again")

# ASSIGNMENT:
"""
Build an improved version of the guessing game,
The student with the most improved version gets 1k recharge card.
"""