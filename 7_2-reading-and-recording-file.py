# 1
f = open('workfile', 'w', encoding="utf-8")

f.close()


# 2
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

print(f.closed)