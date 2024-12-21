print("great!")
print('snake')
print('doesn\'t')
print("doesn\'t")
print("\"Yes,\" they said.")
print('"Yes," they said.')
print('"Isn\'t," they said.')
print(r'C:\some\name') # r щоб вивести рядок без переносу спеціальним символом

print("""\
Usage: thingy [OPTIONS]
    -h                         Display this usage message
    -H hostname                Hostname to connect to
    
""")
print(3 * 'Py' + 'thon')
print('py' 'thon')
print("python "
      "language for programs")

pref = 'py'
print(pref + 'thon')

word = "python"
print(word[0:2])
print(word[-1:-3])
print(word[:3])
print(word[0:])
print(word[2:20])
print(word[:30])
print(word[:4] + word[4:])

# word[0] = 'J' #error

print('J' + word[1:])

st = 'supercalifragilisticexpialidocious'
print(len(st))