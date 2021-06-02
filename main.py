from board import *

b = Board(board =[0, 0, 0, 0, 1, 0, 0, 4, 4, 4, 4, 4, 4, 0],withStealing=True)

player1 = True


while(not b.isOver()):
    b.printBoard()
    if(player1):
        print("player 1 turn, enter bucket num:")
    else:
        print("player 2 turn, enter bucket num:")

    bucket_num = int(input())
    b.makeMove(bucket_num - 1, player1)

    if(not b.getPlayAgain):
        player1 = not player1


b.finalMove(not player1)    
b.printBoard()    


