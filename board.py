import numpy as np


class Board:

    def __init__(self):
        self.board_matrix=self.initialize_board()

    @staticmethod
    def initialize_board():
        input_board=np.full(9,'N',dtype='str').reshape(3,3)
        return input_board


    def reset_board(self):
        self.board_matrix=self.initialize_board()

    def display_board(self):
        n=0
        nrows,ncols=self.board_matrix.shape

        while n<nrows:

            if n!=(nrows-1):
                print('  |   | ')
                print(self.board_matrix[n,0]+' | '+self.board_matrix[n,1]+' |'+self.board_matrix[n,2])
                print('  |   | ')
                print('----------')
            else:
                print('  |   | ')
                print(self.board_matrix[n,0]+' | '+self.board_matrix[n,1]+' |'+self.board_matrix[n,2])
                print('  |   | ')
            n+=1



    def board_update(self,position, char):
       pos=self.translate(position)
       if (self.board_matrix[pos[0],pos[1]]=='X') | (self.board_matrix[pos[0],pos[1]]=='O'):
           raise Exception('Invalid position')
       self.board_matrix[pos[0],pos[1]]=char
       return self.board_matrix



    def check_winner(self,player_num):
        # check rows
        for rw in self.board_matrix:
            if 'N' in rw:
                continue
            elif len(set(list(rw)))==1:
                return True,player_num

        # check columns
        r,c=self.board_matrix.shape
        row=0
        col=0

        while col<c:
            # print(self.board_matrix[:,col])
            if 'N' in self.board_matrix[:,col]:
                col+=1
                continue
            elif len(set(self.board_matrix[:,col]))==1:
                return True,player_num
            col+=1

        #check diagonals
        diag_values={1:[[0,0],[1,1],[2,2]],2:[[0,2],[1,1],[2,0]]}
        n=1
        while n<3:
            tmp=[self.board_matrix[v[0],v[1]] for v in diag_values[n]]
            if 'N' in tmp:
                n+=1
                continue
            elif len(set(tmp))==1:
                return True,player_num

            n+=1
        return False,player_num



    @staticmethod
    def translate(position):
        if position<=3:
            return 0,position-1
        elif 3<position<=5:
            return 1,position-4
        elif 6<position<=9:
            return 2,position-7
        else:
            raise Exception('Not a valid value')





