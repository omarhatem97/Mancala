from ai import AI
from board import Board

b = Board(board =None,withStealing=True)

player1 = True
ai = AI(b)

while(not b.isOver()):
    b.printBoard()
    if(player1):
        print("player 1 turn, enter bucket num: ", end="")
        bucket_num = int(input())
        
    else:
        print("player 2 turn, enter bucket num:")
        maximum, best_move = ai.find_best_move((b,1), 1, ismax=False)
        print(maximum, best_move)

    b.makeMove(bucket_num - 1, player1)

    if(not b.getPlayAgain()):
        player1 = not player1


b.finalMove(not player1)    
b.printBoard()    


