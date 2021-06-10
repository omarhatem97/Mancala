from player import Player
from board import *
from copy import deepcopy
# b = Board(board =[0,0,0,0,0,8,13,0,0,5,9,0,0,18],withStealing=True)







print("WELCOME TO MANCALA GAME!!")
with_steal = int(input('If you want to Enable stealing press 1, if you do not want to play with stealing press 0\n'))

print ("Please choose difficulty of AI")
Ai_diff = int(input())
print ("Please choose difficulty of Human in case Human use Play Now!")
Hu_diff = int(input())
print ("Please choose player to start\n1- Human\n2- AI")
player = input()


b = Board(board =Constants.DEFAULT_BOARD,withStealing=with_steal)

ai_player = Player(Constants.AI, Ai_diff)
Hu_player = Player(Constants.HUMAN, Hu_diff)

if player == '1':
    player = Constants.HUMAN
elif player =='2':
    player = Constants.AI 


while(not b.isOver()):
    b.printBoard()

   

    if player == Constants.HUMAN:
        print("HUMAN  turn, enter bucket num or press 'P' for Play Now!:")
        x = input()
        if x == 'P' or x == 'p':
            move = Hu_player.best_move(b)[1] + 1
        else:
            move = int(x)
        player_name = 'HUMAN'


    else:
        move = ai_player.best_move(b)[1] + 1
        player_name = 'AI'

  
    print(f'this is {player_name} turn, and choose number {move}\n')
    b.makeMove(move - 1, player)

   

    if(not b.getPlayAgain()):
        player = not player


b.finalMove(player)    
b.printBoard()

player_score , AI_score = b.getScore()
print(f'Player Score: {player_score}\n AI Score: {AI_score}')

