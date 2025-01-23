basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('orange' in basket)

print('crabglass' in basket)

a = set('abracadabra') # створення наборів
b = set('alacazam')

print(a) # літери з слова а
print(a - b) # унікальні літери які є ьілтки в а
print(a | b) # лірери які є в двох словах
print(a & b) # однакові літери в а і b
print(a ^ b) # унікальні літери які є в а і b

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)