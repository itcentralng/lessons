import json
from random import choice
import time
"""

STATE & CAPITAL

1) Users should be able to join with their names
2) The games shows you the name of a randomly chosen state in Nigeria and expects you to give the capital
3) Every right answer gives the user 5 points
4) Every wrong answer deducts 4 points
5) When the game ends, the score is saved to a file named scores.json and the leaderboard is displayed

"""
print("Welcome to the State and Capital Guessing Game\n")
user = input("Enter your username: ")
score = 0
states = open("states.txt", "r")
states = states.read()
states = json.loads(states)

play = True

correct = []

timeallowed = 10

while play:
    state = choice(states)
    states.pop(states.index(state))
    if len(states) == 0:
        scores = open("scores.json", "r")
        old_scores = json.loads(scores.read())
        old_scores[user] = score
        scores.close()
        scores = open("scores.json", "w")
        scores.write(json.dumps(old_scores))
        scores.close()
        play = False
        print('Challenge Complete')
        print(f"{user} you are exiting the game\n")
        print(f"{user} your score is {score}\n")
        print('---------------------------------\n')
        print(f"{'LEADERBOARD':>20}")
        print('|NAME|SCORE|\n')
        for name, score in old_scores.items():
            print(f"{name}|{score}|\n")
    else:
        start = time.time()
        capital = input(f"{user} Guess the capital of {state.get('state').get('name')}: ")
        if capital.lower().strip() == state.get('state').get('capital').lower().strip():
            score += 5
            print(f"{user} you are correct! you get 5 points")
            correct.append(state)
        elif capital == 'exit':
            scores = open("scores.json", "r")
            old_scores = json.loads(scores.read())
            old_scores[user] = score
            scores.close()
            scores = open("scores.json", "w")
            scores.write(json.dumps(old_scores))
            scores.close()
            play = False
            print(f"{user} you are exiting the game\n")
            print(f"{user} your score is {score}\n")
            print('---------------------------------\n')
            print(f"{'LEADERBOARD':>20}")
            print('|NAME|SCORE|\n')
            for name, score in old_scores.items():
                print(f"{name}|{score}|\n")


        else:
            score -= 4
            print(f"{user} you are wrong! you lose 4 points")
        end = time.time()
        if end - start > timeallowed:
            score -= 3
            print(f"\nTimeout!!! you lose 3 points")
        
"""
GAME IMPRVOEMENTS

1) Leaderboard should not be repeated in the code
2) The game should have multiple difficulty levels
3) Level should either be selected by the user or selected for the user based on their score
4) The game should have a timer such that if a user answers when the time elapses, 3 points are deducted
"""