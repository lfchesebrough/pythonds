# coding: utf-8



# 3rd function call generate and score, print best attempt so far,
# See if you can improve upon the program in the self check by
# keeping letters that are correct and only modifying one character
# in the best string so far. This is a type of algorithm in the class of
# ‘hill climbing’ algorithms, that is we only keep the result if it is better
# than the previous one.

import string
import random

# random string generator with alphabet letters and spaces
def generate(N):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(N))

# create a score comparing two strings, 1 point for every matched character in the same position
def score(goal, attempt):
    score = 0
    for i in range(len(attempt)):
        if attempt[i] == goal[i]:
            score += 1
    return score

# randomly generate a string until you randomly match a target string, keep track of best attempt
def monkey(target):
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

# match a target string by matching one character at a time
def bettermonkey(target):
    attempt = generate(28)
    for i in range(len(target)):
        targetletter = target[i]
        attemptletter = attempt[i]
        while targetletter != attemptletter:
            newattempt = random.choice(string.ascii_lowercase + ' ')
            if newattempt == targetletter:
                attemptletter = newattempt
                if i < len(target) - 1:
                    attempt = attempt[:i] + newattempt + attempt[i+1:]
                else:
                    attempt = attempt[:i] + newattempt
        print(attempt)
    return attempt
