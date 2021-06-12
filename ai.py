from board import Board


class AI():
    def __init__(self, board):
        self.board  = board
        self.player1 = True
        self.ai = False
    
    def generate_children(self, board:Board):
        #generate children states(nodes) for a given state
        #return list of board states
        children = []

        for bucket in range(7, 13, 1):
            if(bucket):
                temp_board = board
                temp_board.makeMove(bucket-7, self.ai)
                children.append((temp_board, bucket))
        return children



    def find_best_move(self, child, depth, ismax):
        #return the index of the bucket which will be the best move heuristically
        maximum = -1e9
        if(depth == 0):
            if(ismax):
                return max(maximum, child[0].estimate()), child[1]
            else:
                return min(maximum, child[0].estimate()), child[1]


        children = self.generate_children(child[0])
        for child in children:
            print('estimate :' + str(child[0].estimate())) #debugging only
            
            maxim, rightchild =  self.find_best_move(child, depth-1, not ismax)
        
        return maxim, rightchild-7

        
        
        