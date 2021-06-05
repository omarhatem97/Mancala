from board import *
from copy import deepcopy
b = Board(board =[0, 0, 0, 0, 1, 0, 0, 4, 4, 4, 4, 4, 4, 0],withStealing=True)

player1 = True

# def test(b):
#     b.clear_buckets()

# a = deepcopy(b)
# test(a)
# b.printBoard()

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

player_score , AI_score = b.getScore()
print(f'Player Score: {player_score}\n AI Score: {AI_score}')

