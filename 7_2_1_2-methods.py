with open('workfile.txt', 'w', encoding="utf-8") as f:
    # read_data = f.readline()
    # read_dat = f.readline()
    chars_written = f.write('Thus test\n')
    # for line in f:
    #     print(line, end=' ')

# print(read_data)
# print(read_dat)

print(chars_written)
print(f.closed)