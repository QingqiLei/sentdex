game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
string = "I want to play a game"
print("initial string: " + str(id(string)))
def game_board(player = 0, row = 0, column = 0):
    game[row][column] = player #  changed
    string = "a game"  # not changed
    print("not global:    ",id(string))  # not a same string
game_board()
print(game)
print(string)
print(id(string))

def game_board():
    global string
    string = "a game"
    print("global:        ",id(string))  # get a new id
game_board()
print(string)
print("after global:  ",id(string))  # retain the new id, literally change the string

def game_board(string1):
    string1 = "two games"
    print("use string as a parameter: ",id(string1)) # not the same string

game_board(string)
print(string)  # not changed to "two games"
