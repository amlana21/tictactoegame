from board import Board
from player import Player


err=True
while err:

    try:
        plyr_1_char=str(input('Player 1 enter your character(X or O):'))
        if not(plyr_1_char in ['X','O']):
            raise Exception('Enter a correct character.')
        else:
            player1=Player(1,plyr_1_char)
            if plyr_1_char=='X':
                player2=Player(2,'O')
            else:
                player2=Player(2,'X')
        err=False
    except Exception as e:
        print(e)
print(f'Player1 Character: {player1.char}')
print(f'Player2 Character: {player2.char}')
err=True


board_obj=Board()
board_obj.display_board()
repeat_game=True
game_ctr=0
while repeat_game:
    if game_ctr!=0:
        while err:
            try:
                board_obj.reset_board()
                board_obj.display_board()
                player1.reset_player_selection(player2)
                err=False
            except:
                print('Enter a correct character.')
    err=True
    print('Randomizing Turn..')
    first_turn=Player.randomize_turn()
    print(first_turn)
    while  not board_obj.check_winner(first_turn)[0]:
        while err:
            try:
                inputchar=Player.validate_input(input(f'Player {first_turn} enter your position(1-9):'))
                board_obj.board_update(int(inputchar),(lambda x:player1.char if x==1 else player2.char)(first_turn))
                err=False
            except :
                print('Invalid Position. Try again!!')

        err=True
        board_obj.display_board()
        rslt=board_obj.check_winner(first_turn)
        first_turn=(lambda x: Player.switch_player(first_turn) if not x[0] else first_turn)(rslt)
        print(inputchar)
    if first_turn==1:
        player1.winner=True
        print('Player 1 is the winner')
    elif first_turn==2:
        player2.winner=True
        print('Player 2 is the winner')


    game_ctr+=1
    repeat_game=(lambda x:True if x=='Y' else False)(input('Do you want to replay?(Y/N)'))
        

