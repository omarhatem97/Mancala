class Board(object):

    def __init__(self, board=None):
        # save last values of board
        self.__playagain = False
        if (board):
            self.board = board[:]

        # setup board
        else:
            self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
            # self.board = [0 for i in range(14)]
            # for i in range(0, 6, 1): self.board[i] = 4
            # for i in range(7, 13, 1): self.board[i] = 4
            return

    def makeMove(self, bucket):
        # copy_bucket=bucket
        stones = self.board[bucket]

        # turn of human (0-->5 buckets)
        if bucket < 6:
            while (stones > 0):
                bucket += 1
                bucket = bucket % 14
                if bucket == 13:
                    continue  # dont add stone in the Ai store
                else:
                    self.board[bucket] += 1  # add stones in each bucket
                stones -= 1

                # play  with stealing
            if bucket < 6 and self.board[bucket] == 1 and self.board[12 - bucket] != 0:
                self.board[6] += 1 + self.board[12 - bucket]
                self.board[12 - bucket] = 0
                self.board[bucket] = 0

            if bucket == 6:
                self.__playagain = True
        # turn of Ai (7--->12 buckets)
        else:
            while (stones > 0):
                bucket += 1
                bucket = bucket % 14
                if bucket == 6:
                    continue  # dont add stone in the humman store
                else:
                    self.board[bucket] += 1  # add stones in each bucket
                stones -= 1

                # play  with stealing
            if bucket > 6 and bucket != 13 and self.board[bucket] == 1 and self.board[12 - bucket] != 0:
                self.board[13] += 1 + self.board[12 - bucket]
                self.board[12 - bucket] = 0
                self.board[bucket] = 0

            if bucket == 13:
                self.__playagain = True

    def isOver(self):
        # human buckets are zero
        # ai buckets are zero
        sum_human = 0
        sum_ai = 0

        for bucket in range(6):
            sum_human += self.board[bucket]

        for bucket in range(7, 13, 1):
            sum_ai += self.board[bucket]

        if (sum_human == 0 or sum_ai == 0):
            return True
        return False
