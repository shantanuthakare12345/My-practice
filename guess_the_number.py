import random

def game():
    jackpot = int (random.randint(1,100))
    print("**************************************")
    print("GUESS THE NUMBER")
    print("**************************************")

    user = int(input("Enter the number:- "))

    while jackpot != user :            
        if(jackpot>user):
            user=int(input("ENTER TEH BIG NUMBER:- "))
            
        elif(jackpot<user):
            user=int(input("ENTER THE SMALL NUMBER:- "))
                
    print("YOU WON THE GAME:- ",user)
    a = input("if you wont to continue the press (+) or exit then press (-):-")
    if(a=="+"):
        game()
    else:
        print("........THANK YOU........!")




game()



