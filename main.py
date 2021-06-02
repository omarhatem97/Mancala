from board import *

b = Board()

player1 = True


while(not b.isOver()):
    b.printBoard()
    if(player1):
        print("player 1 turn, enter bucket num:")
    else:
        print("player 2 turn, enter bucket num:")

    bucket_num = int(input())
    b.makeMove(bucket_num - 1, player1)
    
    player1 = not player1


