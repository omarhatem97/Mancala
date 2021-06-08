import board
from board import Board
import Constants
from copy import deepcopy
import math
class Player:

    def __init__(self, player_type, difficulty=0):
        self.player_type = player_type
        self.difficulty = difficulty


    def available_moves(self, board, player):
        '''
            return available moves for player at any board state
        '''
        moves = []
        if player == Constants.HUMAN:
            for bucket in Constants.HUMAN_BUCKETS:
                if board.board[bucket] > 0:
                    moves.append(bucket)

        else:
            for bucket in Constants.AI_BUCKETS:
                if board.board[bucket] > 0:
                    moves.append(bucket)
        return moves



    def find_best_move_rec(self,board, depth, alpha, beta, player):

        '''
            this is a recursive function to find the best move, given a certin difficulty, here the difficulty
            represents how many levels to traverse inside the graph in a depth first search manner

            so each graph level would try to maximize or minimize the score according to which player is playing in this level

            so for ex. if the AI player is the one called this function to find the best move, in every level 
            that is the turn for the AI player, the algorith will search for the maximum score in the children nodes
            and vica versa


        '''

        
        if board.isOver() or depth == 0 :
            return (self.cost(board) , -1)


        best_score_move = -1

        maximizing = (player == self.player_type)


        if maximizing:
            best_score = -1 * math.inf
        else:
            best_score = math.inf  



        for move in self.available_moves(board, player):

            new_board = deepcopy(board)
            new_board.makeMove(move, player)

            # we need to check if the same player gets to play gain then we don't change the player
            if new_board.getPlayAgain():

                cur_value, cur_move = self.find_best_move_rec(new_board, depth-1 , alpha, beta, player)
            else:

                cur_value, cur_move = self.find_best_move_rec(new_board, depth-1 , alpha, beta, not player)


            if (maximizing and cur_value > best_score) or ( not maximizing and cur_value < best_score):
                best_score = cur_value 
                best_score_move =  move

            # alpha beta pruning 
            if maximizing:
                alpha = max(alpha, cur_value)
            
            else: 
                beta = min(beta , cur_value)

            # terminating condition
            if alpha > beta:
                break

        return (best_score, best_score_move)



    def best_move(self, board):
        
        board_copy = deepcopy(board)

        move = self.find_best_move_rec(board_copy, self.difficulty, -1 * math.inf, math.inf, self.player_type )

        return move

    



    def cost(self, board):
        '''
            this function will calculate an approximate score for the current board

            we will give each stone in buckets a point and each stone in store 2 points 

            then we return the difference between the scores

        '''

        human_score = 0
        ai_score = 0


        # clac human score
        for bucket in Constants.HUMAN_BUCKETS:
            human_score += board.board[bucket]

        human_score +=  2 * board.board[Constants.HUMAN_STORE]


        # clac AI score
        for bucket in Constants.AI_BUCKETS:
            ai_score += board.board[bucket]

        ai_score +=  2 * board.board[Constants.AI_STORE]

        # here we return human_score - ai_score if we trying to find best move for human, otherwise we return ai_score - human_score
        return (  (human_score - ai_score) if self.player_type == Constants.HUMAN else (ai_score - human_score))




# Testing 
# b = Board(board =Constants.DEFAULT_BOARD,withStealing=True)

# b.printBoard()
# p = Player(Constants.AI, 4)



# best = p.best_move(b)[1] + 1 

# print(best)
