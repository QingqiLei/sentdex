game = [[1, 2, 3], [2, 2, 2], [0, 0, 0]]

def win(current_game):
    for row in current_game:
        print(row)
        not_match = False
        for item in row:
            if item != row[0]:
                not_match = True
        if not not_match:
            print("winner")
win(game)
print(game.count(game[0]) == len(game))

def winner(current_game):
    for row in current_game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print("winner!!")
winner(game)