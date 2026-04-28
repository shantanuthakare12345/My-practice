
import random

def Game(name,attempt,win,loss,draw):
    option = [0,1,2]
    computer = random.choice(option)
    name = name
    user = int(input("Enter the value:-  "))
    attempt = attempt + 1
    win = win
    loss = loss
    draw = draw

    if (user == computer):
        print("Match Draw")
        draw = draw + 1

    elif user == 0 and computer == 2:
        print(name," Win The Game")
        print("Computer pass :- scissor")
        print(name,"pass :- stone ")
        win = win + 1

    elif user == 1 and computer == 0:
        print(name," Win The Game")
        print("Computer pass :- stone")
        print(name,"pass :- paper ")
        win = win + 1

    elif user == 2 and computer == 1:
        print(name," Win The Game")
        print("Computer pass :- paper")
        print(name,"pass :- scissor ")
        win = win + 1

    elif user in option:
        print("Computer Win The Game")
        print("Computer pass :- ",computer)
        loss = loss + 1
        if (user == 0):
            print(name,"pass :- stone ")
        elif(user == 1):
            print(name,"pass :- paper ")
        elif(user == 2):
            print(name,"pass :- scissor")
    else:
        print("Invalid Input")

    
    while(True):
        a = input("if you wont to continue the press (y) or exit then press (n):- ")
        if(a=="y"):
            Game(name,attempt,win,loss,draw)
        elif(a=="n"):
            print("You Attempt the Game ",attempt)
            print("You Win:- ",win)
            print("Computer Win:- ",loss)
            print("Draw:- ",draw)
            print("........THANK YOU........!")
            break
        else:
            print("Enter the valid input")

print("**************************************")
print("        STONE PAPER SCISSORS")
print("**************************************")
print(""" The Rules of the Game
    stone = 0
    paper = 1
    scissor = 2""")

name = input("Enter the name of plyer:- ")

Game(name,0,0,0,0)




