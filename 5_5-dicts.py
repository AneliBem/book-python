tel = {'jack': 4008, 'snape': 4903}
tel['guido'] = 4127

print(tel)
print(tel['jack'])

del tel['snape']
tel['irv'] = 4127

print(tel)

print(list(tel)) # list key
print(sorted(tel)) # sort list key

print('guido' in tel)
print('jack' not in tel)

print(dict([('sape', 4193), ('guido', 4127), ('jack', 4098)])) # creative dict

print({x: x**2 for x in (2, 4, 6)})

print(dict(sape=4139, guido=4127, jack=4098))

