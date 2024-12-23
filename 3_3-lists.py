lists = [1, 4, 9, 16, 25]
print(lists)
print(lists[0])
print(lists[-2])
print(lists + [36, 49, 64])

cub = [1, 8, 27, 65, 125]
cub4 = 4 ** 3
cub[3] = cub4
print(cub)

rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))
rgba.append("Alph")
print(rgb)

correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)

litt = ["a", "b", "c", "d", "e", "h"]
print(litt)

litt[2:6] = ["C", "D", "E", "H"]
print(litt)

litt[2:6] = []
print(litt)

litt[:] = []
print(litt)

print(len(litt))

a = ["a", "b", "c", "d"]
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0][2])
print(x[1][1])