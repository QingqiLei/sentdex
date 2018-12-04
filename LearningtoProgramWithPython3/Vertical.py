game = [[1, 2, 3],
        [2, 2, 2],
        [0, 2, 0]]

for col in range(len(game)):
    check = []

    for row in game:
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print("Winner !")

cols = list(reversed(range(len(game))))
print(type(reversed(range(len(game))))) # range_iterator
rows = range(len(game))

cols[2]
for i in rows:
    print(i, cols[i] )
print()
for col, row, in zip(reversed(range(len(game))), range(len(game))):
    print(col, row)

print()

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])
    print(col, row)
print(diags)

