import random
playagain="yes"
while playagain=="yes":
    choose=input("choose rock paper or scissor")
    while choose!="rock" and choose!="paper" and choose!="scissor":
        choose=input("choose rock paper or scissor")
    computer=random.randint(1,3)
    if computer==1:
        print("rock")
        if choose=="rock":
            print("tie")
        elif choose=="scissor":
            print("you lose")
        elif choose=="paper":
            print("you win")
    elif computer==2:
        print("scissor")
        if choose=="rock":
            print("you win")
        elif choose=="scissor":
            print("tie")
        elif choose=="paper":
            print("you lose")
    elif computer==3:
        print("paper")
        if choose=="rock":
            print("you lose")
        elif choose=="scissor":
            print("you win")
        elif choose=="paper":
            print("tie")
    playagain=input("do you want to play again")
    while playagain!="no" and playagain!="yes":
        playagain=input("do you want to play again")