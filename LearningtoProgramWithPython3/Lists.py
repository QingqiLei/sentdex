game = [0, 0, 0]
print(game)
for i in game:
    print(i)

game1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
count = 0
for i in game1:
    print(count, i)
    count += 1
    # for j in i:
    # print(j)

# enumerate is a built-in function
for count, row in enumerate(game1):
    print(count, row)
    for item in row:
        count +=1
