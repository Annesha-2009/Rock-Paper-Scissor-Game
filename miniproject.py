# ROCK PAPER SCISSORS GAME

import random

def game(comp,you):
    if comp == you:
        return None
    elif comp =='r':
        if you =='p':
            return True
        elif you =='s':
            return False
    elif comp =='p':
        if you =='s':
            return True
        elif you =='r':
            return False
    elif comp =='s':
        if you =='p':
            return True
        elif you =='r':
            return False

randNo = random.randint(1,3)
if randNo == 1:
    comp ='r'
elif randNo == 2:
    comp ='p'
elif randNo == 3:
    comp ='s'
print("Computer Turn : Rock(r) , Paper(p) , Scissors(s) ? ")
you = input("Your Turn : Rock(r) , Paper(p) , Scissors(s) ? ")
print("Computer Chose : ", comp)
print("You Chose : ", you)

a = game(comp,you)
if a == None:
    print("The game is a Tie !!")
elif a:
    print("You Win !!")
else:
    print("Computer Wins !!")