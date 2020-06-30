import string
import random

def generate():
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(28))

def score(goal, attempt):
    score = 0
    for i in range(len(attempt)):
        if attempt[i] == goal[i]:
            score += 1
    return score

def attempt(target):
    checkpoint, goal, bestattempt  = 0, target, generate()
    highscore = score(goal, bestattempt)
    while highscore < 15:
        newattempt = generate()
        tryscore = score(goal, newattempt)
        if tryscore > highscore:
            highscore = tryscore
            bestattempt = newattempt
        checkpoint +=1
        if checkpoint == 1000:
            print(bestattempt, highscore)
            checkpoint = 0
    return bestattempt

print('methinks it is like a weasel')
