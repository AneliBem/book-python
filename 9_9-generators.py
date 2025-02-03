def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

    print(data)

for char in reverse('golf'):
    print(char)