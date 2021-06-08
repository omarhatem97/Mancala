from player import Player
from board import *
from copy import deepcopy
b = Board(board =[0,0,0,0,0,8,13,0,0,5,9,0,0,18],withStealing=True)

# b = Board(board =Constants.DEFAULT_BOARD,withStealing=True)


# def test(b):
#     b.clear_buckets()

# a = deepcopy(b)
# test(a)
# b.printBoard()



print("WELCOME TO MANCALA GAME!!")
print ("Please choose player to start\n 1- Human\n2- AI")
player = input()

ai_player = Player(Constants.AI, 1)

if player == '1':
    player = Constants.HUMAN
elif player =='2':
    player = Constants.AI 


while(not b.isOver()):
    b.printBoard()

   

    if player == Constants.HUMAN:
        print("HUMAN  turn, enter bucket num:")
        move = int(input())
        player_name = 'HUMAN'


    else:
        move = ai_player.best_move(b)[1] + 1
        player_name = 'AI'

    
    print(f'this is {player_name} turn, and choose number {move}\n')
    b.makeMove(move - 1, player)

   

    if(not b.getPlayAgain()):
        player = not player


b.finalMove( player)    
b.printBoard()

player_score , AI_score = b.getScore()
print(f'Player Score: {player_score}\n AI Score: {AI_score}')

