squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


square = list(map(lambda x: x**2, range(10)))

print(square)


squar = [x**2 for x in range(10)]

print(squar)


combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

print(combs)


comb = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            comb.append((x, y))

print(comb)



vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x>=0])
print([abs(x) for x in vec])
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])
print([(x, x**2) for x in range(6)])
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])


# experiment
pi1 = []
for i in range(1, 6):
    pi1.append([str(round(pi, i))])

print(pi1)