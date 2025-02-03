rey = sum(i*i for i in range(10))
print(rey)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
yer = sum(x * y for x, y in zip(xvec, yvec))
print(yer)

# unique_words = set(word for line in page  for word in line.split())

# valedictorian = max((student.gps, student.name) for student in graduates)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))