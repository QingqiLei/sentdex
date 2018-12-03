game = [[0,0,0],[0,0,0],[0,0,0]]

def game_board(player = 0, row = 0, column = 0, just_display = False):
    try:

        if not just_display:
            print("show")
            game[row][column] = player
            for count, row in enumerate(game):
                print(count, row)
    except IndexError as e:
        print(" something wrong! ! ! ",e)

    except Exception as e:
        print(" something went very wrong!! ",e)

    finally:
        print("finally") # runs every time

game_board(1,1,3)
game_board(game_board,1,2)
game_board(game_board,game_board,2)

raise IndexError  # cause a error
