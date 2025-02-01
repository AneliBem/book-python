class MyClass:
    def f(self):
        return "hello world"
x = MyClass()

x.f()
xf = x.f
count = 0
while count < 5:
    print(xf())
    count += 1