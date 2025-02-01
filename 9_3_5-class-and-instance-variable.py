class Dog:

    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.trick= []

    def add_trick(self, trick):
        self.trick.append(trick)

d = Dog('Fibo')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.trick)
print(e.trick)
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)