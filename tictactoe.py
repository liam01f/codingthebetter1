import random
playergame=input("2 player or agaist ai")
if playergame=="ai":
    board=[["_","_","_"],["_","_","_"],["_","_","_"]]
    print(board[0])
    print(board[1])
    print(board[2])
    print()
    while True:
        playerschoose1=input("what row do you want to go in")
        playerschoose2=input("what colum do you want to choose")
        while board[int(playerschoose1)][int(playerschoose2)]=="x" or board[int(playerschoose1)][int(playerschoose2)]=="o":
            print("you can not go there")
            playerschoose1=input("what row do you want to go in")
            playerschoose2=input("what colum do you want to choose")
        board[int(playerschoose1)][int(playerschoose2)]="x"

        print(board[0])
        print(board[1])
        print(board[2])
        print()

        computer1=random.randint(0,2)
        computer2=random.randint(0,2)
        if board[0][0]!="_" and board[0][1]!="_" and board[0][2]!="_" and board[1][0]!="_" and board[1][1]!="_" and board[1][2]!="_" and board[2][0]!="_" and board[2][1]!="_" and board[2][2]!="_":
                print("tie goes to the computer")
                print("ha ha loser you lose")
                break
        while board[int(computer1)][int(computer2)]=="o" or board[int(computer1)][int(computer2)]=="x":
            computer1=random.randint(0,2)
            computer2=random.randint(0,2)
        board[int(computer1)][int(computer2)]="o"
        print(board[0])
        print(board[1])
        print(board[2])
        print()
        if board[0][0]=="x" and board[0][1]=="x" and board[0][2]=="x":
            print("you win")
            break
        elif board[0][0]=="x" and board[1][0]=="x" and board[2][0]=="x":
            print("you win")
            break
        elif board[0][1]=="x" and board[1][1]=="x" and board[1][2]=="x":
            print("you win")
            break
        elif board[0][2]=="x" and board[1][2]=="x" and board[2][2]=="x":
            print("you win")
            break
        elif board[1][0]=="x" and board[1][1]=="x" and board[1][2]=="x":
            print("you win")
            break
        elif board[2][0]=="x" and board[2][1]=="x" and board[2][2]=="x":
            print("you win")
            break
        elif board[0][0]=="x" and board[1][1]=="x" and board[2][2]=="x":
            print("you win")
            break
        elif board[0][2]=="x" and board[1][1]=="x" and board[2][0]=="x":
            print("you win")
            break
        if board[0][0]=="o" and board[0][1]=="o" and board[0][2]=="o":
            print("ha ha loser you lose")
            break
        elif board[0][0]=="o" and board[1][0]=="o" and board[2][0]=="o":
            print("ha ha loser you lose")
            break
        elif board[0][1]=="o" and board[1][1]=="o" and board[1][2]=="o":
            print("ha ha loser you lose")
            break
        elif board[0][2]=="o" and board[1][2]=="o" and board[2][2]=="o":
            print("ha ha loser you lose")
            break
        elif board[1][0]=="o" and board[1][1]=="o" and board[1][2]=="o":
            print("ha ha loser you lose")
            break
        elif board[2][0]=="o" and board[2][1]=="o" and board[2][2]=="o":
            print("ha ha loser you lose")
            break
        elif board[0][0]=="o" and board[1][1]=="o" and board[2][2]=="o":
            print("ha ha loser you lose")
            break
        elif board[0][2]=="o" and board[1][1]=="o" and board[2][0]=="o":
            print("ha ha loser you lose")
            break