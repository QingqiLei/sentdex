import itertools
player_choice = itertools.cycle([1,2,3,4])
for i in range(10):
    print(next(player_choice))

# iterable: a thing that is iterable, we can iterate over
# iterator: a special object with next() method
print()
x = [1,2,3,4]          # List is iterable

n = itertools.cycle(x) # iterator! ... also iterable
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

y = iter(x)  # iterator.. also iterable, can only iterate once.
for i in y:
    print(i)

for i in y:
    print(i)

print(f"x[0] = {x[0]}")

