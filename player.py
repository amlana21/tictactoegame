import numpy as np

class Player:

    def __init__(self,num,char):
        self.num=num
        self.char=char
        self.winner=False

    def set_winner(self):
        self.winner=True

    def reset_player_selection(self,plyr2obj):
        char=str(input('Player 1 enter your character:'))
        if not(char in ['X','O']):
            raise Exception('wrong character')
        else:
            self.char=char
            self.winner=False
            if char=='X':
                plyr2obj.char='O'
                plyr2obj.winner=False
            else:
                plyr2obj.char='X'
                plyr2obj.winner=False
    @classmethod
    def randomize_turn(cls):
        return np.random.randint(1,3)
    @classmethod
    def validate_input(cls,inpt):


        if int(inpt) in [1,2,3,4,5,6,7,8,9]:
            return inpt
        else:
            raise Exception('Invalid input. Try again!!')


    @classmethod
    def switch_player(cls,plyr):
        return (lambda x:2 if x==1 else 1)(plyr)


