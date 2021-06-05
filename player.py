import board
import Constants


class player:

    def __init__(self, player_type, difficulty=0):
        self.playet_type = player_type
        self.difficulty = difficulty


    def available_moves(self, board):
        '''
            return available moves for player at any board state
        '''
        moves = []
        if self.playet_type == Constants.HUMAN:
            for bucket in Constants.HUMAN_BUCKETS:
                if board.board[bucket] > 0:
                    moves.append[bucket]

        else:
            for bucket in Constants.AI_BUCKETS:
                if board.board[bucket] > 0:
                    moves.append[bucket]
        return moves

    def best_move(self, board):
        pass

    
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
        return (  (human_score - ai_score) if self.player_type == Constants.Constants.HUMAN else (ai_score - human_score))

