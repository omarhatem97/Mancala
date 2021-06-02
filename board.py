import builtins


class Board(object):

    def __init__(self, board=None, withStealing =False):
        # save last values of board
        self.__playagain = False
        self.score = []
        self.__withStealing = withStealing


        if (board):
            self.board = board[:]
        # setup board
        else:
            self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
            
      
    def printBoard(self):

        print("\t", end="")
        for i in range(12, 6, -1):
            print(str(self.board[i]), end= "\t")

        print("\n")
        print(str(self.board[13]) + "\t"*7 + str(self.board[6]))

        print("\t", end="")
        for i in range(6):
            print(str(self.board[i]),end= "\t")

        print("")


    def getPlayAgain(self):
        return self.__playagain


    def getScore(self):
        return [self.board[6], self.board[13]]


    def get_total_buckets(self,player1):
        """
        get total bucket of the player
        """
        sum = 0
        if(player1):
            for bucket in range(6):
                sum += self.board[bucket]

        else:
            for bucket in range(7, 13, 1):
                sum += self.board[bucket]

        return sum


    def finalMove (self, player1):
        """
            if game is over, it adds the buckets of the opponent player to his store
        """
        sum = self.get_total_buckets(player1)
        if(player1):
            self.board[6]+=sum

        else:
            self.board[13] += sum

        self.clear_buckets()



    def clear_buckets(self):
        """
            clear opponent and players bucket (make them zeroes)
        """
        for i in range(14):
            if(i == 6 or i== 13):
                continue
            self.board[i] = 0


    def makeMove(self, bucket, player1):
        # turn of human (0-->5 buckets)
        if player1:
            copy_bucket=bucket
            stones = self.board[bucket]
            while (stones > 0):
                bucket = (bucket+1) % 14
                if bucket == 13:
                    continue  # dont add stone in the Ai store
                else:
                    self.board[bucket] += 1  # add stones in each bucket
                stones -= 1
            self.board[copy_bucket] = 0

            # play  with stealing
            if(self.__withStealing):
                if player1 and self.board[bucket] == 1 and self.board[12- bucket] != 0:
                    self.board[6] += 1 + self.board[12 - bucket]
                    self.board[12 - bucket] = 0
                    self.board[bucket] = 0

                if bucket == 6:
                    self.__playagain = True
        # turn of Ai (7--->12 buckets)
        else:
            
            bucket = bucket + 7
            stones = self.board[bucket]
            copy_bucket = bucket
            while (stones > 0):
                bucket = (bucket+1) % 14
                if bucket == 6:
                    continue  # dont add stone in the humman store
                else:
                    self.board[bucket] += 1  # add stones in each bucket

                stones -= 1
            print("copy bucket:", copy_bucket)
            self.board[copy_bucket] = 0

            # play  with stealing
            if(self.__withStealing):
                if not player1 and bucket != 13 and self.board[bucket] == 1 and self.board[12 - bucket] != 0:
                    self.board[13] += 1 + self.board[12 - bucket]
                    self.board[12 - bucket] = 0
                    self.board[bucket] = 0

                if bucket == 13:
                    self.__playagain = True


    def isOver(self):
        # human buckets are zero
        # ai buckets are zero
        player1 = True
        sum_human = self.get_total_buckets(player1)
        sum_ai = self.get_total_buckets(not player1)

        if (sum_human == 0 or sum_ai == 0):
            return True

        return False
