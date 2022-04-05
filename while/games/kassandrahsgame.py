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
questions = {'n':number_questions, 's':spelling_questions}
score = 0
name = input('enter your name dear subscriber \n')
print(f'{name.title()}! welcome to our guessing game')
chooice = input('kindly enter n for the number game and s for the spelling game \n')
while play:
    try:
        question = random.choice(questions.get(chooice))
        submitted_answer = input(question.get('q')+": ")
        if submitted_answer == 'done':
            play = False
        elif submitted_answer== str(question.get('a')):
            score =score+1
            print(f'Way to go {name}! your answer {submitted_answer} is coamrrect\n\n')
        elif submitted_answer!=str(question.get('a')):
            print(f"sorry you lost a point the correct answer is{question.get('a')}")
            score=score-1
        print(f'your score so far is {score} points\n')
    except:print(f'check the question{submitted_answer} again please and provide the correct answer')