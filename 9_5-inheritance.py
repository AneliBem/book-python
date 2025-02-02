class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello, my name is {self.name}.'

class Child(Parent):
    def play(self):
        return f'{self.name} is playing.'

c = Child('Alice')
print(c.greet())
print(c.play())
