
game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def game_board():
    for count, row in enumerate(game):
        print(count, row)


x = game_board

game[0][0] = 34
game_board()

x()  # tricky


def addition(x: int, y):
    return x + y


z = addition(5, 3)
print(z)


def game_board(player=0, row=0, column=0, just_display=False):  # default value of the parameters
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)


game_board(1, 2, 2, False)
