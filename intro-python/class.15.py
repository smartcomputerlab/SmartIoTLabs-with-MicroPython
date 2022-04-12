class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
x=MyClass()

x.counter = 1
x.toto =3

while x.counter < 10:
    x.counter = x.counter * 2

print(x.counter)
print(x.f())
print(x.i)
print(x.toto)


del x.toto
del x.counter

